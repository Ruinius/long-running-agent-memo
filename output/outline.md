# Executive Strategy Memo Outline: Building a Long-Running Autonomous Agents Business Unit

**Author:** Tiger Huang
**Date:** August 2026  
**Classification:** Autonomous AI Agent Growth Strategy
**Audience:** Executive Leadership

## Executive Summary

**1. Long-Running Autonomous Agents vs. Interactive Co-Pilots & Stateless Swarms:** The evolution of AI agents has unfolded across three distinct paradigms. First, interactive co-pilots emerged to assist users synchronously in real-time tasks like coding, writing, and research through direct turn-by-turn interactions. Second, agent swarms introduced parallel, multi-agent workflows—whether interactive or autonomous—built to maximize throughput for labor-intensive tasks, though remaining simple and stateless. Today, we have entered the era of long-running autonomous agents, engineered to operate independently like human digital workers over extended horizons of days and weeks. This autonomy relies on two structural pillars: **Durable Execution State**—the ability to persist process states, event logs, and tool actions so agents can hibernate, await human sign-offs, and resume cleanly across system restarts without losing context—and **Persistent Memory**, which maintains operational history, past decisions, and domain knowledge across sessions.

**2. High-Impact Market Opportunities & Industry Leaders:** While coding agents represent the most lucrative application area, AI-assisted software development is already a crowded market dominated by frontier labs and specialized startups. Consequently, the next best high-margin commercial opportunities for enterprise AI agent ventures lie in core business operations: **Outbound Business Development (BDR)** (prospect sourcing, contact enrichment, and lead qualification), **IT Service Management (ITSM)** (automated helpdesk ticket resolution and access provisioning), **Financial Services KYC & Loan Origination** (automated identity verification and underwriting packages), and **Enterprise Legacy Software Modernization** (automated dependency updates and codebase refactoring). Industry leadership is defined across pioneering platforms and open-source foundations:

- **Cognition AI (Scott Wu):** Co-founder & CEO Scott Wu highlights the strategic shift in software engineering, noting that _"Software engineers will operate more like architects, creatively structuring problems for armies of Devins to reliably execute on"_ (Scott Wu, Cognition AI Strategy Update, June 2026).
- **Sierra AI (Bret Taylor):** Co-founder Bret Taylor emphasizes the enterprise evolution toward autonomous action, stating that _"AI agents are emerging as the new digital front door for enterprises, taking direct business actions rather than merely serving as passive conversational interfaces"_ (Bret Taylor, Sierra AI Keynote, February 2026).
- **OpenWorker / DeepLearning.AI (Andrew Ng):** Framework creator Andrew Ng emphasized the shift to task completion at the OpenWorker launch, stating that _"The fundamental shift in AI is moving beyond conversational text responses to delivering finished work and tangible deliverables as a true digital co-worker"_ (Andrew Ng, OpenWorker Release, July 2026).

**3. Execution Strategy: FDE Pods as PMF SWAT Teams:** Capturing these high-margin opportunities requires deploying Forward Deployed Engineering (FDE) pods as the core growth engine for AI agent companies. Embedded directly within customer environments, these elite A-teams rapidly solve vertical product-market fit for AI agents across unique customer workflows. Crucially, FDE pods are neither routine SaaS implementation teams (which are unsustainably expensive to staff with AI talent) nor IT consulting practices (which rely on labor arbitrage). While SaaS vendors and consulting firms frequently attempt to adopt AI company language without altering their underlying products or services—creating market confusion—true FDE pods operate as a scarce pool of Silicon Valley talent, dedicated to building AI agent capabilities in the vertical.

---

## 1. Defining Long-Running Autonomous Agents: Architecture, State Persistence, and Market Reality

### Technical Definition and Core Primitives

Long-running autonomous agents are software workers built to operate over long time horizons using persistent memory and saved execution states. Unlike interactive co-pilots that rely on continuous back-and-forth engagement with the user, or stateless swarms that run quick batch jobs before clearing memory, long-running agents execute continuous background loops over hours, days, or weeks—responding to system events, scheduled timers, or database updates.

Three core capabilities govern long-running agent execution:

- **Durable Execution State:** Periodically saving work-in-progress, memory state, and tool action histories to persistent disk storage. If an agent hits an idle period or waits for a human approval, it hibernates safely and consumes zero AI compute tokens, resuming cleanly when triggered without losing context.
- **Isolated Digital Workspaces:** Secure, dedicated execution environments equipped with file systems, terminal access, and enterprise API connections.
- **Self-Correcting Planning:** Autonomous evaluation loops where agents monitor intermediate outputs, recognize errors or unexpected system responses, and adjust their strategy without waiting for human prompts.

#### Comparative Overview: Interactive AI Co-Pilots vs. Stateless Agent Swarms vs. Long-Running Autonomous Agents

| Feature                               | Interactive AI Co-Pilots                                         | Stateless Agent Swarms                                               | Long-Running Autonomous Agents                                                 |
| :------------------------------------ | :--------------------------------------------------------------- | :------------------------------------------------------------------- | :----------------------------------------------------------------------------- |
| **Execution Horizon**                 | Minutes (ephemeral, synchronous back-and-forth user sessions).   | Hours (short batch task loops).                                      | Days to Weeks (continuous background loops).                                   |
| **Memory & State Model**              | In-memory session context; resets when window closes.            | Message queues between agents; resets upon job completion.           | Persistent memory and durable execution state saved to storage.                |
| **Digital Workspaces**                | Sandboxed single-request tool calls.                             | Shared temporary scratchpads per agent.                              | Dedicated long-lived environments (file systems, terminal, enterprise APIs).   |
| **Decision Autonomy**                 | Human-guided, back-and-forth prompt interaction.                | Pre-defined task delegation across agents.                           | Autonomous self-reflection, trajectory tracking, and re-planning.              |
| **Human Interaction**                 | Direct, synchronous back-and-forth engagement.                   | Unattended batch execution; unhandled errors cause failure.          | Asynchronous pause-and-resume; hibernates while awaiting approvals.            |
| **Primary Operational Failure Modes** | Context exhaustion, prompt drift, immediate session termination. | Inter-agent coordination overhead, message flooding, error cascades. | Memory accumulation drift, circular retry loops, token budget overruns.        |
| **Core Enterprise Use Cases**         | Interactive code completion, pair writing, live document search. | Parallel web research, batch processing, data extraction.            | Autonomous BDR lead qualification, ITSM access automation, legacy refactoring. |

### End-to-End Operational Workflow: ITSM Long-Running Agent

> **Workflow Definition:** A long-running IT service agent maintains saved state across system events, security compliance checks, human sign-offs, and multi-system API calls over a multi-day lifecycle.

1. **Ticket Ingestion & Task Initialization:**
   - **Trigger:** An employee submits a helpdesk ticket requesting temporary elevated database access for production troubleshooting.
   - **Agent Action:** The agent wakes up on a webhook event, ingests the request details (User ID, requested system, duration, business reason), and creates a saved execution checkpoint.

2. **Policy Verification & Identity Pre-Checks:**
   - **Agent Action:** The agent queries enterprise identity systems (Okta, Entra ID) and HR records to verify employee identity, active department role, and security compliance standing.
   - **Evaluation:** It checks company access rules and determines that production database access requires manager approval and Security Operations sign-off.

3. **Hibernation & Approval Dispatch:**
   - **Agent Action:** The agent generates a risk-scored approval request with contextual links and posts it to Slack/Teams and ServiceNow.
   - **State Hibernation:** The agent serializes its complete execution context and tool state to persistent storage. It hibernates, consuming zero AI compute tokens while awaiting human approval.

4. **Event Re-Activation & Provisioning:**
   - **Trigger:** The security manager approves the request via Slack 14 hours later.
   - **Agent Action:** An incoming webhook re-activates the agent thread. The agent restores its saved state from storage, verifies the approval token, and calls access management tools (HashiCorp Vault, AWS IAM) to generate scoped, time-bound credentials.

5. **Verification, Audit Logging & Closure:**
   - **Agent Action:** The agent runs a synthetic test to confirm access is active, securely sends credential instructions to the user, and logs an immutable audit trail to security monitoring tools (Datadog, Splunk).
   - **Resolution:** The agent marks the ticket "Resolved", schedules an event timer to verify credential revocation when the time-to-live expires, and safely closes its execution thread.

---

## 2. High-Value Enterprise Use Cases: Workflows, Guardrails, and Quantitative KPIs

### Criteria for Ideal Early Agent Deployment

Early agent deployments succeed best in structured business workflows characterized by explicit decision rules, high transaction volume, clear security boundaries, and easily measured ROI.

Crucially, **general greenfield coding tools (building apps from scratch) have matured into an intensely saturated red-ocean market**, dominated by frontier model labs and developer tool startups (Cognition/Devin, Factory, OpenHands). Competing directly in generic coding tools offers poor differentiation for enterprise AI ventures.

Instead, high-value commercial opportunities lie in two areas:

1. **Core Enterprise Operations:** **Outbound BDR** (prospecting and qualification), **IT Service Management (ITSM)** (helpdesk ticket resolution and access provisioning), and **KYC & Financial Loan Origination** (identity verification and credit analysis).
2. **Enterprise Legacy Modernization:** **Legacy Codebase Modernization** (automated dependency updates, security vulnerability remediation, and COBOL/legacy Java refactoring across thousands of enterprise repositories), which addresses massive enterprise IT maintenance budgets rather than generic greenfield coding.

### Primary Use Case Deep Dives

#### Outbound BDR Agent: Lead Sourcing, Enrichment, and Qualification

> **Definition:** An autonomous sales worker that identifies, enriches, and qualifies prospective corporate accounts.

- **Workflow Execution:** Queries public and commercial databases to assemble prospect lists, enriches contact details, drafts tailored outreach campaigns, and evaluates prospect responses against Ideal Customer Profiles.
- **Guardrails:** Daily contact limits, automated opt-out enforcement, and mandatory handoffs to human account executives once qualification criteria are met.
- **Internal Dog-Fooding & Dual Benefit:** Powers the venture's own growth pipeline by sourcing enterprise buyer leads. The team refines data connectors and personalization logic on live prospect interactions while expanding its customer base.
- **Quantitative KPIs:** Cost per qualified opportunity, meeting booking rate, and data enrichment accuracy.

#### ITSM Agent: IT Helpdesk Automation and Access Management

> **Definition:** An autonomous IT software worker that ingests, diagnoses, and resolves corporate IT helpdesk tickets and user access requests.

- **Workflow Execution:** Monitors ticketing systems (Jira Service Management, ServiceNow, Slack/Teams), parses user requests, queries identity providers (Okta, Active Directory), executes automated password resets or software provisioning scripts, and closes tickets upon verification.
- **Guardrails:** Strict role-based access policies, mandatory human sign-off for elevated administrative permissions, and immutable execution logs.
- **Internal Dog-Fooding & Dual Benefit:** Automated internally to resolve employee IT requests, optimizing workflow triggers and API resolution scripts on live tickets before commercial enterprise deployment.
- **Quantitative KPIs:** 70–80% auto-resolution rate for tier-1 helpdesk tickets, mean time to resolution (MTTR) reduced from hours to seconds, and 100% compliance audit pass rate.

#### Financial Services Agent: KYC Processing, Document Verification, and Loan Origination

> **Definition:** An autonomous compliance specialist that automates applicant document intake, identity verification (KYC/AML), and credit risk analysis.

- **Workflow Execution:** Ingests applicant documents (tax returns, bank statements, corporate filings), queries credit bureaus and identity verification APIs, calculates risk metrics, and prepares complete underwriting packages with recommended credit terms.
- **Guardrails:** Strict adherence to financial regulations (FCRA, Fair Lending, KYC/AML), mandatory human sign-off on borderline credit scores, and immutable audit logging.
- **Internal Dog-Fooding & Partner Sandboxes:** AI ventures cannot originate loans internally. Instead, internal dog-fooding focuses on **internal vendor background checks, counterparty risk screening, and employee verification workflows**, while core loan origination modules are battle-tested in design-partner regulatory sandboxes prior to enterprise commercial launch.
- **Quantitative KPIs:** 80% faster processing time (minutes instead of days), 90%+ automated document parsing accuracy, zero compliance audit failures, and lower processing cost per application.

#### Tail Procurement Agent: Automating Supplier RFQs

> **Definition:** An autonomous procurement worker that manages request-for-quote (RFQ) cycles across secondary and tertiary supplier catalogs.

- **Workflow Execution:** Scrapes internal ERP requisitions, identifies candidate suppliers, issues standardized RFQs, compiles incoming quotes against corporate rules, and recommends purchase decisions.
- **Guardrails:** Fixed spending caps, pre-approved vendor whitelists, and mandatory human approval whenever quote prices vary beyond set limits.
- **Internal Dog-Fooding & Dual Benefit:** Deploying the agent internally automates the venture’s own vendor purchasing, sharpening quote-parsing loops on live company spending while cutting tail procurement overhead by 8–12%.
- **Quantitative KPIs:** 75% faster RFQ cycles (reduced from weeks to hours), 8–12% savings on unmanaged tail spend, and 100% audit compliance.

#### Legacy Enterprise Software Modernization Agent: Codebase Maintenance & Refactoring

> **Definition:** An autonomous software engineering worker focused on enterprise codebase maintenance, dependency upgrades, security patching, and legacy refactoring.

- **Workflow Execution:** Ingests maintenance tickets from Jira/GitHub, scans enterprise repositories, sets up sandboxed development environments, updates outdated dependencies, refactors legacy code patterns, runs test suites, and opens pull requests.
- **Guardrails:** Mandatory human code review before merging, sandboxed execution with restricted network access, and test suite pass requirements.
- **Market Positioning & Dog-Fooding:** Avoids generic greenfield code generation. Instead, it targets multi-billion dollar enterprise legacy maintenance budgets. Dog-fooded internally to maintain the venture's own software repos, test runners, and API wrappers.
- **Quantitative KPIs:** Pull request merge rate, percentage of routine dependency updates automated, zero security regression rate, and backlog ticket MTTR reduction.

### Comparative Use Case Analysis

| Use Case                                 | Core Operational Workflow                                        | Primary Guardrail                                                 | Dog-Fooding & Dual Benefit Strategy                                                                                 | Key Quantitative KPI                                         |
| :--------------------------------------- | :--------------------------------------------------------------- | :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------- |
| **Outbound BDR**                         | Prospecting, contact enrichment, qualification outreach.         | Outreach limits & automated opt-out enforcement.                  | **High:** Sources internal customer pipeline while refining outreach models on live leads.                          | Cost per qualified opportunity & meeting booking rate.       |
| **ITSM Helpdesk**                        | Ticket parsing, access provisioning, automated troubleshooting.  | Role-based access caps & human sign-off on elevated permissions.  | **High:** Resolves internal employee IT tickets while battle-testing resolution scripts.                            | 70–80% auto-resolution rate & MTTR in seconds.               |
| **Financial Services KYC & Origination** | Document extraction, KYC/AML checks, credit package drafting.    | Regulatory compliance rules & human sign-off on credit decisions. | **Reconciled:** Dog-fooded internally on vendor/counterparty checks; core loan modules tested in partner sandboxes. | 80% faster processing time & zero compliance audit failures. |
| **Tail Procurement RFQs**                | RFQ issuance, quote evaluation, purchase recommendations.        | Spending caps & pre-approved vendor whitelists.                   | **High:** Refines RFQ handling on internal vendor spend while lowering company costs.                               | Tail spend savings % & RFQ cycle time reduction.             |
| **Legacy Software Modernization**        | Dependency upgrades, security patching, legacy code refactoring. | Sandboxed execution & mandatory human code review.                | **High:** Battle-tested internally on company codebase maintenance; avoids generic greenfield coding competition.   | PR merge rate & routine maintenance ticket velocity boost.   |

---

## 3. The Forward Deployed Engineering (FDE) Pod: Bridging Customization and Enterprise Reality

### Industry Consensus: The Industrial Machine Paradigm & Growth Engine

An industry consensus has solidified across enterprise AI ventures: deploying **Forward Deployed Engineering (FDE)** teams is indispensable for enterprise AI agent adoption. Off-the-shelf SaaS models fail because AI language models are probabilistic, whereas corporate environments are bound by fragmented IT systems, incomplete data schemas, and unwritten operational rules.

> **Key Analogy:** Enterprise AI agent companies do not operate like low-touch SaaS vendors. They function like precision industrial equipment manufacturers—analogous to ASML deploying specialized engineering teams directly inside semiconductor fabs to calibrate, integrate, and maintain complex lithography machinery.

Far from being mere onboarding support, the FDE pod serves as the AI agent venture's primary **Engine of Growth** and **Product-Market Fit (PMF) Discovery**. Embedded frontline pods unlock multi-million dollar enterprise accounts that standard sales teams cannot close alone, executing a dual strategic mandate:

1. **Solve Workflow Gaps & Drive Immediate Revenue:** Bridge the gap between AI agent capabilities and customer-specific IT workflows, securing long-term enterprise contracts.
2. **Translate PMF & Drive Scalable Platform Growth:** Translate custom customer implementations into generalizable, platform-wide agent capabilities.

### Pod Architecture: Technical Fluency Meets Business Context

Deploying FDE is explicitly structured as a multi-disciplinary **pod**, rather than assigning lone developers. Navigating corporate politics, uncovering informal workflows omitted from official documentation, and engineering resilient software loops requires a cross-functional team structure across three core roles:

#### Role 1: AI Solution Manager — The "What"

> **Profile:** A business operator—typically with a background in management consulting, product strategy, or enterprise operations—who aligns business objectives with AI capabilities. (Also commonly titled **Deployment Strategist**, **Agent Strategist**, or **Engagement Manager**).

The AI Solution Manager establishes **what** processes to automate: mapping informal business logic into structured workflows, uncovering real-world edge cases omitted from client documentation, and securing executive buy-in.

#### Role 2: Forward Deployed Engineer — The "How"

> **Profile:** A software and machine learning engineer focused on rapid system integration, custom API bindings, context management, and live debugging. (Also commonly titled **Machine Learning Engineer** or **Applied AI Engineer**).

The Forward Deployed Engineer executes **how** the system operates: building API connectors, writing error-handling wrappers for legacy IT systems, implementing memory management routines, and refining execution loops directly within client environments.

#### Role 3: AI Architect — The "Why"

> **Profile:** A systems specialist who analyzes model reasoning, guardrail stability, supervisor alignment, and memory performance over extended execution runs. (Also commonly titled **Forward Deployed Data Scientist** or **Forward Deployed AI Researcher**).

The AI Architect diagnoses **why** agents drift or fail in production: inspecting reasoning trajectories, tuning supervisor safeguards, designing memory structures, and ensuring operational stability across multi-day execution loops.

### Economic Trajectory: Sequential Vertical Mastery & Managing Custom Code

While team-intensive during initial client onboarding, the FDE pod's ultimate economic objective is self-elimination within a vertical through software abstraction. Achieving this trajectory relies on **sequential vertical mastery**—mastering one industry sector before redeploying to the next:

- **Vertical PMF Progression (100% -> 80% -> 98%):** An FDE pod initially works on-site to drive an agent solution to **100% PMF for an anchor client**. When deployed to a second client _within the same industry vertical_, the base product delivers **~80% PMF out-of-the-box**. The FDE team bridges the remaining 20% gap, abstracts shared workflows, and repeats this progression until achieving **~98% PMF across the sector**.
- **Handling Un-Abstractable Custom Code:** In enterprise IT, approximately 10–15% of client integration logic (e.g., custom mainframe wrappers or proprietary database schemas) will remain fundamentally un-abstractable. The pod isolates this client-specific logic within modular Layer 2 adapters, preventing custom "glue code" from polluting the core product engine.
- **Sequential Industry Handoff:** Once an industry vertical reaches ~98% PMF—with common workflows abstracted into automated setup tooling—the FDE pod hands off that sector to standard support teams and redeploys to crack the next adjacent industry market.

### Failure Modes and Strategic Discipline: The Art of Graceful Rejection

Without strict operational boundaries, FDE pods risk falling into structural traps:

1. **The "Subsidized IT Consultancy" Trap (Wrong Business Model):** Degrading into a custom IT services firm selling billable hours. AI agent ventures operate on a completely different model—selling autonomous software workers rather than selling human hours.
2. **The "Glorified Implementation Team" Trap (Unsustainable Cost Structure):** Assigning Tier-1 FDE teams to routine maintenance or permanent implementation overhead, creating a cost structure that is too expensive to sustain and starves new vertical expansion of top talent.

#### Strategic Discipline and Graceful Rejection

To avoid these traps, the venture must maintain **disciplined focus on generalizable software**. The FDE pod must possess the executive backing to **gracefully say "no" to clients** when a requested workflow is hyper-fragmented, non-scalable, or would result in single-use code that cannot be abstracted into the core platform.

---

## 4. Agent Monetization & Risk Allocation: From Consumption to Sovereign MSAs

### 1. Consumption-Based Pricing: Tokens vs. Agent Compute Units (ACUs)

Early AI ventures billed strictly on consumption. However, as agent workflows grew longer and more complex, enterprise buyers pushed back against raw token meters due to three core issues: **unpredictable costs**, **misaligned incentives** (where vendor revenue increases when agents get stuck in retry loops), and **opaque value alignment** (paying for AI token volume rather than business results).

To address token metering friction, consumption pricing evolved into two tiers:

- **Raw Token / API Consumption:** Billed per 1M input/output tokens. Penalizes system retries and context re-reading, creating severe cost volatility for enterprise IT budgets.
- **Agent Compute Units (ACUs):** Billed per normalized work unit (e.g., 1 ACU = ~15 minutes of active VM/LLM work). While ACUs abstract raw token counts and eliminate idle billing, **ACUs are fundamentally still consumption-driven**. As a result, costs remain unpredictable on complex multi-day tasks, and incentives remain misaligned because customers pay for the vendor's compute during inefficient retry loops.

### 2. Outcome-Based Pricing: Benefits, Unit-Economic Risks, and Safeguards

To eliminate financial risk for corporate buyers, leading platforms charge strictly per completed outcome:

- **Operational Risk Shift:** The vendor absorbs compute costs, retry loops, and context maintenance. The customer is billed exclusively upon a verifiably completed task (e.g., a resolved helpdesk ticket or finalized lead qualification). If an agent fails to resolve an issue, the customer pays nothing.
- **Unit-Economic Exposure (The Vendor Risk):** Because AI models are probabilistic, complex edge cases can trigger 50+ retry loops before failing. Under pure outcome pricing, unconstrained agent loops can burn massive token compute with zero revenue, destroying gross margins.
- **Necessary Risk Safeguards:** To protect unit economics, outcome pricing must include structural safeguards:
  1. **Hard Step Caps:** A strict ceiling on reasoning steps (e.g., max 15 tool calls per task) before automatically escalating to a human operator.
  2. **Hybrid Base + Success Pricing:** A modest monthly platform fee (covering baseline infrastructure) paired with a success fee per resolved task.
  3. **Task Scope Boundaries:** Strict input validation to reject underspecified or out-of-scope tasks before execution begins.

### 3. Sovereign Managed Service Agreements (MSAs) for Demanding Enterprise Sectors

For government defense agencies, tier-1 global banks, and major healthcare providers, standard cloud consumption or outcome pricing fails to meet strict control mandates. These buyers operate under unique strategic requirements:

- **Data Sovereignty & On-Premise Execution:** Demanding absolute control over data and systems, requiring on-premise model deployment, private cloud hosting, and air-gapped network execution.
- **Proprietary Process Ownership:** Viewing agent workflows as digital encapsulations of their trade secrets, insisting on full ownership of custom IP developed for their environments.
- **Price Agnosticism for Value:** Possessing large capital budgets, these institutions are price-agnostic for software that solves mission-critical compliance or operational bottlenecks.

> **Key Strategic Dilemma:** If an AI agent company surrenders IP ownership and cloud hosting, how does it build a recurring software business without degrading into a low-margin IT consultancy?

The resolution lies in structured, multi-year **Sovereign Managed Service Agreements (MSAs)**:

- **Upfront IP Transfer & Deployment Fee:** Fairly compensates the venture upfront for custom workflow development and initial deployment effort.
- **Recurring Value-Share & System Maintenance Fee:** Establishes an ongoing multi-year recurring fee tied to system maintenance, model performance upgrades, and shared economic savings generated by the agent.
- **Commercial Result:** Protects software-like valuation multiples while securing multi-million dollar recurring accounts in highly regulated sectors.

### Pricing and Risk Allocation Comparison

| Pricing Model                  | Billing Basis                               | Risk Owner      | Customer Value Alignment                                       | Unit-Economic Safeguards                                                    |
| :----------------------------- | :------------------------------------------ | :-------------- | :------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Token Consumption**          | Per 1M input/output tokens.                 | Customer        | Low (Penalizes retries; unpredictable costs).                  | None (Vendor benefits from retries).                                        |
| **Agent Compute Units (ACUs)** | Per active work unit (~15m VM/LLM work).    | Customer        | Low-Medium (Simpler metering, but costs remain unpredictable). | Idle billing excluded.                                                      |
| **Outcome-Based Pricing**      | Fixed fee per verifiably completed task.    | Vendor          | High (Direct ROI matching; pay for results).                   | **Mandatory:** Hard step caps, human escalation triggers, hybrid base fees. |
| **Sovereign Managed Services** | Multi-year MSA + recurring value-share fee. | Shared / Vendor | High (On-premise control, IP transfer, recurring upgrades).    | Upfront deployment fee + SLA value-share boundaries.                        |

---

## 5. Venture Execution Blueprint: Building, Deploying, and Scaling the Agent Business

### 1. The 3-Phase Execution Roadmap: From Foundation to Vertical Scale

Building a commercial AI agent venture requires a disciplined, three-step execution strategy designed to minimize upfront capital burn, battle-test system stability, and accelerate vertical product-market fit (PMF).

#### Phase 1: Open-Source Framework Initialization (Avoiding Engine Re-Invention)

Rather than expending scarce engineering resources building agent runners from scratch, the venture bootstraps its platform on battle-tested open-source foundations (such as Andrew Ng's **OpenWorker** framework or **Cayu.dev**). Bootstrapping on open-source foundations allows core engineering talent to focus on high-value proprietary capabilities—specifically **Durable Execution State** serialization, **Context Management**, and **Deterministic Supervisor Guardrails**.

#### Phase 2: Internal Dog-Fooding & Operational Battle-Testing

Before exposing software to external enterprise clients, the venture deploys its agents internally across core operational vectors:

- **Outbound BDR:** Sourcing prospective enterprise accounts, enriching contact profiles, and qualifying leads to power the venture's own sales pipeline.
- **Internal Helpdesk & ITSM:** Automating internal employee access provisioning, password resets, helpdesk ticket parsing, and developer environment setups.
- **Vendor Background Checks & Counterparty Verification:** Automating internal vendor compliance, document parsing, and identity checks (preparing core modules for Financial Services pilots).
- **Legacy Software Maintenance:** Deploying maintenance tools internally to update dependencies, patch security flaws, and manage the venture's codebase.

Internal dog-fooding exposes state recovery bugs, memory drift, and tool failure cascades in a controlled, low-risk environment prior to commercial launch.

#### Phase 3: FDE Pod Deployment & Vertical PMF Escalation

With a validated core engine, the venture deploys multidisciplinary **Forward Deployed Engineering (FDE)** pods to enterprise anchor clients. Operating as frontline PMF SWAT teams, these pods embed on-site to bridge the gap between AI capabilities and client IT infrastructure. By executing the **100% -> 80% -> 98% PMF progression** within targeted industry verticals, FDE pods transform anchor-client customizations into building AI agent capabilities in the vertical.

---

### 2. The 3-Layer Architectural Abstraction Framework

To maintain software margins and avoid becoming an IT services business, development teams must enforce rigid separation between core engine capabilities, client business rules, and generalizable tool connectors.

```
+-----------------------------------------------------------------------+
|                       LAYER 1: CORE AGENT ENGINE                      |
|  - Durable Execution State Serializer   - Self-Correcting Reflection  |
|  - Context Compaction Engine            - Supervisor Audit & Logging  |
|  - Dynamic Model Routing & SLM/LLM      - Persistent Memory R&D       |
|  * 100% Proprietary Venture IP (Managed by Core Product Team)        |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|            LAYER 2: CUSTOM SKILLS & DETERMINISTIC GOVERNANCE          |
|  - Declarative SKILL.md Packages        - Deterministic Policy Engines|
|  - Ad-Hoc Execution Scripts & Tooling   - JSON Schema Validators      |
|  - Custom Client Business Rules         - Dedicated Evaluation Suites |
|  * Modular IP (Venture Retains Sanitized IP / Client Buyout via MSA) |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|         LAYER 3: GENERALIZABLE TOOLS & ENTERPRISE ACTION ECOSYSTEM    |
|  - Enterprise API Wrappers (SAP/Jira)   - Browser Automation Drivers  |
|  - File & Document Generators           - Scoped Least-Privilege Suites|
|  * Shared Platform Registry (Accumulated to Drive ~98% Vertical PMF)  |
+-----------------------------------------------------------------------+
```

#### Layer 1: Core Agent Engine (Proprietary Venture IP)

> **Governance & IP:** 100% proprietary IP owned exclusively by the AI agent venture.

The central platform engine handles execution lifecycle, state durability, and system governance. Layer 1 is managed by a **dedicated core product team** that continuously improves universal agent capabilities:

- **Durable Execution Serializer:** Saves work-in-progress, execution graphs, and tool states to persistent storage, enabling clean pause-and-resume hibernation across system restarts.
- **Context Compaction Engine:** Summarizes long tool action histories, prunes stale observation logs, and prevents memory decay over multi-day execution loops.
- **Dynamic Model Routing:** Intelligently routes sub-tasks between fast small language models (SLMs) for routine tool calls and frontier LLMs for complex reasoning, keeping compute costs low.
- **Persistent Memory Architecture:** Implements multi-tiered retrieval stores to maintain long-term domain knowledge and operational history across sessions.
- **Supervisor Audit & Safeguard Layer:** Enforces deterministic compliance checks, monitors agent reasoning drift, and manages asynchronous human-in-the-loop approval gates.

#### Layer 2: Custom Skills & Deterministic Governance (Client Business Rules & Policy Engines)

> **Governance & IP:** Built and accumulated over time as part of the **~98% Vertical PMF Growth Flywheel**. Isolated in modular configuration files, declarative `SKILL.md` packages, and deterministic policy engines. The venture retains ownership of all sanitized skills and rules by default, while allowing enterprise customers to negotiate full IP buyouts via Sovereign MSAs.

Layer 2 isolates client-specific operational rules, business logic, and domain expertise from the central engine. Crucially, enterprise governance requires pairing prompt-based instructions with deterministic enforcement:

- **Declarative `SKILL.md` Packages:** Modular instruction sets containing domain expertise, business logic, decision trees, contextual guidance, and associated helper scripts.
- **Deterministic Policy Engines & Schema Validators:** Prompt instructions alone are stochastic and insufficient for strict enterprise compliance. Layer 2 pairs `SKILL.md` packages with **deterministic policy engines** (e.g., Open Policy Agent / REGO rules and JSON Schema validators). Prompts guide general reasoning; policy engines enforce non-negotiable compliance rules, approval thresholds, and security boundaries.
- **Dedicated Evaluation Suites (`eval/`):** Standardized benchmark suites that evaluate skill execution across real-world edge cases to guarantee stability and prevent regressions before deployment.

#### Layer 3: Generalizable Tools & Enterprise Action Ecosystem (Shared Platform Registry)

> **Governance & IP:** Accumulated across deployments to achieve ~98% industry-wide Product-Market Fit (PMF), cataloged in the shared platform registry for universal cross-client deployment.

Layer 3 provides the comprehensive suite of standardized, reusable tools required for an autonomous agent to take direct actions across enterprise systems:

- **Enterprise API Connectors:** Pre-built, rate-limited connectors for core business systems (Salesforce, SAP, Jira, ServiceNow, Workday).
- **Browser & GUI Automation:** Headless browser drivers (Playwright, Puppeteer) and visual DOM parsers to interact with legacy web applications lacking native APIs.
- **Terminal & Code Sandboxes:** Isolated bash/PowerShell harnesses, Python execution runners, git handlers, and CLI tool modules.
- **Data & File Tools:** SQL/NoSQL query execution engines, vector search interfaces, document OCR parsers, and file extractors.
- **Document & Asset Generators:** Automated presentation engines (e.g., PowerPoint generators adhering to corporate brand templates), PDF report builders, and executive memo compilers.
- **Scoped Tool Suites & Least-Privilege Design:** Not all agents receive access to all tools. Exposing unconstrained tools bloats prompt context and introduces security risks. Platform architects enforce **Scoped Tool Suites**—custom, role-specific bundles of tools (e.g., an ITSM Provisioning Suite vs. a BDR Outreach Suite)—to enforce strict least-privilege security boundaries.

---

## Strategic Conclusion

Long-running autonomous agents represent the next major shift in corporate productivity, moving AI from casual conversation to complex background task execution. Embedded Forward Deployed Engineering (FDE) pods serve as the vital engine of growth, bridging the gap between probabilistic language models and messy corporate IT infrastructure. Yet long-term commercial value belongs to companies that sidestep the subsidized IT consultancy trap—focusing on scalable operational workflows, managing unit-economic risks through capped outcome pricing, and enforcing a decoupled three-layer architecture. By systematically converting frontline deployment intensity into reusable software IP and deterministic governance, disciplined ventures will transform custom client integrations into sector-defining, high-margin automation platforms.
