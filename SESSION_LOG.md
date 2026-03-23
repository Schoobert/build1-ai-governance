# Session Log — Build 1: AI Governance Readiness Assessment Tool

## March 12, 2026
- Set up MacBook Air (macOS Tahoe 26.3.1)
- Installed Homebrew, Python 3.14, Node.js v25, Git, Claude Code
- Created project directory with CLAUDE.md, .env, .gitignore
- Claude Code authenticated and confirmed reading CLAUDE.md
- All risk register items unchecked — pre-M1, no code written yet
- Loaded $50 API credit, auto-reload off

## March 17, 2026 — M1 complete
- Built core agentic pipeline: config.py, input_handler.py, pipeline.py, main.py
- Token limits enforced in code: 500 form / 800 free text / 1,300 total input / 2,000 output
- Two-model architecture implemented: Haiku for validation, Sonnet for classification/reasoning
- All model strings centralized in config.py — no hardcoding elsewhere
- Mandatory disclaimer (exact CLAUDE.md language) appears top and bottom of every output
- Local token logging operational: api_usage_log.txt logs assessment_id, model, step, tokens, cost — no raw content
- Bug fixed: load_dotenv(override=True) required because shell had ANTHROPIC_API_KEY='' set in environment
- M1 all six risk checks passed
- M2 spot-checks completed same session — all three risk tiers validated with fictional test cases:
  - Minimal: AI Email Spam Filter — $0.0150, 1,003 input / 1,015 output tokens
  - High: AI Performance Review System — $0.0146, 849 input / 955 output tokens
  - Limited: AI Customer Service Chatbot — $0.0143, 947 input / 976 output tokens
- One M2 item left open: EUR-Lex regulatory reference verification (manual — complete before M3 sign-off)
- Next session: M3 Streamlit front-end

