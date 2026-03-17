# config.py
# Single source of truth for all model strings, token limits, and cost estimates.
# Update here only — do not reference model strings or limits elsewhere in the codebase.

# ---------------------------------------------------------------------------
# Model selection
# Haiku: validation, formatting, utility steps (no regulatory reasoning required)
# Sonnet: risk classification, regulatory mapping, gap analysis, roadmap generation
# DO NOT use Opus — cost not justified at POC stage
# DO NOT reference these strings anywhere else in the codebase
# ---------------------------------------------------------------------------
HAIKU_MODEL = "claude-haiku-4-5-20251001"
SONNET_MODEL = "claude-sonnet-4-6"

# ---------------------------------------------------------------------------
# Token limits — enforced in code, not just documented
# ---------------------------------------------------------------------------
MAX_FORM_TOKENS = 500         # Combined budget for all structured form fields
MAX_FREETEXT_TOKENS = 800     # Free-text description field
MAX_TOTAL_INPUT_TOKENS = 1300 # Hard cap: form + free text combined
MAX_OUTPUT_TOKENS = 2000      # Hard cap on Sonnet generation output

# Daily usage cap per user (enforced at Supabase level in M3)
MAX_ASSESSMENTS_PER_USER_PER_DAY = 10

# ---------------------------------------------------------------------------
# Cost estimates per 1,000 tokens (USD)
# Last verified: 2026-03-17 — recalculate if Anthropic changes pricing
# Haiku 4.5: $0.80/M input, $4.00/M output
# Sonnet 4.6: $3.00/M input, $15.00/M output
# ---------------------------------------------------------------------------
HAIKU_INPUT_COST_PER_1K = 0.00080
HAIKU_OUTPUT_COST_PER_1K = 0.00400
SONNET_INPUT_COST_PER_1K = 0.00300
SONNET_OUTPUT_COST_PER_1K = 0.01500

# ---------------------------------------------------------------------------
# Local usage log (Supabase logging added in M3)
# Logs assessment_id, token counts, cost — never raw content
# ---------------------------------------------------------------------------
USAGE_LOG_PATH = "api_usage_log.txt"
