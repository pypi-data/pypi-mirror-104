"""
Main interface for es service client

Usage::

    ```python
    import boto3
    from mypy_boto3_es import ElasticsearchServiceClient

    client: ElasticsearchServiceClient = boto3.client("es")
    ```
"""
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_es.literals import (
    DescribeReservedElasticsearchInstanceOfferingsPaginatorName,
    DescribeReservedElasticsearchInstancesPaginatorName,
    ESPartitionInstanceType,
    GetUpgradeHistoryPaginatorName,
    ListElasticsearchInstanceTypesPaginatorName,
    ListElasticsearchVersionsPaginatorName,
    LogType,
    PackageType,
)
from mypy_boto3_es.paginator import (
    DescribeReservedElasticsearchInstanceOfferingsPaginator,
    DescribeReservedElasticsearchInstancesPaginator,
    GetUpgradeHistoryPaginator,
    ListElasticsearchInstanceTypesPaginator,
    ListElasticsearchVersionsPaginator,
)
from mypy_boto3_es.type_defs import (
    AcceptInboundCrossClusterSearchConnectionResponseTypeDef,
    AdvancedSecurityOptionsInputTypeDef,
    AssociatePackageResponseTypeDef,
    AutoTuneOptionsInputTypeDef,
    AutoTuneOptionsTypeDef,
    CancelElasticsearchServiceSoftwareUpdateResponseTypeDef,
    CognitoOptionsTypeDef,
    CreateElasticsearchDomainResponseTypeDef,
    CreateOutboundCrossClusterSearchConnectionResponseTypeDef,
    CreatePackageResponseTypeDef,
    DeleteElasticsearchDomainResponseTypeDef,
    DeleteInboundCrossClusterSearchConnectionResponseTypeDef,
    DeleteOutboundCrossClusterSearchConnectionResponseTypeDef,
    DeletePackageResponseTypeDef,
    DescribeDomainAutoTunesResponseTypeDef,
    DescribeElasticsearchDomainConfigResponseTypeDef,
    DescribeElasticsearchDomainResponseTypeDef,
    DescribeElasticsearchDomainsResponseTypeDef,
    DescribeElasticsearchInstanceTypeLimitsResponseTypeDef,
    DescribeInboundCrossClusterSearchConnectionsResponseTypeDef,
    DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef,
    DescribePackagesFilterTypeDef,
    DescribePackagesResponseTypeDef,
    DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef,
    DescribeReservedElasticsearchInstancesResponseTypeDef,
    DissociatePackageResponseTypeDef,
    DomainEndpointOptionsTypeDef,
    DomainInformationTypeDef,
    EBSOptionsTypeDef,
    ElasticsearchClusterConfigTypeDef,
    EncryptionAtRestOptionsTypeDef,
    FilterTypeDef,
    GetCompatibleElasticsearchVersionsResponseTypeDef,
    GetPackageVersionHistoryResponseTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    GetUpgradeStatusResponseTypeDef,
    ListDomainNamesResponseTypeDef,
    ListDomainsForPackageResponseTypeDef,
    ListElasticsearchInstanceTypesResponseTypeDef,
    ListElasticsearchVersionsResponseTypeDef,
    ListPackagesForDomainResponseTypeDef,
    ListTagsResponseTypeDef,
    LogPublishingOptionTypeDef,
    NodeToNodeEncryptionOptionsTypeDef,
    PackageSourceTypeDef,
    PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef,
    RejectInboundCrossClusterSearchConnectionResponseTypeDef,
    SnapshotOptionsTypeDef,
    StartElasticsearchServiceSoftwareUpdateResponseTypeDef,
    TagTypeDef,
    UpdateElasticsearchDomainConfigResponseTypeDef,
    UpdatePackageResponseTypeDef,
    UpgradeElasticsearchDomainResponseTypeDef,
    VPCOptionsTypeDef,
)

__all__ = ("ElasticsearchServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BaseException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DisabledOperationException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ElasticsearchServiceClient:
    """
    [ElasticsearchService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def accept_inbound_cross_cluster_search_connection(
        self, CrossClusterSearchConnectionId: str
    ) -> AcceptInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.accept_inbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.accept_inbound_cross_cluster_search_connection)
        """
    def add_tags(self, ARN: str, TagList: List["TagTypeDef"]) -> None:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.add_tags)
        """
    def associate_package(self, PackageID: str, DomainName: str) -> AssociatePackageResponseTypeDef:
        """
        [Client.associate_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.associate_package)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.can_paginate)
        """
    def cancel_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> CancelElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Client.cancel_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.cancel_elasticsearch_service_software_update)
        """
    def create_elasticsearch_domain(
        self,
        DomainName: str,
        ElasticsearchVersion: str = None,
        ElasticsearchClusterConfig: "ElasticsearchClusterConfigTypeDef" = None,
        EBSOptions: "EBSOptionsTypeDef" = None,
        AccessPolicies: str = None,
        SnapshotOptions: "SnapshotOptionsTypeDef" = None,
        VPCOptions: VPCOptionsTypeDef = None,
        CognitoOptions: "CognitoOptionsTypeDef" = None,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
        NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = None,
        AdvancedOptions: Dict[str, str] = None,
        LogPublishingOptions: Dict[LogType, "LogPublishingOptionTypeDef"] = None,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
        AdvancedSecurityOptions: AdvancedSecurityOptionsInputTypeDef = None,
        AutoTuneOptions: AutoTuneOptionsInputTypeDef = None,
        TagList: List["TagTypeDef"] = None,
    ) -> CreateElasticsearchDomainResponseTypeDef:
        """
        [Client.create_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.create_elasticsearch_domain)
        """
    def create_outbound_cross_cluster_search_connection(
        self,
        SourceDomainInfo: "DomainInformationTypeDef",
        DestinationDomainInfo: "DomainInformationTypeDef",
        ConnectionAlias: str,
    ) -> CreateOutboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.create_outbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.create_outbound_cross_cluster_search_connection)
        """
    def create_package(
        self,
        PackageName: str,
        PackageType: PackageType,
        PackageSource: PackageSourceTypeDef,
        PackageDescription: str = None,
    ) -> CreatePackageResponseTypeDef:
        """
        [Client.create_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.create_package)
        """
    def delete_elasticsearch_domain(
        self, DomainName: str
    ) -> DeleteElasticsearchDomainResponseTypeDef:
        """
        [Client.delete_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_domain)
        """
    def delete_elasticsearch_service_role(self) -> None:
        """
        [Client.delete_elasticsearch_service_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_service_role)
        """
    def delete_inbound_cross_cluster_search_connection(
        self, CrossClusterSearchConnectionId: str
    ) -> DeleteInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.delete_inbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.delete_inbound_cross_cluster_search_connection)
        """
    def delete_outbound_cross_cluster_search_connection(
        self, CrossClusterSearchConnectionId: str
    ) -> DeleteOutboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.delete_outbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.delete_outbound_cross_cluster_search_connection)
        """
    def delete_package(self, PackageID: str) -> DeletePackageResponseTypeDef:
        """
        [Client.delete_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.delete_package)
        """
    def describe_domain_auto_tunes(
        self, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeDomainAutoTunesResponseTypeDef:
        """
        [Client.describe_domain_auto_tunes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_domain_auto_tunes)
        """
    def describe_elasticsearch_domain(
        self, DomainName: str
    ) -> DescribeElasticsearchDomainResponseTypeDef:
        """
        [Client.describe_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain)
        """
    def describe_elasticsearch_domain_config(
        self, DomainName: str
    ) -> DescribeElasticsearchDomainConfigResponseTypeDef:
        """
        [Client.describe_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain_config)
        """
    def describe_elasticsearch_domains(
        self, DomainNames: List[str]
    ) -> DescribeElasticsearchDomainsResponseTypeDef:
        """
        [Client.describe_elasticsearch_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domains)
        """
    def describe_elasticsearch_instance_type_limits(
        self,
        InstanceType: ESPartitionInstanceType,
        ElasticsearchVersion: str,
        DomainName: str = None,
    ) -> DescribeElasticsearchInstanceTypeLimitsResponseTypeDef:
        """
        [Client.describe_elasticsearch_instance_type_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_instance_type_limits)
        """
    def describe_inbound_cross_cluster_search_connections(
        self, Filters: List[FilterTypeDef] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeInboundCrossClusterSearchConnectionsResponseTypeDef:
        """
        [Client.describe_inbound_cross_cluster_search_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_inbound_cross_cluster_search_connections)
        """
    def describe_outbound_cross_cluster_search_connections(
        self, Filters: List[FilterTypeDef] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef:
        """
        [Client.describe_outbound_cross_cluster_search_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_outbound_cross_cluster_search_connections)
        """
    def describe_packages(
        self,
        Filters: List[DescribePackagesFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribePackagesResponseTypeDef:
        """
        [Client.describe_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_packages)
        """
    def describe_reserved_elasticsearch_instance_offerings(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef:
        """
        [Client.describe_reserved_elasticsearch_instance_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instance_offerings)
        """
    def describe_reserved_elasticsearch_instances(
        self,
        ReservedElasticsearchInstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeReservedElasticsearchInstancesResponseTypeDef:
        """
        [Client.describe_reserved_elasticsearch_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instances)
        """
    def dissociate_package(
        self, PackageID: str, DomainName: str
    ) -> DissociatePackageResponseTypeDef:
        """
        [Client.dissociate_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.dissociate_package)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.generate_presigned_url)
        """
    def get_compatible_elasticsearch_versions(
        self, DomainName: str = None
    ) -> GetCompatibleElasticsearchVersionsResponseTypeDef:
        """
        [Client.get_compatible_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.get_compatible_elasticsearch_versions)
        """
    def get_package_version_history(
        self, PackageID: str, MaxResults: int = None, NextToken: str = None
    ) -> GetPackageVersionHistoryResponseTypeDef:
        """
        [Client.get_package_version_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.get_package_version_history)
        """
    def get_upgrade_history(
        self, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> GetUpgradeHistoryResponseTypeDef:
        """
        [Client.get_upgrade_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.get_upgrade_history)
        """
    def get_upgrade_status(self, DomainName: str) -> GetUpgradeStatusResponseTypeDef:
        """
        [Client.get_upgrade_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.get_upgrade_status)
        """
    def list_domain_names(self) -> ListDomainNamesResponseTypeDef:
        """
        [Client.list_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.list_domain_names)
        """
    def list_domains_for_package(
        self, PackageID: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDomainsForPackageResponseTypeDef:
        """
        [Client.list_domains_for_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.list_domains_for_package)
        """
    def list_elasticsearch_instance_types(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListElasticsearchInstanceTypesResponseTypeDef:
        """
        [Client.list_elasticsearch_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_instance_types)
        """
    def list_elasticsearch_versions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListElasticsearchVersionsResponseTypeDef:
        """
        [Client.list_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_versions)
        """
    def list_packages_for_domain(
        self, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListPackagesForDomainResponseTypeDef:
        """
        [Client.list_packages_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.list_packages_for_domain)
        """
    def list_tags(self, ARN: str) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.list_tags)
        """
    def purchase_reserved_elasticsearch_instance_offering(
        self,
        ReservedElasticsearchInstanceOfferingId: str,
        ReservationName: str,
        InstanceCount: int = None,
    ) -> PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef:
        """
        [Client.purchase_reserved_elasticsearch_instance_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.purchase_reserved_elasticsearch_instance_offering)
        """
    def reject_inbound_cross_cluster_search_connection(
        self, CrossClusterSearchConnectionId: str
    ) -> RejectInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.reject_inbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.reject_inbound_cross_cluster_search_connection)
        """
    def remove_tags(self, ARN: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.remove_tags)
        """
    def start_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> StartElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Client.start_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.start_elasticsearch_service_software_update)
        """
    def update_elasticsearch_domain_config(
        self,
        DomainName: str,
        ElasticsearchClusterConfig: "ElasticsearchClusterConfigTypeDef" = None,
        EBSOptions: "EBSOptionsTypeDef" = None,
        SnapshotOptions: "SnapshotOptionsTypeDef" = None,
        VPCOptions: VPCOptionsTypeDef = None,
        CognitoOptions: "CognitoOptionsTypeDef" = None,
        AdvancedOptions: Dict[str, str] = None,
        AccessPolicies: str = None,
        LogPublishingOptions: Dict[LogType, "LogPublishingOptionTypeDef"] = None,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
        AdvancedSecurityOptions: AdvancedSecurityOptionsInputTypeDef = None,
        NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = None,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
        AutoTuneOptions: "AutoTuneOptionsTypeDef" = None,
    ) -> UpdateElasticsearchDomainConfigResponseTypeDef:
        """
        [Client.update_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.update_elasticsearch_domain_config)
        """
    def update_package(
        self,
        PackageID: str,
        PackageSource: PackageSourceTypeDef,
        PackageDescription: str = None,
        CommitMessage: str = None,
    ) -> UpdatePackageResponseTypeDef:
        """
        [Client.update_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.update_package)
        """
    def upgrade_elasticsearch_domain(
        self, DomainName: str, TargetVersion: str, PerformCheckOnly: bool = None
    ) -> UpgradeElasticsearchDomainResponseTypeDef:
        """
        [Client.upgrade_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Client.upgrade_elasticsearch_domain)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeReservedElasticsearchInstanceOfferingsPaginatorName
    ) -> DescribeReservedElasticsearchInstanceOfferingsPaginator:
        """
        [Paginator.DescribeReservedElasticsearchInstanceOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeReservedElasticsearchInstancesPaginatorName
    ) -> DescribeReservedElasticsearchInstancesPaginator:
        """
        [Paginator.DescribeReservedElasticsearchInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)
        """
    @overload
    def get_paginator(
        self, operation_name: GetUpgradeHistoryPaginatorName
    ) -> GetUpgradeHistoryPaginator:
        """
        [Paginator.GetUpgradeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory)
        """
    @overload
    def get_paginator(
        self, operation_name: ListElasticsearchInstanceTypesPaginatorName
    ) -> ListElasticsearchInstanceTypesPaginator:
        """
        [Paginator.ListElasticsearchInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)
        """
    @overload
    def get_paginator(
        self, operation_name: ListElasticsearchVersionsPaginatorName
    ) -> ListElasticsearchVersionsPaginator:
        """
        [Paginator.ListElasticsearchVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions)
        """
