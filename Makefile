PY_ENV = venv
PY_BIN = $(PY_ENV)/bin

PY_DIR = python
PYTEST_ARGS=

all: test_py

$(PY_BIN)/python3:
    @ python3 -m venv $(PY_ENV)
    @ chmod +x $(PY_BIN)/activate
    @ ./$(PY_BIN)/activate

$(PY_BIN)/pip: $(PY_BIN)/python3

$(PY_BIN)/pytest: $(PY_BIN)/pip
    @ $(PY_BIN)/pip3 install -r $(PY_DIR)/requirements.txt

test_py: $(PY_BIN)/pytest
    @ $(PY_BIN)/pytest $(PY_DIR)/**/*.py $(PYTEST_ARGS)

test_py_d: PYTHON_TEST_ARG += -vv
test_py_d: test_py

.PHONY: test_py test_py_d

clean:
    @ rm -rf */.pytest_cache
    @ rm -rf .pytest_cache
    @ rm -rf .coverage

fclean: clean
    @ rm -rf $(PYTHON_ENV_NAME)

.PHONY: clean fclean
