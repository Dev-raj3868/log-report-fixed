import json
from pathlib import Path


REPORT = Path("/app/report.json")


def load_report():
    assert REPORT.exists(), "report.json not found"
    with REPORT.open("r", encoding="utf-8") as f:
        return json.load(f)


def test_output_exists():
    """Success Criterion 1: Produce the required JSON output."""
    assert REPORT.exists(), "report.json not found"


def test_output_is_valid_json():
    """Success Criterion 2: The output must be valid JSON."""
    with REPORT.open("r", encoding="utf-8") as f:
        json.load(f)


def test_required_fields_present():
    """Success Criterion 3: Include all required summary fields."""
    report = load_report()

    assert "total_requests" in report
    assert "clients" in report
    assert "popular_pages" in report


def test_field_types():
    """Success Criterion 4: Required fields have the correct types."""
    report = load_report()

    assert isinstance(report["total_requests"], int)
    assert isinstance(report["clients"], list)
    assert isinstance(report["popular_pages"], list)


def test_popular_pages_schema():
    """Success Criterion 5: Each popular_pages entry has the required fields."""
    report = load_report()

    for page in report["popular_pages"]:
        assert isinstance(page, dict)
        assert "page" in page
        assert "request_count" in page
        assert isinstance(page["page"], str)
        assert isinstance(page["request_count"], int)