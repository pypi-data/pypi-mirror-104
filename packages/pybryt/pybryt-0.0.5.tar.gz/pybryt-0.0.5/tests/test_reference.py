""""""

import os
import dill
import json
import base64
import tempfile
import nbformat
import numpy as np
import pkg_resources
import pytest

from textwrap import dedent
from unittest import mock

from pybryt import ReferenceImplementation, Value
from pybryt.execution import execute_notebook


def generate_reference_notebook():
    """
    """
    nb = nbformat.v4.new_notebook()
    nb.cells.append(nbformat.v4.new_code_cell(dedent("""\
        import pybryt
    """)))
    nb.cells.append(nbformat.v4.new_code_cell(dedent("""\
        def median(S):
            sorted_S = sorted(S) 
            pybryt.Value(sorted_S, name="sorted", group="median", limit=5, success_message="SUCCESS: Sorted the sample correctly", 
                        failure_message="ERROR: The sample was not sorted")
            
            size_of_set = len(S) 
            pybryt.Value(size_of_set, name="size", group="median", success_message = "SUCCESS: Computed the size of the sample", 
                        failure_message="ERROR: Did not capture the size of the set to determine if it is odd or even")
            
            middle = size_of_set // 2
            is_set_size_even = (size_of_set % 2) == 0

            if is_set_size_even:
                return (sorted_S[middle-1] + sorted_S[middle]) / 2
            else:
                return sorted_S[middle]
    """)))
    nb.cells.append(nbformat.v4.new_code_cell(dedent("""\
        import numpy as np
        np.random.seed(42)
        for _ in range(10):
            vals = [np.random.randint(-1000, 1000) for _ in range(np.random.randint(1, 1000))]
            val = median(vals)
            pybryt.Value(val, name="median", group="median", success_message="SUCCESS: computed the correct median", 
                failure_message="ERROR: failed to compute the median")
    """)))
    return nb


def test_reference_construction():
    """
    """
    nb = generate_reference_notebook()

    ref = ReferenceImplementation.compile(nb)

    ref_filename = pkg_resources.resource_filename(__name__, os.path.join("files", "expected_ref.pkl"))
    expected_ref = ReferenceImplementation.load(ref_filename)

    with tempfile.NamedTemporaryFile() as ntf:
        ref.dump(ntf.name)
        second_ref = ReferenceImplementation.load(ntf.name)
        assert ref == second_ref
        assert ref == expected_ref

    # test construction from .py file w/ ReferenceImplementation objects
    ref2_filename = pkg_resources.resource_filename(__name__, os.path.join("files", "expected_ref2.pkl"))
    expected_ref2 = ReferenceImplementation.load(ref2_filename)

    with tempfile.NamedTemporaryFile("w+", suffix=".py") as ntf:
        ntf.write(dedent("""\
            import pybryt
            import numpy as np
            np.random.seed(42)

            def square_evens(arr):
                subarr = arr[arr % 2 == 0]
                v1 = pybryt.Value(subarr)
                subarr = subarr ** 2
                v2 = pybryt.Value(subarr)
                arr = arr.copy()
                arr[arr % 2 == 0] = subarr
                return v1, v2, arr

            annots = []
            for _ in range(10):
                vals = np.array([np.random.randint(-1000, 1000) for _ in range(np.random.randint(1, 1000))])
                v1, v2, val = square_evens(vals)
                annots.append(v1)
                annots.append(v2)
                annots.append(pybryt.Value(val))
            
            ref = pybryt.ReferenceImplementation(annots)
            ref2 = pybryt.ReferenceImplementation([])
        """))

        ntf.seek(0)

        more_refs = ReferenceImplementation.compile(ntf.name)
        assert len(more_refs) == 2
        assert len(more_refs[1].annotations) == 0
        
        ref2 = more_refs[0]
        assert ref2 == expected_ref2


def test_construction_errors():
    """
    """
    with pytest.raises(TypeError, match="annotations should be a list of Annotations"):
        ReferenceImplementation(set())

    with pytest.raises(TypeError, match="Found non-annotation in annotations"):
        ReferenceImplementation([Value(1), Value(2), 3, Value(4)])

    # check that you can't load something that isn't a ReferenceImplementation
    with tempfile.NamedTemporaryFile() as ntf:
        dill.dump(1, ntf)

        ntf.seek(0)

        with pytest.raises(TypeError, match="Unpickled reference implementation has type <class 'int'>"):
            ReferenceImplementation.load(ntf.name)

    # check that loading an empty reference implementation gives an error
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".ipynb") as ntf:
        nbformat.write(nbformat.v4.new_notebook(), ntf)

        ntf.seek(0)

        with pytest.warns(UserWarning, match=f"Could not find any reference implementations in {ntf.name}"):
            ReferenceImplementation.compile(ntf.name)


def test_run_and_results():
    """
    """
    nb = generate_reference_notebook()
    nb.cells.append(nbformat.v4.new_code_cell(dedent("""\
        vals = [np.random.randint(-1000, 1000) for _ in range(np.random.randint(1, 1000))]
        val = median(vals)
        # this annotation is not in the 'median' group
        pybryt.Value(val, success_message="SUCCESS: computed the correct median x2", 
            failure_message="ERROR: failed to compute the median")
    """)))
    ref = ReferenceImplementation.compile(nb)
    _, vals = execute_notebook(nb, "")
    
    res = ref.run(vals)
    assert len(res.results) == 27
    assert res.reference is ref
    assert res.correct is True
    assert (res.to_array() == np.ones(27)).all()
    assert repr(res).startswith("ReferenceResult([\n") and len(repr(res).split("\n")) == 29
    assert res.messages == [
        'SUCCESS: Sorted the sample correctly', 
        'SUCCESS: Computed the size of the sample', 
        'SUCCESS: computed the correct median',
        'SUCCESS: computed the correct median x2',
    ]

    res = ref.run(vals, group="median")
    assert len(res.results) == 26
    assert res.reference is ref
    assert res.correct is True
    assert (res.to_array() == np.ones(26)).all()
    assert repr(res).startswith("ReferenceResult([\n") and len(repr(res).split("\n")) == 28
    assert res.messages == [
        'SUCCESS: Sorted the sample correctly', 
        'SUCCESS: Computed the size of the sample', 
        'SUCCESS: computed the correct median',
    ]

    nb.cells.insert(2, nbformat.v4.new_code_cell("import numpy as np\ndef median(S):\n    return np.median(S)"))
    _, vals = execute_notebook(nb, "")
    
    res = ref.run(vals)
    assert len(res.results) == 27
    assert res.reference is ref
    assert res.correct is False
    assert (res.to_array() == np.array([0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 1, 1])).all()
    assert repr(res).startswith("ReferenceResult([\n") and len(repr(res).split("\n")) == 29
    assert res.messages == [
        'ERROR: The sample was not sorted',
        'ERROR: Did not capture the size of the set to determine if it is odd or even',
        'SUCCESS: computed the correct median',
        'SUCCESS: computed the correct median x2',
    ]

    res_filename = pkg_resources.resource_filename(__name__, os.path.join("files", "expected_result.json"))
    with open(res_filename) as f:
        expected_res_dict = json.load(f)

    for d in expected_res_dict["results"]:
        d.pop("satisfied_at")

    res_dict = res.to_dict()

    # check satisfied_at field here since they won't match up
    assert all(isinstance(d.pop("satisfied_at", None), int) for d in res_dict["results"])

    assert res_dict == expected_res_dict

    with pytest.raises(ValueError, match="Group 'foo' not found"):
        ref.run(vals, group="foo")
