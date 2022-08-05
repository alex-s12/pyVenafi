from typing import List
from properties.response_objects.dataclasses import log
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _Log(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Log')
        self.LogSchema = self._LogSchema(api_obj=api_obj)

    def get(self, component: str = None, from_time: str = None, grouping: int = None, id: int = None,
            limit: int = None, offset: int = None, order: str = None, severity: str = None, text1: str = None,
            text2: str = None, to_time: str = None, value1: str = None, value2: str = None):
        params = {
            'Component': component,
            'FromTime' : from_time,
            'Grouping' : grouping,
            'Id'       : id,
            'Limit'    : limit,
            'Offset'   : offset,
            'Order'    : order,
            'Severity' : severity,
            'Text1'    : text1,
            'Text2'    : text2,
            'ToTime'   : to_time,
            'Value1'   : value1,
            'Value2'   : value2
        }

        class Response(APIResponse):
            log_events: List[log.LogEvent] = ResponseField(default_factory=list, alias='LogEvents')

        return ResponseFactory(response_cls=Response, response=self._get(params=params))

    def post(self, component: str, id: int, grouping: int = None, severity: int = None, source_ip: str = None,
             text1: str = None, text2: str = None, value1: str = None, value2: str = None):
        body = {
            'Component': component,
            'ID'       : id,
            'Grouping' : grouping,
            'Severity' : severity,
            'SourceIp' : source_ip,
            'Text1'    : text1,
            'Text2'    : text2,
            'Value1'   : value1,
            'Value2'   : value2
        }

        class Response(APIResponse):
            log_result: int = ResponseField(alias='LogResult')

        return ResponseFactory(response_cls=Response, response=self._post(data=body))

    def Guid(self, guid: str):
        return self._Guid(guid=guid, api_obj=self._api_obj)

    class _Guid(API):
        def __init__(self, guid: str, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Log/{guid}')

        def get(self):
            class Response(APIResponse):
                log_events: List[log.LogEvent] = ResponseField(default_factory=list, alias='LogEvents')

            return ResponseFactory(response_cls=Response, response=self._get())

    class _LogSchema(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Log/LogSchema')

        def get(self):
            class Response(APIResponse):
                log_event_application_definitions: List[log.LogEventApplicationDefinition] = ResponseField(
                    alias='LogEventApplicationDefinitions'
                )
                log_event_definitions: List[log.LogEventDefinition] = ResponseField(alias='LogEventDefinitions')
                log_result: int = ResponseField(alias='LogResult')

            return ResponseFactory(response_cls=Response, response=self._get())
