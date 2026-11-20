**English** · [Dansk](Step-1-Foundation-da) · [Bahasa Malaysia](Step-1-Foundation-ms)

# Step 1: Project foundation

![Step 1: the first page with five empty lists](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-01.png)

## What we built

A configured Python project that serves a first page: a blue board with five empty lists named Backlog, To Do, In Progress, Review and Done.

## What we gained

- **A local virtual environment.** `python -m venv .venv` keeps the project's packages apart from the system Python, and `python -m pip install --upgrade pip` keeps pip current.
- **One project file.** `pyproject.toml` holds the Python version (3.13 or newer), the empty list of runtime dependencies and the settings of pytest, ruff and mypy.
- **Constants in one place.** `constants.py` holds every literal, so a change is made once.
- **Layers.** `domain`, `application`, `infrastructure` and `presentation` keep the rules apart from the database and the web; imports point inward.
- **MVC for the web.** A controller answers the request and a view builds the HTML.
- **Tests first.** pytest runs unit tests of the view and integration tests of a real server on a free port.
- **Documentation from the source.** Doxygen comments and a `Doxyfile` build the code documentation.
- **Safe screenshots.** A Docker container with a headless browser takes the screenshot, so the desktop is never used.
- **A scan before every push.** opengrep checks the code against local rules.
