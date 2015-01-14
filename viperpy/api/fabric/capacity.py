# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Capacity():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_capacity(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the aggregated capacity info

        Example JSON result from the API:

        {
            "total_capacity": 11311005
        }

        :return: Capacity info for the entire Fabric
        """
        return self.conn.get('vdc/fabric/capacity')
