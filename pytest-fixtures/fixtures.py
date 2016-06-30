import pytest
import requests
import random
from unittest.mock import MagicMock, call, patch

@pytest.fixture
def random_word():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letters) for time in range(8))

def test_upper(random_word):
    assert random_word.upper() != random_word

def test_example_requests(monkeypatch):
    mockrequests = MagicMock(side_effect=[0, 1, 2])
    monkeypatch.setattr(requests, 'get', mockrequests)
    responses = []
    for i in range(3):
        responses.append(requests.get("http://myurl.com/%d" % i))

    assert responses == [0, 1, 2]
    assert mockrequests.call_args_list == [call("http://myurl.com/0"), call("http://myurl.com/1"), call("http://myurl.com/2")]

def test_patch_requests_get():
    with patch.object(requests, 'get') as mock_get:
        mock_get.side_effect = lambda *args,**kwargs: "kk"
        assert requests.get("http://myexample.com") == "kk"
        mock_get.assert_called_once_with("http://myexample.com")
