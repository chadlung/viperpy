# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Audit():
    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_audit_log(self, time_bucket=None):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the bulk auditlogs and alerts in a
        specified time bucket (minute or hour)

        Example JSON result from the API:

        {
            "auditlogs": [
                {
                    "audit_type": "SSH_LOGIN",
                    "description": ""SSHauthentication(login/execution)forsvcuserfrom172.29.114.148to172.29.114.149succeed."",
                    "time_occurred": 1416355120000,
                    "operational_status": "SUCCESS",
                    "auditlog_id": "urn:storageos:AuditLog:de398a6e-2760-4b27-8440-6656355062c2",
                    "service_type": "SystemAudit",
                    "product_id": "ViPR 1.0"
                }
            ]
        }

        :param time_bucket: Time bucket for retrieval of audit logs.
        Acceptable formats are: yyyy-MM-dd'T'HH for hour bucket,
        yyyy-MM-dd'T'HH:mm for minute bucket
        Example: 2014-11-19T00:00
        """
        params = {
            'time_bucket': time_bucket
        }

        return self.conn.get('audit/logs', params=params)
