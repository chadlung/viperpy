# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Volumes():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_volumes_bulk(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the block volumes bulk payload

        :return: A list of volumes IDs
        """
        json_data = self.conn.get('block/volumes/bulk')
        return json_data['id']

    def get_volume(self, volume_id):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the block volume's information

        :return: The block volume's information
        """
        return self.conn.get('block/volumes/{0}'.format(volume_id))
