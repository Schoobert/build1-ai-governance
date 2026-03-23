# main.py
# M1 pipeline test runner.
# Run: python main.py
# Verifies the full pipeline end-to-end with a fictional test case.
# Check api_usage_log.txt after running for token usage records.

import sys
from input_handler import AssessmentInput, validate_and_prepare_input, TokenLimitError
from pipeline import run_assessment, ValidationError


def main():
    print("AI Governance Readiness Assessment Tool — M1 Pipeline Test")
    print("=" * 60)

    # ------------------------------------------------------------------
    # Test case: Minimal risk — AI email spam filter
    # Fictional company, no real data used
    # ------------------------------------------------------------------
    test_input = AssessmentInput(
        use_case_name="AI-Powered Email Spam Filter",
        industry="Professional Services",
        deployment_context=(
            "Internal IT tool used by 250 employees to filter incoming email. "
            "No external-facing use. Managed by the IT department."
        ),
        current_safeguards=(
            "Users can mark false positives. IT reviews quarantine folder weekly. "
            "No automated deletion — all filtered emails go to a quarantine folder."
        ),
        free_text_description=(
            "We are deploying a third-party AI-based spam and phishing detection tool "
            "for our internal email system. The AI model scores incoming emails for "
            "spam likelihood and phishing indicators. Emails above a threshold score "
            "are moved to a quarantine folder where users can review them. No emails "
            "are automatically deleted. The tool is a commercial off-the-shelf product "
            "and we are a downstream deployer, not the developer. We have no visibility "
            "into the underlying model. We currently have no formal AI governance policy "
            "and have not assessed this tool under the EU AI Act."
        ),
    )

    print(f"\nTest case  : {test_input.use_case_name}")
    print(f"Industry   : {test_input.industry}")
    print(f"Assessment : {test_input.assessment_id}")
    print()

    # Step 1: Validate token limits before any API call
    print("Validating input token limits...")
    try:
        validated = validate_and_prepare_input(test_input)
        print("  [OK] Token limits satisfied.")
    except TokenLimitError as e:
        print(f"  [FAIL] Token limit error: {e}")
        sys.exit(1)

    # Step 2: Run the pipeline
    print("Running pipeline (Haiku validation → Sonnet assessment)...")
    try:
        result = run_assessment(validated)
    except EnvironmentError as e:
        print(f"  [FAIL] Environment error: {e}")
        sys.exit(1)
    except ValidationError as e:
        print(f"  [FAIL] Input validation rejected: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"  [FAIL] Unexpected error: {e}")
        sys.exit(1)

    print("  [OK] Pipeline completed.\n")
    print(result)
    print("\n[PASS] M1 pipeline test complete.")
    print("Token usage logged to api_usage_log.txt")


if __name__ == "__main__":
    main()
