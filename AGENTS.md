# AGENTS.md

## Running the project
- `uv` is NOT installed on this machine and there is no `uv.lock`. Use the existing venv directly: `.venv\Scripts\python src\main.py` (project requires Python 3.14; system python is 3.14.6).
- `main.py` calls a remote Ollama server at `http://server.raonworks.com:11434` (hardcoded, `ChatOllama`). Running it requires network access to that host. No API key needed.

## Dependency gotcha
- `pyproject.toml` declares `dependencies = []` but `main.py` imports `langchain_*`, `pydantic`, etc. They are installed ad-hoc in `.venv` only and not declared anywhere. Do NOT run `uv sync`/`pip install`/fresh env setup expecting the project to keep working, and don't treat the empty dep list as authoritative.

## Structure & known issues
- Only real code is `src/main.py`. `src/second.py` is an empty, untracked file.
- `main.py` is a work-in-progress experiment: commented-out `ChatOpenAI`/`ChatGoogleGenerativeAI` blocks, and `ExamParser`/`JsonOutputParser` are defined but not wired into the chain (currently `prompt | llm`, output is plain text).
- The console script `[project.scripts] langchain = "langchain:main"` is broken/stale — there is no `langchain` package dir (file is `src/main.py`), so the `langchain` CLI does not work.

## Conventions
- No tests, linter, formatter, typecheck, or CI configured. There is no verify step to run.
- Commit messages are short Korean phrases (e.g. "PromptTemplate 사용", "partial valriable 작업").
- Comments and template strings in `main.py` are written in Korean; keep that style.
