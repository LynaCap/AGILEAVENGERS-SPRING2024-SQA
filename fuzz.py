# fuzz.py

from hypothesis import given, strategies as st
import traceback
import sys

# Import the methods from their respective modules
from MLForensics.MLForensics_farzana.FAME_ML.py_parser import getPythonAtrributeFuncs, getFunctionAssignments
from MLForensics.MLForensics_farzana.FAME_ML.lint_engine import getDataLoadCount, getModelLoadCounta, getDataPipelineCount

import lint_engine
import py_parser

# Function to handle the writing results to a file
def log_to_file(message):
    with open("fuzz_report.txt", "a") as f:
        f.write(message + "\n")

@given(st.text())
def test_getDataLoadCount(py_file):
    try:
        data_load_count = lint_engine.getDataLoadCount(py_file)
        log_to_file(f"test_getDataLoadCount: Success, Result: {data_load_count}")
    except Exception as e:
        log_to_file(f"test_getDataLoadCount: Failure, Error: {traceback.format_exc()}")

@given(st.text())
def test_getModelLoadCounta(py_file):
    try:
        model_load_counta = lint_engine.getModelLoadCounta(py_file)
        log_to_file(f"test_getModelLoadCounta: Success, Result: {model_load_counta}")
    except Exception as e:
        log_to_file(f"test_getModelLoadCounta: Failure, Error: {traceback.format_exc()}")

@given(st.text())
def test_getDataPipelineCount(py_file):
    try:
        data_pipeline_count = lint_engine.getDataPipelineCount(py_file)
        log_to_file(f"test_getDataPipelineCount: Success, Result: {data_pipeline_count}")
    except Exception as e:
        log_to_file(f"test_getDataPipelineCount: Failure, Error: {traceback.format_exc()}")

@given(st.text())
def test_getPythonAtrributeFuncs(py_file):
    try:
        py_tree = py_parser.getPythonParseObject(py_file)
        attrib_funcs = py_parser.getPythonAtrributeFuncs(py_tree)
        log_to_file(f"test_getPythonAtrributeFuncs: Success, Result: {attrib_funcs}")
    except Exception as e:
        log_to_file(f"test_getPythonAtrributeFuncs: Failure, Error: {traceback.format_exc()}")

@given(st.text())
def test_getFunctionAssignments(py_file):
    try:
        py_tree = py_parser.getPythonParseObject(py_file)
        func_assignments = py_parser.getFunctionAssignments(py_tree)
        log_to_file(f"test_getFunctionAssignments: Success, Result: {func_assignments}")
    except Exception as e:
        log_to_file(f"test_getFunctionAssignments: Failure, Error: {traceback.format_exc()}")

if __name__ == "__main__":
    test_getDataLoadCount()
    test_getModelLoadCounta()
    test_getDataPipelineCount()
    test_getPythonAtrributeFuncs()
    test_getFunctionAssignments()

