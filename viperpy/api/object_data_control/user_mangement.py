# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class UserManagement():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_objectusers(self, namespace=None):
        """
        Get the list of users provisioned for object storage

        Required role(s):

        SYSTEM_MONITOR
        SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "blobuser": [
                {
                    "userid": "user@somewhere",
                    "namespace": "namespace1"
                },
                {
                    "userid": "user2@helloworld",
                    "namespace": "namespace2"
                }
            ]
        }

        If namespace is provided then get list of all the
        users associated with a namespace

        Required role(s):

        SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "blobuser": [
                {
                    "userid": "user@somewhere",
                    "namespace": "namespace1"
                }
            ]
        }

        :param namespace: Example: namespace1

        Required role(s):

        SYSTEM_MONITOR
        SYSTEM_ADMIN


        """
        if namespace:
            return self.conn.get(url='object/users/{0}'.format(namespace))
        else:
            return self.conn.get(url='object/users')

    def get_objectuser_info(self, user):
        """
        Get object user info

        Required role(s):

        SYSTEM_ADMIN
        TENANT_ADMIN

        Example JSON result from the API:

        {
            "namespace": "namespace1",
            "name": "thucydides@peloponnese",
            "locked": False,
            "created": "Mon Jan 12 22:07:50 UTC 2015"
        }

        :param user: Example: thucydides@peloponnese
        """

        return self.conn.get(url='object/users/{0}/info'.format(user))

    def deactivate_objectuser(self, user, namespace=None):
        """
        Delete a user and all associated secret keys

        Required role(s):

        SYSTEM_ADMIN

        No JSON is returned from ViPR

        :param user: Example: user@somewhere
        :param namespace: Example: namespace1 (optional)
        """
        if namespace:
            payload = {
                "user": user,
                "namespace": namespace
            }
        else:
            payload = {
                "user": user
            }

        return self.conn.post(url='object/users/deactivate',
                              json_payload=payload)

    def add_objectuser(self, user, namespace):
        """
        Add a user, which can subsequently be used to create its secret key

        Required role(s):

        SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "link": {
                "href": "/object/user-secret-keys/test1",
                "rel": "self"
            }
        }

        :param user: Example: user@somewhere
        :param user: Example: namespace1
        """

        payload = {
            "user": user,
            "namespace": namespace
        }

        return self.conn.post(url='object/users',
                              json_payload=payload)

    def lock_objectuser(self, user, is_locked=True, namespace=None):
        """
        Lock/Unlock a user

        Required role(s):

        SYSTEM_ADMIN
        TENANT_ADMIN

        Example JSON result from the API:

        TODO: JSON data

        :param user: Example: user@somewhere
        :param namespace: Example: namespace1 (optional)
        :param is_locked: Example: True/False (optional)
        """
        if namespace:
            payload = {
                "user": user,
                "namespace": namespace,
                "isLocked": is_locked
            }
        else:
            payload = {
                "user": user,
                "isLocked": is_locked
            }

        return self.conn.put(url='object/users/lock',
                             json_payload=payload)

    def get_objectuser_lock(self, user, namespace=None):
        """
        Get user lock status

        Required role(s):

        SYSTEM_ADMIN
        TENANT_ADMIN

        Example JSON result from the API:

        TODO: JSON data

        :param user: Example: user@somewhere
        :param namespace: Example: namespace1 (optional)
        """

        if namespace:
            return self.conn.get(
                url='object/users/lock/{0}/{1}'.format(user, namespace))
        else:
            return self.conn.get(
                url='object/users/lock/{0}'.format(user))
