# EU AI Act Readiness Assessor

A lightweight AI-powered tool that helps privacy and legal teams at mid-market companies understand their obligations under the EU AI Act — without a Big 4 consulting engagement or an enterprise GRC platform.

---

## The Problem

The EU AI Act is in force. Mid-market companies deploying AI internally are scrambling to understand their exposure — but most compliance resources are written for large enterprises with dedicated legal teams and six-figure consulting budgets. Privacy counsel, DPOs, and legal operations managers at 100–500 person companies are left to figure it out on their own.

## What This Tool Does

Users submit a description of an AI use case their organization is deploying or considering. The tool:

1. **Classifies the use case** by EU AI Act risk tier (Unacceptable, High, Limited, or Minimal Risk)
2. **Maps applicable obligations** — the specific EU AI Act articles and requirements that apply to that tier
3. **Identifies compliance gaps** based on the organization's current safeguards
4. **Generates a prioritized remediation roadmap** with concrete next steps

Input is a structured form (use case name, industry, deployment context, existing safeguards) plus a free-text description field. Output is a structured on-screen report with classification rationale, regulatory references, identified gaps, and a remediation roadmap.

## Who It's For

- Privacy Counsel
- Data Protection Officers (DPOs)
- Legal Operations Managers
- Chief Privacy Officers

At companies that use AI internally and need to understand their EU AI Act exposure — but don't have the budget for enterprise compliance tooling.

## How It Works

The tool uses a two-model AI pipeline:

- **Claude Haiku** handles input validation and output formatting
- **Claude Sonnet** performs risk tier classification, regulatory mapping, gap analysis, and roadmap generation

Token limits are enforced in code on every request to ensure predictable cost and output quality. Every assessment output includes a mandatory disclaimer that the output is AI-generated and does not constitute legal advice.

## Tech Stack

| Component | Tool |
|---|---|
| AI reasoning | Anthropic Claude API (Sonnet + Haiku) |
| Orchestration | Python |
| Front-end | Streamlit |
| Environment | python-dotenv |

## Current Status

This project is in active development. The core assessment pipeline and Streamlit front-end are complete and running locally. Structured pre-launch testing (20 documented test cases across all risk tiers) is currently in progress before external deployment.

## Important Disclaimer

This tool is for informational purposes only. It does not constitute legal advice, regulatory guidance, or a compliance determination. Classifications and recommendations are AI-generated and have not been reviewed by a qualified attorney or compliance professional. Do not rely on this output as the sole basis for any compliance, product, or business decision. Consult qualified legal counsel before acting on any findings.

---

*Built by Derek Pignatelli using Claude Code and the Anthropic API.*
