# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class HealthMonitor():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_stats(self, node_id=None, interval=0):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve statistics of a virtual machine and its
        active services

        If an interval value is passed it will return differential
        disk stats: difference between first report (contains stats
        for the time since system startup) and second report
        (stats collected during the interval since the first report)

        Required role(s):

        SYSTEM_ADMIN
        SYSTEM_MONITOR


        Example JSON result from the API:

        Too large to show


        :param node_id: node ids for which stats are collected
        :param interval: Specifies amount of time in seconds for differential
        stats

        :return: Virtual machine stats including memory
        usage, I/O for each device and load average numbers.
        Service stats include service memory usage, command
        that invoked it, file descriptors count and other
        stats (uptime, start time, thread count)
        """
        params = {
            'node_id': node_id,
            'interval': interval
        }

        return self.conn.get(
            'monitor/stats', params=params)

    def get_health(self, node_id=None):
        """
        Perform an HTTP GET against the ViPR endpoint to
        retrieve health of node and its services

        Service health status: Good - when a service is up and running
        Unavailable - when a service is not running but is
        registered in coordinator
        Restarted - when service is restarting

        Required role(s):

        SYSTEM_ADMIN
        SYSTEM_MONITOR


        Example JSON result from the API:

        {
            "node_health_list": {
                "node_health": [
                    {
                        "status": "Good",
                        "ip": "172.29.112.104",
                        "node_id": "nilea01-r08-06",
                        "service_health_list": {
                            "service_health": [
                                {
                                    "status": "Good",
                                    "name": "georeplayer"
                                },
                                {
                                    "status": "Good",
                                    "name": "fabric_zk_agent"
                                },
                                {
                                    "status": "Good",
                                    "name": "cm"
                                },
                                {
                                    "status": "Good",
                                    "name": "rm"
                                },
                                {
                                    "status": "Good",
                                    "name": "sysagent"
                                },
                                {
                                    "status": "Good",
                                    "name": "casheadsvc"
                                },
                                {
                                    "status": "Good",
                                    "name": "hdfssvc"
                                },
                                {
                                    "status": "Good",
                                    "name": "ssm"
                                },
                                {
                                    "status": "Good",
                                    "name": "fabricapi"
                                },
                                {
                                    "status": "Good",
                                    "name": "blobsvc"
                                },
                                {
                                    "status": "Good",
                                    "name": "georeceiver"
                                }
                            ]
                        }
                    },
                    {
                        "status": "Good",
                        "ip": "172.29.112.79",
                        "node_id": "nilea01-r05-05",
                        "service_health_list": {
                            "service_health": [
                                {
                                    "status": "Good",
                                    "name": "georeplayer"
                                },
                                {
                                    "status": "Good",
                                    "name": "fabric_zk_agent"
                                },
                                {
                                    "status": "Good",
                                    "name": "cm"
                                },
                                {
                                    "status": "Good",
                                    "name": "rm"
                                },
                                {
                                    "status": "Good",
                                    "name": "sysagent"
                                },
                                {
                                    "status": "Good",
                                    "name": "casheadsvc"
                                },
                                {
                                    "status": "Good",
                                    "name": "hdfssvc"
                                },
                                {
                                    "status": "Good",
                                    "name": "ssm"
                                },
                                {
                                    "status": "Good",
                                    "name": "fabricapi"
                                },
                                {
                                    "status": "Good",
                                    "name": "blobsvc"
                                },
                                {
                                    "status": "Good",
                                    "name": "georeceiver"
                                }
                            ]
                        }
                    }
                ]
            }
        }


        :param node_id: Node ID for which health stats are collected

        :return: The health of the node and its services
        """
        params = {
            'node_id': node_id
        }

        return self.conn.get(
            'monitor/health', params=params)

    def get_diagnostics(self, node_id=None, verbose=None):
        """
        Get results of diagtool shell script for all virtual
        machines in a ViPR controller appliance. Also gives
        test details when verbose option is set.

        Required role(s):

        SYSTEM_ADMIN
        SYSTEM_MONITOR

        Example JSON result from the API:

        {
            "node_diagnostics_list": {
                "node_diagnostics": {
                    "ip": "199.34.96.70",
                    "tests": "None",
                    "node_id": "nilea01-r05-05"
                }
            }
        }

        :param node_id: Node IDs for which diagnostic results are collected
        :param verbose: When set to "1" it will run the command with -v option
        """
        params = {
            'node_id': node_id,
            'verbose': verbose
        }

        return self.conn.get(
            'monitor/diagnostics', params=params)

    def get_storage_stats(self):
        """
        Get the current capacity for object, file and block storage.

        Required role(s):

        SYSTEM_ADMIN
        SYSTEM_MONITOR

        Example JSON result from the API:

        {
            "unstructured": {
                "capacity_kb": "1.103508799488E13"
            },
            "controller": {
                "file_managed_capacity_kb": "0.0",
                "block_managed_capacity_kb": "0.0",
                "free_managed_capacity_kb": "0.0"
            },
            "object": {
                "capacity_kb": "1.103508799488E13"
            }
        }
        """
        return self.conn.get('monitor/storage')
