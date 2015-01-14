# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Node():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_nodes(self, maximum=-1, index=0):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve a list of nodes in the array

        Example JSON result from the API:

        {
            "node": [
                {
                    "link": {
                        "href": "/vdc/fabric/nodes/urn:fabric:node:02edcf91-5086-11e3-a7f8-001e6769f9a1:",
                        "rel": "self"
                    },
                    "id": "urn:fabric:node:02edcf91-5086-11e3-a7f8-001e6769f9a1:",
                    "name": "nilea01-r05-02"
                },
                {
                    "link": {
                        "href": "/vdc/fabric/nodes/urn:fabric:node:24115e71-4fbe-11e3-b044-001e6769e808:",
                        "rel": "self"
                    },
                    "id": "urn:fabric:node:24115e71-4fbe-11e3-b044-001e6769e808:",
                    "name": "nilea01-r05-04"
                }
            ]
        }

        :param maximum: Maximum number of items to return or -1 for all
        :param index: Index to start

        :return: Returns list of nodes in the array
        """
        params = {
            'max': maximum,
            'index': index
        }

        return self.conn.get('vdc/fabric/nodes', params=params)
