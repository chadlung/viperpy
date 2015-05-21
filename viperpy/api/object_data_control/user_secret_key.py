# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class UserSecretKey():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_user_secret_keys(self, uid, namespace=None):
        """
        Get all secret keys for specific user

        Required role(s):

        SYSTEM_MONITOR
        SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "secret_key_1": "NfgLnEzxKV0+iL5i0cfYwDnD7310uQC2VLhMsyVx",
            "key_timestamp_2": "2014-11-03 22:31:53.103",
            "key_timestamp_1": "2014-11-03 22:31:48.432",
            "link": {
                "href": "/object/secret-keys",
                "rel": "self"
            },
            "secret_key_2": "bAt/D2Ybc1Z+iYghwxTk6hIab4u4Mn5fWY/Iww1Z2"
        }

        :param uid: Valid user identifier to get the keys from
        :param namespace: The namespace
        """

        if namespace:
            return self.conn.get(
                url='object/user-secret-keys/{0}/{1}'.format(uid, namespace))
        else:
            return self.conn.get(
                url='object/user-secret-keys/{0}'.format(uid))

    def create_new_secret_key(self, uid, namespace=None,
                              key_expiration=2592000, secret_key=None):
        """
        Create new key for a specific user

        Required role(s):

        SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "link": {
                "rel": "self",
                "href":"/object/user-secret-keys/joedeleteme"
            },
            "secret_key": "p3PZyb//Ch6tM0fUsnesYYnGb+6JHV8WHzS5YHjg",
            "key_timestamp": "2014-12-24 02:08:40.181"
        }

        :param uid: Valid user identifier to create a key for
        :param namespace: The namespace
        :param key_expiration: Defaults to 30 days (2592000 seconds)
        :param secret_key: Manually specify the new secret key (ECS 2.0+).
        """
        payload = {
            "existing_key_expiry_time_mins": key_expiration,
            "namespace": namespace
        }

        if secret_key:
            payload['secretkey'] = secret_key

        return self.conn.post(url='object/user-secret-keys/{0}'.format(uid),
                              json_payload=payload)

    def deactivate_user_secret_key(self, uid, namespace=None,
                                   secret_key=None):
        """
        Create new key for a specific user

        Required role(s):

        SYSTEM_ADMIN

        Example JSON result from the API:

        There is no response body for this call

        :param uid: Valid user identifier to get delete the keys from
        :param namespace: The namespace
        :param secret_key: The secret key to deactivate
        """
        payload = {
            "secret_key": secret_key,
            "namespace": namespace
        }

        return self.conn.post(
            url='object/user-secret-keys/{0}/deactivate'.format(uid),
            json_payload=payload)
