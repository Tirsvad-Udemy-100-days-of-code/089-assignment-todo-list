**English** · [Dansk](Step-6-Wrap-Up-da) · [Bahasa Malaysia](Step-6-Wrap-Up-ms)

# Step 6: Wrap-up and reflection

![Step 6: the finished board](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-06.png)

## What we built

The last step adds no feature. It checks that the whole project works for the people it is for: a course participant who clones it, creates a `.venv`, runs the tests and starts the board, and a visitor who only reads the description, the README and this wiki. The full quality pass (tests, coverage, the browser tests in a container, source documentation, the code scan and the framework checks) ran on the final code.

## What we gained

- **A project that can be handed over.** The README setup was followed literally in a clean container.
- **One page set in three languages**, with a sidebar and a language line on every page.
- **A reflection** (below) that names what was easy, what was hard and what we would change.

## Reflection

- **Approach.** Plan first: a business case, stakeholders, a project plan and six milestones were accepted before the first line of code. Each milestone was one branch, one review and one pull request, and each step produced a screenshot and a wiki page.
- **What was easy.** The domain rules and SQLite. A board, lists and cards are a small model, and the layers kept the rules free of HTTP and SQL, so most tests ran in milliseconds against an in-memory store.
- **What was hard.** Drag and drop. The browser events are low level: the drop position has to be computed from the pointer, and a test must drag with a real browser. Dates were also harder than expected, because a forgiving parser accepts shapes you do not want.
- **Biggest learning.** A framework is a choice with a cost. The standard library (`http.server`, `sqlite3`) was enough, so the project has no runtime dependencies and the reader sees every layer. A web framework would have saved routing code; it would also have hidden the lesson.
- **What to do differently.** Start the browser tests earlier, give the router a small test table from day one, and decide on the stack with the user before the first milestone, so a late change of mind costs nothing.
