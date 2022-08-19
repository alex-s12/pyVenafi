from __future__ import annotations
from pytpp.api.api_base import OutputModel, ApiField
from datetime import datetime
from typing import List


class Device(OutputModel):
    guid: str = ApiField(alias='guid')
    name: str = ApiField(alias='name')
    dn: str = ApiField(alias='dn')
    environment: str = ApiField(alias='environment')
    is_scanned: bool = ApiField(alias='isScanned')
    is_agent: bool = ApiField(alias='isAgent')
    interface: str = ApiField(alias='interface')
    platform: str = ApiField(alias='platform')
    state: str = ApiField(alias='state')
    trusted_users: int = ApiField(alias='trustedUsers')
    trusted_root_users: int = ApiField(alias='trustedRootUsers')
    server_access: int = ApiField(alias='serverAccess')
    root_server_access: int = ApiField(alias='rootServerAccess')
    custom_fields: dict = ApiField(alias='customFields')
    scan_status: str = ApiField(alias='scanStatus')
    last_discovery: datetime = ApiField(alias='lastDiscovery')
    connection_errors: List[str] = ApiField(alias='connectionErrors')
    is_write_allowed: bool = ApiField(alias='isWriteAllowed')
    has_failed_authorization_attempts: bool = ApiField(alias='hasFailedAuthorizationAttempts')
