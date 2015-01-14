# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Services():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_services(self):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve a list of services available on the array

        Example JSON result from the API:

        {
            "service": [
                {
                    "link": {
                        "href": "/vdc/fabric/services/urn:fabric:service:Block:",
                        "rel": "self"
                    },
                    "id": "urn:fabric:service:Block:",
                    "name": "Block"
                },
                {
                    "link": {
                        "href": "/vdc/fabric/services/urn:fabric:service:Object:",
                        "rel": "self"
                    },
                    "id": "urn:fabric:service:Object:",
                    "name": "Object"
                }
            ]
        }

        :return: Returns a list of services available on the array
        """
        return self.conn.get('vdc/fabric/services')
