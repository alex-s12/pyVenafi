from venafi.api.session import Session
from venafi.api.websdk.endpoints.authorize import _Authorize
from venafi.api.websdk.endpoints.certificates import _Certificates
from venafi.api.websdk.endpoints.client import _Client
from venafi.api.websdk.endpoints.config import _Config
from venafi.api.websdk.endpoints.config_schema import _ConfigSchema
from venafi.api.websdk.endpoints.credentials import _Credentials
from venafi.api.websdk.endpoints.crypto import _Crypto
from venafi.api.websdk.endpoints.discovery import _Discovery
from venafi.api.websdk.endpoints.identity import _Identity
from venafi.api.websdk.endpoints.log import _Log
from venafi.api.websdk.endpoints.metadata import _Metadata
from venafi.api.websdk.endpoints.permissions import _Permissions
from venafi.api.websdk.endpoints.processing_engines import _ProcessingEngines
from venafi.api.websdk.endpoints.revoke import _Revoke
from venafi.api.websdk.endpoints.ssh import _SSH
from venafi.api.websdk.endpoints.system_status import _SystemStatus
from venafi.api.websdk.endpoints.secret_store import _SecretStore
from venafi.api.websdk.endpoints.workflow import _Workflow
from venafi.api.websdk.endpoints.x509_certificate_store import _X509CertificateStore


class WebSDK:
    def __init__(self, host: str, username=None, password=None, certificate=None):
        self.host = host
        self.username = username
        self.password = password
        self.certificate = certificate

        self.base_url = f'https://{host}/vedsdk'
        self.session = Session(headers={'Content-Type': 'application/json'})
        self.Authorize = _Authorize(self)
        if username and password:
            token = self.Authorize.post(username=username, password=password).token
            self.session.headers.update(token)
        elif certificate:
            raise NotImplementedError('Certificate authentication not available.')

        self.Certificates = _Certificates(self)
        self.Client = _Client(self)
        self.Config = _Config(self)
        self.ConfigSchema = _ConfigSchema(self)
        self.Credentials = _Credentials(self)
        self.Crypto = _Crypto(self)
        self.Discovery = _Discovery(self)
        self.Identity = _Identity(self)
        self.Log = _Log(self)
        self.Metadata = _Metadata(self)
        self.Permissions = _Permissions(self)
        self.ProcessingEngines = _ProcessingEngines(self)
        self.Revoke = _Revoke(self)
        self.SecretStore = _SecretStore(self)
        self.SSH = _SSH(self)
        self.SystemStatus = _SystemStatus(self)
        self.Workflow = _Workflow(self)
        self.X509CertificateStore = _X509CertificateStore(self)

    def re_authenticate(self):
        self.__init__(host=self.host, username=self.username, password=self.password, certificate=self.certificate)
