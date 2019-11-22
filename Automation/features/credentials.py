from features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences


class UsernamePasswordCredential(FeatureBase):
    def __init__(self, auth_obj):
        super().__init__(auth_obj)

    def load(self):
        pass

    def create(self, name, folder, username, password):
        """
        :type name: str
        :type folder: Folder
        :type username: str
        :type password: str
        """
        dn = folder.dn + "\\" + name

        if self.auth.preference == ApiPreferences.aperture:
            self._logger.log(FeatureError.not_implemented(ApiPreferences.aperture).__str__())

        result = self.auth.websdk.Credentials.Create.post(
            credential_path=dn,
            friendly_name='UsernamePassword',
            values=[
                {'Name': 'Username', 'Type': 'string', 'Value': username},
                {'Name': 'Password', 'Type': 'string', 'Value': password}
            ]
        ).result

        self._logger.log('UsernamePassword credential "%s" created successfully.' % dn)

        self.load()
        return self
