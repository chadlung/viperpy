# Standard lib imports
import httplib
import unittest

# Third party imports
from mock import MagicMock
from mock import mock_open
from mock import patch

# Project level imports
from viperpy.util.token_request import TokenRequest
from viperpy.util.exceptions import ViperpyException


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(WhenTestingTokenRequest())
    return test_suite


class WhenTestingTokenRequest(unittest.TestCase):

    def setUp(self):
        self.token_file_contents = '123TOKEN'
        self.response = MagicMock()
        self.session_get = 'viperpy.util.token_request.requests.Session.get'

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

    def test_get_new_token_should_throw_viperpyexception_500(self):
        self.response.status_code = httplib.INTERNAL_SERVER_ERROR
        self.requests = MagicMock(return_value=self.response)
        self.requests.get.side_effect = [self.response]

        with patch(self.session_get, self.requests):
            with self.assertRaises(ViperpyException):
                self.token_request.get_new_token()

    def test_get_new_token_should_throw_viperpyexception_401(self):
        self.response.status_code = httplib.UNAUTHORIZED
        self.requests = MagicMock(return_value=self.response)
        self.requests.get.side_effect = [self.response]

        with patch(self.session_get, self.requests):
            with self.assertRaises(ViperpyException):
                self.token_request.get_new_token()

if __name__ == '__main__':
    unittest.main()
