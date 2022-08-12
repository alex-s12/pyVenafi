from typing import List
from pytpp.api.websdk.models import secret_store
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _X509CertificateStore:
    def __init__(self, api_obj):
        self.Add = self._Add(api_obj=api_obj)
        self.Lookup = self._Lookup(api_obj=api_obj)
        self.LookupExpiring = self._LookupExpiring(api_obj=api_obj)
        self.Remove = self._Remove(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)

    class _Add(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Add')

        def post(self, owner_dn: str, certificate_collection_strings: list = None, certificate_string: str = None,
                 protection_key: str = None, typed_name_values: list = None):
            body = {
                'CertificateCollectionStrings': certificate_collection_strings,
                'CertificateString'           : certificate_string,
                'OwnerDN'                     : owner_dn,
                'ProtectionKey'               : protection_key,
                'TypedNameValues'             : typed_name_values
            }

            class Output(WebSdkOutputModel):
                leaf_existed: bool = ApiField(alias='LeafExisted')
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_id: int = ApiField(alias='VaultId')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Lookup(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Lookup')

        def post(self, certificate_string: str = None, name: str = None, owner_dn: str = None, value: str = None):
            body = {
                'CertificateString': certificate_string,
                'Name'             : name,
                'OwnerDN'          : owner_dn,
                'Value'            : value
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_id: int = ApiField(alias='VaultId')
                vault_ids: List[int] = ApiField(alias='VaultIds')
                certificate_collection_strings: List[str] = ApiField(alias='CertificateCollectionStrings')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _LookupExpiring(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/LookupExpiring')

        def post(self, days_to_expiration: int, owner_dn: str):
            body = {
                'DaysToExpiration': days_to_expiration,
                'OwnerDN'         : owner_dn
            }

            class Output(WebSdkOutputModel):
                vault_ids: List[int] = ApiField(alias='VaultIds')
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Remove(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Remove')

        def post(self, owner_dn: str, certificate: str = None, vault_id: int = None):
            body = {
                'Certificate': certificate,
                'OwnerDN'    : owner_dn,
                'VaultId'    : vault_id
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Retrieve(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Retrieve')

        def post(self, vault_id: int):
            body = {
                'VaultId': vault_id
            }

            class Output(WebSdkOutputModel):
                certificate_string: str = ApiField(alias='CertificateString')
                typed_name_values: List[secret_store.TypedNameValues] = ApiField(alias='TypedNameValues')
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))
