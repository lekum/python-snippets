import unittest
from funcs import get_title
from unittest.mock import patch

class TestGetURL(unittest.TestCase):

    @patch('funcs.requests.get')
    def test_url(self, mock_requests_get):

        sample_page ="""<html lang="en">
        <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <title>title</title>
        <link rel="stylesheet" type="text/css" href="style.css">
        <script type="text/javascript" src="script.js"></script>
        </head>
        <body></body>
        </html>"""

        mock_requests_get.return_value.content = sample_page
        self.assertEqual(get_title("http://example.org"), "title")
        mock_requests_get.assert_called_with("http://example.org")

if __name__ == "__main__":
    unittest.main()
