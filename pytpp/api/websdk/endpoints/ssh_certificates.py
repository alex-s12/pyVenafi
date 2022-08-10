from datetime import datetime
from typing import List
from pytpp.api.websdk.outputs import ssh_certificates
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _SSHCertificates:
    def __init__(self, api_obj):
        self.CAKeyPair = self._CAKeyPair(api_obj=api_obj)
        self.Request = self._Request(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)
        self.Template = self._Template(api_obj=api_obj)

    class _CAKeyPair:
        def __init__(self, api_obj):
            self.Create = self._Create(api_obj=api_obj)

        class _Create(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='SSHCertificates/CAKeyPair/Create')

            def post(self, name: str, parent_dn: str = None, key_algorithm: str = None,
                     key_storage: str = None, private_key_data: str = None,
                     private_key_passphrase: str = None):
                body = {
                    'Name'                : name,
                    'ParentDN'            : parent_dn,
                    'KeyAlgorithm'        : key_algorithm,
                    'KeyStorage'          : key_storage,
                    'PrivateKeyData'      : private_key_data,
                    'PrivateKeyPassphrase': private_key_passphrase
                }

                class Response(WebSdkOutputModel):
                    created_on: datetime = ApiField(alias='CreatedOn')
                    dn: str = ApiField(alias='DN')
                    fingerprint_sha_256: str = ApiField(alias='FingerprintSHA256')
                    guid: str = ApiField(alias='Guid')
                    key_algorithm: str = ApiField(alias='KeyAlgorithm')
                    key_storage: str = ApiField(alias='KeyStorage')
                    name: str = ApiField(alias='Name')
                    processing_details: ssh_certificates.ProcessingDetails = ApiField(alias='ProcessingDetails')
                    public_key_data: str = ApiField(alias='PublicKeyData')
                    response: ssh_certificates.Output = ApiField(alias='Response')

                return generate_output(response_cls=Response, response=self._post(data=body))

    class _Request(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Request')

        def post(self, ca_dn: str, key_id: str, destination_address: str = None, extensions: str = None, force_command: str = None,
                 object_name: str = None, origin: str = None, policy_dn: str = None, principals: List[str] = None,
                 public_key_data: str = None, source_addresses: List[str] = None, validity_period: str = None,
                 include_certificate_details: bool = False, include_private_key_data: bool = False,
                 private_key_passphrase: str = None, processing_timeout: int = None):
            body = {
                'CADN'                     : ca_dn,
                'KeyId'                    : key_id,
                'DestinationAddress'       : destination_address,
                'Extensions'               : extensions,
                'ForceCommand'             : force_command,
                'ObjectName'               : object_name,
                'Origin'                   : origin,
                'PolicyDN'                 : policy_dn,
                'Principals'               : principals,
                'PublicKeyData'            : public_key_data,
                'SourceAddresses'          : source_addresses,
                'ValidityPeriod'           : validity_period,
                'IncludeCertificateDetails': include_certificate_details,
                'IncludePrivateKeyData'    : include_private_key_data,
                'PrivateKeyPassphrase'     : private_key_passphrase,
                'ProcessingTimeout'        : processing_timeout
            }

            class Response(WebSdkOutputModel):
                dn: str = ApiField(alias='Dn')
                guid: str = ApiField(alias='Guid')
                processing_details: ssh_certificates.ProcessingDetails = ApiField(alias='ProcessingDetails')
                response: ssh_certificates.Output = ApiField(alias='Response')

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _Retrieve(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Retrieve')

        def post(self, dn: str = None, guid: str = None, include_certificate_details: bool = None,
                 include_private_key_data: bool = None, private_key_passphrase: str = None):
            body = {
                'DN'                       : dn,
                'Guid'                     : guid,
                'IncludeCertificateDetails': include_certificate_details,
                'IncludePrivateKeyData'    : include_private_key_data,
                'PrivateKeyPassphrase'     : private_key_passphrase
            }

            class Response(WebSdkOutputModel):
                ca_dn: str = ApiField(alias='CADN')
                ca_guid: str = ApiField(alias='CAGuid')
                certificate_data: str = ApiField(alias='CertificateData')
                certificate_details: ssh_certificates.CertificateDetails = ApiField(alias='CertificateDetails')
                dn: str = ApiField(alias='DN')
                guid: str = ApiField(alias='Guid')
                key_id: str = ApiField(alias='KeyID')
                private_key_data: str = ApiField(alias='PrivateKeyData')
                processing_details: ssh_certificates.ProcessingDetails = ApiField(alias='ProcessingDetails')
                public_key_data: str = ApiField(alias='PublicKeyData')
                request_details: ssh_certificates.RequestDetails = ApiField(alias='RequestDetails')
                response: ssh_certificates.Output = ApiField(alias='Response')

            return generate_output(response_cls=Response, response=self._post(data=body))

    class _Template(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Template')
            self.Retrieve = self._Retrieve(api_obj=api_obj)

        class _Retrieve(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSHCertificates/Template/Retrieve')
                self.PublicKeyData = self._PublicKeyData(api_obj=api_obj)

            def post(self, template_dn: str = None, template_guid: str = None, include_ca_keypair_details: bool = None):
                body = {
                    'DN'                     : template_dn,
                    'Guid'                   : template_guid,
                    'IncludeCAKeyPairDetails': include_ca_keypair_details
                }

                class Response(WebSdkOutputModel):
                    access_control: ssh_certificates.AccessControl = ApiField(alias='AccessControl')
                    api_client: ssh_certificates.APIClient = ApiField(alias='APIClient')
                    ca_keypair_guid: str = ApiField(alias='CAKeyPairGuid')
                    ca_keypair_dn: str = ApiField(alias='CAKeyPairDN')
                    ca_keypair: ssh_certificates.CAKeyPair = ApiField(alias='CAKeyPair')
                    certificate: ssh_certificates.Certificate = ApiField(alias='Certificate')
                    contacts: List[str] = ApiField(default_factory=list, alias='Contacts')
                    created_on: datetime = ApiField(alias='CreatedOn')
                    dn: str = ApiField(alias='DN')
                    guid: str = ApiField(alias='Guid')
                    name: str = ApiField(alias='Name')
                    response: ssh_certificates.Output = ApiField(alias='Response')

                return generate_output(response_cls=Response, response=self._post(data=body))

            class _PublicKeyData(WebSdkEndpoint):
                def __init__(self, api_obj):
                    super().__init__(api_obj=api_obj, url='SSHCertificates/Template/Retrieve/PublicKeyData')

                def get(self, template_dn: str = None, template_guid: str = None):
                    params = {
                        'DN'  : template_dn,
                        'Guid': template_guid,
                    }

                    class Response(WebSdkOutputModel):
                        response: ssh_certificates.Output = ApiField(alias='Response')

                    return generate_output(response_cls=Response, response=self._get(params=params))
