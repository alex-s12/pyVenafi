from venafi.api.api_base import API, json_response_property
from venafi.logger import logger, LogLevels
import json


class _Users:
    def __init__(self, aperture_obj):
        self.Authorize = self._Authorize(aperture_obj=aperture_obj)

    class _Authorize(API):
        def __init__(self, aperture_obj):
            super().__init__(
                api_obj=aperture_obj,
                url='/users/authorize',
                valid_return_codes=[200]
            )

        @property
        @json_response_property()
        def token(self) -> dict:
            logger.log('Aperture API Key retrieved.', level=LogLevels.low.level)
            token = "VENAFI " + self._from_json('apiKey')
            return {'Authorization': token}

        def post(self, username, password):
            """
            This POST method is written differently in order to effectively omit the password from being logged.
            """
            body = {
                "username": username,
                "password": password
            }

            self.json_response = self._post(data=body)
            return self
