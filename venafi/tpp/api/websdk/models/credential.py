from __future__ import annotations
from venafi.tpp.api.websdk.models.resultcodes import ResultCodes
from venafi.tpp.api.api_base import ObjectModel, ApiField
from typing import Literal

CredentialType = Literal[
    'Username and Password Credential',
    'Password Credential'
]


class Result(ObjectModel):
    code: int = ApiField()

    @property
    def credential_result(self):
        return ResultCodes.Credential.get(self.code, 'Unknown')


class CredentialInfo(ObjectModel):
    class_name: str = ApiField(alias='ClassName')
    full_name: str = ApiField(alias='FullName')


class NameTypeValue(ObjectModel):
    name: str = ApiField(alias='Name')
    type: str = ApiField(alias='Type')
    value: str = ApiField(alias='Value')