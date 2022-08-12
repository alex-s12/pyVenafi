from pytpp.api.api_base import generate_output, ApiField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from pytpp.plugins.api.aperture.models import config


class _ConfigObjects:
    def __init__(self, api_obj):
        self.Policies = self._Policies(api_obj)

    class _Policies(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/configobjects/policies')

        def post(self, name, container):
            body = {
                "DN": container + "\\" + name
            }

            class Output(ApertureOutputModel):
                object: config.Object = ApiField()

            return generate_output(output_cls=Output, response=self._post(data=body), root_field='object')
