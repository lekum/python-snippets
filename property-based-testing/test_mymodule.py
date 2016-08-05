from hypothesis import given
from hypothesis import strategies as st

from mymodule import random_choice

@given(st.lists(st.text()))
def test_random_choice_over_list_of_strings(s):
    if len(s) == 0:
        return None
    r = random_choice(s)
    assert r in s

@given(st.lists(st.integers()))
def test_random_choice_over_list_of_integers(s):
    if len(s) == 0:
        return None
    r = random_choice(s)
    assert r in s

@given(st.text())
def test_random_choice_over_a_string(s):
    if len(s) == 0:
        return None
    r = random_choice(s)
    assert r in s
