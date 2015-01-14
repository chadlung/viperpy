# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class ObjectSoftQuota():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_bucket_quota(self, namespace, bucket_name):
        """
        Gets Bucket SoftQuota

        Required role(s):

        This call has no restrictions

        Example JSON result from the API:

        TODO: JSON data
        """
        return self.conn.get(
            url='object/softquota/buckets/{0}/{1}'.format(
                namespace, bucket_name))

    def get_namespace_quota(self, namespace):
        """
        Gets Namespace SoftQuota

        Required role(s):

        This call has no restrictions

        Example JSON result from the API:

        TODO: JSON data
        """
        return self.conn.get(
            url='object/softquota/namespace/{0}'.format(namespace))

    def update_bucket_quota(self, bucket_name, soft_quota_in_gb):
        """
        Update the Bucket Soft Quota

        Required role(s):

        This call has no restrictions

        Example JSON result from the API:

        TODO: JSON data
        """
        self._verify_is_num(soft_quota_in_gb)

        payload = {
            "namespace": "",
            "soft_quota_in_gb": soft_quota_in_gb
        }

        return self.conn.put(
            url='object/softquota/buckets/{0}'.format(bucket_name),
            json_payload=payload)

    def update_namespace_quota(self, namespace, soft_quota_in_gb):
        """
        Update the Namespace Soft Quota

        Required role(s):

        This call has no restrictions

        Example JSON result from the API:

        TODO: JSON data
        """
        self._verify_is_num(soft_quota_in_gb)

        payload = {
            "soft_quota_in_gb": soft_quota_in_gb
        }

        return self.conn.put(
            url='object/softquota/namespace/{0}'.format(namespace),
            json_payload=payload)

    def remove_bucket_quota(self, namespace, bucket_name):
        """
        Remove Bucket Quota

        Required role(s):

        This call has no restrictions

        Example JSON result from the API:

        TODO: JSON data
        """
        return self.conn.put(
            url='object/softquota/buckets/{0}/{1}'.format(
                namespace, bucket_name))

    @staticmethod
    def _verify_is_num(value):
        try:
            return int(value)
        except ValueError as err:
            raise err
