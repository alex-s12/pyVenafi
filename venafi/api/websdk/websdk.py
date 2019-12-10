from api.session import Session
from api.websdk.endpoints.authorize import _Authorize
from api.websdk.endpoints.identity import _Identity
from api.websdk.endpoints.config import _Config
from api.websdk.endpoints.credentials import _Credentials
from api.websdk.endpoints.certificates import _Certificates
from api.websdk.endpoints.secret_store import _SecretStore


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

        self.Identity = _Identity(self)
        self.Config = _Config(self)
        self.Credentials = _Credentials(self)
        self.Certificates = _Certificates(self)
        self.SecretStore = _SecretStore(self)

    def re_authenticate(self):
        self.__init__(host=self.host, username=self.username, password=self.password, certificate=self.certificate)