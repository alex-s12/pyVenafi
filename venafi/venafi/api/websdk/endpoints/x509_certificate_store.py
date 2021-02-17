from typing import List
from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.secret_store import SecretStore


class _X509CertificateStore:
    def __init__(self, api_obj):
        self.Add = self._Add(api_obj=api_obj)
        self.Lookup = self._Lookup(api_obj=api_obj)
        self.LookupExpiring = self._LookupExpiring(api_obj=api_obj)
        self.Remove = self._Remove(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)

    class _Add(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Add')

        def post(self, owner_dn: str, certificate_collection_strings: list = None, ceritificate_string: str = None,
                 protection_key: str = None, typed_name_values: list = None):
            body = {
                'CertificateCollectionStrings': certificate_collection_strings,
                'CertificateString': ceritificate_string,
                'OwnerDN': owner_dn,
                'ProtectionKey': protection_key,
                'TypedNameValues': typed_name_values
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def leaf_existed(self) -> bool:
                    return self.json_response('LeafExisted')

                @property
                @json_response_property()
                def result(self):
                    return SecretStore.Result(self.json_response('Result'))

                @property
                @json_response_property()
                def vault_id(self) -> int:
                    return self.json_response('VaultId')

            return _Response(response=self._post(data=body), api_source=self._api_source)

    class _Lookup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Lookup')

        def post(self, certificate_string: str = None, name: str = None, owner_dn: str = None, value: str = None):
            body = {
                'CertificateString': certificate_string,
                'Name': name,
                'OwnerDN': owner_dn,
                'Value': value
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def vault_id(self) -> int:
                    return self.json_response('VaultId')

                @property
                @json_response_property()
                def vault_ids(self) -> List[int]:
                    return self.json_response('VaultIds')

                @property
                @json_response_property()
                def certificate_collection_strings(self) -> List[str]:
                    return self.json_response('CertificateCollectionStrings')

                @property
                @json_response_property()
                def result(self):
                    return SecretStore.Result(self.json_response('Result'))

            return _Response(response=self._post(data=body), api_source=self._api_source)

    class _LookupExpiring(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/LookupExpiring')

        def post(self, days_to_expiration: int, owner_dn: str):
            body = {
                'DaysToExpiration': days_to_expiration,
                'OwnerDN': owner_dn
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def vault_ids(self) -> List[int]:
                    return self.json_response('VaultIds')

                @property
                @json_response_property()
                def result(self):
                    return SecretStore.Result(self.json_response('Result'))

            return _Response(response=self._post(data=body), api_source=self._api_source)

    class _Remove(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Remove')

        def post(self, owner_dn: str, certificate: str = None, vault_id: int = None):
            body = {
                'Certificate': certificate,
                'OwnerDN': owner_dn,
                'VaultId': vault_id
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return SecretStore.Result(self.json_response('Result'))

            return _Response(response=self._post(data=body), api_source=self._api_source)

    class _Retrieve(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/X509CertificateStore/Retrieve')

        def post(self, vault_id: int):
            body = {
                'VaultId': vault_id
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def certificate_string(self) -> str:
                    return self.json_response('CertificateString')

                @property
                @json_response_property()
                def result(self):
                    return SecretStore.Result(self.json_response('Result'))

                @property
                @json_response_property()
                def typed_name_values(self):
                    return SecretStore.TypedNameValues(self.json_response('TypedNameValues'))

            return _Response(response=self._post(data=body), api_source=self._api_source)
