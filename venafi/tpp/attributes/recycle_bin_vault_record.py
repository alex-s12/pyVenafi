from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class RecycleBinVaultRecordAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Recycle Bin Vault Record"
