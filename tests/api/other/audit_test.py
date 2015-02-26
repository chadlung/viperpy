# Standard lib imports
import httplib
import unittest

# Third party imports
from mock import MagicMock
from mock import patch

# Project level imports
from viperpy import Viperpy
from viperpy.util.exceptions import ViperpyException


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(WhenTestingApiOtherAudit())
    return test_suite


class WhenTestingApiOtherAudit(unittest.TestCase):

    def setUp(self):
        self.vipr_endpoint = 'https://127.0.0.1:4443'
        self.token_endpoint = 'https://127.0.0.1:4443/login'

        self.client = Viperpy(
            vipr_endpoint=self.vipr_endpoint,
            token_endpoint=self.token_endpoint
        )

        self.returned_json = {
            "auditlogs": [
                {
                    "audit_type": "SSH_LOGIN",
                    "description": "SSHauthentication(login/execution)"
                                   "forsvcuserfrom172.29.114.148to"
                                   "172.29.114.149succeed.",
                    "time_occurred": 1416355120000,
                    "operational_status": "SUCCESS",
                    "auditlog_id": "urn:storageos:AuditLog:"
                                   "de398a6e-2760-4b27-8440-6656355062c2",
                    "service_type": "SystemAudit",
                    "product_id": "ViPR 2.1"
                }
            ]
        }

        self.response = MagicMock()

    def test_get_audit_log_should_throw_viperpyexception(self):
        self.response.status_code = httplib.INTERNAL_SERVER_ERROR
        self.requests = MagicMock(return_value=self.response)
        self.requests.get.side_effect = [self.response]

        with patch('viperpy.util.token_request.TokenRequest.get_new_token',
                   return_value='FAKE-TOKEN-123'):
            with patch('viperpy.util.token_request.requests.Session.get'):
                with self.assertRaises(ViperpyException):
                    self.client.audit.get_audit_log(
                        time_bucket='2014-11-19T00:00'
                    )

    def test_get_audit_log(self):
        self.response.status_code = httplib.OK
        self.response.body = self.returned_json
        self.response.json = MagicMock(return_value=self.returned_json)
        self.requests = MagicMock(return_value=self.response)
        self.requests.get.side_effect = [self.response]

        with patch(
                'viperpy.util.token_request.TokenRequest._get_existing_token',
                return_value='FAKE-TOKEN-123'):
            with patch('viperpy.requests.Session.get', self.requests):
                returned_json = self.client.audit.get_audit_log(
                    time_bucket='2014-11-19T00:00'
                )
                self.assertEquals(returned_json, self.returned_json)

if __name__ == '__main__':
    unittest.main()
