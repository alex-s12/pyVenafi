from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from venafi.tpp.plugins import Authenticate
from venafi.tpp.api.websdk.models import config
from venafi.tpp.features.bases.feature_base import feature
from venafi.tpp.features.definitions.exceptions import UnexpectedValue
from venafi.tpp.features.discovery import NetworkDiscovery as _NetworkDiscovery
from venafi.tpp.plugins.api.aperture.enums.network_discovery import NetworkDiscovery as _NetworkDiscoveryProperties


@feature(_NetworkDiscovery.__feature__)
class NetworkDiscovery(_NetworkDiscovery):
    """
    This feature provides high-level interaction with TPP Network Discovery objects.
    """

    def __init__(self, api: 'Authenticate'):
        super().__init__(api=api)
        if TYPE_CHECKING:
            self._api = api

    def run_now(self, job: 'Union[config.Object, str]', timeout: int = 60):
        """
        Runs a job despite any scheduling. This does not return until the job is processing, or has a `Processing` Attribute.

        Args:
            job: Config object or name of the discovery job.
            timeout: Timeout in seconds within which the job should start.
        """
        job_obj = self._get_config_object(
            self._get_dn(job, parent_dn=self._discovery_dn)
        )
        self._api.aperture.Jobs.NetworkDiscovery.Guid(job_obj.guid).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.run_now
        )

        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=0.5):
                if self.is_in_progress(job=job_obj):
                    return

        raise UnexpectedValue(
            f'Expected the job "{job_obj.dn}" to start progress, but it did not.'
        )

    def cancel(self, job: 'Union[config.Object, str]'):
        """
        Cancels a currently running job.

        Args:
            job: Config object or GUID of the discovery job.
        """
        self._api.aperture.Jobs.NetworkDiscovery.Guid(
            self._get_guid(job, parent_dn=self._discovery_dn)
        ).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.cancel
        )

    def pause(self, job: 'Union[config.Object, str]'):
        """
        Pauses a currently running job.

        Args:
            job: Config object or GUID of the discovery job.
        """
        self._api.aperture.Jobs.NetworkDiscovery.Guid(
            self._get_guid(job, parent_dn=self._discovery_dn)
        ).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.pause
        )

    def resume(self, job: 'Union[config.Object, str]'):
        """
        Resumes a currently paused job.

        Args:
            job: Config object or GUID of the discovery job.
        """
        self._api.aperture.Jobs.NetworkDiscovery.Guid(
            self._get_guid(job, parent_dn=self._discovery_dn)
        ).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.resume
        )

    def place_results(self, job: 'Union[config.Object, str]'):
        """
        Places the results of the discovery job according to the placement rules.

        Args:
            job: Config object or GUID of the discovery job.
        """
        self._api.aperture.Jobs.NetworkDiscovery.Guid(
            self._get_guid(job, parent_dn=self._discovery_dn)
        ).Actions.post(
            job_action=_NetworkDiscoveryProperties.Actions.place_now
        )
