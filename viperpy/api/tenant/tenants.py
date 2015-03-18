# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Tenants():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_tenants_bulk(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the tenants bulk payload

        :return: A list of Tenant IDs
        """
        json_data = self.conn.get('tenants/bulk')
        return json_data['id']

    def get_tenant(self, tenant_id):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the tenant's information

        :return: The tenant's information
        """
        return self.conn.get('tenants/{0}'.format(tenant_id))

    def get_subtenants(self, tenant_id):
        return self.conn.get('tenants/{0}/subtenants'.format(tenant_id))
