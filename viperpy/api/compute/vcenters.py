# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Vcenters():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_vcenters_bulk(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the vcenter bulk payload

        :return: A list of vcenters IDs
        """
        json_data = self.conn.get('compute/vcenters/bulk')
        return json_data['id']

    def get_vcenters_bulk_by_id(self, vcenter_ids):
        """
        Retrieve detailed information about a set of vcenters

        :param vcenter_ids: A list of vcenter IDs
        :return: A list of vcenters
        """
        json_data = self.conn.post(url='compute/vcenters/bulk',
                                   json_payload={"id": vcenter_ids})
        return json_data['vcenter']

    def get_vcenter(self, vcenter_id):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the vCenter's information

        :return: The vcenter's information
        """
        return self.conn.get('compute/vcenters/{0}'.format(vcenter_id))

    def update(self, vcenter_id, ip_address=None, name=None, port_number=None,
               username=None, password=None, use_ssl=None, os_version=None):
        '''
        Update the configuration of a vCenter object

        :param vcenter_id: ID of the vCenter object to update
        :param ip_address: The IP address of the vCenter (optional)
        :param name: Inventory name of the vCenter (optional)
        :param port_number: Port to use for communication with the vCenter (optional)
        :param username: Username to use to connect to the vCenter (optional)
        :param password: Password to use to connect to the vCenter (optional)
        :param use_ssl: Whether to use SSL for communication (optional)
        :param os_version: OS version of the vCenter (optional)
        :return: The vcenter's information
        '''
        payload = {
            'ip_address': ip_address,
            'name': name,
            'port_number': port_number,
            'username': username,
            'password': password,
            'use_ssl': use_ssl,
            'os_version': os_version
        }
        # Remove empty values from payload
        payload = dict((k, v) for k, v in payload.iteritems() if v)
        return payload
        return self.conn.put(url='compute/vcenters/{0}'.format(vcenter_id),
                             json_payload=payload)

    def discover(self, vcenter_id):
        """
        Perform an HTTP POST against the ViPR endpoint to
        discover a vCenter

        :return: The vcenter's information
        """
        return self.conn.post('compute/vcenters/{0}/discover'.format(vcenter_id))
