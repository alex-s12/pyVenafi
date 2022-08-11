from pytpp.api.api_base import ApiField, generate_output
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from pytpp.plugins.api.aperture.outputs import device
from typing import List


class _Device(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(
            api_obj=api_obj,
            url=f'/device'
        )

        self.BulkOperations = self._BulkOperations(api_obj)
        self.GetStatus = self._GetStatus(api_obj)

    def post(self, ssh_type: str = "", job: str = "", custom_field_name: str = "",
             custom_field_value: List[str] = None, common_name: List[str] = None, properties: List[str] = None,
             environment: List[str] = None, folder: List[str] = None, status: List[str] = None,
             include_sub_folders: bool = False, offset: int = 0, limit: int = 20):
        body = {
            "Type"             : ssh_type,
            "Job"              : job,
            "CustomFieldName"  : custom_field_value,
            "CustomFieldValue" : custom_field_name or [],
            "CommonName"       : common_name or [],
            "Properties"       : properties or [],
            "Environment"      : environment or [],
            "Folder"           : folder or [],
            "Status"           : status or [],
            "IncludeSubfolders": include_sub_folders,
            "Offset"           : offset,
            "Limit"            : limit
        }

        class Response(ApertureOutputModel):
            total_count: int = ApiField(key='totalCount')
            devices_list_items: List[device.Device] = ApiField(alias='devicesListItems', default_factory=list)

        return generate_output(output_cls=Response, response=self._post(data=body))

    class _GetStatus(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(
                api_obj=api_obj,
                url=f'/device/GetStatus'
            )

        def get(self, device_guid: str):
            params = {
                'deviceGuid': device_guid
            }

            class Response(ApertureOutputModel):
                is_out_of_compliance: bool = ApiField(alias='isOutOfCompliance')
                discovery_stage: int = ApiField(alias='discoveryStage')
                discovery_status: str = ApiField(alias='discoveryStatus')

            return generate_output(output_cls=Response, response=self._get(params=params))

    class _BulkOperations:
        def __init__(self, api_obj):
            self._api_obj = api_obj
            self.SetAgentlessDiscoveryToDo = self._SetAgentlessDiscoveryToDo(api_obj=self._api_obj)
            self.ResetFailedAuthAttempts = self._ResetFailedAuthAttempts(api_obj=self._api_obj)

        class _SetAgentlessDiscoveryToDo(ApertureEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url=f'/device/bulkOperations/SetAgentlessDiscoveryToDo')

            def post(self, device_guids: List[str]):
                return generate_output(output_cls=ApertureOutputModel, response=self._post(data=device_guids))

        class _ResetFailedAuthAttempts(ApertureEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url=f'/device/bulkOperations/resetFailedAuthAttempts')

            def post(self, device_guids: List[str]):
                return generate_output(output_cls=ApertureOutputModel, response=self._post(data=device_guids))
