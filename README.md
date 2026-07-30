# Long-Running-Agent-Memo Framework

An automated, operator-grade framework designed to research complex artificial intelligence topics—specifically long-running AI agents, autonomous execution loops, persistent agent memory architectures, trajectory management, and background task scheduling—and compile premium, investor-ready executive strategy memos.

The repository provides automated tools to extract information from primary sources, synthesize web and literature findings, and compile publication-quality drafts into polished Microsoft Word (.docx) and PDF formats.

---

## 1. Core Architecture & Project Features

*   **Custom Research Skill (`research-memo`)**: A structured, step-by-step framework located at `skills/research_memo/SKILL.md` to guide agents or developers through topic definition, multi-source research, outline approval, and executive drafting.
*   **High-Fidelity Document Compilers**: Custom Python export scripts powered by `python-docx` and `xhtml2pdf` to transform raw markdown drafts into beautiful, formatted Word and PDF outputs, adhering to professional typography standards.
*   **Elite Styling & Formatting Alignments**: Deep alignment with enterprise strategy memo conventions, utilizing strict structural patterns, role profile blockquotes, and comparative matrices.
*   **Structured Research Database**: Dedicated storage in `research/` for source-level findings, grounding all strategic assertions and architecture metrics in hard reality.

---

## 2. Repository Structure

Below is the directory tree of the framework:

```
long-running-agent-memo/
├── AGENTS.md            # Developer & agent architectural guidelines, rules, and structures
├── LICENSE              # MIT License
├── pyproject.toml       # Python package dependencies and metadata managed via uv
├── README.md            # Public-facing repository documentation and execution instructions
├── uv.lock              # Lockfile for precise virtual environment replication
├── docs/                # Style, formatting, and layout standards
│   ├── formatting.md    # Strict typographical rules, headings, and elements (no separator lines, no GitHub alerts)
│   └── writing_style.md # Tone and structure rules (pragmatic, operator-led, fact-driven, humble but expert)
├── inputs/              # User-provided primary source files (raw transcripts, manuals, PDFs)
├── reference/           # Master structural reference memos
├── research/            # Structured source-level findings and verbatim literature excerpts
├── output/              # Synthesized executive memo drafts, outlines, Word documents, and PDFs
│   ├── outline.md       # Approved structural blueprint for the memo
│   ├── memo.md          # Primary executive memo draft in markdown format
│   ├── memo.docx        # Polished Microsoft Word export
│   └── memo.pdf         # Beautiful PDF export
└── skills/              # Custom workspace integrations and execution scripts
    ├── research_memo/   
    │   └── SKILL.md     # Custom agent skill detailing the systematic research workflow
    └── scripts/         # Executable utility helper scripts
        ├── export_docx.py # Compiles a markdown memo to polished Word format
        ├── export_pdf.py  # Compiles a markdown memo to beautiful PDF format
        ├── read_docx.py   # Utility to extract clean text from a Word document
        └── read_pdf.py    # Utility to extract clean text from a PDF document
```

---

## 3. Setup & Environment

This repository utilizes `uv` as the default Python package manager for high-performance dependency tracking and virtual environment isolation.

### Prerequisites

*   Ensure Python 3.14+ (or Python 3.10+) is installed.
*   Ensure `uv` is installed and on your system `PATH`.

### Installation

Initialize the virtual environment and install project dependencies:

```powershell
# Create the virtual environment
uv venv

# Install project dependencies
uv sync
```

---

## 4. Operational Workflow

To generate a premium executive memo, follow the systematic workflow detailed in the custom skill:

### Step 1: Tone & Style Alignment
Ensure deep familiarity with `docs/writing_style.md` and `docs/formatting.md`. The memo must remain decisive, fact-grounded, and free of hype, avoiding horizontal lines (`---`) and developer alerts (`[!IMPORTANT]`) in favor of elegant blockquotes (`>`) and clear Level-3 numbered subheadings.

### Step 2: Solicit Research Focus Areas
Define the target research topics or organizational dynamics (e.g., long-running agent loops, context window compaction, tool permission boundaries, multi-agent coordination).

### Step 3: Scan Primary Source Inputs
Place highly trusted manuals, papers, or transcripts inside `inputs/`. Extract key insights to ground all downstream arguments.

### Step 4: Multi-Source Web & Science Research
Execute searches to gather relevant data. For each major source, create a dedicated file under `research/` cataloging:
1.  Source Citation (direct URL/DOI)
2.  Concise Summary
3.  Raw Verbatim Excerpts (containing precise metrics, arguments, and dates)

### Step 5: Outline Formulation
Draft the structural outline inside `output/outline.md` and align with stakeholders prior to writing the full draft.

### Step 6: Draft the Memo
Synthesize the facts and draft `output/memo.md` in strict alignment with formatting and writing rules.

### Step 7: Document Compilation
Run the export scripts to generate Word and PDF assets under `output/`.

---

## 5. Execution & Utility Commands

All scripts must be executed using the `uv run` pattern.

### Compiling Markdown drafts to PDF and Word (.docx)

By default, the export scripts target `output/memo.md` and generate outputs in the same directory:

```powershell
# Compile output/memo.md to Microsoft Word (output/memo.docx)
uv run python skills/scripts/export_docx.py

# Compile output/memo.md to PDF (output/memo.pdf)
uv run python skills/scripts/export_pdf.py
```

To compile a custom markdown file or define a specific output destination, supply them as arguments:

```powershell
# Custom Word Export
uv run python skills/scripts/export_docx.py output/outline.md output/outline.docx

# Custom PDF Export
uv run python skills/scripts/export_pdf.py output/outline.md output/outline.pdf
```

### Parsing Text from Source Files

Extract clean text from primary Word or PDF inputs for easy scanning:

```powershell
# Parse PDF source text
uv run python skills/scripts/read_pdf.py inputs/source_document.pdf tmp/extracted_text.txt

# Parse Word source text
uv run python skills/scripts/read_docx.py inputs/source_transcript.docx tmp/extracted_text.txt
```

---

## 6. Premium Standards Checklist

Before sharing any compiled memos, verify that:
*   [x] **No Placeholders**: All bracketed variables, incomplete metrics, and date templates have been fully resolved.
*   [x] **No Forbidden Formatting**: No horizontal separator lines (`---`) or GitHub-style alerts are present in final draft files.
*   [x] **First-Use Bolding**: Crucial terminology, custom roles, and specific platform names are bolded upon their first appearance in each section.
*   [x] **Sequential Numbering**: All major Level-2 headings are numbered sequentially.
*   [x] **Operator Tone**: The narrative is analytical, expert, and grounded in structural realities rather than promotional buzzwords.
