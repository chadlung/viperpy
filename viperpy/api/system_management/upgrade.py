# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Upgrade():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_target_version(self):
        """
        Show the current target version

        Required role(s):

        SYSTEM_ADMIN
        RESTRICTED_SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "target_version": "vipr-2.1.0.1.447"
        }

        """
        return self.conn.get('upgrade/target-version')

    def get_cluster_state(self, force=False):
        """
        Show cluster state

        Required role(s):

        SYSTEM_ADMIN
        SECURITY_ADMIN
        SYSTEM_MONITOR

        Example JSON result from the API:

        {
            "target_state": {
                "available_versions": {
                    "available_version": "vipr-2.1.0.1.447"
                },
                "current_version": "vipr-2.1.0.1.447",
                "config_version": "1416366397891"
            },
            "control_nodes": {
                "entry": [
                    {
                        "value": {
                            "available_versions": {
                                "available_version": "vipr-2.1.0.1.447"
                            },
                            "current_version": "vipr-2.1.0.1.447",
                            "config_version": "1416366397891"
                        },
                        "key": "vipr3"
                    },
                    {
                        "value": {
                            "available_versions": {
                                "available_version": "vipr-2.1.0.1.447"
                            },
                            "current_version": "vipr-2.1.0.1.447",
                            "config_version": "1416366397891"
                        },
                        "key": "vipr2"
                    },
                    {
                        "value": {
                            "available_versions": {
                                "available_version": "vipr-2.1.0.1.447"
                            },
                            "current_version": "vipr-2.1.0.1.447",
                            "config_version": "1416366397891"
                        },
                        "key": "vipr1"
                    }
                ]
            },
            "cluster_state": "STABLE"
        }

        :param force: If force=True it will show all removable versions even
        though the installed versions are less than MAX_SOFTWARE_VERSIONS
        """
        params = {
            'force': force
        }

        return self.conn.get(
            'upgrade/cluster-state', params=params)

    def get_download_progress(self):
        """
        Check the version downloading progress.
        The download could be from remote repository

        Required role(s):

        SYSTEM_ADMIN
        RESTRICTED_SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "progress": "None",
            "imageSize": "0"
        }

        """
        return self.conn.get('upgrade/image/download/progress')
