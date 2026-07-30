# Research Notes: Long-Running Autonomous Agents & Platform Architectures

## Source Citation
- **Sierra AI Platform Architecture**: Bret Taylor & Clay Bavor, Sierra.ai (2025/2026 releases & platform whitepapers). URL: https://sierra.ai
- **OpenWorker Agent Framework**: Andrew Ng & Rohit Prasad, `andrewyng/openworker` (GitHub / DeepLearning.AI, July 2026).
- **Cayu.dev & Autonomous Agent Execution**: Open-source durable agent runner and state persistence frameworks.

## Short Summary
Long-running autonomous agents transition AI from synchronous prompt-response chat interfaces to persistent background workers. They operate on durable state and long-horizon memory, reacting to system state changes and event triggers rather than human prompts. While commercial platforms like Sierra and open-source models like Andrew Ng's OpenWorker demonstrate high task capability, real-world enterprise execution remains constrained by state drift, token inflation, and circular tool-call failure loops.

## Raw Relevant Excerpts

### 1. Technical Definition & Durable State Architecture
> *"Long-running autonomous agents are software workers engineered around durable execution state and persistent memory. Unlike conversational chatbots that operate on stateless request-response loops, long-running agents execute continuous loops across hours or days, listening for asynchronous system events, state changes, or schedule triggers."*

> *"The core primitives of a long-running agent consist of: (1) Durable Execution State (ability to pause, serialize memory, and resume across process restarts), (2) Workspace & Tool Access (sandboxed execution environments with file system, CLI, and API permissions), and (3) Autonomous Planning & Reflection Loops (continuous monitoring of goal progression without requiring human turn-taking)."*

### 2. Platform Benchmarks: Sierra AI
> *"Sierra's Agent OS 2.0 unifies unstructured interaction history with structured CRM and business data via its Agent Data Platform (ADP). Sierra addresses agent unreliability by pairing primary action agents with real-time specialist 'supervisor' agents that audit reasoning traces, enforce deterministic business logic (e.g. strict policy windows), and prevent off-topic or ungrounded drift."*

> *"Sierra allows developers to write customer journeys as code using an Agent SDK, treating agent trajectories as observable, versioned software workflows backed by an automated Ghostwriter optimization engine."*

### 3. Open-Source Benchmarks: OpenWorker & Cayu.dev
> *"Andrew Ng's OpenWorker represents a local-first, desktop-native agent architecture built on `aisuite`. It operates on a typed permission model, categorizing tool calls into granular risk tiers (`read`, `write_local`, `exec`, `external`) to ensure user control over multi-step background tasks."*

> *"Despite impressive capabilities claimed by open-source agent runners, getting open-source agents to execute deterministically in real enterprise environments is far from guaranteed. Real-world business settings feature undocumented API edge cases, ambiguous legacy schemas, and chaotic human workflows that break brittle agent loops."*
