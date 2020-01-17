from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.ssh import SSH


class _SSH:
    def __init__(self, websdk_obj):
        self.AddAuthorizedKey = self._AddAuthorizedKey(websdk_obj=websdk_obj)
        self.AddHostPrivateKey = self._AddHostPrivateKey(websdk_obj=websdk_obj)
        self.AddKnownHostKey = self._AddKnownHostKey(websdk_obj=websdk_obj)
        self.AddSelfServiceKey = self._AddSelfServiceKey(websdk_obj=websdk_obj)
        self.AddSelfServiceAuthorizedKey = self._AddSelfServiceAuthorizedKey(websdk_obj=websdk_obj)
        self.AddSelfServicePrivateKey = self._AddSelfServicePrivateKey(websdk_obj=websdk_obj)
        self.AddUserPrivateKey = self._AddUserPrivateKey(websdk_obj=websdk_obj)
        self.ApproveKeyOperation = self._ApproveKeyOperation(websdk_obj=websdk_obj)
        self.CancelKeyOperation = self._CancelKeyOperation(websdk_obj=websdk_obj)
        self.CancelRotation = self._CancelRotation(websdk_obj=websdk_obj)
        self.ChangePrivateKeyPassphrase = self._ChangePrivateKeyPassphrase(websdk_obj=websdk_obj)
        self.ConfirmSelfServiceKeyInstallation = self._ConfirmSelfServiceKeyInstallation(websdk_obj=websdk_obj)
        self.DeleteUnmatchedKeyset = self._DeleteUnmatchedKeyset(websdk_obj=websdk_obj)
        self.Devices = self._Devices(websdk_obj=websdk_obj)
        self.EditKeyOptions = self._EditKeyOptions(websdk_obj=websdk_obj)
        self.EditSelfServiceAuthorizedKey = self._EditSelfServiceAuthorizedKey(websdk_obj=websdk_obj)
        self.ExportSelfServiceKey = self._ExportSelfServiceKey(websdk_obj=websdk_obj)
        self.ExportSelfServicePrivateKey = self._ExportSelfServicePrivateKey(websdk_obj=websdk_obj)
        self.ImportAuthorizedKey = self._ImportAuthorizedKey(websdk_obj=websdk_obj)
        self.ImportKeyUsageData = self._ImportKeyUsageData(websdk_obj=websdk_obj)
        self.ImportPrivateKey = self._ImportPrivateKey(websdk_obj=websdk_obj)
        self.KeyDetails = self._KeyDetails(websdk_obj=websdk_obj)
        self.KeysetDetails = self._KeysetDetails(websdk_obj=websdk_obj)
        self.KeyUsage = self._KeyUsage(websdk_obj=websdk_obj)
        self.MoveKeysetsToPolicy = self._MoveKeysetsToPolicy(websdk_obj=websdk_obj)
        self.RejectKeyOperation = self._RejectKeyOperation(websdk_obj=websdk_obj)
        self.RemoveKey = self._RemoveKey(websdk_obj=websdk_obj)
        self.RetryKeyOperation = self._RetryKeyOperation(websdk_obj=websdk_obj)
        self.RetryRotation = self._RetryRotation(websdk_obj=websdk_obj)
        self.Rotate = self._Rotate(websdk_obj=websdk_obj)
        self.SetUnmatchedKeysetPassPhrase = self._SetUnmatchedKeysetPassPhrase(websdk_obj=websdk_obj)
        self.SkipKeyRotation = self._SkipKeyRotation(websdk_obj=websdk_obj)
        self.Widget = self._Widget(websdk_obj=websdk_obj)

    class _AddAuthorizedKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/AddAuthorizedKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_id(self) -> str:
            return self._from_json('KeyId')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, device_guid: str, filepath: str, keyset_id: str, username: str, allowed_source_restricition: list = None,
                 denied_source_restriction: list = None, forced_command: str = None, format: str = None, options: list = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restricition,
                'DeniedSourceRestriction': denied_source_restriction,
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'ForcedCommand': forced_command,
                'Format': format,
                'KeysetId': keyset_id,
                'Options': options,
                'Username': username
            }
            
            self.json_response = self._post(data=body)
            
            return self

    class _AddHostPrivateKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/AddHostPrivateKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_id(self) -> str:
            return self._from_json('KeyId')

        @property
        @json_response_property()
        def keyset_id(self) -> str:
            return self._from_json('KeysetId')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, device_guid: str, filepath: str, username: str, format: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'Username': username
            }

            self.json_response = self._post(data=body)
            return self

    class _AddKnownHostKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/AddKnownHostKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_id(self) -> str:
            return self._from_json('KeyId')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, device_guid: str, filepath: str, keyset_id: str, username: str, format: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeysetId': keyset_id,
                'Username': username
            }

            self.json_response = self._post(data=body)
            return self

    class _AddSelfServiceKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/AddSelfServiceKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_id(self) -> str:
            return self._from_json('KeyId')

        @property
        @json_response_property()
        def keyset_id(self) -> str:
            return self._from_json('KeysetId')

        @property
        @json_response_property()
        def notes(self) -> str:
            return self._from_json('Notes')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, folder_id: str, location: str, notes: str, owner: str, contact_email: str = None, keyset_id: str = None):
            body = {
                'ContactEmail': contact_email,
                'FolderId': folder_id,
                'KeysetId': keyset_id,
                'Location': location,
                'Notes': notes,
                'Owner': owner
            }

            self.json_response = self._post(data=body)
            return self

    class _AddSelfServiceAuthorizedKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/AddSelfServiceAuthorizedKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_id(self) -> str:
            return self._from_json('KeyId')

        @property
        @json_response_property()
        def keyset_id(self) -> str:
            return self._from_json('KeysetId')

        @property
        @json_response_property()
        def notes(self) -> str:
            return self._from_json('Notes')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, allowed_source_restriction: list, denied_source_restriction: list, folder_id: str, location: str, notes: str,
                 options: list, owner: str, contact_email: str = None, forced_command: str = None, keyset_id: str = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'ContactEmail': contact_email,
                'DeniedSourceRestriction': denied_source_restriction,
                'FolderId': folder_id,
                'ForcedCommand': forced_command,
                'KeysetId': keyset_id,
                'Location': location,
                'Notes': notes,
                'Options': options,
                'Owner': owner
            }

            self.json_response = self._post(data=body)
            return self

    class _AddSelfServicePrivateKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/AddSelfServicePrivateKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def owner(self) -> str:
            return self._from_json('Owner')

        @property
        @json_response_property()
        def location(self) -> str:
            return self._from_json('Location')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, folder_id: str, location: str, notes: str, owner: str, contact_email: str = None, keyset_id: str = None):
            body = {
                'ContactEmail': contact_email,
                'FolderId': folder_id,
                'KeysetId': keyset_id,
                'Location': location,
                'Notes': notes,
                'Owner': owner
            }

            self.json_response = self._post(data=body)
            return self

    class _AddUserPrivateKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/AddUserPrivateKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_id(self) -> str:
            return self._from_json('KeyId')

        @property
        @json_response_property()
        def keyset_id(self) -> str:
            return self._from_json('KeysetId')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, device_guid: str, filepath: str, username: str, format: str = None, keyset_id: str = None, passphrase: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeysetId': keyset_id,
                'Passphrase': passphrase,
                'Username': username
            }

            self.json_response = self._post(data=body)
            return self

    class _ApproveKeyOperation(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/ApproveKeyOperation', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str, comment: str):
            body = {
                'KeyId': key_id,
                'Comment': comment
            }

            self.json_response = self._post(data=body)
            return self

    class _CancelKeyOperation(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/CancelKeyOperation', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str):
            body = {
                'KeyId': key_id
            }

            self.json_response = self._post(data=body)
            return self

    class _CancelRotation(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/CancelRotation', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            self.json_response = self._post(data=body)
            return self

    class _ChangePrivateKeyPassphrase(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/ChangePrivateKeyPassphrase', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str, passphrase: str):
            body = {
                'KeysetId': key_id,
                'Passphrase': passphrase
            }

            self.json_response = self._post(data=body)
            return self

    class _ConfirmSelfServiceKeyInstallation(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/ConfirmSelfServiceKeyInstallation', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            self.json_response = self._post(data=body)
            return self

    class _DeleteUnmatchedKeyset(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/DeleteUnmatchedKeyset', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, unmatched_trust_id: str):
            body = {
                'UnmatchedTrustId': unmatched_trust_id
            }

            self.json_response = self._post(data=body)
            return self

    class _Devices(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/Devices', valid_return_codes=[200])

        @property
        @json_response_property()
        def data(self):
            return [SSH.DeviceData(d) for d in self._from_json('Data')]

        def post(self, page_size: int, offset: int = None, ssh_device_filter: dict = None):
            body = {
                'PageSize': page_size,
                'Offset': offset,
                'SshDeviceFilter': ssh_device_filter
            }

            self.json_response = self._post(data=body)
            return self

    class _EditSelfServiceAuthorizedKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/EditSelfServiceAuthorizedKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str, allowed_source_restriction: list = None, comments: str = None, denied_source_restriction: list = None,
                 forced_command: str = None, location: str = None, notes: str = None, options: list = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'Comments': comments,
                'DeniedSourceRestriction': denied_source_restriction,
                'ForcedCommand': forced_command,
                'KeyId': key_id,
                'Location': location,
                'Notes': notes,
                'Options': options
            }

            self.json_response = self._post(data=body)
            return self

    class _ExportSelfServiceKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/ExportSelfServiceKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_material(self) -> str:
            return self._from_json('KeyMaterial')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str, format: str = None, passphrase: str = None):
            body = {
                'KeyId': key_id,
                'Format': format,
                'Passphrase': passphrase
            }

            self.json_response = self._post(data=body)
            return self

    class _ExportSelfServicePrivateKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/ExportSelfServicePrivateKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_id(self) -> str:
            return self._from_json('KeyId')

        @property
        @json_response_property()
        def keyset_id(self) -> str:
            return self._from_json('KeysetId')

        @property
        @json_response_property()
        def notes(self) -> str:
            return self._from_json('Notes')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str, format: str = None, passphrase: str = None):
            body = {
                'KeyId': key_id,
                'Format': format,
                'Passphrase': passphrase
            }

            self.json_response = self._post(data=body)
            return self

    class _ImportAuthorizedKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/ImportAuthorizedKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_id(self) -> str:
            return self._from_json('KeyId')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, device_guid: str, filepath: str, format: str, key_content_base_64: str, username: str):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeyContentBase64': key_content_base_64,
                'Username': username
            }

            self.json_response = self._post(data=body)
            return self

    class _ImportKeyUsageData(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/ImportKeyUsageData', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('SshWebResponse'))

        def post(self, log_data: list):
            body = {
                'LogData': log_data
            }

            self.json_response = self._post(data=body)
            return self

    class _ImportPrivateKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/ImportPrivateKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_id(self) -> str:
            return self._from_json('KeyId')

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, device_guid: str, filepath: str, format: str, key_content_base_64: str, username: str, passphrase: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeyContentBase64': key_content_base_64,
                'Passphrase': passphrase,
                'Username': username
            }

            self.json_response = self._post(data=body)
            return self

    class _EditKeyOptions(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/EditKeyOptions', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str, allowed_source_restriction: list = None, denied_source_restriction: list = None,
                 forced_command: str = None, options: list = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'DeniedSourceRestriction': denied_source_restriction,
                'ForcedCommand': forced_command,
                'KeyId': key_id,
                'Options': options
            }

            self.json_response = self._post(data=body)
            return self

    class _KeyDetails(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/KeyDetails', valid_return_codes=[200])

        @property
        @json_response_property()
        def key_data(self):
            return [SSH.KeyData(d) for d in self._from_json('KeyData')]

        def post(self, key_id: list):
            body = {
                'KeyId': key_id
            }

            self.json_response = self._post(data=body)
            return self

    class _KeysetDetails(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/KeysetDetails', valid_return_codes=[200])

        @property
        @json_response_property()
        def access(self):
            return self._from_json('Access')

        @property
        @json_response_property()
        def algorithm(self):
            return self._from_json('Algorithm')

        @property
        @json_response_property()
        def data(self):
            return [SSH.KeyData(key) for key in self._from_json('Data')]

        @property
        @json_response_property()
        def fingerprint_md5(self):
            return self._from_json('FingerprintMD5')

        @property
        @json_response_property()
        def fingerprint_sha256(self):
            return self._from_json('FingerprintSHA256')

        @property
        @json_response_property()
        def keyset_id(self):
            return self._from_json('KeysetId')

        @property
        @json_response_property()
        def last_rotation_date(self):
            return self._from_json('LastRotationDate')

        @property
        @json_response_property()
        def last_used(self):
            return self._from_json('LastUsed')

        @property
        @json_response_property()
        def length(self):
            return self._from_json('Length')

        @property
        @json_response_property()
        def private_keys(self):
            return [SSH.KeyData(key) for key in self._from_json('PrivateKeys')]

        @property
        @json_response_property()
        def process_status(self):
            return self._from_json('ProcessStatus')

        @property
        @json_response_property()
        def public_keys(self):
            return [SSH.KeyData(key) for key in self._from_json('PublicKeys')]

        @property
        @json_response_property()
        def rotation_stage(self):
            return self._from_json('RotationStage')

        @property
        @json_response_property()
        def type(self):
            return self._from_json('Type')

        @property
        @json_response_property()
        def violation_status(self):
            return self._from_json('ViolationStatus')

        def get(self, keyset_id: list, load_key_data: bool = None):
            params = {
                'KeysetId': keyset_id,
                'LoadKeyData': load_key_data
            }

            self.json_response = self._get(params=params)
            return self

        def post(self, keyset_filter: list, load_key_data: bool = None, offset: int = None, page_size: int = None):
            body = {
                'KeysetFilter': keyset_filter,
                'LoadKeyData': load_key_data,
                'Offset': offset,
                'PageSize': page_size
            }

            self.json_response = self._post(data=body)
            return self

    class _KeyUsage(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/KeyUsage', valid_return_codes=[200])

        @property
        @json_response_property()
        def data(self):
            return [SSH.KeyUsageData(key) for key in self._from_json('Data')]

        def post(self, ssh_key_usage_filter: list, load_key_data: bool = None, page_size: int = None, offset: int = None):
            body = {
                'SshKeyUsageFilter': ssh_key_usage_filter,
                'LoadKeyData': load_key_data,
                'PageSize': page_size,
                'Offset': offset
            }

            self.json_response = self._post(data=body)
            return self

    class _MoveKeysetsToPolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/MoveKeysetsToPolicy', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, keyset_ids: list, policy_path: str):
            body = {
                'KeysetIds': keyset_ids,
                'PolicyPath': policy_path
            }

            self.json_response = self._post(data=body)
            return self

    class _RejectKeyOperation(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/RejectKeyOperation', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str, comment: str):
            body = {
                'KeyId': key_id,
                'Comment': comment
            }

            self.json_response = self._post(data=body)
            return self

    class _RemoveKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/RemoveKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str):
            body = {
                'KeyId': key_id
            }

            self.json_response = self._post(data=body)
            return self

    class _RetryKeyOperation(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/RetryKeyOperation', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str):
            body = {
                'KeyId': key_id
            }

            self.json_response = self._post(data=body)
            return self

    class _RetryRotation(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/RetryRotation', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            self.json_response = self._post(data=body)
            return self

    class _Rotate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/Rotate', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, allow_skip_on_rotation: bool, keyset_id: str):
            body = {
                'AllowSkipOnRotation': allow_skip_on_rotation,
                'KeysetId': keyset_id
            }

            self.json_response = self._post(data=body)
            return self

    class _SetUnmatchedKeysetPassPhrase(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/SetUnmatchedKeysetPassPhrase', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, passphrase: str, unmatched_trust_id: str):
            body = {
                'Passphrase': passphrase,
                'UnmatchedTrustId': unmatched_trust_id
            }

            self.json_response = self._post(data=body)
            return self

    class _SkipKeyRotation(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SSH/SkipKeyRotation', valid_return_codes=[200])

        @property
        @json_response_property()
        def response(self):
            return SSH.Response(self._from_json('Response'))

        def post(self, key_id: str):
            body = {
                'KeyId': key_id
            }

            self.json_response = self._post(data=body)
            return self

    class _Widget:
        def __init__(self, websdk_obj):
            self.CriticalAlerts = self._CriticalAlerts(websdk_obj=websdk_obj)
            self.PolicyViolations = self._PolicyViolations(websdk_obj=websdk_obj)
            self.Stats = self._Stats(websdk_obj=websdk_obj)

        class _CriticalAlerts(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SSH/Widget/CriticalAlerts', valid_return_codes=[200])

            @property
            @json_response_property()
            def root_orphans(self) -> int:
                return self._from_json('RootOrphans')

            @property
            @json_response_property()
            def non_root_orphans(self) -> int:
                return self._from_json('NonRootOrphans')

            @property
            @json_response_property()
            def accessible_root_accounts(self) -> int:
                return self._from_json('AccessibleRootAccounts')

            @property
            @json_response_property()
            def shared_private_keys(self) -> int:
                return self._from_json('SharedPrivateKeys')

            @property
            @json_response_property()
            def non_compliant_duplicate_private_keys(self) -> int:
                return self._from_json('NonCompliantDuplicatePrivateKeys')

            @property
            @json_response_property()
            def very_small_key(self) -> int:
                return self._from_json('VerySmallKey')

            def get(self, min_allowed_key_length: int):
                params = {
                    'minAllowedKeyLength': min_allowed_key_length
                }

                self.json_response = self._get(params=params)
                return self

        class _PolicyViolations(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SSH/Widget/PolicyViolations', valid_return_codes=[200])

            @property
            @json_response_property()
            def non_compliant_force_command(self):
                return self._from_json('NonCompliantForceCommand')

            @property
            @json_response_property()
            def non_compliant_source_restriction(self):
                return self._from_json('NonCompliantSourceRestriction')

            @property
            @json_response_property()
            def missing_options(self):
                return self._from_json('MissingOptions')

            @property
            @json_response_property()
            def non_compliant_algorithm(self):
                return self._from_json('NonCompliantAlgorithm')

            @property
            @json_response_property()
            def vulnerable_protocol(self):
                return self._from_json('VulnerableProtocol')

            @property
            @json_response_property()
            def non_compliant_vendor_format(self):
                return self._from_json('NonCompliantVendorFormat')

            @property
            @json_response_property()
            def key_older_than_policy(self):
                return self._from_json('KeyOlderThanPolicy')

            @property
            @json_response_property()
            def shared_server_account(self):
                return self._from_json('SharedServerAccount')

            @property
            @json_response_property()
            def key_smaller_than_policy(self):
                return self._from_json('KeySmallerThanPolicy')

            @property
            @json_response_property()
            def duplicate_private_keys(self):
                return self._from_json('DuplicatePrivateKeys')

            @property
            @json_response_property()
            def root_access(self):
                return self._from_json('RootAccess')

            def get(self):
                self.json_response = self._get()
                return self

        class _Stats(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SSH/Widget/Stats', valid_return_codes=[200])

            @property
            @json_response_property()
            def name_value_pairs(self) -> dict:
                return self._from_json()

            def get(self, group_by: str):
                params = {
                    'GroupBy': group_by
                }

                self.json_response = self._get(params=params)
                return self