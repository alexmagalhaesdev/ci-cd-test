.PHONY: install lint format type test ci build run pre-commit-install pre-commit-run

install:
	uv sync --all-groups

lint:
	uv run ruff check .

format:
	uv run ruff format .

type:
	uv run ty check .

test:
	uv run pytest $(PYTEST_ARGS)

ci: lint type test

build:
	uv run python -m build

run:
	uv run uvicorn app.main:app --reload

pre-commit-install:
	uv run pre-commit install

pre-commit-run:
	uv run pre-commit run --all-files
