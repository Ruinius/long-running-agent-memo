# Research Notes: High-Value Agent Use Cases & 3-Layer Venture Architecture

## Source Citation
- **Enterprise Workflow Automation Benchmark (2025/2026)**: Case studies in tail-vendor procurement, BDR lead qualification, and loan origination/underwriting/KYC agents.
- **Agentic Systems Architecture Blueprint**: Design patterns for decoupling core agent engines, custom domain skills, and reusable integration toolkits.

## Short Summary
The most successful early deployments for long-running autonomous agents target well-bounded enterprise workflows characterized by deterministic scripts, quantitative KPIs, and explicit guardrails. Ideal use cases include tail-vendor procurement RFQs, outbound BDR lead sourcing, and financial loan origination/KYC processing. Building a scalable agent venture requires bootstrapping on open-source foundations, internal dog-fooding, and aggressively separating code across three architectural layers: Core Agent Design, Custom Skills, and Generalizable Tools & Integrations.

## Raw Relevant Excerpts

### 1. Exciting Enterprise Use Cases
> *"1. Procurement Tail-Vendor RFQ Agent: Automates request-for-quote (RFQ) workflows across secondary and tertiary supplier catalogs. Operates autonomously to source vendor catalogs, solicit standardized quotes, evaluate terms against compliance scripts, and present optimized recommendations. KPI: Reduction in cycle time from weeks to hours and 8-12% spend savings on unmanaged tail spend. Strategic Benefit: The venture deploys this internally first to cut software/vendor overhead while perfecting multi-step vendor negotiation trajectories."*

> *"2. Business Development Representative (BDR) Lead Qualification Agent: Sources target account lists, enriches contact data across public and proprietary databases, conducts multi-step email/social outbound messaging, and qualifies inbound responses against strict ICP criteria. KPI: Cost per qualified pipeline opportunity generated. Strategic Benefit: Serves as the venture's internal growth engine, generating enterprise pipeline while continuously battle-testing contact enrichment tools on real prospects."*

> *"3. Financial Services Loan Origination & KYC Agent: Executes structured loan application intake, Know Your Customer (KYC/AML) verification, debt-to-income (DTI) risk calculations, and underwriting package generation. Operates under strict compliance guardrails (FCRA, Fair Lending, KYC/AML) with mandatory human sign-off on high-risk files. KPI: Time-to-decision reduction (hours/days to minutes), 90%+ auto-verification rate, and zero KYC audit failure rate."*

### 2. Venture Execution Blueprint: Bootstrap & Dog-Fooding
> *"To launch a new long-running agent business, founders should select a robust open-source agent framework (e.g., OpenWorker or Cayu.dev) rather than building execution runners from scratch. The venture should immediately deploy internal-facing agents (Procurement and BDR) to solve its own operational pain points ('eating own dog food'). This provides a double benefit: it perfects application trajectories and connector resilience on live internal workflows while delivering immediate operational cost savings and pipeline growth before external enterprise rollouts."*

### 3. The 3-Layer Architectural Abstraction
> *"To prevent an FDE-led venture from devolving into a pure IT consulting shop, teams must aggressively segregate intellectual property across three distinct layers during customer deployments:"*
> *"Layer 1: Core Agent Design — The generalizable, reusable engine responsible for durable state management, context compaction, trajectory planning, and supervisor auditing."*
> *"Layer 2: Custom Skills — Customer-specific or domain-specific prompt scripts, decision trees, guardrail rules, and workflow parameters."*
> *"Layer 3: Generalizable Tools & Integrations — Modular API wrappers, database connectors, desktop automation scripts, and auth handlers that can be reused across multiple enterprise deployments."*
