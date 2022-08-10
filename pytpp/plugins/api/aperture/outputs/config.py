from pytpp.api.api_base import ApiField, OutputModel
from typing import Optional


class Object(OutputModel):
    absolute_guid: str = ApiField(alias='parentPolicyGuid')
    dn: str = ApiField(alias='dn')
    guid: str = ApiField(alias='id')
    config_id: Optional[int] = ApiField()
    name: str = ApiField(alias='name')
    parent: str = ApiField(alias='parentDn')
    revision: Optional[int] = ApiField()
    type_name: str = ApiField(alias='typeNam')
