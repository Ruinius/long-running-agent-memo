# Research Notes: Agent Economics, Cost Dynamics, & Enterprise Pricing Models

## Source Citation
- **SaaS & AI Agent Billing Frameworks**: Industry benchmarks on token consumption vs. outcome-based billing models (2025/2026).
- **Cognition AI (Devin) & Sierra Billing Case Studies**: Billing documentation on Agent Compute Units (ACUs) and business outcome pricing.

## Short Summary
Pricing remains a central challenge for long-running autonomous agent ventures. Traditional consumption-based pricing (per token or compute unit) causes customer friction due to cost unpredictability and inflationary token usage during circular error loops. The market is pivoting toward outcome-based "price-per-completed-task" models where vendors absorb task cost risks. For sovereign AI contracts and regulated enterprises, complex managed service agreements remain dominant, driven by mandatory IP ownership and on-premise execution requirements.

## Raw Relevant Excerpts

### 1. Erosion of Trust in Token-Based Consumption Pricing
> *"Early AI SaaS providers billed customers based on raw token usage or API call volume. As enterprise buyers became sophisticated, trust in token pricing degraded rapidly. Customers realized that token billing incentivizes vendor inefficiency: when an agent gets stuck in a retry loop or re-reads massive context buffers, the customer pays for the vendor's architectural flaws."*

> *"Token pricing creates friction by forcing customers to audit individual LLM prompt calls rather than evaluating holistic business ROI. It makes forecasting monthly IT operating expenditure nearly impossible for long-horizon agentic workflows."*

### 2. Emergence of Price-Per-Completed-Task & Risk Reallocation
> *"Outcome-based pricing—specifically pricing per completed task—shifts technical execution risk from the customer to the vendor. Under models like Cognition's Agent Compute Unit (ACU) abstractions or flat task billing, the vendor takes on the risk of model inefficiency, prompt retries, and context compaction overhead."*

> *"By pricing on completed work units (e.g., $15 per resolved procurement RFQ or $50 per qualified BDR lead), the customer can directly benchmark the agent against their internal cost-per-task baseline or human labor equivalency, eliminating buying friction."*

### 3. Sovereign AI & Enterprise Managed Service Contracts
> *"For sovereign AI deployments (government agencies, defense, highly regulated financial institutions, and tier-1 healthcare enterprises), standard SaaS outcome pricing is insufficient. These clients demand Managed Service Agreements (MSAs) featuring: (1) Mandatory on-premise or isolated VPC deployments, (2) Strict zero-data-retention and proprietary fine-tuning isolation, and (3) Explicit intellectual property (IP) ownership over all custom workflow scripts and domain tool bindings."*
