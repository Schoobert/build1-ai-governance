# input_handler.py
# Accepts structured form fields and free-text description.
# Enforces token limits before any API call is made.

import uuid
from dataclasses import dataclass, field
from config import MAX_FORM_TOKENS, MAX_FREETEXT_TOKENS, MAX_TOTAL_INPUT_TOKENS


@dataclass
class AssessmentInput:
    use_case_name: str
    industry: str
    deployment_context: str
    current_safeguards: str
    free_text_description: str
    assessment_id: str = field(default_factory=lambda: str(uuid.uuid4()))


class TokenLimitError(Exception):
    """Raised when input exceeds a configured token limit."""
    pass


def estimate_tokens(text: str) -> int:
    """
    Conservative token estimate using characters / 3.

    Intentionally overestimates (true ratio is closer to 1 token per 4 chars for
    English) to provide a safety buffer. Better to reject borderline inputs than
    to silently exceed limits and incur unexpected cost or API errors.
    """
    return (len(text) + 2) // 3


def validate_and_prepare_input(raw_input: AssessmentInput) -> AssessmentInput:
    """
    Validates token limits on all input fields.

    Raises TokenLimitError with a descriptive message if any limit is exceeded.
    Returns the input unchanged if all limits are satisfied.

    Checks (in order):
      1. Form fields combined <= MAX_FORM_TOKENS (500)
      2. Free-text description <= MAX_FREETEXT_TOKENS (800)
      3. Total input <= MAX_TOTAL_INPUT_TOKENS (1300) — hard cap
    """
    # Check form fields combined
    form_text = " ".join([
        raw_input.use_case_name,
        raw_input.industry,
        raw_input.deployment_context,
        raw_input.current_safeguards,
    ])
    form_tokens = estimate_tokens(form_text)

    if form_tokens > MAX_FORM_TOKENS:
        raise TokenLimitError(
            f"Form fields exceed limit: ~{form_tokens} estimated tokens "
            f"(max {MAX_FORM_TOKENS}). Please shorten your entries."
        )

    # Check free-text field
    freetext_tokens = estimate_tokens(raw_input.free_text_description)

    if freetext_tokens > MAX_FREETEXT_TOKENS:
        raise TokenLimitError(
            f"Free-text description exceeds limit: ~{freetext_tokens} estimated tokens "
            f"(max {MAX_FREETEXT_TOKENS}, approximately 2,400 characters). "
            f"Please shorten your description."
        )

    # Hard cap on total
    total_tokens = form_tokens + freetext_tokens
    if total_tokens > MAX_TOTAL_INPUT_TOKENS:
        raise TokenLimitError(
            f"Total input exceeds hard cap: ~{total_tokens} estimated tokens "
            f"(max {MAX_TOTAL_INPUT_TOKENS}). Please reduce form fields or description."
        )

    return raw_input


def format_for_prompt(inp: AssessmentInput) -> str:
    """Returns all input fields as a structured string for inclusion in prompts."""
    return (
        f"Use Case Name: {inp.use_case_name}\n"
        f"Industry: {inp.industry}\n"
        f"Deployment Context: {inp.deployment_context}\n"
        f"Current Safeguards in Place: {inp.current_safeguards}\n"
        f"Description: {inp.free_text_description}"
    )
