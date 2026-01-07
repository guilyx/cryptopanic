.PHONY: help install install-dev test test-cov lint format type-check clean build

help:
	@echo "Available commands:"
	@echo "  make install       - Install the package"
	@echo "  make install-dev   - Install the package with dev dependencies"
	@echo "  make test          - Run tests"
	@echo "  make test-cov     - Run tests with coverage"
	@echo "  make lint          - Run linters (ruff, black check)"
	@echo "  make format        - Format code (black, ruff)"
	@echo "  make type-check    - Run type checker (mypy)"
	@echo "  make clean         - Clean build artifacts"
	@echo "  make build         - Build the package"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest

test-cov:
	pytest --cov=cryptopanic --cov-report=html --cov-report=term-missing

lint:
	ruff check .
	black --check .
	mypy cryptopanic

format:
	black .
	ruff check --fix .

type-check:
	mypy cryptopanic

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf htmlcov/
	rm -rf coverage.xml
	find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

build:
	python -m build
