"""
Main interface for docdb service client

Usage::

    ```python
    import boto3
    from mypy_boto3_docdb import DocDBClient

    client: DocDBClient = boto3.client("docdb")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_docdb.literals import (
    DBInstanceAvailableWaiterName,
    DBInstanceDeletedWaiterName,
    DescribeCertificatesPaginatorName,
    DescribeDBClusterParameterGroupsPaginatorName,
    DescribeDBClusterParametersPaginatorName,
    DescribeDBClusterSnapshotsPaginatorName,
    DescribeDBClustersPaginatorName,
    DescribeDBEngineVersionsPaginatorName,
    DescribeDBInstancesPaginatorName,
    DescribeDBSubnetGroupsPaginatorName,
    DescribeEventsPaginatorName,
    DescribeEventSubscriptionsPaginatorName,
    DescribeOrderableDBInstanceOptionsPaginatorName,
    DescribePendingMaintenanceActionsPaginatorName,
    SourceType,
)
from mypy_boto3_docdb.paginator import (
    DescribeCertificatesPaginator,
    DescribeDBClusterParameterGroupsPaginator,
    DescribeDBClusterParametersPaginator,
    DescribeDBClusterSnapshotsPaginator,
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
    DescribePendingMaintenanceActionsPaginator,
)
from mypy_boto3_docdb.type_defs import (
    AddSourceIdentifierToSubscriptionResultTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    CertificateMessageTypeDef,
    CloudwatchLogsExportConfigurationTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionResultTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    FailoverDBClusterResultTypeDef,
    FilterTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    ParameterTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    RebootDBInstanceResultTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    StartDBClusterResultTypeDef,
    StopDBClusterResultTypeDef,
    TagListMessageTypeDef,
    TagTypeDef,
)
from mypy_boto3_docdb.waiter import DBInstanceAvailableWaiter, DBInstanceDeletedWaiter

__all__ = ("DocDBClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    CertificateNotFoundFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DBClusterAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterNotFoundFault: Type[BotocoreClientError]
    DBClusterParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBClusterQuotaExceededFault: Type[BotocoreClientError]
    DBClusterSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterSnapshotNotFoundFault: Type[BotocoreClientError]
    DBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSecurityGroupNotFoundFault: Type[BotocoreClientError]
    DBSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBSnapshotNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSubnetGroupDoesNotCoverEnoughAZs: Type[BotocoreClientError]
    DBSubnetGroupNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSubnetQuotaExceededFault: Type[BotocoreClientError]
    DBUpgradeDependencyFailureFault: Type[BotocoreClientError]
    EventSubscriptionQuotaExceededFault: Type[BotocoreClientError]
    InstanceQuotaExceededFault: Type[BotocoreClientError]
    InsufficientDBClusterCapacityFault: Type[BotocoreClientError]
    InsufficientDBInstanceCapacityFault: Type[BotocoreClientError]
    InsufficientStorageClusterCapacityFault: Type[BotocoreClientError]
    InvalidDBClusterSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBClusterStateFault: Type[BotocoreClientError]
    InvalidDBInstanceStateFault: Type[BotocoreClientError]
    InvalidDBParameterGroupStateFault: Type[BotocoreClientError]
    InvalidDBSecurityGroupStateFault: Type[BotocoreClientError]
    InvalidDBSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupStateFault: Type[BotocoreClientError]
    InvalidDBSubnetStateFault: Type[BotocoreClientError]
    InvalidEventSubscriptionStateFault: Type[BotocoreClientError]
    InvalidRestoreFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    KMSKeyNotAccessibleFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    SNSTopicArnNotFoundFault: Type[BotocoreClientError]
    SharedSnapshotQuotaExceededFault: Type[BotocoreClientError]
    SnapshotQuotaExceededFault: Type[BotocoreClientError]
    SourceNotFoundFault: Type[BotocoreClientError]
    StorageQuotaExceededFault: Type[BotocoreClientError]
    StorageTypeNotSupportedFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    SubscriptionAlreadyExistFault: Type[BotocoreClientError]
    SubscriptionCategoryNotFoundFault: Type[BotocoreClientError]
    SubscriptionNotFoundFault: Type[BotocoreClientError]

class DocDBClient:
    """
    [DocDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def add_source_identifier_to_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        [Client.add_source_identifier_to_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.add_source_identifier_to_subscription)
        """
    def add_tags_to_resource(self, ResourceName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.add_tags_to_resource)
        """
    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.apply_pending_maintenance_action)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.can_paginate)
        """
    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        [Client.copy_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.copy_db_cluster_parameter_group)
        """
    def copy_db_cluster_snapshot(
        self,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        CopyTags: bool = None,
        Tags: List["TagTypeDef"] = None,
        SourceRegion: str = None,
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        [Client.copy_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.copy_db_cluster_snapshot)
        """
    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        MasterUserPassword: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        Tags: List["TagTypeDef"] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
        SourceRegion: str = None,
    ) -> CreateDBClusterResultTypeDef:
        """
        [Client.create_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.create_db_cluster)
        """
    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        [Client.create_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.create_db_cluster_parameter_group)
        """
    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        [Client.create_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.create_db_cluster_snapshot)
        """
    def create_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBClusterIdentifier: str,
        AvailabilityZone: str = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List["TagTypeDef"] = None,
        PromotionTier: int = None,
    ) -> CreateDBInstanceResultTypeDef:
        """
        [Client.create_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.create_db_instance)
        """
    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        [Client.create_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.create_db_subnet_group)
        """
    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.create_event_subscription)
        """
    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> DeleteDBClusterResultTypeDef:
        """
        [Client.delete_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.delete_db_cluster)
        """
    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str) -> None:
        """
        [Client.delete_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.delete_db_cluster_parameter_group)
        """
    def delete_db_cluster_snapshot(
        self, DBClusterSnapshotIdentifier: str
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        [Client.delete_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.delete_db_cluster_snapshot)
        """
    def delete_db_instance(self, DBInstanceIdentifier: str) -> DeleteDBInstanceResultTypeDef:
        """
        [Client.delete_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.delete_db_instance)
        """
    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
        """
        [Client.delete_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.delete_db_subnet_group)
        """
    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.delete_event_subscription)
        """
    def describe_certificates(
        self,
        CertificateIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> CertificateMessageTypeDef:
        """
        [Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_certificates)
        """
    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        [Client.describe_db_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_db_cluster_parameter_groups)
        """
    def describe_db_cluster_parameters(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        [Client.describe_db_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_db_cluster_parameters)
        """
    def describe_db_cluster_snapshot_attributes(
        self, DBClusterSnapshotIdentifier: str
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        [Client.describe_db_cluster_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_db_cluster_snapshot_attributes)
        """
    def describe_db_cluster_snapshots(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        [Client.describe_db_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_db_cluster_snapshots)
        """
    def describe_db_clusters(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterMessageTypeDef:
        """
        [Client.describe_db_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_db_clusters)
        """
    def describe_db_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
    ) -> DBEngineVersionMessageTypeDef:
        """
        [Client.describe_db_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_db_engine_versions)
        """
    def describe_db_instances(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBInstanceMessageTypeDef:
        """
        [Client.describe_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_db_instances)
        """
    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBSubnetGroupMessageTypeDef:
        """
        [Client.describe_db_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_db_subnet_groups)
        """
    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        [Client.describe_engine_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_engine_default_cluster_parameters)
        """
    def describe_event_categories(
        self, SourceType: str = None, Filters: List[FilterTypeDef] = None
    ) -> EventCategoriesMessageTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_event_categories)
        """
    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventSubscriptionsMessageTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_event_subscriptions)
        """
    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: SourceType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventsMessageTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_events)
        """
    def describe_orderable_db_instance_options(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        [Client.describe_orderable_db_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_orderable_db_instance_options)
        """
    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.describe_pending_maintenance_actions)
        """
    def failover_db_cluster(
        self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None
    ) -> FailoverDBClusterResultTypeDef:
        """
        [Client.failover_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.failover_db_cluster)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.generate_presigned_url)
        """
    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[FilterTypeDef] = None
    ) -> TagListMessageTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.list_tags_for_resource)
        """
    def modify_db_cluster(
        self,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = None,
        ApplyImmediately: bool = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Port: int = None,
        MasterUserPassword: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
    ) -> ModifyDBClusterResultTypeDef:
        """
        [Client.modify_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.modify_db_cluster)
        """
    def modify_db_cluster_parameter_group(
        self, DBClusterParameterGroupName: str, Parameters: List["ParameterTypeDef"]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Client.modify_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.modify_db_cluster_parameter_group)
        """
    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        [Client.modify_db_cluster_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.modify_db_cluster_snapshot_attribute)
        """
    def modify_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str = None,
        ApplyImmediately: bool = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        NewDBInstanceIdentifier: str = None,
        CACertificateIdentifier: str = None,
        PromotionTier: int = None,
    ) -> ModifyDBInstanceResultTypeDef:
        """
        [Client.modify_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.modify_db_instance)
        """
    def modify_db_subnet_group(
        self, DBSubnetGroupName: str, SubnetIds: List[str], DBSubnetGroupDescription: str = None
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        [Client.modify_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.modify_db_subnet_group)
        """
    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None,
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.modify_event_subscription)
        """
    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> RebootDBInstanceResultTypeDef:
        """
        [Client.reboot_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.reboot_db_instance)
        """
    def remove_source_identifier_from_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        [Client.remove_source_identifier_from_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.remove_source_identifier_from_subscription)
        """
    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.remove_tags_from_resource)
        """
    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Client.reset_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.reset_db_cluster_parameter_group)
        """
    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        [Client.restore_db_cluster_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.restore_db_cluster_from_snapshot)
        """
    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreToTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        [Client.restore_db_cluster_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.restore_db_cluster_to_point_in_time)
        """
    def start_db_cluster(self, DBClusterIdentifier: str) -> StartDBClusterResultTypeDef:
        """
        [Client.start_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.start_db_cluster)
        """
    def stop_db_cluster(self, DBClusterIdentifier: str) -> StopDBClusterResultTypeDef:
        """
        [Client.stop_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Client.stop_db_cluster)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeCertificatesPaginatorName
    ) -> DescribeCertificatesPaginator:
        """
        [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeCertificates)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeDBClusterParameterGroupsPaginatorName
    ) -> DescribeDBClusterParameterGroupsPaginator:
        """
        [Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusterParameterGroups)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeDBClusterParametersPaginatorName
    ) -> DescribeDBClusterParametersPaginator:
        """
        [Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusterParameters)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeDBClusterSnapshotsPaginatorName
    ) -> DescribeDBClusterSnapshotsPaginator:
        """
        [Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusterSnapshots)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeDBClustersPaginatorName
    ) -> DescribeDBClustersPaginator:
        """
        [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusters)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeDBEngineVersionsPaginatorName
    ) -> DescribeDBEngineVersionsPaginator:
        """
        [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeDBEngineVersions)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeDBInstancesPaginatorName
    ) -> DescribeDBInstancesPaginator:
        """
        [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeDBInstances)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeDBSubnetGroupsPaginatorName
    ) -> DescribeDBSubnetGroupsPaginator:
        """
        [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeDBSubnetGroups)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeEventSubscriptionsPaginatorName
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeEventSubscriptions)
        """
    @overload
    def get_paginator(self, operation_name: DescribeEventsPaginatorName) -> DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeEvents)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeOrderableDBInstanceOptionsPaginatorName
    ) -> DescribeOrderableDBInstanceOptionsPaginator:
        """
        [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribePendingMaintenanceActionsPaginatorName
    ) -> DescribePendingMaintenanceActionsPaginator:
        """
        [Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Paginator.DescribePendingMaintenanceActions)
        """
    @overload
    def get_waiter(self, waiter_name: DBInstanceAvailableWaiterName) -> DBInstanceAvailableWaiter:
        """
        [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Waiter.DBInstanceAvailable)
        """
    @overload
    def get_waiter(self, waiter_name: DBInstanceDeletedWaiterName) -> DBInstanceDeletedWaiter:
        """
        [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/docdb.html#DocDB.Waiter.DBInstanceDeleted)
        """
