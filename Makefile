.PHONY: install test build release clean

install:
	pip install '.[dev]'

test:
	python run_tests.py

coverage:
	coverage run run_tests.py
	coverage report
	coverage xml

build:
	python -m build

clean:
	rm -rf dist *.egg-info coverage.xml build

lint:
	ruff format
	ruff check . --fix
	mypy . --install-types --non-interactive --exclude build
