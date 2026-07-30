---
name: research-memo
description: >-
  A custom agent skill to research and draft premium memos. It structures the process
  of style extraction, topic gathering, primary input analysis, multi-source research
  synthesis, outline formulation, and draft development for long-running AI agents.
---

# Research Memo Custom Skill

## Overview
This skill provides a systematic framework for conducting deep research on specialized AI and long-running agentic topics and producing a premium, operator-grade memo. It guides the agent through style alignment, topic gathering, scanning user-provided primary sources, executing target research, generating structured source-level findings, and drafting the final memo.

## Directory Structure
- `inputs/` - Primary source files (PDFs, text, transcripts, architecture specs) provided by the user.
- `reference/` - Core structural references or style guides.
- `docs/writing_style.md` - Synthesized style, tone, terminology, and structural rules.
- `research/` - Source-level research findings and raw extractions.
- `output/` - Final drafts and polished versions of the research memo.

## Workflow

### Step 1: Synthesize/Update Writing Style Guidelines
Check if `docs/writing_style.md` exists and is up to date with any files in the `reference/` folder. Ensure adherence to:
- **Tone**: Professional, operator-led, decisive, authoritative.
- **Structural Patterns**: Upfront summary, matrices, ranked competencies, actionable headings.
- **Style Conventions**: Avoid horizontal separator lines ("---") and developer alert flags ("[!IMPORTANT]"); use clean standard blockquotes (">") instead.

### Step 2: Solicit Research Topics
Ask the user for the specific research topics or focal areas to cover in the memo (e.g., long-horizon task execution, context compaction, state persistence, agentic tool safety).

### Step 3: Scan Primary Source Inputs
Look in the `inputs/` folder for any manuals, PDFs, or files placed by the user. Extract key sections, tables, and frameworks, grounding core arguments in these inputs.

### Step 4: Perform Web & API Research
For each topic, perform targeted research and gather relevant data. Create dedicated markdown files in `research/` with:
1. **Source Citation**: Direct URL, title, or filename.
2. **Short Summary**: A concise 2-3 sentence overview of the source's main point.
3. **Raw Relevant Excerpts**: Original verbatim quotes, data points, and metrics.

### Step 5: Formulate & Align on Memo Outline
Draft the structural outline inside `output/outline.md` and align with stakeholders prior to writing the full draft.

### Step 6: Draft the Memo
Synthesize findings from `research/` and draft the final memo in `output/memo.md`. Ensure strict alignment with formatting and writing rules.

### Step 7: Export the Memo (On User Request Only)
Export the final draft markdown file to Word (DOCX) and PDF formats using the scripts inside `skills/scripts/` ONLY when explicitly requested by the user. Do not perform automatic exports.

## Common Mistakes
- **Hype and Buzzwords**: Avoid speculative or overly promotional marketing language. Stick to clear, operator-grade insights.
- **Vague Citations**: In the research phase, always save exact source URLs or names along with the raw verbatim excerpts. Do not summarize from memory.
- **Unstructured Drafting**: Skipping Step 5 (Outline approval) leading to poorly organized or disjointed drafts.
- **Overwriting Source of Truth Files**: Always verify output filenames (`memo.docx` / `memo.pdf`) to protect client-shared reference versions.
