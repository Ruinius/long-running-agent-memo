# Executive Strategy Memo Outline: Building a High-Growth Venture on Long-Running Autonomous Agents and Forward Deployed Engineering Pods

**Author:** Venture Strategy & AI Engineering Team  
**Date:** July 2026  
**Classification:** Strategic Business Blueprint  
**Audience:** Executive Leadership, Venture Founders, Product & Engineering Leaders

## Executive Summary

**1. Long-Running Autonomous Agents vs. Chatbots & Stateless Swarms:** Long-running autonomous agents mark a fundamental departure from both conversational chatbots and stateless multi-agent swarms. Chatbots operate on synchronous, ephemeral prompt-response transactions, while stateless agent swarms execute immediate, multi-agent loops that reset memory between tasks. Long-running agents, by contrast, act independently over extended time horizons (hours, days, or weeks) across asynchronous background events. This autonomy relies on two architectural pillars: **Durable Execution State**—the ability to serialize process memory, event logs, and tool call histories to persistent storage so agents can pause, await human sign-offs, and resume cleanly across process restarts without state loss—and **Persistent Memory**, which maintains operational context, past trajectories, and domain knowledge across sessions.

**2. High-Impact Market Opportunities & Industry Leaders:** By far the largest and most compelling commercial opportunity for long-running autonomous agents is **Autonomous Coding Agents** (software development, bug fixing, repo migration, and automated pull requests). This is followed by high-value enterprise workflow automation in **Outbound BDR** (autonomous prospect sourcing, contact enrichment, and lead qualification) and **IT Service Management (ITSM)** (automated helpdesk ticket resolution, system provisioning, and access management), with secondary opportunities in **Tail Procurement RFQs**, **Loan Origination**, and **KYC Processing**. Market leadership is defined across pioneering agent platforms and open-source foundations:

- **Cognition AI (Scott Wu):** Founder and CEO Scott Wu highlights the shift to autonomous software engineering, noting that _"Teaching AI to be a programmer is a deep algorithmic problem that requires an agent to look steps into the future, take ownership of entire complex tasks, and focus on verifiable output rather than raw token usage"_ (Scott Wu, Cognition AI / Devin Launch & Industry Address, 2024/2026).
- **Sierra AI (Bret Taylor):** Enterprise agent platform co-founder Bret Taylor emphasizes that _"AI should be an extension of a company's brand, operating as an always-on agent that takes direct action rather than just answering questions"_ (Bret Taylor, Sierra AI Launch & Platform Declaration, 2024/2025).
- **OpenWorker (Andrew Ng):** Open-source agent framework creator Andrew Ng asserts that _"For the majority of businesses, focus on building applications using agentic workflows rather than solely scaling traditional AI. That's where the greatest opportunity lies"_ (Andrew Ng, DeepLearning.AI / OpenWorker Release, July 2026).

**3. Execution Strategy: FDE Pods as PMF SWAT Teams:** Capturing these market opportunities requires deploying high-touch Forward Deployed Engineering (FDE) pods composed of **AI Solution Managers**, **Machine Learning Engineers** (Forward Deployed Engineers), and **AI Architects**. However, ventures frequently fail by falling into two major traps: treating pods as permanent implementation overhead or, worse, low-margin IT consultancies selling billable hours (the "Palantir Trap"). The winning model treats FDE pods as **product-market-fit searching SWAT teams**. Embedded directly inside customer environments, these SWAT teams focus on scalable use cases, solving immediate operational bottlenecks while systematically extracting custom client integrations into generalizable agent designs and tools.

## 1. Defining Long-Running Autonomous Agents: Architecture, State Persistence, and Market Reality

### Technical Definition and Core Primitives

Long-running autonomous agents are software workers engineered around persistent memory and durable execution states. Unlike conversational chatbots that process brief, one-off interactions, and stateless multi-agent swarms that execute immediate task loops but reset memory between runs, long-running agents execute continuous background loops over hours, days, or weeks, responding to system events, scheduled timers, or database updates.

Three core capabilities govern long-running agent execution:

- **Durable Execution State:** Saving process memory, command history, and tool states to persistent storage. This allows an agent to pause during idle periods or while awaiting human approvals, then resume cleanly across system restarts without losing context.
- **Workspace and Tool Provisioning:** Isolated digital work environments equipped with file systems, terminal access, and secure enterprise API connections.
- **Autonomous Planning and Reflection:** Self-correcting feedback loops in which agents monitor their own progress, review intermediate results, and adjust course without waiting for human prompts.

#### Architectural Comparison: Traditional AI Chatbots vs. Multi-Agent Swarms vs. Long-Running Autonomous Agents

|                                  | Traditional AI Chatbots                                                  | Stateless Multi-Agent Swarms                                            | Long-Running Autonomous Agents                                               |
| :------------------------------- | :----------------------------------------------------------------------- | :---------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| **Execution Horizon**            | Ephemeral, synchronous user-driven sessions (seconds to minutes).        | Short-lived, batch task execution loops (minutes to hours).             | Continuous, asynchronous background loops (hours, days, or weeks).           |
| **State & Memory Model**         | Transient in-memory context window; resets upon session termination.     | In-flight inter-agent message passing; resets memory between runs.      | Persistent memory and durable process state serialized to disk/database.     |
| **Workspace & Tooling**          | Sandboxed function calling with ephemeral request/response payloads.     | Shared memory bus or queue with ephemeral scratchpads per agent.        | Isolated long-lived environments (file systems, terminal, enterprise APIs).  |
| **Planning & Autonomy**          | Reactive single-prompt completions or simple step-by-step chains.        | Directed DAG workflow or hierarchical delegation across agents.         | Self-correcting autonomous reflection, trajectory tracking, and re-planning. |
| **Human Interaction**            | Synchronous blocking; requires active human presence for input.          | Unattended batch execution; unhandled errors cause job failure.         | Asynchronous pause-and-resume; hibernates state while awaiting approval.     |
| **Primary Failure Modes**        | Context exhaustion, prompt drift, and immediate session termination.     | Inter-agent coordination overhead, message flooding, and error cascade. | Long-term context drift, circular retry loops, and token cost accumulation.  |
| **Primary Enterprise Use Cases** | Conversational search, document Q&A, and interactive writing assistance. | Parallel data extraction, web research synthesis, and batch processing. | Autonomous coding (repo maintenance), outbound BDR, and ITSM automation.     |

### End-to-End Operational Workflow: ITSM Long-Running Autonomous Agent

> **Workflow Definition:** A long-running ITSM autonomous agent maintains persistent state across asynchronous system events, compliance evaluations, human approval gates, and multi-system infrastructure API calls over multi-day execution lifecycles.

1. **Ticket Ingestion & Parsing:**
   - **Trigger:** A user submits an IT helpdesk ticket (e.g., via ServiceNow or Jira Service Management) requesting elevated database access for a production troubleshooting session.
   - **Agent Action:** The long-running agent wakes up on a webhook event, ingests the raw ticket payload, extracts parameters (User ID, requested resource, environment, duration, justification), and initializes a durable execution state.

2. **Policy Audit & IAM Pre-Checks:**
   - **Agent Action:** The agent executes background API queries against enterprise IAM systems (Okta, Entra ID) and HR directories to verify employee identity, security training status, and active department role.
   - **Evaluation:** It checks corporate Role-Based Access Control (RBAC) policies and identifies that production database access requires Tier-2 Manager sign-off and Security Operations approval.

3. **Asynchronous Hibernation & Approval Dispatch:**
   - **Agent Action:** The agent generates risk-scored approval requests containing context links and posts them to Slack/Teams and ServiceNow.
   - **State Hibernation:** The agent serializes its complete execution context, process memory, and tool state to disk/database. It enters a low-resource hibernation state, consuming zero LLM token compute while awaiting human intervention.

4. **Event-Driven Deserialization & Provisioning:**
   - **Trigger:** The security manager approves the request via a Slack interactive button 14 hours later.
   - **Agent Action:** An incoming webhook re-activates the agent thread. The agent deserializes its saved state, validates the cryptographic signature of the approval event, and calls PAM (Privileged Access Management) tools (e.g., HashiCorp Vault, AWS IAM Identity Center) to generate time-bound, scoped database credentials.

5. **Verification, Audit Logging & Ticket Lifecycle Closure:**
   - **Agent Action:** The agent performs synthetic connectivity checks to confirm access activation, securely returns credential instructions to the requesting user, and logs an immutable audit trace to SIEM tools (Datadog, Splunk).
   - **Resolution:** The agent updates ticket status to "Resolved", sets an asynchronous timer event to verify credential revocation after the approved TTL window, and safely closes its execution context.

## 2. High-Value Enterprise Use Cases: Workflows, Guardrails, and Quantitative KPIs

### Criteria for Ideal Early Agent Deployment

Early agent deployments succeed best in structured, rule-based corporate workflows with clear decision boundaries and easily measured financial returns.

By far the most lucrative and dominant commercial opportunity is the **Autonomous Coding Agent** (software development, bug fixing, repo migration, and automated pull requests). Both frontier labs and specialized model-agnostic players—such as Factory and OpenHands—have aggressively moved to capture this high-margin market. Ironically, software engineering is structurally far more complex than most other enterprise use cases, requiring multi-turn trajectory planning, terminal sandboxing, and continuous execution feedback loops. However, intense **Internal Dog-Fooding** (AI engineering teams building tools for their own software workflows) paired with overwhelming market demand accelerated its development and established coding as the flagship agent paradigm.

In contrast, other early enterprise use cases—such as **Outbound BDR** (sales lead sourcing and qualification), **IT Service Management (ITSM)** (helpdesk resolution), **Tail Procurement RFQs**, **Loan Origination**, and **KYC Processing**—focus on comparatively less complex workflows. These applications operate on deterministic business rules and structured schema transformations that do not require extensive Reinforcement Learning from Human Feedback (RLHF / Human-Led Reinforcement) or non-deterministic execution environments. Beyond market demand, internal dog-fooding remains vital across all categories, enabling AI ventures to validate memory retention, context compaction, and tool orchestration on daily operational tasks while yielding immediate internal returns.

### Primary Use Case Deep Dives

#### Autonomous Coding Agent: Software Engineering and Codebase Maintenance

> **Definition:** An autonomous software engineering worker (e.g., Devin) that ingests engineering tickets, sets up development environments, writes code, runs test suites, and opens pull requests.

- **Workflow Execution:** Ingests task requirements from Jira/GitHub issues, analyzes repository codebases, sets up sandboxed terminal environments, writes code modifications, executes unit/integration tests, and submits complete pull requests for human review.
- **Guardrails:** Mandatory human code review before merging, sandboxed execution environments with restricted network access, and test suite pass requirements.
- **Internal Dog-Fooding & Dual Benefit:** Deployed internally to maintain the venture's own software codebase and build custom connectors. This battle-tests terminal tool use, file editing, and test execution loops while accelerating product development velocity.
- **Quantitative KPIs:** Pull request merge rate, percentage of internal code written by agents (targeting 90%+), unit test pass rate, and time-to-resolution for backlog bug tickets.

#### Outbound BDR Agent: Lead Sourcing, Enrichment, and Qualification

> **Definition:** An autonomous sales development representative that identifies, enriches, and qualifies potential customer accounts.

- **Workflow Execution:** Queries public and commercial databases to assemble prospect lists, enriches contact details, drafts tailored outreach campaigns, and evaluates prospect responses against Ideal Customer Profiles.
- **Guardrails:** Daily outreach limits, automated opt-out enforcement, and mandatory handoffs to human sales reps once qualification criteria are met.
- **Internal Dog-Fooding & Dual Benefit:** Powers the venture's own growth by sourcing enterprise buyer leads. The team refines data connectors and personalization logic on live sales prospect interactions, filling its customer pipeline as it polishes the product.
- **Quantitative KPIs:** Cost per qualified pipeline lead, meeting booking rate, and data enrichment accuracy.

#### ITSM Agent: IT Helpdesk Automation and Access Management

> **Definition:** An autonomous IT service software worker that ingests, diagnoses, and resolves corporate IT helpdesk tickets and user access requests.

- **Workflow Execution:** Monitors ticketing systems (Jira Service Management, ServiceNow, Slack/Teams helpdesk), parses user requests, queries identity providers (Okta, Active Directory), executes automated password resets, software provisioning, or VPN troubleshooting scripts, and closes tickets upon verification.
- **Guardrails:** Strict RBAC access policies, mandatory human approval for administrative elevated privileges, and audit-immutable execution logs.
- **Internal Dog-Fooding & Dual Benefit:** Automated internally to resolve employee IT requests, optimizing workflow triggers and API resolution scripts on live tickets before commercial enterprise deployment.
- **Quantitative KPIs:** 70–80% auto-resolution rate of tier-1 helpdesk tickets, mean time to resolution (MTTR) reduced from hours to seconds, and 100% compliance auditing.

#### Procurement Agent: Automating Tail-Vendor RFQs

> **Definition:** An autonomous software worker that manages request-for-quote (RFQ) cycles across secondary and tertiary supplier catalogs.

- **Workflow Execution:** Scrapes internal ERP requisitions, identifies candidate suppliers, issues standardized RFQs, compiles incoming quotes against corporate rules, and recommends purchase decisions.
- **Guardrails:** Fixed spending caps, whitelists of pre-approved vendors, and mandatory human approval whenever quote prices vary beyond set limits.
- **Internal Dog-Fooding & Dual Benefit:** Deploying the agent internally automates the venture’s own procurement. This sharpens quote-parsing loops on live company spending while cutting vendor overhead by 8–12%.
- **Quantitative KPIs:** 75% faster RFQ cycles (reduced from weeks to hours), 8–12% savings on unmanaged tail spend, and 100% audit compliance.

#### Financial Services Agent: Loan Origination, Underwriting, and KYC Processing

> **Definition:** An autonomous compliance and credit specialist that automates loan application intake, identity verification (KYC/AML), and credit risk analysis.

- **Workflow Execution:** Processes applicant documents (W-2s, tax returns, bank statements), queries credit bureaus and identity APIs, calculates risk metrics, and prepares complete underwriting files with recommended credit terms or rejection notices.
- **Guardrails:** Strict adherence to financial regulations (FCRA, Fair Lending, KYC/AML), required human sign-off on borderline credit scores, and immutable audit logs.
- **External Partner Pilots & Expansion (No Internal Dog-Fooding):** Because AI software ventures do not originate loans or process credit applications internally, this use case lacks a direct internal dog-fooding loop. Instead, it is validated via design partner pilots and regulatory sandboxes, serving as a high-margin enterprise expansion product once the core agent platform is proven.
- **Quantitative KPIs:** 80% faster decision times (minutes instead of days), 90%+ automated document processing, zero compliance audit failures, and reduced cost per loan.

### Comparative Use Case Analysis

| Use Case                             | Core Workflow                                                             | Primary Guardrail                                             | Internal Dog-Fooding & Dual Benefit                                                                        | Key Quantitative KPI                                  |
| :----------------------------------- | :------------------------------------------------------------------------ | :------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- |
| **Autonomous Coding** (Flagship #1)  | Ticket parsing, code editing, test execution, PR submission               | Mandatory human code review & test suite pass                 | **Highest:** Powers internal software development and writes venture's own product code                    | PR merge rate, 90%+ auto-written code, MTTR reduction |
| **Outbound BDR** (Primary)           | Prospect sourcing, lead enrichment, outreach                              | Contact limits & opt-out rules                                | **High:** Drives internal sales pipeline while tuning qualification models on live leads                   | Cost per qualified opportunity                        |
| **ITSM Helpdesk** (Primary)          | Helpdesk ticket parsing, access provisioning, automated troubleshooting   | RBAC access caps & human sign-off on elevated permissions     | **High:** Automates internal IT tickets while battle-testing resolution scripts                            | 70-80% auto-resolution rate & MTTR in seconds         |
| **Tail Procurement**                 | RFQ issuance, quote evaluation, purchase recommendation                   | Spending caps & vendor whitelists                             | **High:** Refines RFQ handling on internal vendor spend while lowering company costs                       | Tail spend savings % & cycle time reduction           |
| **Financial Loan Origination & KYC** | Document extraction, KYC/AML checks, credit underwriting package drafting | Regulatory compliance (FCRA/KYC), human sign-off on high risk | **None (External Sandboxes):** Lacks internal dog-fooding loop; validated via institutional partner pilots | Time-to-decision reduction & zero KYC audit failures  |

## 3. The Forward Deployed Engineering (FDE) Pod: Bridging Customization and Enterprise Reality

### Industry Consensus: The Industrial Machine Paradigm & Growth Engine

An industry-wide consensus has solidified across frontier AI ventures: deploying **Forward Deployed Engineering (FDE)** teams is indispensable for enterprise AI agent adoption. Standard off-the-shelf SaaS models fail in agentic deployments because language models are fundamentally stochastic, while corporate environments are bound by messy IT infrastructure, fragmented data schemas, and unwritten workplace rules.

> **Key Insight:** Enterprise AI agent companies do not operate like traditional, low-touch SaaS vendors. Instead, they function like industrial precision equipment manufacturers—analogous to ASML deploying specialized engineering teams to integrate, calibrate, and maintain DUV lithography machinery directly within semiconductor fabs.

Far more than an onboarding or deployment team, the FDE pod serves as the venture's primary **Engine of Growth** and **Product-Market Fit (PMF) Discovery**. Embedded frontline pods unlock multi-million dollar enterprise accounts that standard sales teams cannot close alone, executing a dual strategic mandate:

- **Navigating Operational Reality:** Engineering custom connectors, API wrappers, and context management logic to handle messy enterprise data and undocumented workflows on-site.
- **Abstracting Platform IP:** Systematically capturing recurring integration patterns across clients to convert bespoke glue code into core, standardized platform capabilities.

### Pod Architecture: Technical Fluency Meets Social Capability

Deploying FDE is explicitly structured as a multi-disciplinary **pod**, rather than a collection of lone-wolf developers. Successfully driving enterprise adoption requires navigating corporate politics, uncovering informal workflows that diverge from official documentation, and engineering resilient software loops—a cross-functional mandate that cannot be fulfilled by any single individual.

While every pod member must be both technically fluent and socially capable, the pod maintains strict operational specialization across three core roles:

#### Role 1: AI Solution Manager / Agent Strategist — The "What"

> **Profile:** A business operator—often with a background in management consulting, product strategy, or enterprise operations—who links executive goals to AI technical capabilities.

The AI Solution Manager establishes **what** processes to automate: navigating corporate politics, mapping informal business logic into structured agent workflows, uncovering real-world edge cases omitted from client documentation, and securing executive alignment.

#### Role 2: Forward Deployed / Machine Learning Engineer — The "How"

> **Profile:** A practical software and machine learning engineer focused on rapid integrations, custom API bindings, context management, and live system debugging.

The Forward Deployed Engineer executes **how** the system operates: building custom API connectors, writing error-handling wrappers for legacy IT systems, implementing memory compaction routines, and refining live agent execution loops directly within client environments.

#### Role 3: AI Architect / Forward Deployed AI Researcher — The "Why"

> **Profile:** A systems specialist who analyzes model reasoning, prompt stability, supervisor alignment, and memory architecture over extended execution runs.

The Pragmatic AI Architect diagnoses **why** agents drift or fail in production: inspecting reasoning trajectories, tuning supervisor agent safeguards, designing persistent memory stores, and ensuring execution stability across multi-day execution loops.

### Economic Trajectory: Sequential Vertical Mastery & Platform Abstraction

While team-intensive during initial client onboarding, the FDE pod's ultimate economic objective is self-elimination within a vertical through platform abstraction. However, unlocking this trajectory relies entirely on **sequential vertical mastery**—the team must master and codify one industry vertical before redeploying to conquer the next:

- **Vertical PMF Escalation (The 100% -> 80% -> 98% Progression):** PMF discovery requires staying tightly focused within a single industry vertical. An FDE pod initially works to drive an agent solution to **100% PMF for an anchor client**. When deployed to a second client _within the same vertical_, the base product delivers **~80% PMF out-of-the-box**. The FDE team bridges the remaining 20% gap, abstracts shared workflows, and repeats this targeted progression until achieving **~98% PMF across the entire sector**.
- **Sequential Industry Handoff:** Once a vertical reaches ~98% PMF—with common workflows abstracted into automated setup tooling—the FDE pod hands off that sector to traditional, low-cost implementation teams and redeploys its elite problem-solving talent to crack the next adjacent industry market.
- **The Risk of Premature Horizontal Expansion:** Jumping between unrelated verticals before mastering the current one produces fragmented, single-use codebases, resets the PMF discovery curve to zero with each client, and destroys the transition to a scalable platform.
- **De-Risking Enterprise Sales & NRR:** Active pod oversight eliminates deployment friction to win major contracts while protecting Net Revenue Retention (NRR) by preventing silent agent failures during early rollouts.
- **Accelerating the Low-Touch Transition:** Frontline pods systematically capture recurring integration patterns, driving onboarding timelines down from months to days as vertical platform IP matures.

### Failure Modes and Strategic Discipline: The Art of Graceful Rejection

Without strict operational boundaries, FDE pods risk falling into structural traps that misalign business models and talent allocation:

1. **The "Consulting Firm" Trap (Labor Arbitrage vs. Software Product):** While IT consulting is a high-margin business with valuation multiples that have converged with software in recent years, consulting firms fundamentally sell human labor and rely on geography-based labor arbitrage to scale. AI agent ventures operate on a completely different business model—selling autonomous AI agents, not offshore or headcount labor. Treating FDE pods as billable IT consultants shifts focus away from software scalability toward custom labor delivery.
2. **The "Perpetual Implementation" Trap (Misallocating Tier-1 Talent):** Traditional IT implementation teams are designed to deploy highly mature, standardized products, but they are not trained to navigate and execute complex, non-deterministic AI agent builds. Conversely, FDE pods represent Tier-1 A-teams that are far too expensive to be used as permanent implementation crutches for mature products. Continuing to assign elite FDE teams to routine maintenance or mature deployments creates an unsustainable cost structure.

#### Strategic Discipline and Graceful Rejection

To avoid these failure modes, the venture must maintain a **razor-sharp focus on generalizable code and scalable use cases**. The FDE pod must possess the executive backing and strategic discipline to **gracefully say "no" to clients** when a requested workflow is inherently non-scalable, hyper-fragmented, or would result in overwhelmingly single-use code that cannot be abstracted into the core product platform.

## 4. Agent Monetization & Risk Allocation: From Consumption Models to Outcome Pricing

### 1. Consumption-Based Pricing: Tokens vs. Agent Compute Units (ACUs)

Early AI agent ventures billed strictly on consumption. However, as agentic workflows grew longer and more complex, corporate buyers increasingly pushed back against raw token meters due to three core friction points: **unpredictable costs**, **misaligned incentives** (where vendor revenue increases when agents get stuck in retry loops), and **opaque value alignment** (paying for LLM token volume rather than business results).

To mitigate raw token complexity, consumption pricing evolved into two distinct tiers:

- **Raw Token / API Consumption:** Billed per 1M input/output tokens. This model penalizes system retries and context re-reading, creating severe cost volatility for enterprise IT budgets.
- **Agent Compute Units (ACUs) / Active Work Consumption:** Pioneered by Cognition (Devin), this model abstracts raw token metering by packaging VM runtime, LLM inference, and tool execution into normalized work units (e.g., 1 ACU = ~15 minutes of active, autonomous work). While ACUs eliminate idle billing and make work-unit metering easier to track, **ACUs are fundamentally still consumption-driven**. As a result, they retain all three core flaws of consumption billing: costs remain unpredictable on complex tasks, incentives remain misaligned (customers pay for the vendor's compute during retry or inefficient reasoning loops), and pricing measures vendor effort rather than delivered business value.

### 2. Outcome-Based Pricing: Price Per Completed Task / Resolution

To eliminate operational risk for corporate buyers, leading enterprise agent platforms—most prominently **Sierra AI**—are pioneering true outcome-based pricing:

- **Shift in Operational Risk:** The vendor absorbs all underlying compute costs, retry loops, context compaction overhead, and failed reasoning trajectories. The customer is billed exclusively upon a verifiably completed task or successful resolution (for example, Sierra charging per resolved customer interaction or per finalized enterprise workflow). If an agent fails to resolve an issue or escalates to a human operator, the customer is not billed for the attempt.
- **Direct ROI Alignment:** Co-founder Bret Taylor encapsulates the thesis: _"If you're selling software that completes a job, what is the secular business model for that? Let's pay for a job well done."_ Outcome pricing allows corporate buyers to evaluate AI agent costs directly against internal human labor expenses, establishing an immediate, unambiguous business case.

### 3. Sovereign Managed Service Agreements (MSAs) for Massive Demanding Customers

For defense agencies, financial institutions, and heavily regulated enterprises, standard consumption or outcome pricing is paired with structured Managed Service Agreements:

- **Intellectual Property Ownership:** Customers retain rights to custom workflow scripts, specialized domain prompts, and integrations built for their systems.
- **Data Sovereignty and On-Premise Execution:** Requirements to run software within private clouds or air-gapped networks to comply with security regulations.
- **Service Guarantees:** Multi-year contracts with strict uptime guarantees, dedicated technical support, and zero-data-retention policies.

### Pricing and Risk Allocation Comparison

| Pricing Model                  | Billing Basis                      | Risk Owner      | Customer Value Alignment                             | Primary Industry Examples                        |
| :----------------------------- | :--------------------------------- | :-------------- | :--------------------------------------------------- | :----------------------------------------------- |
| **Token Consumption**          | Per 1M input/output tokens         | Customer        | Low (Penalizes retries; opaque value)                | Raw API providers, early developer tools         |
| **Agent Compute Units (ACUs)** | Per active work unit (~15m VM/LLM) | Customer        | Low - Medium (Retains unpredictable costs & retries) | Cognition (Devin), autonomous dev agents         |
| **Outcome-Based Pricing**      | Fixed fee per successful outcome   | Vendor          | High (Direct ROI against human labor)                | Sierra AI, specialized vertical business agents  |
| **Sovereign Managed Services** | Fixed MSA + custom engineering fee | Shared / Vendor | High (Includes IP & security governance)             | Defense, government, highly regulated enterprise |

## 5. Venture Execution Blueprint: Building, Deploying, and Scaling the Agent Business

### Phased Execution Strategy

Building a commercial AI agent venture requires a disciplined, three-step execution strategy:

1. **Build on Open-Source Frameworks:** Avoid building agent runtime runners from scratch. Launch using proven open-source foundations (such as Andrew Ng's OpenWorker or Cayu.dev).
2. **Dog-Food Internally:** Run agents in-house to automate company operations (such as lead generation, client onboarding, and internal testing). In-house deployment exposes memory decay and tool errors before software touches customers.
3. **Deploy FDE Pods for Customer Onboarding:** Place technical pods with early enterprise clients to build custom connectors, refine workflows, and earn institutional trust.

### Customization Friction and IP Segregation

Initial customer deployments inevitably require custom work. Engineering pods will need to write custom API connectors and workflow rules for each new client. To prevent the company from becoming a low-margin IT service business, development teams must strictly separate code changes into three architectural layers.

### The 3-Layer Architectural Abstraction

#### Layer 1: Core Agent Design

The central platform engine. Contains state persistence tools, memory compression algorithms, primary planning loops, supervisor auditing modules, and system metrics. Any engine improvements made by FDE pods are folded back into the main product.

#### Layer 2: Custom Skills

Client-specific business rules, decision pathways, guardrail parameters, and policy constraints. These are isolated in separate configuration files, keeping customer logic detached from the core engine.

#### Layer 3: Generalizable Tools & Integrations

Standardized, reusable software connectors, database tools, desktop automation scripts, and authentication modules (such as wrappers for Salesforce, Jira, SAP, and Slack). Connectors built for one customer are cataloged for immediate reuse across future clients.

### The 3-Layer Platform Architecture

```
+-----------------------------------------------------------------------+
|                       LAYER 1: CORE AGENT DESIGN                      |
|  - Durable Execution State       - Planning & Reflection Loop         |
|  - Context Compaction Engine     - Supervisor Audit Layer             |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|                         LAYER 2: CUSTOM SKILLS                        |
|  - Domain Business Logic         - Policy Guardrails & Rules          |
|  - Client Workflow Scripts       - Context Compression Schemas        |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|               LAYER 3: GENERALIZABLE TOOLS & INTEGRATIONS              |
|  - Enterprise API Wrappers       - Database & File Connectors         |
|  - Desktop Automation Tools      - Standard Auth Handlers             |
+-----------------------------------------------------------------------+
```

By enforcing clear boundaries across these three layers, FDE pods steadily transform bespoke client projects into a scalable, high-margin software platform.
