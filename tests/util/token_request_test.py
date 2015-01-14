# Standard lib imports
import unittest

# Third party imports
from mock import MagicMock
from mock import mock_open
from mock import patch

# Project level imports
from viperpy.util.token_request import TokenRequest


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(WhenTestingTokenRequest())
    return test_suite


class WhenTestingTokenRequest(unittest.TestCase):

    def setUp(self):
        self.token_file_contents = '123TOKEN'
        self.conf = MagicMock()

        self.token_request = TokenRequest(username='someone',
                                          password='password',
                                          vipr_endpoint='https://localhost',
                                          token_endpoint='https://localhost',
                                          verify_ssl=False,
                                          token_filename='viperpy.tkn',
                                          token_location='/tmp',
                                          request_timeout=5.0,
                                          cache_token=True)

    def test_should_get_existing_token(self):
        with patch('os.path.isfile', return_value=True),\
            patch('__builtin__.open', mock_open(read_data='123TOKEN'),
                  create=True):
            self.assertEqual(self.token_request._get_existing_token(),
                             self.token_file_contents)

    def test_should_not_get_existing_token(self):
        with patch('os.path.isfile', return_value=False):
            self.assertEqual(self.token_request._get_existing_token(), None)

if __name__ == '__main__':
    unittest.main()
