# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Namespace():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_namespaces(self):
        """
        Returns the identifiers for all of the configured namespaces

        Required role(s):

        SYSTEM_MONITOR
        SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "namespace": [
                {
                    "link": {
                        "href": "/object/namespaces/namespace/namespace1",
                        "rel": "self"
                    },
                    "name": "namespace1",
                    "id": "namespace1"
                },
                {
                    "link": {
                        "href": "/object/namespaces/namespace/namespace2",
                        "rel": "self"
                    },
                    "name": "namespace2",
                    "id": "namespace2"
                }
            ]
        }
        """
        return self.conn.get(url='object/namespaces')

    def get_namespace_info(self, namespace_identifier):
        """
        Returns detailed info for a specific namespace

        Required role(s):

        SYSTEM_MONITOR
        SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "default_data_services_vpool": "rn:storageos:ReplicationGroupInfo:0c10681a-9b32-4b85-961f-1424ba1e7133:global",
            "remote": "None",
            "name": "namespace1",
            "tags": [],
            "global": "None",
            "disallowed_vpools_list": [],
            "vdc": "None",
            "inactive": "False",
            "link": {
                "href": "/object/namespaces/namespace/namespace1",
                "rel": "self"
            },
            "default_object_project": "rn:storageos:Project:9dec8645-b467-4c6a-a2f2-287cbc746201:global",
            "allowed_vpools_list": [],
            "id": "namespace1",
            "tenant": "rn:storageos:TenantOrg:0324851a-9411-474d-a8f7-29bfff07f536:global"
        }

        :param namespace_identifier: Namespace identifier
        """
        return self.conn.get(
            url='object/namespaces/namespace/{0}'.format(
                namespace_identifier))
