from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes


class CodeSigningPreQualifiedActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Pre Qualified Action"