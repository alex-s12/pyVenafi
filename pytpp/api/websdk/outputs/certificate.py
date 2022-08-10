from pytpp.api.api_base import OutputModel, ApiField
from datetime import datetime
from typing import List, Literal

CertificateFormat = Literal['Base64', 'Base64 (PKCS #8)', 'DER', 'JKS', 'PKCS #7', 'PKCS #12']


class Link(OutputModel):
    details: str = ApiField(alias='Details')
    next: str = ApiField(alias='Next')
    previous: str = ApiField(alias='Previous')


class CertificateDetails(OutputModel):
    aia_ca_issuer_url: List[str] = ApiField(alias='AIACAIssuerURL')
    aia_key_identifier: str = ApiField(alias='AIAKeyIdentifier')
    c: str = ApiField(alias='C')
    cdp_uri: str = ApiField(alias='CDPURI')
    cn: str = ApiField(alias='CN')
    elliptic_curve: str = ApiField(alias='EllipticCurve')
    enhanced_key_usage: str = ApiField(alias='EnhancedKeyUsage')
    issuer: str = ApiField(alias='Issuer')
    key_algorithm: str = ApiField(alias='KeyAlgorithm')
    key_size: int = ApiField(alias='KeySize')
    key_usage: str = ApiField(alias='KeyUsage')
    l: str = ApiField(alias='L')
    o: str = ApiField(alias='O')
    ou: List[str] = ApiField(alias='OU')
    public_key_hash: str = ApiField(alias='PublicKeyHash')
    revocation_date: datetime = ApiField(alias='RevocationDate')
    revocation_status: str = ApiField(alias='RevocationStatus')
    s: str = ApiField(alias='S')
    ski_key_identifier: str = ApiField(alias='SKIKeyIdentifier')
    serial: str = ApiField(alias='Serial')
    signature_algorithm: str = ApiField(alias='SignatureAlgorithm')
    signature_algorithm_oid: str = ApiField(alias='SignatureAlgorithmOID')
    store_added: datetime = ApiField(alias='StoreAdded')
    subject: str = ApiField(alias='Subject')
    subject_alt_name_dns: List[str] = ApiField(alias='SubjectAltNameDNS')
    subject_alt_name_email: List[str] = ApiField(alias='SubjectAltNameEmail')
    subject_alt_name_ip_address: List[str] = ApiField(alias='SubjectAltNameIPAddress')
    subject_alt_name_other_name_upn: List[str] = ApiField(alias='SubjectAltNameOtherNameUPN')
    subject_alt_name_uri: List[str] = ApiField(alias='SubjectAltNameUri')
    template_major_version: str = ApiField(alias='TemplateMajorVersion')
    template_minor_version: str = ApiField(alias='TemplateMajorVersion')
    template_name: str = ApiField(alias='TemplateName')
    template_oid: str = ApiField(alias='TemplateOID')
    thumbprint: str = ApiField(alias='Thumbprint')
    valid_from: datetime = ApiField(alias='ValidFrom')
    valid_to: datetime = ApiField(alias='ValidTo')


class PreviousVersions(OutputModel):
    certificate_details: CertificateDetails = ApiField(alias='CertificateDetails')
    vault_id: int = ApiField(alias='VaultId')


class ProcessingDetails(OutputModel):
    in_error: bool = ApiField(alias='InError')
    stage: int = ApiField(alias='Stage')
    status: str = ApiField(alias='Status')


class RenewalDetails(OutputModel):
    city: str = ApiField(alias='City')
    country: str = ApiField(alias='Country')
    organization: str = ApiField(alias='Organization')
    organizational_unit: List[str] = ApiField(alias='OrganizationalUnit')
    state: str = ApiField(alias='State')
    subject: str = ApiField(alias='Subject')
    subject_alt_name_dns: List[str] = ApiField(alias='SubjectAltNameDns')
    subject_alt_name_email: List[str] = ApiField(alias='SubjectAltNameEmail')
    subject_alt_name_ip_address: List[str] = ApiField(alias='SubjectAltNameIpAddress')
    subject_alt_name_other_name_upn: List[str] = ApiField(alias='SubjectAltNameOtherNameUpn')
    subject_alt_name_uri: List[str] = ApiField(alias='SubjectAltNameUri')
    valid_from: datetime = ApiField(alias='ValidFrom')
    valid_to: datetime = ApiField(alias='ValidTo')


class ValidationDetails(OutputModel):
    last_validation_state_update: str = ApiField(alias='LastValidationStateUpdate')
    validation_state: str = ApiField(alias='ValidationState')


class File(OutputModel):
    installation: str = ApiField(alias='Installation')
    performed_on: datetime = ApiField(alias='PerformedOn')
    result: List[str] = ApiField(alias='Result')


class BitMaskValues(OutputModel):
    bitmask: int = ApiField(alias='Bitmask')
    values: List[str] = ApiField(alias='Values')


class SANS(OutputModel):
    dns: List[str] = ApiField(alias='Dns')
    ip: List[str] = ApiField(alias='Ip')


class Compliant(OutputModel):
    compliant: bool = ApiField(alias='Compliant')


class CompliantSingleValue(Compliant):
    value: str = ApiField(alias='Value')


class CompliantMultiValue(Compliant):
    values: List[str] = ApiField(alias='Values')


class Locked(OutputModel):
    locked: bool = ApiField(alias='Locked')


class LockedSingleValue(Locked):
    value: str = ApiField(alias='Value')


class LockedMultiValue(Locked):
    values: list = ApiField(alias='Values')


class LockedKeyPair(OutputModel):
    key_algorithm: LockedSingleValue = ApiField(alias='KeyAlgorithm')
    key_size: LockedSingleValue = ApiField(alias='KeySize')


class LockedSubject(OutputModel):
    city: LockedSingleValue = ApiField(alias='City')
    country: LockedSingleValue = ApiField(alias='Country')
    organization: LockedSingleValue = ApiField(alias='Organization')
    organizational_units: LockedMultiValue = ApiField(alias='OrganizationalUnits')
    state: LockedSingleValue = ApiField(alias='State')


class CSRDetails(OutputModel):
    city: CompliantSingleValue = ApiField(alias='City')
    common_name: CompliantSingleValue = ApiField(alias='CommonName')
    country: CompliantSingleValue = ApiField(alias='Country')
    key_algorithm: CompliantSingleValue = ApiField(alias='KeyAlgorithm')
    key_size: CompliantSingleValue = ApiField(alias='KeySize')
    organization: CompliantSingleValue = ApiField(alias='Organization')
    organizational_unit: CompliantMultiValue = ApiField(alias='OrganizationalUnit')
    private_key_reused: CompliantSingleValue = ApiField(alias='PrivateKeyReused')
    state: CompliantSingleValue = ApiField(alias='State')
    subj_alt_name_dns: CompliantMultiValue = ApiField(alias='SubjAltNameDns')
    subj_alt_name_email: CompliantMultiValue = ApiField(alias='SubjAltNameEmail')
    subj_alt_name_ip: CompliantMultiValue = ApiField(alias='SubjAltNameIp')
    subj_alt_name_upn: CompliantMultiValue = ApiField(alias='SubjAltNameUpn')
    subj_alt_name_uri: CompliantMultiValue = ApiField(alias='SubjAltNameUri')


class NameTypeValue(OutputModel):
    name: str = ApiField(alias='Name')
    type: str = ApiField(alias='Type')
    value: str = ApiField(alias='Value')


class SslTlsResult(OutputModel):
    chain: BitMaskValues = ApiField(alias='Chain')
    end_entity: BitMaskValues = ApiField(alias='EndEntity')
    id: int = ApiField(alias='Id')
    protocols: BitMaskValues = ApiField(alias='Protocols')


class SslTls(OutputModel):
    host: str = ApiField(alias='Host')
    ip_address: str = ApiField(alias='IpAddress')
    port: int = ApiField(alias='Port')
    result: SslTlsResult = ApiField(alias='Result')
    sources: List[str] = ApiField(alias='Sources')


class Policy(OutputModel):
    certificate_authority: LockedSingleValue = ApiField(alias='CertificateAuthority')
    csr_generation: LockedSingleValue = ApiField(alias='CsrGeneration')
    management_type: LockedSingleValue = ApiField(alias='ManagementType')
    key_generation: LockedSingleValue = ApiField(alias='KeyGeneration')
    key_pair: LockedKeyPair = ApiField(alias='KeyPair')
    private_key_reuse_allowed: bool = ApiField(alias='PrivateKeyReuseAllowed')
    subj_alt_name_dns_allowed: bool = ApiField(alias='SubjAltNameDnsAllowed')
    subj_alt_name_email_allowed: bool = ApiField(alias='SubjAltNameEmailAllowed')
    subj_alt_name_ip_allowed: bool = ApiField(alias='SubjAltNameIpAllowed')
    subj_alt_name_upn_allowed: bool = ApiField(alias='SubjAltNameUpnAllowed')
    subj_alt_name_uri_allowed: bool = ApiField(alias='SubjAltNameUriAllowed')
    subject: LockedSubject = ApiField(alias='Subject')
    unique_subject_enforced: bool = ApiField(alias='UniqueSubjectEnforced')
    whitelisted_domains: List[str] = ApiField(alias='WhitelistedDomains')
    wildcards_allowed: bool = ApiField(alias='WildcardsAllowed')


class CSR(OutputModel):
    details: CSRDetails = ApiField('Details')
    enrollable: bool = ApiField('Enrollable')


class X509(OutputModel):
    cn: str = ApiField(alias='Cn')
    issuer: str = ApiField(alias='Issuer')
    key_algorithm: str = ApiField(alias='KeyAlgorithm')
    key_size: int = ApiField(alias='KeySize')
    sans: SANS = ApiField(alias='Sans')
    serial: str = ApiField(alias='Serial')
    subject: str = ApiField(alias='Subject')
    thumbprint: str = ApiField(alias='Thumbprint')
    valid_from: datetime = ApiField(alias='ValidFrom')
    valid_to: datetime = ApiField(alias='ValidTo')


class Certificate(OutputModel):
    created_on: datetime = ApiField(alias='CreatedOn')
    dn: str = ApiField(alias='DN')
    guid: str = ApiField(alias='Guid')
    name: str = ApiField(alias='Name')
    parent_dn: str = ApiField(alias='ParentDn')
    schema_class: str = ApiField(alias='SchemaClass')
    x509: X509 = ApiField(alias='X509')
    links: List[Link] = ApiField(alias='_links')
