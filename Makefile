PROJECT_NAME := $(shell basename `pwd`)
PACKAGE_NAME := my_project_template

.PHONY: clean clean-test clean-pyc clean-build docs help test test-all
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -fr allure_report

lint: ## check style with flake8
	uv tool run ruff check

behave: clean-test ## run the behave tests, generate and serve report
	- uv run behave -f allure_behave.formatter:AllureFormatter -o allure_report
	allure serve allure_report

pytest: clean-test ## run tests quickly with the default Python
	uv run pytest

test: clean-test ## run all(BDD and unit) tests
	uv run pytest
	uv run behave

coverage: ## check code coverage quickly with the default Python
	coverage run --source my_project_template -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

dist: clean ## builds source and wheel package
	uv build
	ls -l dist

docker-build: ## build a docker image for the service
	docker build -t my-project-template-service:0.0.1 .

docker: docker-build ## build a docker image and run the service
	docker run --name my-project-template -p 8080:8080 my-project-template-service:0.0.1

install: clean ## install the package to the active Python's site-packages
	uv sync --all-groups
	pre-commit install

venv: ## creates a Python3 virtualenv environment in venv
	uv venv --prompt $(PROJECT_NAME)-venv

activate: ## activate a virtual environment. Run `make venv` before activating.
	@echo "====================================================================="
	@echo "To activate the new virtual environment, execute the following from your shell"
	@echo "source venv/bin/activate"
