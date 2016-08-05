from hypothesis import given, example
from hypothesis.strategies import text

@example('helLo!')
@given(text())
def test_upper_and_lower(s):
    assert s == s

