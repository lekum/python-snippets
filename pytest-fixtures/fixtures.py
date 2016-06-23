import pytest
import random

@pytest.fixture
def random_word():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letters) for time in range(8))

def test_upper(random_word):
    assert random_word.upper() != random_word

