# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class VirtualPools():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_vpools_bulk(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the block vpools bulk payload

        :return: A list of vpools IDs
        """
        json_data = self.conn.get('block/vpools/bulk')
        return json_data['id']

    def get_vpools_bulk_by_id(self, vpool_ids):
        """
        Retrieve detailed information about a set of vpools

        :param vpool_ids: A list of vpool IDs
        :return: A list of vpools
        """
        json_data = self.conn.post(url='block/vpools/bulk',
                                   json_payload={"id": vpool_ids})
        return json_data['block_vpool']

    def get_vpool(self, vpool_id):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the block vpool's information

        :return: The block vpool's information
        """
        return self.conn.get('block/vpools/{0}'.format(vpool_id))
