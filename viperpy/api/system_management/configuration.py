# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Configuration():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_config_properties(self):
        """
        Get system configuration properties

        Required role(s):

        SYSTEM_ADMIN
        SECURITY_ADMIN

        Example JSON result from the API:

        (Output is much longer, shortened for space concerns)

        {
            "properties": {
                "entry": [
                    {
                        "value": "0",
                        "key": "certificate_version"
                    },
                    {
                        "value": "5.9",
                        "key": "compute_redhat_linux_version"
                    },
                    {
                        "value": "11",
                        "key": "compute_suse_linux_version"
                    },
                    {
                        "value": "5.0",
                        "key": "compute_vmware_vcenter_version"
                    },
                    {
                        "value": "6.0.6002",
                        "key": "compute_windows_version"
                    }
                ]
            }
        }
        """
        return self.conn.get('config/properties')
