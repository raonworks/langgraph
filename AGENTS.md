# AGENTS.md

## Running the project

- `uv` is NOT installed on this machine and there is no `uv.lock`. Use the existing venv directly: `.venv\Scripts\python src\main.py` (project requires Python 3.14; system python is 3.14.6).
- `main.py` calls a remote Ollama server at `http://server.raonworks.com:11434` (hardcoded, `ChatOllama`). Running it requires network access to that host. No API key needed.

## Dependency gotcha

- `pyproject.toml` declares `dependencies = []` but `main.py` imports `langchain_*`, `pydantic`, etc. They are installed ad-hoc in `.venv` only and not declared anywhere. Do NOT run `uv sync`/`pip install`/fresh env setup expecting the project to keep working, and don't treat the empty dep list as authoritative.

## Structure & known issues

- The project contains multiple Python files: `src/main.py`, `src/second.py`, and `src/state.py`.
- `src/main.py` is a work-in-progress experiment using LangChain with Ollama integration:
  - Currently uses `ChatOllama` with model "llama3:8b"
  - Has commented-out `ChatOpenAI` and `ChatGoogleGenerativeAI` configurations
  - Includes `ExamParser` and `JsonOutputParser` definitions but they are not currently wired into the chain
  - The chain is set up as `prompt | llm` (not using the parser)
- `src/second.py` contains a LangGraph implementation with a simple state graph that returns "hi, langgraph!!!"
- `src/state.py` contains basic state definitions and a simple addition operation
- The console script `[project.scripts] langchain = "langchain:main"` is broken/stale — there is no `langchain` package dir (file is `src/main.py`), so the `langchain` CLI does not work.

## Conventions

- No tests, linter, formatter, typecheck, or CI configured. There is no verify step to run.
- Commit messages are short Korean phrases (e.g. "PromptTemplate 사용", "partial valriable 작업").
- Comments and template strings in `main.py` are written in Korean; keep that style.
