from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes
from pytpp.attributes.x509_certificate_base import X509CertificateBaseAttributes


class ClientCertificateWorkAttributes(ClientWorkBaseAttributes, X509CertificateBaseAttributes, metaclass=PropertyMeta):
	certificate_container = Attribute('Certificate Container')
	naming_pattern = Attribute('Naming Pattern')
	transfer_allowed = Attribute('Transfer Allowed', min_version='18.3')
