# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class UserInfo():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def whoami(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the list of tenants that the user
        maps to including the details of the mappings.
        It also returns a list of the virtual data center
        roles and tenant roles assigned to this user

        Example JSON result from the API:

        {
            "subtenant_roles": [],
            "distinguished_name": "root",
            "home_tenant_roles": [],
            "vdc_roles": [
                "RESTRICTED_SECURITY_ADMIN",
                "SYSTEM_AUDITOR",
                "RESTRICTED_SYSTEM_ADMIN",
                "SYSTEM_MONITOR"
            ],
            "common_name": "root",
            "tenant": "urn:storageos:TenantOrg:0474851a-9481-474d-a8f7-29cfaf07f536:global"
        }
        """

        return self.conn.get('user/whoami')

    def get_tenant(self, username=None):
        """
        Perform an HTTP GET against the ViPR endpoint to
        evaluate the tenancies that this user maps to based
        on the mappings defined in the Tenants in the system.

        If the username param is not specified it will fetch
        the common_name from the whoami results.

        Example JSON result from the API:

        {
            "tenant": [
                {
                    "id": "urn:storageos:TenantOrg:9474851b-9481-474d-a8f1-29cfaf07f536:global"
                }
            ]
        }

        :param username: The username for which to retrieve the tenant list
        """

        if username:
            params = {
                'username': username
            }
        else:
            whoami_data = self.whoami()
            params = {
                'username': whoami_data['common_name']
            }

        return self.conn.get(
            'user/tenant', params=params)
