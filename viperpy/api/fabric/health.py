# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Health():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_health(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the VDC's health

        Example JSON result from the API:

        {
            "status": "GOOD",
            "sw_version": "fabric-1.0.0.1",
            "node_count": 48
        }

        :return: The health information
        """
        return self.conn.get('vdc/fabric/health')
