from pytpp.api.api_base import OutputModel, ApiField
from datetime import datetime
from typing import List


class Engine(OutputModel):
    dn: str = ApiField(alias='Dn')
    display_name: str = ApiField(alias='DisplayName')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    name: str = ApiField(alias='Name')


class IisService(OutputModel):
    modules: List[str] = ApiField(alias='modules')
    time_since_first_seen: datetime = ApiField(alias='timeSinceFirstSeen')
    time_since_last_seen: datetime = ApiField(alias='timeSinceLastSeen')
    status: str = ApiField(alias='status')


class LogServerService(IisService): ...  # This is currently the same.


class vPlatformService(OutputModel):
    configured_latency: int = ApiField(alias='configuredLatency')
    configured_mode: str = ApiField(alias='configuredMode')
    configured_work: int = ApiField(alias='configuredWork')
    current_latency: int = ApiField(alias='currentLatency')
    current_mode: str = ApiField(alias='currentMode')
    current_work: int = ApiField(alias='currentWork')
    modules: List[str] = ApiField(alias='modules')
    status: str = ApiField(alias='status')
    time_since_first_seen: datetime = ApiField(alias='timeSinceFirstSeen')
    time_since_last_seen: datetime = ApiField(alias='timeSinceLastSeen')


class Services(OutputModel):
    vplatform: vPlatformService = ApiField(alias='Vplatform')
    log_server: LogServerService = ApiField(alias='LogServer')
    iis: IisService = ApiField(alias='Iis')


class SystemStatus(OutputModel):
    engine_dn: str = ApiField(alias='engineDn')
    engine_name: str = ApiField(alias='engineName')
    services: Services = ApiField(alias='services')
    version: str = ApiField(alias='version')


class Task(OutputModel):
    display_name: str = ApiField(alias='DisplayName')
    name: str = ApiField(alias='Name')
    start_time: datetime = ApiField(alias='StartTime')
    stop_time: datetime = ApiField(alias='StopTime')
    warning_count: int = ApiField(alias='WarningCount')


class UpgradeInfo(OutputModel):
    id: str = ApiField(alias='Id')
    start_time: datetime = ApiField(alias='StartTime')
    versions: List[str] = ApiField(alias='Versions')


class UpgradeStatus(OutputModel):
    engine: 'Engine' = ApiField(alias='Engine')
    status: str = ApiField(alias='Status')
    upgrade_start_time: datetime = ApiField(alias='UpgradeStartTime')
    upgrade_stop_time: datetime = ApiField(alias='UpgradeStopTime')
    tasks_completed: List[Task] = ApiField(alias='TasksCompleted')
    tasks_pending: List[Task] = ApiField(alias='TasksPending')
    tasks_running: List[Task] = ApiField(alias='TasksRunning')


class UpgradeSummary(OutputModel):
    status: str = ApiField(alias='Status')
    upgrade_start_time: datetime = ApiField(alias='UpgradeStartTime')
    upgrade_stop_time: datetime = ApiField(alias='UpgradeStopTime')
    completed_tasks: int = ApiField(alias='CompletedTasks')
    target_version: str = ApiField(alias='TargetVersion')
    engines_complete: int = ApiField(alias='EnginesComplete')
    engines_running: int = ApiField(alias='EnginesRunning')
    engines_blocked: int = ApiField(alias='EnginesBlocked')
    engines_in_error: int = ApiField(alias='EnginesInError')
    engines_pending_install: int = ApiField(alias='EnginesPendingInstall')
