from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.log import Log


class _Log(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/Log')

    def get(self, component: str = None, from_time: str = None, grouping: int = None, id: int = None,
            limit: int = None, offset: int = None, order: str = None, severity: str = None, text1: str = None,
            text2: str = None, to_time: str = None, value1: str = None, value2: str = None):
        params = {
            'Component': component,
            'FromTime': from_time,
            'Grouping': grouping,
            'Id': id,
            'Limit': limit,
            'Offset': offset,
            'Order': order,
            'Severity': severity,
            'Text1': text1,
            'Text2': text2,
            'ToTime': to_time,
            'Value1': value1,
            'Value2': value2
        }
        
        class _Response(APIResponse):
            def __init__(self, response, expected_return_codes, api_source):
                super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

            @property
            @json_response_property()
            def log_events(self):
                return [Log.LogEvent(log) for log in self._from_json('LogEvents')]

        return _Response(
            response=self._get(params=params),
            expected_return_codes=[200],
            api_source=self._api_source
        )

    def post(self, component: str, id: int, grouping: int = None, severity: int = None, source_ip: str = None,
             text1: str = None, text2: str = None, value1: str = None, value2: str = None):
        body = {
            'Component': component,
            'ID': id,
            'Grouping': grouping,
            'Severity': severity,
            'SourceIp': source_ip,
            'Text1': text1,
            'Text2': text2,
            'Value1': value1,
            'Value2': value2
        }

        class _Response(APIResponse):
            def __init__(self, response, expected_return_codes, api_source):
                super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

            @property
            @json_response_property()
            def log_result(self) -> int:
                return self._from_json('LogResult')

        return _Response(
            response=self._post(data=body),
            expected_return_codes=[200],
            api_source=self._api_source
        )

    def Guid(self, guid: str):
        return self._Guid(guid=guid, websdk_obj=self._api_obj)

    class _Guid(API):
        def __init__(self, guid: str, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Log/{guid}')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def log_events(self):
                    return [Log.LogEvent(log) for log in self._from_json('LogEvents')]

            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )
