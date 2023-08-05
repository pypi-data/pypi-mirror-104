"""
Main interface for workspaces service type definitions.

Usage::

    ```python
    from mypy_boto3_workspaces.type_defs import AccountModificationTypeDef

    data: AccountModificationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_workspaces.literals import (
    AccessPropertyValue,
    AssociationStatus,
    Compute,
    ConnectionAliasState,
    ConnectionState,
    DedicatedTenancyModificationStateEnum,
    DedicatedTenancySupportResultEnum,
    ModificationResourceEnum,
    ModificationStateEnum,
    OperatingSystemType,
    ReconnectEnum,
    RunningMode,
    Tenancy,
    WorkspaceDirectoryState,
    WorkspaceDirectoryType,
    WorkspaceImageRequiredTenancy,
    WorkspaceImageState,
    WorkspaceState,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountModificationTypeDef",
    "ClientPropertiesResultTypeDef",
    "ClientPropertiesTypeDef",
    "ComputeTypeTypeDef",
    "ConnectionAliasAssociationTypeDef",
    "ConnectionAliasPermissionTypeDef",
    "ConnectionAliasTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "FailedCreateWorkspaceRequestTypeDef",
    "FailedWorkspaceChangeRequestTypeDef",
    "ImagePermissionTypeDef",
    "IpRuleItemTypeDef",
    "ModificationStateTypeDef",
    "OperatingSystemTypeDef",
    "RootStorageTypeDef",
    "SelfservicePermissionsTypeDef",
    "SnapshotTypeDef",
    "TagTypeDef",
    "UserStorageTypeDef",
    "WorkspaceAccessPropertiesTypeDef",
    "WorkspaceBundleTypeDef",
    "WorkspaceConnectionStatusTypeDef",
    "WorkspaceDirectoryTypeDef",
    "WorkspaceImageTypeDef",
    "WorkspacePropertiesTypeDef",
    "WorkspaceRequestTypeDef",
    "WorkspaceTypeDef",
    "WorkspacesIpGroupTypeDef",
    "AssociateConnectionAliasResultTypeDef",
    "CopyWorkspaceImageResultTypeDef",
    "CreateConnectionAliasResultTypeDef",
    "CreateIpGroupResultTypeDef",
    "CreateWorkspaceBundleResultTypeDef",
    "CreateWorkspacesResultTypeDef",
    "DescribeAccountModificationsResultTypeDef",
    "DescribeAccountResultTypeDef",
    "DescribeClientPropertiesResultTypeDef",
    "DescribeConnectionAliasPermissionsResultTypeDef",
    "DescribeConnectionAliasesResultTypeDef",
    "DescribeIpGroupsResultTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeWorkspaceBundlesResultTypeDef",
    "DescribeWorkspaceDirectoriesResultTypeDef",
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    "DescribeWorkspaceImagesResultTypeDef",
    "DescribeWorkspaceSnapshotsResultTypeDef",
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    "DescribeWorkspacesResultTypeDef",
    "ImportWorkspaceImageResultTypeDef",
    "ListAvailableManagementCidrRangesResultTypeDef",
    "MigrateWorkspaceResultTypeDef",
    "PaginatorConfigTypeDef",
    "RebootRequestTypeDef",
    "RebootWorkspacesResultTypeDef",
    "RebuildRequestTypeDef",
    "RebuildWorkspacesResultTypeDef",
    "StartRequestTypeDef",
    "StartWorkspacesResultTypeDef",
    "StopRequestTypeDef",
    "StopWorkspacesResultTypeDef",
    "TerminateRequestTypeDef",
    "TerminateWorkspacesResultTypeDef",
    "WorkspaceCreationPropertiesTypeDef",
)

AccountModificationTypeDef = TypedDict(
    "AccountModificationTypeDef",
    {
        "ModificationState": DedicatedTenancyModificationStateEnum,
        "DedicatedTenancySupport": DedicatedTenancySupportResultEnum,
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientPropertiesResultTypeDef = TypedDict(
    "ClientPropertiesResultTypeDef",
    {"ResourceId": str, "ClientProperties": "ClientPropertiesTypeDef"},
    total=False,
)

ClientPropertiesTypeDef = TypedDict(
    "ClientPropertiesTypeDef", {"ReconnectEnabled": ReconnectEnum}, total=False
)

ComputeTypeTypeDef = TypedDict("ComputeTypeTypeDef", {"Name": Compute}, total=False)

ConnectionAliasAssociationTypeDef = TypedDict(
    "ConnectionAliasAssociationTypeDef",
    {
        "AssociationStatus": AssociationStatus,
        "AssociatedAccountId": str,
        "ResourceId": str,
        "ConnectionIdentifier": str,
    },
    total=False,
)

ConnectionAliasPermissionTypeDef = TypedDict(
    "ConnectionAliasPermissionTypeDef", {"SharedAccountId": str, "AllowAssociation": bool}
)

ConnectionAliasTypeDef = TypedDict(
    "ConnectionAliasTypeDef",
    {
        "ConnectionString": str,
        "AliasId": str,
        "State": ConnectionAliasState,
        "OwnerAccountId": str,
        "Associations": List["ConnectionAliasAssociationTypeDef"],
    },
    total=False,
)

DefaultWorkspaceCreationPropertiesTypeDef = TypedDict(
    "DefaultWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)

FailedCreateWorkspaceRequestTypeDef = TypedDict(
    "FailedCreateWorkspaceRequestTypeDef",
    {"WorkspaceRequest": "WorkspaceRequestTypeDef", "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

FailedWorkspaceChangeRequestTypeDef = TypedDict(
    "FailedWorkspaceChangeRequestTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ImagePermissionTypeDef = TypedDict("ImagePermissionTypeDef", {"SharedAccountId": str}, total=False)

IpRuleItemTypeDef = TypedDict("IpRuleItemTypeDef", {"ipRule": str, "ruleDesc": str}, total=False)

ModificationStateTypeDef = TypedDict(
    "ModificationStateTypeDef",
    {"Resource": ModificationResourceEnum, "State": ModificationStateEnum},
    total=False,
)

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef", {"Type": OperatingSystemType}, total=False
)

RootStorageTypeDef = TypedDict("RootStorageTypeDef", {"Capacity": str}, total=False)

SelfservicePermissionsTypeDef = TypedDict(
    "SelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": ReconnectEnum,
        "IncreaseVolumeSize": ReconnectEnum,
        "ChangeComputeType": ReconnectEnum,
        "SwitchRunningMode": ReconnectEnum,
        "RebuildWorkspace": ReconnectEnum,
    },
    total=False,
)

SnapshotTypeDef = TypedDict("SnapshotTypeDef", {"SnapshotTime": datetime}, total=False)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


UserStorageTypeDef = TypedDict("UserStorageTypeDef", {"Capacity": str}, total=False)

WorkspaceAccessPropertiesTypeDef = TypedDict(
    "WorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": AccessPropertyValue,
        "DeviceTypeOsx": AccessPropertyValue,
        "DeviceTypeWeb": AccessPropertyValue,
        "DeviceTypeIos": AccessPropertyValue,
        "DeviceTypeAndroid": AccessPropertyValue,
        "DeviceTypeChromeOs": AccessPropertyValue,
        "DeviceTypeZeroClient": AccessPropertyValue,
    },
    total=False,
)

WorkspaceBundleTypeDef = TypedDict(
    "WorkspaceBundleTypeDef",
    {
        "BundleId": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "ImageId": str,
        "RootStorage": "RootStorageTypeDef",
        "UserStorage": "UserStorageTypeDef",
        "ComputeType": "ComputeTypeTypeDef",
        "LastUpdatedTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)

WorkspaceConnectionStatusTypeDef = TypedDict(
    "WorkspaceConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": ConnectionState,
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
    total=False,
)

WorkspaceDirectoryTypeDef = TypedDict(
    "WorkspaceDirectoryTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "DirectoryName": str,
        "RegistrationCode": str,
        "SubnetIds": List[str],
        "DnsIpAddresses": List[str],
        "CustomerUserName": str,
        "IamRoleId": str,
        "DirectoryType": WorkspaceDirectoryType,
        "WorkspaceSecurityGroupId": str,
        "State": WorkspaceDirectoryState,
        "WorkspaceCreationProperties": "DefaultWorkspaceCreationPropertiesTypeDef",
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": "WorkspaceAccessPropertiesTypeDef",
        "Tenancy": Tenancy,
        "SelfservicePermissions": "SelfservicePermissionsTypeDef",
    },
    total=False,
)

WorkspaceImageTypeDef = TypedDict(
    "WorkspaceImageTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": "OperatingSystemTypeDef",
        "State": WorkspaceImageState,
        "RequiredTenancy": WorkspaceImageRequiredTenancy,
        "ErrorCode": str,
        "ErrorMessage": str,
        "Created": datetime,
        "OwnerAccountId": str,
    },
    total=False,
)

WorkspacePropertiesTypeDef = TypedDict(
    "WorkspacePropertiesTypeDef",
    {
        "RunningMode": RunningMode,
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Compute,
    },
    total=False,
)

_RequiredWorkspaceRequestTypeDef = TypedDict(
    "_RequiredWorkspaceRequestTypeDef", {"DirectoryId": str, "UserName": str, "BundleId": str}
)
_OptionalWorkspaceRequestTypeDef = TypedDict(
    "_OptionalWorkspaceRequestTypeDef",
    {
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class WorkspaceRequestTypeDef(_RequiredWorkspaceRequestTypeDef, _OptionalWorkspaceRequestTypeDef):
    pass


WorkspaceTypeDef = TypedDict(
    "WorkspaceTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": WorkspaceState,
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
        "ModificationStates": List["ModificationStateTypeDef"],
    },
    total=False,
)

WorkspacesIpGroupTypeDef = TypedDict(
    "WorkspacesIpGroupTypeDef",
    {"groupId": str, "groupName": str, "groupDesc": str, "userRules": List["IpRuleItemTypeDef"]},
    total=False,
)

AssociateConnectionAliasResultTypeDef = TypedDict(
    "AssociateConnectionAliasResultTypeDef", {"ConnectionIdentifier": str}, total=False
)

CopyWorkspaceImageResultTypeDef = TypedDict(
    "CopyWorkspaceImageResultTypeDef", {"ImageId": str}, total=False
)

CreateConnectionAliasResultTypeDef = TypedDict(
    "CreateConnectionAliasResultTypeDef", {"AliasId": str}, total=False
)

CreateIpGroupResultTypeDef = TypedDict("CreateIpGroupResultTypeDef", {"GroupId": str}, total=False)

CreateWorkspaceBundleResultTypeDef = TypedDict(
    "CreateWorkspaceBundleResultTypeDef", {"WorkspaceBundle": "WorkspaceBundleTypeDef"}, total=False
)

CreateWorkspacesResultTypeDef = TypedDict(
    "CreateWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedCreateWorkspaceRequestTypeDef"],
        "PendingRequests": List["WorkspaceTypeDef"],
    },
    total=False,
)

DescribeAccountModificationsResultTypeDef = TypedDict(
    "DescribeAccountModificationsResultTypeDef",
    {"AccountModifications": List["AccountModificationTypeDef"], "NextToken": str},
    total=False,
)

DescribeAccountResultTypeDef = TypedDict(
    "DescribeAccountResultTypeDef",
    {
        "DedicatedTenancySupport": DedicatedTenancySupportResultEnum,
        "DedicatedTenancyManagementCidrRange": str,
    },
    total=False,
)

DescribeClientPropertiesResultTypeDef = TypedDict(
    "DescribeClientPropertiesResultTypeDef",
    {"ClientPropertiesList": List["ClientPropertiesResultTypeDef"]},
    total=False,
)

DescribeConnectionAliasPermissionsResultTypeDef = TypedDict(
    "DescribeConnectionAliasPermissionsResultTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermissions": List["ConnectionAliasPermissionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeConnectionAliasesResultTypeDef = TypedDict(
    "DescribeConnectionAliasesResultTypeDef",
    {"ConnectionAliases": List["ConnectionAliasTypeDef"], "NextToken": str},
    total=False,
)

DescribeIpGroupsResultTypeDef = TypedDict(
    "DescribeIpGroupsResultTypeDef",
    {"Result": List["WorkspacesIpGroupTypeDef"], "NextToken": str},
    total=False,
)

DescribeTagsResultTypeDef = TypedDict(
    "DescribeTagsResultTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

DescribeWorkspaceBundlesResultTypeDef = TypedDict(
    "DescribeWorkspaceBundlesResultTypeDef",
    {"Bundles": List["WorkspaceBundleTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspaceDirectoriesResultTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesResultTypeDef",
    {"Directories": List["WorkspaceDirectoryTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspaceImagePermissionsResultTypeDef = TypedDict(
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    {"ImageId": str, "ImagePermissions": List["ImagePermissionTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspaceImagesResultTypeDef = TypedDict(
    "DescribeWorkspaceImagesResultTypeDef",
    {"Images": List["WorkspaceImageTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspaceSnapshotsResultTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsResultTypeDef",
    {"RebuildSnapshots": List["SnapshotTypeDef"], "RestoreSnapshots": List["SnapshotTypeDef"]},
    total=False,
)

DescribeWorkspacesConnectionStatusResultTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    {"WorkspacesConnectionStatus": List["WorkspaceConnectionStatusTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspacesResultTypeDef = TypedDict(
    "DescribeWorkspacesResultTypeDef",
    {"Workspaces": List["WorkspaceTypeDef"], "NextToken": str},
    total=False,
)

ImportWorkspaceImageResultTypeDef = TypedDict(
    "ImportWorkspaceImageResultTypeDef", {"ImageId": str}, total=False
)

ListAvailableManagementCidrRangesResultTypeDef = TypedDict(
    "ListAvailableManagementCidrRangesResultTypeDef",
    {"ManagementCidrRanges": List[str], "NextToken": str},
    total=False,
)

MigrateWorkspaceResultTypeDef = TypedDict(
    "MigrateWorkspaceResultTypeDef",
    {"SourceWorkspaceId": str, "TargetWorkspaceId": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RebootRequestTypeDef = TypedDict("RebootRequestTypeDef", {"WorkspaceId": str})

RebootWorkspacesResultTypeDef = TypedDict(
    "RebootWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

RebuildRequestTypeDef = TypedDict("RebuildRequestTypeDef", {"WorkspaceId": str})

RebuildWorkspacesResultTypeDef = TypedDict(
    "RebuildWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

StartRequestTypeDef = TypedDict("StartRequestTypeDef", {"WorkspaceId": str}, total=False)

StartWorkspacesResultTypeDef = TypedDict(
    "StartWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

StopRequestTypeDef = TypedDict("StopRequestTypeDef", {"WorkspaceId": str}, total=False)

StopWorkspacesResultTypeDef = TypedDict(
    "StopWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

TerminateRequestTypeDef = TypedDict("TerminateRequestTypeDef", {"WorkspaceId": str})

TerminateWorkspacesResultTypeDef = TypedDict(
    "TerminateWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

WorkspaceCreationPropertiesTypeDef = TypedDict(
    "WorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)
