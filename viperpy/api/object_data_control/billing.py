# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Billing():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_bucket_billing_info(self, namespace, bucket_name):
        """
        Gets billing information about a bucket, specifically the current
        object count and storage utilization for the bucket.

        Required role(s):

        SYSTEM_ADMIN
        SYSTEM_MONITOR
        TENANT_ADMIN

        TODO: Add JSON sample

        :param namespace: The namespace containing the bucket
        :param bucket_name: The bucket name
        """
        return self.conn.get(
            'object/billing/buckets/{0}/{1}/info'.format(
                namespace, bucket_name))

    def get_bucket_namespace_info(
            self, namespace, include_bucket_detail, marker=None):
        """
        Gets billing information about a namespace and its buckets. Note that
        due to the fact that sampling a namespace's buckets takes some time
        it's possible that the values for the buckets will not sum to equal
        the namespace's values.

        Required role(s):

        SYSTEM_ADMIN
        SYSTEM_MONITOR
        TENANT_ADMIN

        TODO: Add JSON sample

        :param namespace: The namespace containing the bucket
        :param include_bucket_detail: Whether to include bucket details
        :param marker: Used to continue a truncated response. Omit this
        parameter on the first request
        """

        params = {
            'include_bucket_detail': include_bucket_detail,
            'marker': marker
        }

        return self.conn.get(
            'object/billing/namespace/{namespace}/info'.format(namespace),
            params=params)

    def get_bucket_billing_sample(
            self, namespace, bucket_name, start_time, end_time):
        """
        Gets billing information for a bucket over the given time range.
        By default, buckets are sampled every 5 minutes. If the requested
        time range includes multiple samples, the data will be aggregated.

        Required role(s):

        SYSTEM_ADMIN
        SYSTEM_MONITOR
        TENANT_ADMIN


        TODO: Add JSON sample

        :param namespace: The namespace containing the bucket
        :param bucket_name: The bucket name
        :param start_time: Starting time for the sample(s) in ISO-8601 minute
        format
        :param end_time: Ending time for the sample(s) in ISO-8601 minute
        format
        """
        params = {
            'start_time': start_time,
            'end_time': end_time
        }

        return self.conn.get(
            'object/billing/buckets/{0}/{1}/sample'.format(
                namespace, bucket_name), params=params)

    def get_namespace_billing_sample(
            self, namespace, start_time, end_time, include_bucket_detail,
            marker=None):
        """
        Gets billing information for a particular time period for a namespace
        and optionally its buckets. Note that this method will return one and
        only one time sample so if the start_time and end_time do not align
        with a sampled time period, the matching samples will be aggregated.
        Check the response for the actual time period sampled. Also note that
        due to the fact that sampling a namespace's buckets takes some time
        it's possible that the values for the buckets will not sum to equal
        the namespace's values.

        Required role(s):

        SYSTEM_ADMIN
        SYSTEM_MONITOR
        TENANT_ADMIN


        TODO: Add JSON sample

        :param namespace: The namespace containing the bucket
        :param start_time: Starting time for the sample(s) in ISO-8601 minute
        format
        :param end_time: Ending time for the sample(s) in ISO-8601 minute
        format
        :param include_bucket_detail: Whether to include bucket details
        :param marker: Used to continue a truncated response. Omit this
        parameter on the first request
        """
        params = {
            'start_time': start_time,
            'end_time': end_time,
            'include_bucket_detail': include_bucket_detail,
            'marker': marker
        }

        if marker is None:
            return self.conn.get(
                'object/billing/namespace/{0}/sample'.format(namespace),
                params=params)
