from venafi.tpp.api.api_base import generate_output, ApiField
from venafi.tpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from venafi.tpp.plugins.api.aperture.enums.certificate_inventory import Field, Filter
from venafi.tpp.plugins.api.aperture.models import certificate_inventory
from typing import List, Dict


class _Certificates(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/certificates')
        self.Filters = self._Filters(api_obj=self._api_obj, url=f'{self._url}/filters')

    class _Filters(ApertureEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.Apply = self._Apply(api_obj=self._api_obj, url=f'{self._url}/apply')

        class _Apply(ApertureEndpoint):
            def post(self, fields: List[str] = None, filters: Dict[str, List] = None, is_sort_ascending: bool = True,
                     limit: int = 100, offset: int = 0, sort_field: str = 'Name'):
                fields = fields or [
                    Field.allowed_app_type,
                    Field.aperture_status,
                    Field.dn,
                    Field.error_details,
                    Field.id,
                    Field.installations,
                    Field.is_rename_allowed,
                    Field.key_size,
                    Field.name,
                    Field.risks,
                    Field.single_click_actions,
                    Field.status_details,
                    Field.tls_endpoints,
                    Field.valid_to,
                ]
                filters = filters or {
                    Filter.status: ["Managed"]
                }
                body = {
                    'fields'         : fields,
                    'filters'        : filters,
                    'isSortAscending': is_sort_ascending,
                    'limit'          : limit,
                    'offset'         : offset,
                    'sortField'      : sort_field
                }

                class Output(ApertureOutputModel):
                    certificates: List[certificate_inventory.CertificateDetails] = ApiField(default_factory=list)

                return generate_output(output_cls=Output, response=self._post(data=body), root_field='certificates')