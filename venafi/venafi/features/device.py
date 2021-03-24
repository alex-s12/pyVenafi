from venafi.properties.config import DevicesClassNames, DeviceAttributes, DeviceAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, feature


class _DeviceBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, object_dn: str):
        """
        Deletes the device object specified. Since there are no secret store data attached to this object,
        only a config delete is performed.

        Args:
            object_dn: Absolute path to the device object.
        """
        self._config_delete(object_dn=object_dn)


@feature()
class Device(_DeviceBase):
    """
    This feature provides high-level interaction with TPP device objects.
    """
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Device object in TPP.

        Args:
            name: Name of the device object .
            parent_folder_dn: Absolute path to the parent folder of the device object.
            hostname: DNS or IP Address of the device.
            credential_dn: Absolute path to the credential object for this device.
            attributes: List of attributes pertaining to the device object.

        Returns:
            Config object representing the device.

        """
        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=DevicesClassNames.device,
            attributes=attributes
        )
