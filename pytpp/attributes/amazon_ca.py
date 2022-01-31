from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class AmazonCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Amazon CA"
	access_key_id = Attribute('Access Key ID', min_version='16.1')
	amazon_private_ca = Attribute('Amazon Private CA', min_version='21.2')
	aws_credential_dn = Attribute('Aws Credential DN', min_version='18.3')
	domain_control_validation = Attribute('Domain Control Validation', min_version='16.1')
	interval = Attribute('Interval', min_version='16.1')
	keys_generated_by_the_ca = Attribute('Keys Generated By The CA', min_version='21.2')
	region_code = Attribute('Region Code', min_version='16.1')
	retrieval_period = Attribute('Retrieval Period', min_version='16.1')
	secret_access_key = Attribute('Secret Access Key', min_version='16.1')
	signature_algorithm = Attribute('Signature Algorithm', min_version='21.2')
	use_private_ca = Attribute('Use Private CA', min_version='21.2')