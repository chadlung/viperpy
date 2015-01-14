# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Disk():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_disks(self, maximum=-1, index=0):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve the list of disks in the array

        Example JSON result from the API:

        {
            "disk": [
                {
                    "node_id": "urn:fabric:node:8f2c5a01-5551-11e3-b4fd-001e676a04b4:",
                    "link": {
                        "href": "/vdc/fabric/disks/urn:fabric:disk:003e12d7-9b4d-41fc-a353-ceeadec26827:",
                        "rel": "self"
                    },
                    "id": "urn:fabric:disk:003e12d7-9bdd-42fc-a353-ceeadec26827:",
                    "name": "/dev/sdav1"
                },
                {
                    "node_id": "urn:fabric:node:37f71ce1-51f8-11e3-b5f5-001e6769fd3e:",
                    "link": {
                        "href": "/vdc/fabric/disks/urn:fabric:disk:0391c6a3-35ed-449e-a247-4920c375c226:",
                        "rel": "self"
                    },
                    "id": "urn:fabric:disk:0091b6a3-35ed-449e-a247-4920c375c276:",
                    "name": "/dev/sdae1"
                }
            ]
        }

        :param maximum: Maximum number of items to return or -1 for all
        :param index: Index to start

        :return: Returns list of disks in the array
        """
        params = {
            'index': index,
            'max': maximum
        }

        return self.conn.get('vdc/fabric/disks', params=params)

    def get_disk_by_urn(self, urn=''):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve info about a single disk

        Example JSON result from the API:

        {
            "disk_hwid": "1EG5TP7B",
            "link": {
                "href": "/vdc/fabric/disks/urn:fabric:disk:0091c6a3-35fd-449e-a247-4920c375c226:",
                "rel": "self"
            },
            "id": "urn:fabric:disk:0091c6a3-35ed-449e-a247-4920c335c226:",
            "disk_swid": "0091c6a3-37ed-449e-a247-4920c375c226",
            "name": "/dev/sdae1"
        }

        :param urn: URN value of the disk to fetch info on

        :return: Returns info about a single disk
        """
        return self.conn.get('vdc/fabric/disks/{0}'.format(urn))

    def get_disk_capacity(self, urn=''):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve single disk capacity info

        Example JSON result from the API:

        {
            "total_capacity": 6021
        }

        :param urn: URN value of the disk to fetch capacity info on

        :return: Returns single disk capacity info
        """
        return self.conn.get('vdc/fabric/disks/{0}/capacity'.format(urn))
