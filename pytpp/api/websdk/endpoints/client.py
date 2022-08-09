from typing import List
from properties.response_objects.dataclasses import client
from pytpp.api.api_base import WebSdkEndpoint, WebSdkResponse, ResponseFactory, ResponseField


class _Client(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Client')
        self.Delete = self._Delete(api_obj=api_obj)
        self.Details = self._Details(api_obj=api_obj)
        self.Work = self._Work(api_obj=api_obj)

    def get(self, client_version: str = None, client_type: client.ClientType = None, host_name: str = None, ip_address: str = None,
            last_seen_on: str = None, last_seen_on_greater: str = None, last_seen_on_less: str = None, mac_address: str = None,
            os_name: client.OSNameType = None, os_version: str = None, region: str = None, serial_number: int = None, sid: str = None,
            user_name: str = None, virtual_machine_id: int = None):
        params = {
            'ClientVersion'    : client_version,
            'client.ClientType'       : client_type,
            'HostName'         : host_name,
            'IpAddress'        : ip_address,
            'LastSeenOn'       : last_seen_on,
            'LastSeenOnGreater': last_seen_on_greater,
            'LastSeenOnLess'   : last_seen_on_less,
            'MacAddress'       : mac_address,
            'OSName'           : os_name,
            'OSVersion'        : os_version,
            'Region'           : region,
            'SerialNumber'     : serial_number,
            'SID'              : sid,
            'UserName'         : user_name,
            'VirtualMachineId' : virtual_machine_id
        }

        class Response(WebSdkResponse):
            clients: List[client.Client] = ResponseField(default_factory=list)
            error_description: str = ResponseField(alias='error_description')
            error: str = ResponseField(alias='error')

        return ResponseFactory(response=self._get(params=params), response_cls=Response, root_field='clients')

    class _Delete(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Client/Delete')

        def post(self, clients: list, delete_associated_devices: bool = False):
            body = {
                'Clients'                : clients,
                'DeleteAssociatedDevices': delete_associated_devices
            }

            class Response(WebSdkResponse):
                deleted_count: int = ResponseField(alias='DeletedCount')
                error_description: str = ResponseField(alias='error_description')
                error: str = ResponseField(alias='error')

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _Details(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Client/Details')

        def get(self, client_version: int = None, client_type: str = None, host_name: str = None, ip_address: str = None,
                last_seen_on: str = None, last_seen_on_greater: str = None, last_seen_on_less: str = None, mac_address: str = None,
                os_name: client.OSNameType = None, os_version: str = None, region: str = None, serial_number: int = None,
                sid: str = None, user_name: str = None, virtual_machine_id: int = None):
            params = {
                'ClientVersion'    : client_version,
                'client.ClientType'       : client_type,
                'HostName'         : host_name,
                'IpAddress'        : ip_address,
                'LastSeenOn'       : last_seen_on,
                'LastSeenOnGreater': last_seen_on_greater,
                'LastSeenOnLess'   : last_seen_on_less,
                'MacAddress'       : mac_address,
                'OSName'           : os_name,
                'OSVersion'        : os_version,
                'Region'           : region,
                'SerialNumber'     : serial_number,
                'SID'              : sid,
                'UserName'         : user_name,
                'VirtualMachineId' : virtual_machine_id
            }

            class Response(WebSdkResponse):
                details: List[client.ClientDetails] = ResponseField(default_factory=list)
                error_description: str = ResponseField(alias='error_description')
                error: str = ResponseField(alias='error')

            return ResponseFactory(response=self._get(params=params), response_cls=Response, root_field='details')

    class _Work(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Client/Work')

        def get(self, work_type: client.WorkType = None):
            params = {
                'client.WorkType': work_type
            }

            class Response(WebSdkResponse):
                works: List[client.Work] = ResponseField(default_factory=list)
                error_description: str = ResponseField(alias='error_description')
                error: str = ResponseField(alias='error')

            return ResponseFactory(response=self._get(params=params), response_cls=Response, root_field='works')
