# Plano: esteira CI/CD com GitHub Actions (Python + uv + ruff + ty + pytest + make)

## Problema
Configurar uma esteira CI/CD para um projeto Python simples no GitHub Actions, usando `uv` para ambiente/dependências e `make` como interface única para lint, type-check e testes.

## Abordagem proposta
1. Estruturar o projeto Python com `pyproject.toml`, dependências de runtime/dev e configuração de ferramentas (`ruff`, `ty`, `pytest`) gerenciadas por `uv`.
2. Criar `Makefile` com alvos padronizados para instalar dependências, lint, format/check, type-check e testes.
3. Implementar workflow de **CI** (`.github/workflows/ci.yml`) para PR/push rodando `make` (ruff + ty + pytest).
4. Implementar workflow de **CD** (`.github/workflows/cd.yml`) para tags/release (build de pacote e publicação, com opção de upload de artifacts e/ou publish para PyPI via segredo).
5. Garantir consistência local/CI: os mesmos comandos do `Makefile` usados no pipeline.

## Todos
- **bootstrap-python-uv**
  - Criar estrutura inicial (`src/`, `tests/`) e `pyproject.toml`.
  - Configurar `uv` com deps de desenvolvimento: `ruff`, `ty`, `pytest`.
  - Definir configuração mínima das ferramentas no `pyproject.toml`.

- **create-makefile-targets**
  - Criar `Makefile` com alvos: `install`, `lint`, `type`, `test`, `ci`.
  - Garantir que todos os alvos executem via `uv run`.

- **create-ci-workflow**
  - Criar `.github/workflows/ci.yml` com gatilhos `push` e `pull_request`.
  - Instalar Python + `uv`, restaurar cache de dependências quando aplicável.
  - Executar `make ci`.

- **create-cd-workflow**
  - Criar `.github/workflows/cd.yml` com gatilho em tags (`v*`) e `workflow_dispatch`.
  - Gerar build do pacote.
  - Publicar artifacts e preparar publicação (PyPI) via segredo/configuração segura.

- **document-usage**
  - Atualizar `README` com instruções locais (`uv`, `make`) e visão geral dos workflows.

## Dependências entre todos
- `create-makefile-targets` depende de `bootstrap-python-uv`.
- `create-ci-workflow` depende de `create-makefile-targets`.
- `create-cd-workflow` depende de `bootstrap-python-uv`.
- `document-usage` depende de `create-ci-workflow` e `create-cd-workflow`.

## Notas
- `ty` pode variar conforme o ecossistema/projeto; se houver incompatibilidade, alinhar versão e comando exatos no `Makefile`.
- Publicação em PyPI exige segredo/token (ou Trusted Publisher); sem credenciais, o CD deve ao menos gerar artifacts de release.
- A esteira deve falhar explicitamente em lint/type/test, sem fallback silencioso.
