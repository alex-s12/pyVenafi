from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.agent_driver_base import AgentDriverBaseAttributes
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes


class AgentDriverAttributes(AgentDriverBaseAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Driver"
