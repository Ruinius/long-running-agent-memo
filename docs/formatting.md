# Executive Memo Formatting Standards

This document establishes the strict markdown formatting, typography, and layout rules for enterprise AI strategy memos.

All generated memos must strictly adhere to these guidelines to ensure a premium, publisher-grade aesthetic.

---

## 1. Metadata Block

Every memo must begin with a standardized metadata header to establish the document context. Do not use horizontal lines or decorative boxes around this block.

### Structure Template:
```markdown
# [Full Document Title]

**Author:** [Author Name]  
**Date:** [Month Year]  
**Classification:** [e.g., AI Strategy Memo]  
**Audience:** [Target Audience, e.g., Enterprise AI Leaders, Executives, Investors]
```

> **Important Syntax Note:** Each metadata line (except the final one) must end with precisely **two trailing spaces** to force a clean HTML line break (`<br>`) in standard markdown rendering without initiating a new paragraph block.

---

## 2. Heading Hierarchy & Numbering

Maintain a clean, logical heading structure to ensure high scannability.

* **Level 1 Heading (`#`)**: Used **exclusively** once for the document title at the very top of the page.
* **Level 2 Headings (`##`)**: Used for the "Executive Summary" and main numbered chapters.
  * Chapter titles must be numbered sequentially: `## 1. First Major Chapter`, `## 2. Second Major Chapter`.
* **Level 3 Headings (`###`)**: Used for subsections, case studies, specific role descriptions, or strategic imperatives.
  * Example: `### Long-Running Loop Architecture`
  * Example: `### Role 1: The Strategist — The "What"` (Note the space-surrounded em dash ` — ` for structural clarity in headers).

---

## 3. Structural Elements & Styling

### 3.1. Standard Comparative Matrices (Tables)
Use markdown tables to compare multiple dimensions or entities. 
* **Header Alignment**: Left-align all columns using `:---` in the alignment row.
* **First Column Style**: Bold the category names in the leftmost column to act as clean row labels (e.g., `**Memory Model**`).
* **Content Density**: Cells must be dense, clear, and highly specific.

#### Markdown Template:
```markdown
| | Entity A | Entity B |
| :--- | :--- | :--- |
| **Dimension 1** | Value A1 | Value B1 |
| **Dimension 2** | Value A2 | Value B2 |
```

### 3.2. Role Profiles & High-Impact Callouts
Highlight key definitions, roles, or insights using a dedicated blockquote pattern:
* Use a Level 3 heading to introduce the element.
* Follow the heading immediately with a single-paragraph blockquote (`>`) starting with a bolded label (e.g., `**Profile:**`, `**Definition:**`).
* Place all supporting analysis and details in standard paragraphs immediately below the blockquote block (do not indent these paragraphs with `>`).

#### Markdown Template:
```markdown
### Role 1: The Strategist — The "What"

> **Profile:** Elite, technically fluent hybrid talent—frequently ex-MBB consultants, former product managers, or deep domain experts—with exceptional communication skills and a demonstrated ability to earn executive respect.

The Strategist's mandate is to define the operational roadmap...
```

---

## 4. Typography & Punctuation Conventions

* **Em Dash (`—`)**: Use standard em dashes without spaces to connect parenthetical thoughts or add emphasis within paragraphs (e.g., `model competition—it is a deployment competition`). Use space-surrounded em dashes (` — `) only in Level 3 headers to divide a title.
* **Term Highlighting (Bolding)**: Bold key operational roles, custom platforms, and specialized terms on their first appearance in a section (e.g., `**Autonomous Loop**`, `**Context Compaction**`).
* **List Usage**: Avoid long, simple bulleted lists in the main body. Instead, write in dense, analytical paragraphs or use Level 3 subheadings to structure major points. When bulleted lists are necessary, keep them concise and use standard asterisks (`*`).

---

## 5. Prohibited Formatting Elements

To maintain the premium, operator-grade aesthetic of the memo, the following elements are **strictly forbidden**:

1. **No Horizontal Separator Lines (`---`)**: Never use three or more hyphens to draw a horizontal line between sections in final memo outputs.
2. **No Developer Alert Blocks / GitHub Callouts**: Absolutely do not use GitHub-style alert wrappers (such as `[!IMPORTANT]`, `[!NOTE]`, `[!WARNING]`, `[!TIP]`). Use standard blockquotes (`>`) instead.
3. **No Placeholders**: Never include empty templates, unresolved brackets (e.g., `[Insert Date Here]`), or unverified metrics. If a metric is unknown, it must be researched and fully resolved before compiling.
