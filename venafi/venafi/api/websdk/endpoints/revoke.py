from venafi.api.api_base import API, APIResponse


class _Revoke:
    def __init__(self, api_obj):
        self.Token = self._Token(api_obj=api_obj)

    class _Token(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Revoke/Token')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def get(self):
            self._log_api_deprecated_warning()

            return APIResponse(response=self._get(), api_source=self._api_source)
