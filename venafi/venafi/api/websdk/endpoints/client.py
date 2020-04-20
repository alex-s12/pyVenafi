from typing import List
from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.client import Client


class _Client(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/Client')
        self.Delete = self._Delete(websdk_obj=websdk_obj)
        self.Details = self._Details(websdk_obj=websdk_obj)
        self.Work = self._Work(websdk_obj=websdk_obj)

    def get(self, client_version: int = None, client_type: str = None, host_name: str = None, ip_address: str = None,
            last_seen_on: str = None,last_seen_on_greater: str = None, last_seen_on_less: str = None, mac_address: str = None,
            os_name: str = None, os_version: str = None, region: str = None, serial_number: int = None, sid: str = None,
            user_name: str = None, virtual_machine_id: int = None):
        params = {
            'ClientVersion': client_version,
            'ClientType': client_type,
            'HostName': host_name,
            'IpAddress': ip_address,
            'LastSeenOn': last_seen_on,
            'LastSeenOnGreater': last_seen_on_greater,
            'LastSeenOnLess': last_seen_on_less,
            'MacAddress': mac_address,
            'OSName': os_name,
            'OSVersion': os_version,
            'Region': region,
            'SerialNumber': serial_number,
            'SID': sid,
            'UserName': user_name,
            'VirtualMachineId': virtual_machine_id
        }

        class _Response(APIResponse):
            def __init__(self, response, expected_return_codes, api_source):
                super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

            @property
            @json_response_property(return_on_204=list)
            def clients(self):
                return [Client.Client(client, self._api_source) for client in self._from_json()]

        return _Response(
            response=self._get(params=params),
            expected_return_codes=[200, 204],
            api_source=self._api_source
        )

    class _Delete(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Client/Delete')

        def post(self, clients: list, delete_associated_devices: bool = False):
            body = {
                'Clients': clients,
                'DeleteAssociatedDevices': delete_associated_devices
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def deleted_count(self) -> int:
                    return self._from_json(key='DeletedCount')

                @property
                @json_response_property()
                def errors(self) -> List[str]:
                    return self._from_json(key='Errors')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Details(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Client/Details')

        def get(self, client_version: int = None, client_type: str = None, host_name: str = None, ip_address: str = None,
                last_seen_on: str = None, last_seen_on_greater: str = None, last_seen_on_less: str = None, mac_address: str = None,
                os_name: str = None, os_version: str = None, region: str = None, serial_number: int = None, sid: str = None, user_name: str = None,
                virtual_machine_id: int = None):
            params = {
                'ClientVersion': client_version,
                'ClientType': client_type,
                'HostName': host_name,
                'IpAddress': ip_address,
                'LastSeenOn': last_seen_on,
                'LastSeenOnGreater': last_seen_on_greater,
                'LastSeenOnLess': last_seen_on_less,
                'MacAddress': mac_address,
                'OSName': os_name,
                'OSVersion': os_version,
                'Region': region,
                'SerialNumber': serial_number,
                'SID': sid,
                'UserName': user_name,
                'VirtualMachineId': virtual_machine_id
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property(return_on_204=list)
                def details(self):
                    return [Client.ClientDetails(client, self._api_source) for client in self._from_json()]

            return _Response(
                response=self._get(params=params),
                expected_return_codes=[200, 204],
                api_source=self._api_source
            )

    class _Work(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Client/Work')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property(return_on_204=list)
                def works(self):
                    return [Client.Work(work, self._api_source) for work in self._from_json()]

            return _Response(
                response=self._get(),
                expected_return_codes=[200, 204],
                api_source=self._api_source
            )
