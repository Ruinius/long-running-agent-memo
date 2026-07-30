# Long-Running-Agent-Memo Reference Documentation (AGENTS.md)

Welcome! This file serves as the core developer and agent reference for the `long-running-agent-memo` project. It defines the system architecture, directory structure, coding standards, environment instructions, and workflow rules.

---

## 1. Project Overview
The `long-running-agent-memo` repository provides a structured, automated framework to research complex topics (specifically around long-running AI agents, autonomous execution loops, agentic memory architectures, trajectory management, and background task scheduling) and synthesize premium, operator-grade executive memos. It contains helper scripts to extract information from primary PDF/Word sources and compile finished markdown drafts into beautifully formatted Word (.docx) and PDF files.

---

## 2. Directory Structure

Below is the complete file and directory layout of the repository:

* **`AGENTS.md`** - *[This File]* Primary reference for developers/agents. Contains structure, environment rules, and guidelines.
* **`LICENSE`** - MIT License for this codebase.
* **`README.md`** - Public-facing project documentation outlining overview, installation, custom skills, and execution commands.
* **`pyproject.toml`** - Python package configuration and dependencies managed via `uv`.
* **`uv.lock`** - Dependency lockfile managed via `uv`.
* **`docs/`** - Guidelines and documentation.
  * `docs/formatting.md` - Technical markdown formatting, layout, and typographic rules.
  * `docs/writing_style.md` - Core writing guidelines detailing tone, structure, and style.
* **`inputs/`** - Directory for primary source files (e.g., raw PDFs, text transcripts) provided by the user.
* **`reference/`** - Reference materials that establish style and formatting (e.g., standard PDFs or pre-existing memos).
* **`research/`** - Structured source-level research profiles generated during Step 4 of the workflow.
* **`output/`** - Finished memo drafts in markdown, Word (.docx), and PDF formats.
  * `output/outline.md` - Structured, fact-grounded blueprint for the final executive memo.
  * `output/memo.md` - Primary executive memo draft in markdown format.
  * `output/memo.docx` - Compiled Microsoft Word version.
  * `output/memo.pdf` - Compiled PDF version.
* **`skills/`** - Custom tools and workspace integrations.
  * `skills/research_memo/SKILL.md` - Definition of the `research-memo` custom agent skill.
  * `skills/scripts/` - Executable Python helper utilities.
    * `skills/scripts/export_docx.py` - Script to compile markdown to polished Word files.
    * `skills/scripts/export_pdf.py` - Script to compile markdown to beautiful PDFs.
    * `skills/scripts/read_docx.py` - Script to extract text from a Word document.
    * `skills/scripts/read_pdf.py` - Script to extract text from a PDF file.
* **`tmp/`** - Local temporary workspace for scratch files and logs.

---

## 3. Environment & Tooling Rules

* **Operating System**: Windows (using PowerShell `pwsh` for terminal operations).
* **Virtual Environment**: Managed exclusively via `uv`. Never use raw `pip` or `venv`.
* **Environment Setup**: Initialize with `uv venv`.
* **Execution Pattern**: Always execute Python scripts with `uv run`. For example:
  ```powershell
  uv run python skills/scripts/export_docx.py
  ```
* **Adding Dependencies**: Use `uv add <package>` to add new libraries to the environment, automatically updating `pyproject.toml` and `uv.lock`.
* **Temporary Files**: Save any scratch scripts, local testing files, and logs inside `tmp/` (never in the project root, user home, or `C:\`).

---

## 4. Architectural Patterns & Guidelines

### Writing Style & Formatting Alignment
All compiled memos must strictly follow `docs/writing_style.md` and `docs/formatting.md`:
* **Tone**: Professional, operator-led, fact-driven, decisive, and humble but expert.
* **Layout**: Standardized metadata headers, clear chapter numbering, comparative tables, and structured subheading-led flows.
* **Format Restrictions**: 
  * **AVOID** developer callout blocks or GitHub-style alerts (such as `[!IMPORTANT]`, `[!NOTE]`, `[!WARNING]`) in executive outputs.
  * **AVOID** horizontal separator lines (`---`) in output documents.
  * **USE** standard blockquotes (starting with `>`) for highlighting key insights, role profiles, and takeaways.

### Export Guidelines
The scripts inside `skills/scripts/` are used to convert markdown sources to final documents.
* Target files should always be output under `output/` with matching basenames (e.g., `output/memo.md` compiles to `output/memo.docx` and `output/memo.pdf`).
* Never overwrite client-shared reference source-of-truth files in `reference/` or other directories.
