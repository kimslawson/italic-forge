.PHONY: check format lint test type

UV_CACHE_DIR ?= .uv-cache
export UV_CACHE_DIR

check: lint type test

format:
	uv run ruff format .

lint:
	uv run ruff check .
	uv run ruff format --check .

type:
	uv run mypy

test:
	uv run pytest
