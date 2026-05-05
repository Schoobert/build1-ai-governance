# EU AI Act Governance Readiness Assessment Tool

A working AI-powered tool that helps organizations understand their obligations under the EU AI Act.

## Live Demo

[Try it here → ai-governance-tool.streamlit.app](https://ai-governance-tool.streamlit.app/)

## What It Does

Companies using AI internally face real compliance obligations under the EU AI Act. This tool lets a user input an AI use case, and autonomously:

- Classifies it by risk tier (Unacceptable, High, Limited, or Minimal Risk)
- Runs an Article 5 prohibited practice screen
- Maps applicable regulatory obligations to the specific use case
- Identifies compliance gaps
- Produces a prioritized remediation roadmap with timelines

Built for mid-market organizations who need practical EU AI Act guidance without enterprise-priced consultants.

## Built With

- Claude API (classification, gap analysis, roadmap generation)
- Python + Streamlit
- Anthropic claude-sonnet model

## About

Built by Derek Pignatelli — Privacy and AI Governance program leader with 18+ years of experience at Meta and Amazon. This tool demonstrates applied AI governance expertise and practical Claude API integration.

[LinkedIn](https://www.linkedin.com/in/derekpignatelli) | [GitHub](https://github.com/Schoobert)

## What I Learned

AI agents default to the path of least resistance on QA. Claude Code initially proposed validating the tool against 3 test cases. For a risk classification tool making regulatory judgments, that is nowhere near sufficient. I had to explicitly define testing scope and push back on shortcuts. Working effectively with AI coding agents means knowing when their defaults are adequate and when to override them.

Building with AI is cognitively demanding in a different way than building without it. The easy problems disappear because the agent solves them. What remains is continuous high-level judgment: evaluating outputs, catching errors, making architectural decisions, and knowing when something is good enough to ship. Long sessions were more mentally taxing than expected, not less.

AI assistance for session continuity is underrated. Using Claude to track progress across build sessions, maintain context between days, and pick up where the last session ended was more valuable than anticipated. It compressed the reorientation tax at the start of each session significantly.

## Production Considerations

This tool is scoped as a single-user portfolio demo. A production version would require user authentication and multi-tenant data isolation so that assessments from one organization are never accessible to another.

Assessment inputs — including AI use case descriptions and current safeguard details — are processed by the Anthropic API. A production version would require explicit user consent flows and a privacy policy disclosing that third-party AI services are used to process submitted data.

Token costs scale with both input length and assessment volume. A production version would need prompt caching on stable system prompt content, per-user usage caps, and usage-based pricing calibrated to actual cost-per-assessment to remain economically viable at scale.

The regulatory references in this tool reflect the EU AI Act as implemented at the time of the build. The Act's implementing acts and national supervisory authority guidance are still being finalized. A production version would need an ongoing process for reviewing and updating regulatory mappings as official guidance evolves — static regulatory content becomes a liability in an active enforcement environment.

This tool produces structured guidance to help organizations understand their potential obligations — it does not produce legal advice. A production version would require prominent, counsel-reviewed disclaimer language, and would need to consider whether the outputs create professional liability exposure depending on jurisdiction and use context.

## Disclaimer

This tool does not constitute legal advice. All article references should be verified against current EUR-Lex text.
