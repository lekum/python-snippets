import pytest
import requests
import random
from unittest.mock import MagicMock

@pytest.fixture
def random_word():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letters) for time in range(8))

def test_upper(random_word):
    assert random_word.upper() != random_word

def test_example_requests(monkeypatch):
    mockreturn = MagicMock(return_value="kk")
    monkeypatch.setattr(requests, 'get', mockreturn)
    r = requests.get("http://myurl.com")
    assert r == "kk"
    mockreturn.assert_called_once_with("http://myurl.com")
