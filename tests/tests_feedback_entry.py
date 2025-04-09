def test_collect_feedback_empty_input(monkeypatch):
    """Test that collect_feedback handles empty input."""
    inputs = iter(['', '', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    feedback = collect_feedback()
    assert feedback['student_id'] == ''
    assert feedback['subject'] == ''
    assert feedback['comments'] == ''
