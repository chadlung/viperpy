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
        Get the current managed capacity.

        Example JSON result from the API:

        """
        # TODO: Add the JSON output (endpoint when tested was returning an error, confirmed this with cURL
        return self.conn.get(url='object/capacity')
