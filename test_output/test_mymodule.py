import mymodule
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestMyModule(TestCase):
    def test_prints(self):
        text = "this is an example"
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            mymodule.print_greeting(text)
            self.assertEqual(fake_stdout.getvalue(), "Hi %s!\n" % text)

