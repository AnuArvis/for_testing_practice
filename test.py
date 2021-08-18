def test_get_strand_output():
    """given well formed input it should produce expected output"""
    assert get_strand(0, 2) == "+"
    assert get_strand(20, 20000) == "+"
    assert get_strand(20000, 20) == "-"
    assert get_strand(2, 0) == "-"

test_get_strand_output()
