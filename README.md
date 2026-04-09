# ci-cd-test

Projeto Python simples com FastAPI, tipagem explícita e modelos Pydantic.

## Rodando localmente com uv

```bash
make install
make run
```

API disponível em `http://127.0.0.1:8000`.

## Qualidade e testes

```bash
make lint
make type
make test
make ci
```

## Pre-commit

```bash
make pre-commit-install
make pre-commit-run
```

## GitHub Actions

- `CI` (`.github/workflows/ci.yml`): roda em `push` para `main` e `pull_request`, executando `make ci`.
- `CD` (`.github/workflows/cd.yml`): roda em tag `v*` e `workflow_dispatch`, gera artefatos em `dist/` e publica no PyPI se `PYPI_API_TOKEN` estiver configurado.
