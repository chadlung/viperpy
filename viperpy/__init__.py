# Standard lib imports
import json
import os

# Third party imports
import requests

# Project level imports
from viperpy.api.authentication import Authentication

from viperpy.api.fabric.capacity import Capacity as FabricCapacity
from viperpy.api.fabric.disk import Disk
from viperpy.api.fabric.health import Health
from viperpy.api.fabric.node import Node
from viperpy.api.fabric.services import Services

from viperpy.api.object_data_control.billing import Billing
from viperpy.api.object_data_control.bucket import Bucket
from viperpy.api.object_data_control.capacity_info \
    import Capacity as ObjectDataControlCapacity
from viperpy.api.object_data_control.namespace import Namespace
from viperpy.api.object_data_control.object_soft_quota import ObjectSoftQuota
from viperpy.api.object_data_control.user_mangement import UserManagement
from viperpy.api.object_data_control.user_secret_key import UserSecretKey

from viperpy.api.other.audit import Audit
from viperpy.api.other.user_info import UserInfo

from viperpy.api.system_management.configuration import Configuration
from viperpy.api.system_management.health_monitor import HealthMonitor
from viperpy.api.system_management.upgrade import Upgrade

from viperpy.api.tenant.projects import Projects
from viperpy.api.tenant.tenants import Tenants

from viperpy.api.block.volumes import Volumes
from viperpy.api.block.vpools import VirtualPools
from viperpy.api.license import License

from viperpy.util.exceptions import ViperpyException
from viperpy.util.token_request import TokenRequest


class Viperpy(object):

    def __init__(self, username=None, password=None, token=None,
                 vipr_endpoint=None, token_endpoint=None, verify_ssl=False,
                 token_filename='viperpy.tkn', token_location='/tmp',
                 request_timeout=15.0, cache_token=True):
        """
        Creates the ViperPy class that the client will directly work with

        :param username: The username to fetch a token
        :param password: The password to fetch a token
        :param token: Supply a valid token to use instead of username/password
        :param vipr_endpoint: The URL where ViPR is located
        :param token_endpoint: The URL where the ViPR login is located
        :param verify_ssl: Verify SSL certificates
        :param token_filename: The name of the cached token filename
        :param token_location: By default this is stored in /tmp
        :param request_timeout: How long to wait for ViPR to respond
        :param cache_token: Whether to cache the token, by default this is true
        you should only switch this to false when you want to directly fetch
        a token for a user
        """

        self.username = username
        self.password = password
        self.token = token
        self.vipr_endpoint = vipr_endpoint.rstrip('/')
        self.token_endpoint = token_endpoint.rstrip('/')
        self.verify_ssl = verify_ssl
        self.token_filename = token_filename
        self.token_location = token_location
        self.request_timeout = request_timeout
        self.cache_token = cache_token
        self._session = requests.Session()
        self._token_request = TokenRequest(
            username=self.username,
            password=self.password,
            vipr_endpoint=self.vipr_endpoint,
            token_endpoint=self.token_endpoint,
            verify_ssl=self.verify_ssl,
            token_filename=self.token_filename,
            token_location=self.token_location,
            request_timeout=self.request_timeout,
            cache_token=self.cache_token)
        self.token_file = os.path.join(
            self.token_location, self.token_filename)

        # API -> Authentication
        self.authentication = Authentication(self)

        # API -> Fabric
        self.fabric_capacity = FabricCapacity(self)
        self.disk = Disk(self)
        self.health = Health(self)
        self.node = Node(self)
        self.services = Services(self)

        # API -> Object Data Control
        self.billing = Billing(self)
        self.bucket = Bucket(self)
        self.object_data_control_capacity = ObjectDataControlCapacity(self)
        self.namespace = Namespace(self)
        self.user_management = UserManagement(self)
        self.user_secret_key = UserSecretKey(self)
        self.object_soft_quota = ObjectSoftQuota(self)

        # API -> Other
        self.audit = Audit(self)
        self.user_info = UserInfo(self)

        # API -> System Management
        self.configuration = Configuration(self)
        self.health_monitor = HealthMonitor(self)
        self.upgrade = Upgrade(self)

        # API -> Tenant
        self.tenants = Tenants(self)
        self.projects = Projects(self)

        # API -> Block Volumes
        self.block_volumes = Volumes(self)
        self.block_vpools = VirtualPools(self)

        # API -> License
        self.license = License(self)

    def get_token(self):
        """
        Get a token directly back, typically you want to set the cache_token
        param for ViperPy to false for this call.

        :return: A valid token or an ViperPy exception
        """
        return self._token_request.get_new_token()

    def remove_cached_token(self):
        """
        Remove the cached token file, this is useful if you switch users
        and want to use a different token
        """
        if os.path.isfile(self.token_file):
            os.remove(self.token_file)

    def _fetch_headers(self):
        if self.token:
            return {'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'x-sds-auth-token': self.token}
        else:
            return {'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'x-sds-auth-token': self._token_request.get_token()}

    def _construct_url(self, url):
        return '{0}/{1}'.format(self.vipr_endpoint, url)

    def get(self, url, params=None):
        return self._request(url, params=params)

    def post(self, url, json_payload='{}'):
        return self._request(url, json_payload, http_verb='POST')

    def put(self, url, json_payload='{}'):
        return self._request(url, json_payload, http_verb='PUT')

    def _request(self, url, json_payload='{}', http_verb='GET', params=None):
        json_payload = json.dumps(json_payload)

        try:
            if http_verb == "PUT":
                req = self._session.put(
                    self._construct_url(url),
                    verify=self.verify_ssl,
                    headers=self._fetch_headers(),
                    timeout=self.request_timeout,
                    data=json_payload)
            elif http_verb == 'POST':
                req = self._session.post(
                    self._construct_url(url),
                    verify=self.verify_ssl,
                    headers=self._fetch_headers(),
                    timeout=self.request_timeout,
                    data=json_payload)
            else:  # Default to GET
                req = self._session.get(
                    self._construct_url(url),
                    verify=self.verify_ssl,
                    headers=self._fetch_headers(),
                    timeout=self.request_timeout,
                    params=params)

            if req.status_code != 200:
                raise ViperpyException(
                    http_status_code=req.status_code,
                    vipr_message=req.text)
            return req.json()

        except requests.ConnectionError as conn_err:
            raise ViperpyException(message=conn_err.message)
        except requests.HTTPError as http_err:
            raise ViperpyException(message=http_err.message)
        except requests.RequestException as req_err:
            raise ViperpyException(message=req_err.message)
        except ValueError:
            return
