from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class F5LTMAdvancedAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "F5 LTM Advanced"
	advanced_settings_bundle_name = Attribute('Advanced Settings Bundle Name')
	advertised_ca = Attribute('Advertised CA')
	archive_location = Attribute('Archive Location')
	authentication_frequency = Attribute('Authentication Frequency')
	build = Attribute('Build')
	bundle_certificate = Attribute('Bundle Certificate')
	bundle_certificate_collection = Attribute('Bundle Certificate Collection')
	crl = Attribute('CRL')
	certificate_chain_name = Attribute('Certificate Chain Name')
	certificate_name = Attribute('Certificate Name')
	chain_traversal_depth = Attribute('Chain Traversal Depth')
	client_authentication_certificate = Attribute('Client Authentication Certificate')
	config_sync = Attribute('Config Sync')
	connection_attempts = Attribute('Connection Attempts', min_version='16.4')
	delete_previous_cert_and_key = Attribute('Delete Previous Cert And Key')
	device_certificate = Attribute('Device Certificate')
	file_validation_disabled = Attribute('File Validation Disabled')
	fips_key = Attribute('Fips Key')
	force_profile_update = Attribute('Force Profile Update', min_version='16.3')
	install_chain_file = Attribute('Install Chain File')
	last_used_host = Attribute('Last Used Host')
	network_validation_disabled = Attribute('Network Validation Disabled')
	overwrite_certificate = Attribute('Overwrite Certificate')
	overwrite_existing_chain = Attribute('Overwrite Existing Chain')
	parent_ssl_profile_name = Attribute('Parent SSL Profile Name')
	partition = Attribute('Partition')
	previous_certificate = Attribute('Previous Certificate')
	previous_key = Attribute('Previous Key')
	provisioning_to = Attribute('Provisioning To')
	sni_default = Attribute('SNI Default', min_version='16.3')
	sni_server_name = Attribute('SNI Server Name', min_version='16.3')
	ssh_port = Attribute('SSH Port')
	ssl_profile_name = Attribute('SSL Profile Name')
	ssl_profile_type = Attribute('SSL Profile Type')
	server_authentication_certificate = Attribute('Server Authentication Certificate')
	server_authentication_name = Attribute('Server Authentication Name')
	system_id = Attribute('System Id')
	trusted_ca = Attribute('Trusted CA')
	use_advanced_settings = Attribute('Use Advanced Settings')
	use_basic_provisioning = Attribute('Use Basic Provisioning')
	use_rest_api = Attribute('Use REST API', min_version='21.3')
	version = Attribute('Version')
	virtual_server_name = Attribute('Virtual Server Name')
	virtual_server_partition = Attribute('Virtual Server Partition')