# fuzz.py
from hypothesis import given, strategies as st

# Import the methods from their respective modules
# Adjust the imports according to the actual structure of your project
from MLForensics.MLForensics_farzana.FAME_ML.py_parser import getPythonAtrributeFuncs, getFunctionAssignments
from MLForensics.MLForensics_farzana.FAME_ML.lint_engine import getDataLoadCount, getModelLoadCounta, getDataPipelineCount

import lint_engine
import py_parser

@given(st.text())
def test_getDataLoadCount(py_file):
    try:
        data_load_count = lint_engine.getDataLoadCount(py_file)
        assert isinstance(data_load_count, int)
    except (ValueError, FileNotFoundError, SyntaxError) as e:
        # Handle specific exceptions separately if needed
        assert False, f"Exception occurred: {str(e)}"

@given(st.text())
def test_getModelLoadCounta(py_file):
    try:
        model_load_counta = lint_engine.getModelLoadCounta(py_file)
        assert isinstance(model_load_counta, int)
    except Exception as e:
        assert False, f"Exception occurred: {str(e)}"

@given(st.text())
def test_getDataPipelineCount(py_file):
    try:
        data_pipeline_count = lint_engine.getDataPipelineCount(py_file)
        assert isinstance(data_pipeline_count, int)
    except Exception as e:
        assert False, f"Exception occurred: {str(e)}"

@given(st.text())
def test_getPythonAtrributeFuncs(py_file):
    try:
        py_tree = py_parser.getPythonParseObject(py_file)
        attrib_funcs = py_parser.getPythonAtrributeFuncs(py_tree)
        assert isinstance(attrib_funcs, list)
    except (ValueError, FileNotFoundError, SyntaxError) as e:
        assert False, f"Exception occurred: {str(e)}"

@given(st.text())
def test_getFunctionAssignments(py_file):
    try:
        py_tree = py_parser.getPythonParseObject(py_file)
        func_assignments = py_parser.getFunctionAssignments(py_tree)
        assert isinstance(func_assignments, list)
    except (ValueError, FileNotFoundError, SyntaxError) as e:
        assert False, f"Exception occurred: {str(e)}"

if __name__ == "__main__":
    test_getDataLoadCount()
    test_getModelLoadCounta()
    test_getDataPipelineCount()
    test_getPythonAtrributeFuncs()
    test_getFunctionAssignments()
