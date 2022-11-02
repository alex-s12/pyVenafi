from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes


class EngineRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Engine Root"
    acme_certificates_folder = Attribute('ACME Certificates Folder', min_version='17.2')
    acme_enabled = Attribute('ACME Enabled', min_version='17.2')
    adaptable_script_max_file_size = Attribute('Adaptable Script Max File Size', min_version='19.3')
    advanced_key_protect = Attribute('Advanced Key Protect', min_version='18.1')
    allow_acme_folder_creation = Attribute('Allow ACME Folder Creation', min_version='17.2')
    authentication_scheme = Attribute('Authentication Scheme')
    automatically_apply_filters = Attribute('Automatically Apply Filters', min_version='21.3')
    disabled_features = Attribute('Disabled Features', min_version='21.1')
    flow_process_expiry = Attribute('Flow Process Expiry', min_version='21.2')
    key_pair_renewal_flow = Attribute('Key Pair Renewal Flow', min_version='20.2')
    known_cloud_service = Attribute('Known Cloud Service', min_version='17.1')
    known_cloud_service_region = Attribute('Known Cloud Service Region', min_version='17.1')
    large_tree_support = Attribute('Large Tree Support')
    managed_by_options = Attribute('Managed By Options')
    monitored_uri_verification_engine_info = Attribute('Monitored URI Verification Engine Info')
    monitored_uri_verification_identifier = Attribute('Monitored URI Verification Identifier')
    monitored_uri_verification_last_check = Attribute('Monitored URI Verification Last Check')
    monitored_uri_verification_last_notification = Attribute('Monitored URI Verification Last Notification')
    monitored_uri_verification_uri_identifier = Attribute('Monitored URI Verification URI Identifier')
    oam_enabled = Attribute('OAM Enabled')
    oam_headervar = Attribute('OAM HeaderVar')
    oam_logout_url = Attribute('OAM Logout Url', min_version='20.1')
    operating_environment = Attribute('Operating Environment', min_version='15.1')
    options = Attribute('Options', min_version='20.4')
    pendo_events_last_sent = Attribute('Pendo Events Last Sent', min_version='21.4')
    require_password = Attribute('Require Password')
    revocation_check_issuer_dn = Attribute('Revocation Check Issuer DN')
    revocation_check_issuer_identifier = Attribute('Revocation Check Issuer Identifier')
    secret_key_renewal_flow = Attribute('Secret Key Renewal Flow', min_version='20.2')
    tn_aperture_plugin_vault_id = Attribute('TN Aperture Plugin Vault Id', min_version='18.1')
    tn_public_cas = Attribute('TN Public CAs', min_version='18.4')
    tn_widget_vault = Attribute('TN Widget Vault', min_version='18.1')
    teams_enabled = Attribute('Teams Enabled', min_version='20.1')
    teams_options = Attribute('Teams Options', min_version='20.2')
    teams_required = Attribute('Teams Required', min_version='20.1')
    time_stamping_certificate_dn = Attribute('Time Stamping Certificate DN', min_version='20.3')
    time_stamping_proxy_host_urls = Attribute('Time Stamping Proxy Host URLs', min_version='20.3')
    time_stamping_proxy_options = Attribute('Time Stamping Proxy Options', min_version='20.3')
    timeout = Attribute('Timeout', min_version='21.1')
    trustnet_critical_event_notification_emails = Attribute('TrustNet Critical Event Notification Emails', min_version='18.2')
    trustnet_emergency_event_notification_emails = Attribute('TrustNet Emergency Event Notification Emails', min_version='18.2')
    trustnet_heavy_job_schedule = Attribute('TrustNet Heavy Job Schedule', min_version='18.2')
    trustnet_info_event_notification_emails = Attribute('TrustNet Info Event Notification Emails', min_version='18.2')
    trustnet_last_security_event_timestamp = Attribute('TrustNet Last Security Event Timestamp', min_version='18.2')
    trustnet_light_job_schedule = Attribute('TrustNet Light Job Schedule', min_version='18.2')
    trustnet_placement_rules = Attribute('TrustNet Placement Rules', min_version='19.1')
    trustnet_sanitize_emails = Attribute('TrustNet Sanitize Emails', min_version='18.2')
    trustnet_task_last_run = Attribute('TrustNet Task Last Run', min_version='19.1')
    trustnet_trusted_ca = Attribute('TrustNet Trusted CA', min_version='18.2')
    trustnet_untrusted_ca = Attribute('TrustNet Untrusted CA', min_version='18.2')
    trustnet_warning_event_notification_emails = Attribute('TrustNet Warning Event Notification Emails', min_version='18.2')
    trusted_websdk_modules = Attribute('Trusted WebSDK Modules')
    usage_tracking = Attribute('Usage Tracking', min_version='18.1')
    websdk_options = Attribute('WebSDK Options')
    whitelisted_elevation_commands = Attribute('Whitelisted Elevation Commands', min_version='17.1')
    workflow_interval = Attribute('Workflow Interval', min_version='18.2')
    workflow_last_check = Attribute('Workflow Last Check', min_version='18.2')