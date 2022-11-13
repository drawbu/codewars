PYTHON_BASE_INTERPRETER=python3
PYTHON_ENV_NAME=venv
PYTHON_ENV=$(PYTHON_ENV_NAME)/bin
PYTHON_DIR=python
PYTHON_TEST_ARG=

$(PYTHON_ENV):
	@ $(PYTHON_BASE_INTERPRETER) -m venv $(PYTHON_ENV_NAME)
	@ $(PYTHON_ENV)/pip install -r requirements.txt

test: $(PYTHON_ENV)
	@ $(PYTHON_ENV)/pytest python/**/*.py $(PYTHON_TEST_ARG)

adv_test:
	@ make test PYTHON_TEST_ARG=-vv

clean:
	@ rm -rf */.pytest_cache
	@ rm -rf $(PYTHON_ENV_NAME)
