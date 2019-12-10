from api.api_base import API, response_property
from properties.response_objects.certificate import Certificate


class _Certificates(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/Certificates', valid_return_codes=[200])
        self.Associate = self._Associate(websdk_obj=websdk_obj)
        self.CheckPolicy = self._CheckPolicy(websdk_obj=websdk_obj)
        self.Dissociate = self._Dissociate(websdk_obj=websdk_obj)
        self.Import = self._Import(websdk_obj=websdk_obj)
        self.Renew = self._Renew(websdk_obj=websdk_obj)
        self.Request = self._Request(websdk_obj=websdk_obj)
        self.Reset = self._Reset(websdk_obj=websdk_obj)
        self.Retrieve = self._Retrieve(websdk_obj=websdk_obj)
        self.Retry = self._Retry(websdk_obj=websdk_obj)
        self.Revoke = self._Revoke(websdk_obj=websdk_obj)
        self.Validate = self._Validate(websdk_obj=websdk_obj)

    def Guid(self, guid):
        return self._Guid(guid=guid, websdk_obj=self._api_obj)

    @property
    @response_property()
    def links(self):
        lnks = self.json_response(key='_links')
        return [Certificate.Link(lnk) for lnk in lnks]

    @property
    @response_property()
    def x_record_count(self):
        xrc = self.response.headers.get('X-Record-Count')
        return xrc

    @property
    @response_property()
    def certificates(self):
        certs = self.json_response(key='Certificates')
        return [Certificate.Certificate(cert) for cert in certs]

    @property
    @response_property()
    def data_range(self):
        return self.json_response(key='DataRange')

    @property
    @response_property()
    def total_count(self):
        return self.json_response(key='TotalCount')

    def get(self, limit: int = None, offset: int = None, optional_fields: list = None, filters: dict = None):
        params = {
            'Limit': limit,
            'Offset': offset,
            'OptionalFields': optional_fields
        }.update(filters or {})

        self.response = self._get(params=params)

        return self

    class _Associate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Associate', valid_return_codes=[200])

        @property
        @response_property()
        def success(self):
            return self.json_response(key='Success')

        def post(self, application_dn: str, certificate_dn: str, push_to_new: bool):
            body = {
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'PushToNew': push_to_new
            }

            self.response = self._post(data=body)
            return self

    class _CheckPolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/CheckPolicy', valid_return_codes=[200])

        @property
        @response_property()
        def csr(self):
            return Certificate.CSR(self.json_response(key='CSR', error_key='Error'))

        @property
        @response_property()
        def policy(self):
            return Certificate.Policy(self.json_response(key='Policy'))

        def post(self, policy_dn: str, pkcs10: str = None):
            body = {
                'PolicyDN': policy_dn,
                'PKSC10': pkcs10
            }

            self.response = self._post(data=body)

            return self

    class _Dissociate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Dissociate', valid_return_codes=[200])

        @property
        @response_property()
        def success(self):
            return self.json_response(key='Success')

        def post(self, certificate_dn: str, application_dn: list, delete_orphans: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'DeleteOrphans': delete_orphans
            }

            self.response = self._post(data=body)
            return self

    class _Guid(API):
        def __init__(self, guid: str, websdk_obj):
            self._cert_guid = guid
            super().__init__(api_obj=websdk_obj, url='/Certificates/{guid}'.format(guid=self._cert_guid), valid_return_codes=[200])
            self.PreviousVersions = self._PreviousVersions(guid=self._cert_guid, websdk_obj=websdk_obj)
            self.ValidationResults = self._ValidationResults(guid=self._cert_guid, websdk_obj=websdk_obj)

        @property
        @response_property()
        def approver(self):
            return self.json_response(key='Approver')

        @property
        @response_property()
        def certificate_details(self):
            return Certificate.CertificateDetails(self.json_response(key='CertificateDetails'))

        @property
        @response_property()
        def contact(self):
            return self.json_response(key='Contact')

        @property
        @response_property()
        def created_on(self):
            return self.json_response(key='CreatedOn')

        @property
        @response_property()
        def dn(self):
            return self.json_response(key='DN')

        @property
        @response_property()
        def guid(self):
            return self.json_response(key='Guid')

        @property
        @response_property()
        def name(self):
            return self.json_response(key='Name')

        @property
        @response_property()
        def parent_dn(self):
            return self.json_response(key='ParentDN')

        @property
        @response_property()
        def processing_details(self):
            return Certificate.ProcessingDetails(self.json_response(key='ProcessingDetails'))

        @property
        @response_property()
        def renewal_details(self):
            return Certificate.RenewalDetails(self.json_response(key='RenewalDetails'))

        @property
        @response_property()
        def schema_class(self):
            return self.json_response(key='SchemaClass')

        @property
        @response_property()
        def validation_details(self):
            return Certificate.ValidationDetails(self.json_response(key='ValidationDetails'))

        def delete(self):
            self.response = self._delete()
            return self

        def get(self):
            self.response = self._get()
            return self

        def put(self, attribute_data: [dict]):
            body = {
                "AttributeData": attribute_data
            }

            self.response = self._put(data=body)
            return self

        class _PreviousVersions(API):
            def __init__(self, guid: str, websdk_obj):
                self._cert_guid = guid
                super().__init__(
                    api_obj=websdk_obj,
                    url='/Certificates/{guid}/PreviousVersions'.format(guid=self._cert_guid),
                    valid_return_codes=[200]
                )

            @property
            @response_property()
            def success(self):
                return self.json_response(key='Success')

            @property
            @response_property()
            def previous_versions(self):
                versions = self.json_response(key='PreviousVersions')
                return [Certificate.PreviousVersions(version) for version in versions]

            def get(self, exclude_expired: bool = False, exclude_revoked: bool = False):
                params = {
                    'ExcludeExpired': exclude_expired,
                    'ExcludeRevoked': exclude_revoked
                }
                self.response = self._get(params=params)
                return self

        class _ValidationResults(API):
            def __init__(self, guid: str, websdk_obj):
                self._cert_guid = guid
                super().__init__(
                    api_obj=websdk_obj,
                    url='/Certificates/{guid}/ValidationResults'.format(guid=self._cert_guid),
                    valid_return_codes=[200, 204]
                )

            @property
            @response_property()
            def file(self):
                files = self.json_response(key='File')
                return [Certificate.File(f) for f in files]

            @property
            @response_property()
            def ssltls(self):
                ssl = self.json_response(key='SslTls')
                return [Certificate.SslTls(s) for s in ssl]

            def get(self):
                self.response = self._get()
                return self

    class _Import(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Import', valid_return_codes=[200])

        @property
        @response_property()
        def certificate_dn(self):
            return self.json_response(key='CertificateDN')

        @property
        @response_property()
        def certificate_vault_id(self):
            return self.json_response(key='CertificateVaultID')

        @property
        @response_property()
        def guid(self):
            return self.json_response(key='Guid')

        @property
        @response_property()
        def private_key_vault_id(self):
            return self.json_response(key='PrivateKeyVaultID')

        def post(self, certificate_data: str, policy_dn: str, ca_specific_attributes: list = None, object_name: str = None,
                 password: str = None, private_key_data: str = None, reconcile: bool = False):
            body = {
                'CertificateData': certificate_data,
                'PolicyDN': policy_dn,
                'CASpecificAttributes': ca_specific_attributes,
                'ObjectName': object_name,
                'Password': password,
                'PrivateKeyData': private_key_data,
                'Reconcile': reconcile
            }

            self.response = self._post(data=body)
            return self

    class _Renew(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Renew', valid_return_codes=[200])

        @property
        @response_property()
        def success(self):
            return self.json_response(key='Success')

        def post(self, certificate_dn: str, pkcs10: str = None, reenable: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'PKCS10': pkcs10,
                'Reenable': reenable
            }

            self.response = self._post(data=body)
            return self

    class _Request(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Request', valid_return_codes=[200])

        @property
        @response_property()
        def certificate_dn(self):
            return self.json_response(key='CertificateDN')

        @property
        @response_property()
        def guid(self):
            return self.json_response(key='Guid')

        def post(self, policy_dn: str, approvers: [dict] = None, cadn: str = None, ca_specific_attributes: [dict] = None,
                 certificate_type: str = None, city: str = None, contacts: [dict] = None, country: str=None,
                 custom_fields: [dict] = None, created_by: str = None, devices: [dict] = None,
                 disable_automatic_renewal: bool = False, elliptic_curve: str = None, key_algorithm: str = None,
                 key_bit_size: int = None, management_type: str = None, object_name: str = None, organization: str = None,
                 organizational_unit: str = None, pkcs10: str = None, reenable: bool = False, set_work_todo: bool = True,
                 state: str = None, subject: str = None, subject_alt_names: [dict] = None):

            body = {
                'Approvers': approvers,
                'CADN': cadn,
                'CASpecificAttributes': ca_specific_attributes,
                'CertificateType': certificate_type,
                'City': city,
                'Contacts': contacts,
                'Country': country,
                'CustomFields': custom_fields,
                'CreatedBy': created_by,
                'Devices': devices,
                'DisableAutomaticRenewal': disable_automatic_renewal,
                'EllipticCurve': elliptic_curve,
                'KeyAlgorithm': key_algorithm,
                'KeyBitSize': key_bit_size,
                'ManagementType': management_type,
                'ObjectName': object_name,
                'Organization': organization,
                'OrganizationalUnit': organizational_unit,
                'PKCS10': pkcs10,
                'PolicyDN': policy_dn,
                'Reenable': reenable,
                'SetWorkToDo': set_work_todo,
                'State': state,
                'Subject': subject,
                'SubjectAltNames': subject_alt_names
            }

            self.response = self._post(data=body)
            return self

    class _Reset(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Reset', valid_return_codes=[200])

        @property
        @response_property()
        def private_key_mismatch_reset_completed(self):
            return self.json_response(key='PrivateKeyMismatchResetCompleted')

        @property
        @response_property()
        def processing_reset_completed(self):
            return self.json_response(key='ProcessingResetCompleted')

        @property
        @response_property()
        def restart_completed(self):
            return self.json_response(key='RestartCompleted')

        @property
        @response_property()
        def revocation_reset_completed(self):
            return self.json_response(key='RevocationResetCompleted')

        def post(self, certificate_dn: str, restart: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'Restart': restart
            }

            self.response = self._post(data=body)
            return self

    class _Retrieve(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Retrieve', valid_return_codes=[200])

        @property
        @response_property()
        def certificate_data(self):
            return self.json_response(key='CertificateData')

        @property
        @response_property()
        def filename(self):
            return self.json_response(key='Filename')

        @property
        @response_property()
        def format(self):
            return self.json_response(key='Format')

        def get(self, certificate_dn: str, format: str, friendly_name: str, include_chain: bool = False,
                include_private_key: bool = False, keystore_password: str = None, password: str = None,
                root_first_order: bool = False):
            params = {
                'CertificateDN': certificate_dn,
                'Format': format,
                'FriendlyName': friendly_name,
                'IncludeChain': include_chain,
                'IncludePrivateKey': include_private_key,
                'KeystorePassword': keystore_password,
                'Password': password,
                'RootFirstOrder': root_first_order
            }

            self.response = self._get(params=params)
            return self

        def post(self, certificate_dn: str, format: str, friendly_name: str, include_chain: bool = False,
                include_private_key: bool = False, keystore_password: str = None, password: str = None,
                root_first_order: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'Format': format,
                'FriendlyName': friendly_name,
                'IncludeChain': include_chain,
                'IncludePrivateKey': include_private_key,
                'KeystorePassword': keystore_password,
                'Password': password,
                'RootFirstOrder': root_first_order
            }

            self.response = self._post(data=body)
            return self

        def VaultId(self, vault_id: int):
            return self._VaultId(vault_id, self._api_type, )

        class _VaultId(API):
            def __init__(self, vault_id: int, websdk_obj, url):
                super().__init__(api_obj=websdk_obj, url='/Certificates/Retrieve/{vault_id}'.format(vault_id=vault_id), valid_return_codes=[200])
                self._vault_id = vault_id

            @property
            @response_property()
            def certificate_data(self):
                return self.json_response(key='CertificateData')

            @property
            @response_property()
            def filename(self):
                return self.json_response(key='Filename')

            @property
            @response_property()
            def format(self):
                return self.json_response(key='Format')

            def get(self, format: str, friendly_name: str, include_chain: bool = False,
                include_private_key: bool = False, keystore_password: str = None, password: str = None,
                root_first_order: bool = False):

                params = {
                    'Format': format,
                    'FriendlyName': friendly_name,
                    'IncludeChain': include_chain,
                    'IncludePrivateKey': include_private_key,
                    'KeystorePassword': keystore_password,
                    'Password': password,
                    'RootFirstOrder': root_first_order
                }

                self.response = self._get(params=params)
                return self

            def post(self, format: str, friendly_name: str, include_chain: bool = False,
                include_private_key: bool = False, keystore_password: str = None, password: str = None,
                root_first_order: bool = False):

                body = {
                    'Format': format,
                    'FriendlyName': friendly_name,
                    'IncludeChain': include_chain,
                    'IncludePrivateKey': include_private_key,
                    'KeystorePassword': keystore_password,
                    'Password': password,
                    'RootFirstOrder': root_first_order
                }

                self.response = self._post(data=body)
                return self

    class _Retry(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Retry', valid_return_codes=[200])

        @property
        @response_property()
        def success(self):
            return self.json_response(key='Success')

        def post(self, certificate_dn: str):
            body = {
                'CertificateDN': certificate_dn
            }

            self.response = self._post(data=body)
            return self

    class _Revoke(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Revoke', valid_return_codes=[200])

        @property
        @response_property()
        def requested(self):
            return self.json_response(key='Requested')

        @property
        @response_property()
        def success(self):
            return self.json_response(key='Success')

        def post(self, certificate_dn: str = None, thumbprint: str = None, reason: str = None, comments: str = None,
                 disable: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'Thumbprint': thumbprint,
                'Reason': reason,
                'Comments': comments,
                'Disable': disable
            }

            self.response = self._post(data=body)
            return self

    class _Validate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Validate', valid_return_codes=[200])

        @property
        @response_property()
        def success(self):
            return self.json_response(key='Success')

        @property
        @response_property()
        def validated_certificate_dns(self):
            return self.json_response(key='ValidatedCertificateDNs')

        @property
        @response_property()
        def validated_certificate_guids(self):
            return self.json_response(key='ValidatedCertificateGUIDs')

        @property
        @response_property()
        def warnings(self):
            return self.json_response(key='Warnings')

        def post(self, certificate_dns: [str] = None, certificate_guids: [str] = None):
            if not(certificate_dns or certificate_guids):
                raise ValueError('Must supply either a list of Certificate DNs or Certificate GUIDs to validate.')

            body = {
                'CertificateDNs': certificate_dns,
                'CertificateGUIDs': certificate_guids
            }

            self.response = self._post(data=body)
            return self


class WebSDKCertificateError(Exception):
    pass