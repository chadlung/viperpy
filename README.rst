ViperPy
=======

A Python library for interacting with the EMC ViPR API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://travis-ci.org/chadlung/viperpy.svg?branch=master
    :target: https://travis-ci.org/chadlung/viperpy

**Note:** `ViPR <https://www.emc.com/vipr>`__ is an EMC product,
trademarked, copyrighted, etc.

If you are using the ECS (Elastic Cloud Storage) product it is recommended that you
use `ECSMinion <https://github.com/chadlung/ecsminion>`__ to communicate with the
Management APIs.

Using this library is pretty straight forward. ViperPy can be installed
from `PyPi <http://pypi.python.org/>`__:

::

    $ pip install viperpy

Creating an instance of the ViperPy class requires the following
arguments:

+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Name                  | Required   | Default Value     | Description                                                                                                                                   |
+=======================+============+===================+===============================================================================================================================================+
| ``username``          | No         | None              | The username used to fetch the ViPR token                                                                                                     |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``password``          | No         | None              | The password used to fetch the ViPR token                                                                                                     |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``token``             | No         | None              | Pass a token to ViperPy (username/password are ignored then)                                                                                  |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``vipr_endpoint``     | Yes        | None              | The ViPR API endpoint, ex: ``https://192.168.1.146:4443``                                                                                     |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``token_endpoint``    | Yes        | None              | The ViPR API endpoint, ex: ``https://192.168.1.146:4443/login``                                                                               |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``verify_ssl``        | No         | False             | Whether to check a host's SSL certificate                                                                                                     |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``token_filename``    | No         | ``ViperPy.tkn``   | The filename of the temporary token                                                                                                           |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``token_location``    | No         | ``/tmp``          | The location to store the temporary token file                                                                                                |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``request_timeout``   | No         | 15.0              | Stop waiting for a response after a given number of seconds, this is a decimal value. Ex: 10.0 is ten seconds                                 |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``cache_token``       | No         | True              | Whether to cache the token, by default this is true you should only switch this to false when you want to directly fetch a token for a user   |
+-----------------------+------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

Here is an example that goes through most of the API calls. Please note
that some calls take longer to complete than others. Sometimes you may
need to set your ``request_timeout`` to ``60.0``.

::

        from viperpy import Viperpy, ViperpyException
        from viperpy.util.common import get_formatted_time_string

        try:
            client = Viperpy(username='someone',
                               password='password',
                               token_endpoint='https://192.168.1.146:4443/login',
                               vipr_endpoint='https://192.168.1.146:4443',
                               request_timeout=15.0)

            print(client.user_info.whoami())

            print(client.user_info.get_tenant(username=None))

            audit_time_bucket = get_formatted_time_string(2014, 12, 4, 0, None)
            print(client.audit.get_audit_log(audit_time_bucket))

            print(client.fabric_capacity.get_capacity())

            print(client.disk.get_disks(maximum=-3, index=1))

            single_disk_info = client.disk.get_disk_by_urn(
                urn='urn:fabric:disk:00b0b99b-a395-4179-8838-f121b99061fb')
            print(single_disk_info)

            single_disk_capacity_info = client.disk.get_disk_capacity(
                urn='urn:fabric:disk:00b0b99b-a395-4179-8838-f121b99061fb')
            print(single_disk_capacity_info)

            print(client.health.get_health())

            print(client.node.get_nodes(maximum=-5, index=0))

            print(client.services.get_services())

            print(client.bucket.get_buckets('namespace1'))
            print(client.bucket.get_bucket_retention('bucket1'))

            print(client.object_data_control_capacity.get_capacity())

            print(client.namespace.get_namespaces())
            print(client.namespace.get_namespace_info('namespace1'))

            print(client.user_management.get_objectusers())
            print(client.user_management.get_objectusers('namespace1'))

            print(client.user_management.lock_objectuser('myuser1', is_locked=True, namespace='namespace1'))
            print(client.user_management.get_objectuser_info('myuser1'))
            print(client.user_management.lock_objectuser('myuser1', is_locked=False, namespace='namespace1'))
            print(client.user_management.get_objectuser_info('myuser1'))

            print(client.user_secret_key.get_user_secret_keys(uid='user1@test'))

            print(client.configuration.get_config_properties())

            print(client.health_monitor.get_stats())

            health_info = client.health_monitor.get_health(0)
            print(health_info)

            health_info = client.health_monitor.get_stats(
                node_id=['urn:fabric:node:0fedcf91-5086-11e3-a7f8-001e6769f9a1:',
                         'urn:fabric:node:14115e71-4fbe-11e3-b044-001e6769e808:'])
            print(health_info)

            print(client.health_monitor.get_diagnostics(node_id='nilea01-r05-05'))
            print(client.health_monitor.get_storage_stats())

            print(client.upgrade.get_target_version())
            print(client.upgrade.get_cluster_state(True))
            print(client.upgrade.get_download_progress())

            tenants_list = client.tenants.get_tenants_bulk()

            for tenant_id in tenants_list:
                tenant_info = client.tenants.get_tenant(tenant_id)
                print(tenant_info)
                print(tenant_info['name'])

                try:
                    subtenant = client.tenants.get_subtenants(tenant_id)
                    if subtenant:
                        print(subtenant)
                except:
                    pass

            # Beta Billing API:
            print(client.billing.get_bucket_billing_info('namespace1', 'bucket1'))

        except ViperpyException as viperpy_ex:
            print('Message: {0}'.format(viperpy_ex.message))
            print('Status Code Returned: {0}\n'.format(viperpy_ex.http_status_code))
            print('ViPR API Message: {0}'.format(viperpy_ex.vipr_message))
        except Exception as ex:
            print(ex.message)

Example: Use a valid token instead of supplying a username and password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You pass an authentication token directly to ViperPy which means you
don't need to supply a username/password. Here is an example (the token
has been shortened):

::

    client = Viperpy(token='DLAcbGZtbjh6eVB3eUF1TzFEZWNmc0M2VVl2QjBVPQM',
                       token_endpoint='https://192.168.1.146:4443/login',
                       vipr_endpoint='https://192.168.1.146:4443',
                       request_timeout=15.0)

Example: Create, list, and remove object users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    from viperpy import Viperpy, ViperpyException


    if __name__ == "__main__":
        try:
            client = Viperpy(username='someone',
                               password='password',
                               token=None,
                               token_endpoint='https://192.168.1.146:4443/login',
                               vipr_endpoint='https://192.168.1.146:4443',
                               request_timeout=15.0)

            print(client.user_management.add_objectuser(user='mytest1', namespace='namespace1'))
            print(client.user_management.get_objectusers())

            # This next line won't print anything useful as the body is empty
            # If an HTTP 200 is not returned an error with raise, otherwise you can
            # assume that the call was successful
            client.user_management.deactivate_objectuser(user='mytest1')
            print(client.user_management.get_objectusers())

        except ViperpyException as viperpy_ex:
            print('Message: {0}'.format(viperpy_ex.message))
            print('Status Code Returned: {0}\n'.format(viperpy_ex.http_status_code))
            print('ViPR API Message: {0}'.format(viperpy_ex.vipr_message))
        except Exception as ex:
            print(ex.message)

Example: Fetching tokens
^^^^^^^^^^^^^^^^^^^^^^^^

Fetching a token for a user can be done as follows by setting the
``cache_token`` parameter to false and then calling ``get_token``:

::

    from viperpy import Viperpy, ViperpyException


    if __name__ == "__main__":
        try:
            client = Viperpy(username='someone',
                               password='password',
                               token=None,
                               token_endpoint='https://192.168.1.146:4443/login',
                               vipr_endpoint='https://192.168.1.146:4443',
                               request_timeout=15.0,
                               cache_token=False)

            print(client.get_token())

        except ViperpyException as viperpy_ex:
            print('Message: {0}'.format(viperpy_ex.message))
            print('Status Code Returned: {0}\n'.format(viperpy_ex.http_status_code))
            print('ViPR API Message: {0}'.format(viperpy_ex.vipr_message))
        except Exception as ex:
            print(ex.message)

Example: Removing a cached token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    from viperpy import Viperpy, ViperpyException


    if __name__ == "__main__":
        try:
            client = Viperpy(username='someone',
                               password='password',
                               token=None,
                               token_endpoint='https://192.168.1.146:4443/login',
                               vipr_endpoint='https://192.168.1.146:4443',
                               request_timeout=15.0,
                               cache_token=False)

            print(client.remove_cached_token())

        except ViperpyException as viperpy_ex:
            print('Message: {0}'.format(viperpy_ex.message))
            print('Status Code Returned: {0}\n'.format(viperpy_ex.http_status_code))
            print('ViPR API Message: {0}'.format(viperpy_ex.vipr_message))
        except Exception as ex:
            print(ex.message)

ViPR Beta APIs
--------------

Support has been added for the ViPR 2.1.1 (beta) release of the new
Billing and Soft Quota APIs.

Running PEP8
------------

There are some example JSON comments in the source code that are over
the allowed PEP8 length. You can ignore those by running:

::

    $ pep8 --ignore=E501 .

License
-------

This software library is released to you under the EMC Freeware Software
License Agreement. See
`LICENSE <https://github.com/chadlung/viperpy/blob/master/LICENSE>`__
for more information.
