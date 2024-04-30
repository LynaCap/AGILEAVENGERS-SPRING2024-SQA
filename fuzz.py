# fuzz.py

from hypothesis import given, strategies as st
import traceback
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("fuzz_output.log"),
                        logging.StreamHandler(sys.stdout)
                    ])

# Import the methods from their respective modules
from MLForensics.MLForensics_farzana.FAME_ML.py_parser import getPythonAtrributeFuncs, getFunctionAssignments
from MLForensics.MLForensics_farzana.FAME_ML.lint_engine import getDataLoadCount, getModelLoadCounta, getDataPipelineCount

import lint_engine
import py_parser

def log_to_file(message):
    """Helper function to log messages to a text file."""
    with open("fuzz_report.txt", "a") as f:
        f.write(message + "\n")

@given(st.text())
def test_getDataLoadCount(py_file):
    try:
        data_load_count = lint_engine.getDataLoadCount(py_file)
        log_message = f"test_getDataLoadCount: Success, Result: {data_load_count}"
        log_to_file(log_message)
        logging.info(log_message)
    except Exception as e:
        error_message = traceback.format_exc()
        log_to_file(f"test_getDataLoadCount: Failure, Error: {error_message}")
        logging.error(f"test_getDataLoadCount: Failure, Error: {error_message}")

@given(st.text())
def test_getModelLoadCounta(py_file):
    try:
        model_load_counta = lint_engine.getModelLoadCounta(py_file)
        log_message = f"test_getModelLoadCounta: Success, Result: {model_load_counta}"
        log_to_file(log_message)
        logging.info(log_message)
    except Exception as e:
        error_message = traceback.format_exc()
        log_to_file(f"test_getModelLoadCounta: Failure, Error: {error_message}")
        logging.error(f"test_getModelLoadCounta: Failure, Error: {error_message}")

@given(st.text())
def test_getDataPipelineCount(py_file):
    try:
        data_pipeline_count = lint_engine.getDataPipelineCount(py_file)
        log_message = f"test_getDataPipelineCount: Success, Result: {data_pipeline_count}"
        log_to_file(log_message)
        logging.info(log_message)
    except Exception as e:
        error_message = traceback.format_exc()
        log_to_file(f"test_getDataPipelineCount: Failure, Error: {error_message}")
        logging.error(f"test_getDataPipelineCount: Failure, Error: {error_message}")

@given(st.text())
def test_getPythonAtrributeFuncs(py_file):
    try:
        py_tree = py_parser.getPythonParseObject(py_file)
        attrib_funcs = py_parser.getPythonAtrributeFuncs(py_tree)
        log_message = f"test_getPythonAtrributeFuncs: Success, Result: {attrib_funcs}"
        log_to_file(log_message)
        logging.info(log_message)
    except Exception as e:
        error_message = traceback.format_exc()
        log_to_file(f"test_getPythonAtrributeFuncs: Failure, Error: {error_message}")
        logging.error(f"test_getPythonAtrributeFuncs: Failure, Error: {error_message}")

@given(st.text())
def test_getFunctionAssignments(py_file):
    try:
        py_tree = py_parser.getPythonParseObject(py_file)
        func_assignments = py_parser.getFunctionAssignments(py_tree)
        log_message = f"test_getFunctionAssignments: Success, Result: {func_assignments}"
        log_to_file(log_message)
        logging.info(log_message)
    except Exception as e:
        error_message = traceback.format_exc()
        log_to_file(f"test_getFunctionAssignments: Failure, Error: {error_message}")
        logging.error(f"test_getFunctionAssignments: Failure, Error: {error_message}")

if __name__ == "__main__":
    test_getDataLoadCount()
    test_getModelLoadCounta()
    test_getDataPipelineCount()
    test_getPythonAtrributeFuncs()
    test_getFunctionAssignments()

