"""
Main interface for s3 service type definitions.

Usage::

    ```python
    from mypy_boto3_s3.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from mypy_boto3_s3.literals import (
    AnalyticsS3ExportFileFormat,
    ArchiveStatus,
    BucketAccelerateStatus,
    BucketLocationConstraint,
    BucketLogsPermission,
    BucketVersioningStatus,
    CompressionType,
    DeleteMarkerReplicationStatus,
    EncodingType,
    Event,
    ExistingObjectReplicationStatus,
    ExpirationStatus,
    ExpressionType,
    FileHeaderInfo,
    FilterRuleName,
    IntelligentTieringAccessTier,
    IntelligentTieringStatus,
    InventoryFormat,
    InventoryFrequency,
    InventoryIncludedObjectVersions,
    InventoryOptionalField,
    JSONType,
    MetricsStatus,
    MFADelete,
    MFADeleteStatus,
    ObjectCannedACL,
    ObjectLockEnabled,
    ObjectLockLegalHoldStatus,
    ObjectLockMode,
    ObjectLockRetentionMode,
    ObjectOwnership,
    ObjectStorageClass,
    ObjectVersionStorageClass,
    OwnerOverride,
    Payer,
    Permission,
    ProtocolType,
    QuoteFields,
    ReplicaModificationsStatus,
    ReplicationRuleStatus,
    ReplicationStatus,
    ReplicationTimeStatus,
    RequestCharged,
    RestoreRequestType,
    ServerSideEncryption,
    SseKmsEncryptedObjectsStatus,
    StorageClass,
    StorageClassAnalysisSchemaVersion,
    Tier,
    TransitionStorageClass,
    TypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AbortIncompleteMultipartUploadTypeDef",
    "AccessControlTranslationTypeDef",
    "AnalyticsAndOperatorTypeDef",
    "AnalyticsConfigurationTypeDef",
    "AnalyticsExportDestinationTypeDef",
    "AnalyticsFilterTypeDef",
    "AnalyticsS3BucketDestinationTypeDef",
    "BucketTypeDef",
    "CORSRuleTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "CloudFunctionConfigurationTypeDef",
    "CommonPrefixTypeDef",
    "CompletedPartTypeDef",
    "ConditionTypeDef",
    "CopyObjectResultTypeDef",
    "CopyPartResultTypeDef",
    "DefaultRetentionTypeDef",
    "DeleteMarkerEntryTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeletedObjectTypeDef",
    "DestinationTypeDef",
    "EncryptionConfigurationTypeDef",
    "EncryptionTypeDef",
    "ErrorDocumentTypeDef",
    "ErrorTypeDef",
    "ExistingObjectReplicationTypeDef",
    "FilterRuleTypeDef",
    "GlacierJobParametersTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "IndexDocumentTypeDef",
    "InitiatorTypeDef",
    "InputSerializationTypeDef",
    "IntelligentTieringAndOperatorTypeDef",
    "IntelligentTieringConfigurationTypeDef",
    "IntelligentTieringFilterTypeDef",
    "InventoryConfigurationTypeDef",
    "InventoryDestinationTypeDef",
    "InventoryEncryptionTypeDef",
    "InventoryFilterTypeDef",
    "InventoryS3BucketDestinationTypeDef",
    "InventoryScheduleTypeDef",
    "JSONInputTypeDef",
    "JSONOutputTypeDef",
    "LambdaFunctionConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "LoggingEnabledTypeDef",
    "MetadataEntryTypeDef",
    "MetricsAndOperatorTypeDef",
    "MetricsConfigurationTypeDef",
    "MetricsFilterTypeDef",
    "MetricsTypeDef",
    "MultipartUploadTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "NotificationConfigurationFilterTypeDef",
    "ObjectIdentifierTypeDef",
    "ObjectLockConfigurationTypeDef",
    "ObjectLockLegalHoldTypeDef",
    "ObjectLockRetentionTypeDef",
    "ObjectLockRuleTypeDef",
    "ObjectTypeDef",
    "ObjectVersionTypeDef",
    "OutputLocationTypeDef",
    "OutputSerializationTypeDef",
    "OwnerTypeDef",
    "OwnershipControlsRuleTypeDef",
    "OwnershipControlsTypeDef",
    "PartTypeDef",
    "PolicyStatusTypeDef",
    "ProgressEventTypeDef",
    "ProgressTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "QueueConfigurationDeprecatedTypeDef",
    "QueueConfigurationTypeDef",
    "RecordsEventTypeDef",
    "RedirectAllRequestsToTypeDef",
    "RedirectTypeDef",
    "ReplicaModificationsTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationRuleAndOperatorTypeDef",
    "ReplicationRuleFilterTypeDef",
    "ReplicationRuleTypeDef",
    "ReplicationTimeTypeDef",
    "ReplicationTimeValueTypeDef",
    "ResponseMetadata",
    "RoutingRuleTypeDef",
    "RuleTypeDef",
    "S3KeyFilterTypeDef",
    "S3LocationTypeDef",
    "SSEKMSTypeDef",
    "SelectObjectContentEventStreamTypeDef",
    "SelectParametersTypeDef",
    "ServerSideEncryptionByDefaultTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServerSideEncryptionRuleTypeDef",
    "SourceSelectionCriteriaTypeDef",
    "SseKmsEncryptedObjectsTypeDef",
    "StatsEventTypeDef",
    "StatsTypeDef",
    "StorageClassAnalysisDataExportTypeDef",
    "StorageClassAnalysisTypeDef",
    "TagTypeDef",
    "TaggingTypeDef",
    "TargetGrantTypeDef",
    "TieringTypeDef",
    "TopicConfigurationDeprecatedTypeDef",
    "TopicConfigurationTypeDef",
    "TransitionTypeDef",
    "AbortMultipartUploadOutputTypeDef",
    "AccelerateConfigurationTypeDef",
    "AccessControlPolicyTypeDef",
    "BucketLifecycleConfigurationTypeDef",
    "BucketLoggingStatusTypeDef",
    "CORSConfigurationTypeDef",
    "CompleteMultipartUploadOutputTypeDef",
    "CompletedMultipartUploadTypeDef",
    "CopyObjectOutputTypeDef",
    "CopySourceTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketOutputTypeDef",
    "CreateMultipartUploadOutputTypeDef",
    "DeleteObjectOutputTypeDef",
    "DeleteObjectTaggingOutputTypeDef",
    "DeleteObjectsOutputTypeDef",
    "DeleteTypeDef",
    "GetBucketAccelerateConfigurationOutputTypeDef",
    "GetBucketAclOutputTypeDef",
    "GetBucketAnalyticsConfigurationOutputTypeDef",
    "GetBucketCorsOutputTypeDef",
    "GetBucketEncryptionOutputTypeDef",
    "GetBucketIntelligentTieringConfigurationOutputTypeDef",
    "GetBucketInventoryConfigurationOutputTypeDef",
    "GetBucketLifecycleConfigurationOutputTypeDef",
    "GetBucketLifecycleOutputTypeDef",
    "GetBucketLocationOutputTypeDef",
    "GetBucketLoggingOutputTypeDef",
    "GetBucketMetricsConfigurationOutputTypeDef",
    "GetBucketOwnershipControlsOutputTypeDef",
    "GetBucketPolicyOutputTypeDef",
    "GetBucketPolicyStatusOutputTypeDef",
    "GetBucketReplicationOutputTypeDef",
    "GetBucketRequestPaymentOutputTypeDef",
    "GetBucketTaggingOutputTypeDef",
    "GetBucketVersioningOutputTypeDef",
    "GetBucketWebsiteOutputTypeDef",
    "GetObjectAclOutputTypeDef",
    "GetObjectLegalHoldOutputTypeDef",
    "GetObjectLockConfigurationOutputTypeDef",
    "GetObjectOutputTypeDef",
    "GetObjectRetentionOutputTypeDef",
    "GetObjectTaggingOutputTypeDef",
    "GetObjectTorrentOutputTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "HeadObjectOutputTypeDef",
    "LifecycleConfigurationTypeDef",
    "ListBucketAnalyticsConfigurationsOutputTypeDef",
    "ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    "ListBucketInventoryConfigurationsOutputTypeDef",
    "ListBucketMetricsConfigurationsOutputTypeDef",
    "ListBucketsOutputTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "ListObjectVersionsOutputTypeDef",
    "ListObjectsOutputTypeDef",
    "ListObjectsV2OutputTypeDef",
    "ListPartsOutputTypeDef",
    "NotificationConfigurationDeprecatedTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PutObjectAclOutputTypeDef",
    "PutObjectLegalHoldOutputTypeDef",
    "PutObjectLockConfigurationOutputTypeDef",
    "PutObjectOutputTypeDef",
    "PutObjectRetentionOutputTypeDef",
    "PutObjectTaggingOutputTypeDef",
    "RequestPaymentConfigurationTypeDef",
    "RequestProgressTypeDef",
    "RestoreObjectOutputTypeDef",
    "RestoreRequestTypeDef",
    "ScanRangeTypeDef",
    "SelectObjectContentOutputTypeDef",
    "UploadPartCopyOutputTypeDef",
    "UploadPartOutputTypeDef",
    "VersioningConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "WebsiteConfigurationTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef", {"DaysAfterInitiation": int}, total=False
)

AccessControlTranslationTypeDef = TypedDict(
    "AccessControlTranslationTypeDef", {"Owner": OwnerOverride}
)

AnalyticsAndOperatorTypeDef = TypedDict(
    "AnalyticsAndOperatorTypeDef", {"Prefix": str, "Tags": List["TagTypeDef"]}, total=False
)

_RequiredAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredAnalyticsConfigurationTypeDef",
    {"Id": str, "StorageClassAnalysis": "StorageClassAnalysisTypeDef"},
)
_OptionalAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalAnalyticsConfigurationTypeDef", {"Filter": "AnalyticsFilterTypeDef"}, total=False
)

class AnalyticsConfigurationTypeDef(
    _RequiredAnalyticsConfigurationTypeDef, _OptionalAnalyticsConfigurationTypeDef
):
    pass

AnalyticsExportDestinationTypeDef = TypedDict(
    "AnalyticsExportDestinationTypeDef",
    {"S3BucketDestination": "AnalyticsS3BucketDestinationTypeDef"},
)

AnalyticsFilterTypeDef = TypedDict(
    "AnalyticsFilterTypeDef",
    {"Prefix": str, "Tag": "TagTypeDef", "And": "AnalyticsAndOperatorTypeDef"},
    total=False,
)

_RequiredAnalyticsS3BucketDestinationTypeDef = TypedDict(
    "_RequiredAnalyticsS3BucketDestinationTypeDef",
    {"Format": AnalyticsS3ExportFileFormat, "Bucket": str},
)
_OptionalAnalyticsS3BucketDestinationTypeDef = TypedDict(
    "_OptionalAnalyticsS3BucketDestinationTypeDef",
    {"BucketAccountId": str, "Prefix": str},
    total=False,
)

class AnalyticsS3BucketDestinationTypeDef(
    _RequiredAnalyticsS3BucketDestinationTypeDef, _OptionalAnalyticsS3BucketDestinationTypeDef
):
    pass

BucketTypeDef = TypedDict("BucketTypeDef", {"Name": str, "CreationDate": datetime}, total=False)

_RequiredCORSRuleTypeDef = TypedDict(
    "_RequiredCORSRuleTypeDef", {"AllowedMethods": List[str], "AllowedOrigins": List[str]}
)
_OptionalCORSRuleTypeDef = TypedDict(
    "_OptionalCORSRuleTypeDef",
    {"ID": str, "AllowedHeaders": List[str], "ExposeHeaders": List[str], "MaxAgeSeconds": int},
    total=False,
)

class CORSRuleTypeDef(_RequiredCORSRuleTypeDef, _OptionalCORSRuleTypeDef):
    pass

CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": FileHeaderInfo,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)

CSVOutputTypeDef = TypedDict(
    "CSVOutputTypeDef",
    {
        "QuoteFields": QuoteFields,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CloudFunctionConfigurationTypeDef = TypedDict(
    "CloudFunctionConfigurationTypeDef",
    {"Id": str, "Event": Event, "Events": List[Event], "CloudFunction": str, "InvocationRole": str},
    total=False,
)

CommonPrefixTypeDef = TypedDict("CommonPrefixTypeDef", {"Prefix": str}, total=False)

CompletedPartTypeDef = TypedDict(
    "CompletedPartTypeDef", {"ETag": str, "PartNumber": int}, total=False
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef", {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str}, total=False
)

CopyObjectResultTypeDef = TypedDict(
    "CopyObjectResultTypeDef", {"ETag": str, "LastModified": datetime}, total=False
)

CopyPartResultTypeDef = TypedDict(
    "CopyPartResultTypeDef", {"ETag": str, "LastModified": datetime}, total=False
)

DefaultRetentionTypeDef = TypedDict(
    "DefaultRetentionTypeDef",
    {"Mode": ObjectLockRetentionMode, "Days": int, "Years": int},
    total=False,
)

DeleteMarkerEntryTypeDef = TypedDict(
    "DeleteMarkerEntryTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)

DeleteMarkerReplicationTypeDef = TypedDict(
    "DeleteMarkerReplicationTypeDef", {"Status": DeleteMarkerReplicationStatus}, total=False
)

DeletedObjectTypeDef = TypedDict(
    "DeletedObjectTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)

_RequiredDestinationTypeDef = TypedDict("_RequiredDestinationTypeDef", {"Bucket": str})
_OptionalDestinationTypeDef = TypedDict(
    "_OptionalDestinationTypeDef",
    {
        "Account": str,
        "StorageClass": StorageClass,
        "AccessControlTranslation": "AccessControlTranslationTypeDef",
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "ReplicationTime": "ReplicationTimeTypeDef",
        "Metrics": "MetricsTypeDef",
    },
    total=False,
)

class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef", {"ReplicaKmsKeyID": str}, total=False
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef", {"EncryptionType": ServerSideEncryption}
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef", {"KMSKeyId": str, "KMSContext": str}, total=False
)

class EncryptionTypeDef(_RequiredEncryptionTypeDef, _OptionalEncryptionTypeDef):
    pass

ErrorDocumentTypeDef = TypedDict("ErrorDocumentTypeDef", {"Key": str})

ErrorTypeDef = TypedDict(
    "ErrorTypeDef", {"Key": str, "VersionId": str, "Code": str, "Message": str}, total=False
)

ExistingObjectReplicationTypeDef = TypedDict(
    "ExistingObjectReplicationTypeDef", {"Status": ExistingObjectReplicationStatus}
)

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef", {"Name": FilterRuleName, "Value": str}, total=False
)

GlacierJobParametersTypeDef = TypedDict("GlacierJobParametersTypeDef", {"Tier": Tier})

GrantTypeDef = TypedDict(
    "GrantTypeDef", {"Grantee": "GranteeTypeDef", "Permission": Permission}, total=False
)

_RequiredGranteeTypeDef = TypedDict("_RequiredGranteeTypeDef", {"Type": TypeType})
_OptionalGranteeTypeDef = TypedDict(
    "_OptionalGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)

class GranteeTypeDef(_RequiredGranteeTypeDef, _OptionalGranteeTypeDef):
    pass

IndexDocumentTypeDef = TypedDict("IndexDocumentTypeDef", {"Suffix": str})

InitiatorTypeDef = TypedDict("InitiatorTypeDef", {"ID": str, "DisplayName": str}, total=False)

InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef",
    {
        "CSV": "CSVInputTypeDef",
        "CompressionType": CompressionType,
        "JSON": "JSONInputTypeDef",
        "Parquet": Dict[str, Any],
    },
    total=False,
)

IntelligentTieringAndOperatorTypeDef = TypedDict(
    "IntelligentTieringAndOperatorTypeDef", {"Prefix": str, "Tags": List["TagTypeDef"]}, total=False
)

_RequiredIntelligentTieringConfigurationTypeDef = TypedDict(
    "_RequiredIntelligentTieringConfigurationTypeDef",
    {"Id": str, "Status": IntelligentTieringStatus, "Tierings": List["TieringTypeDef"]},
)
_OptionalIntelligentTieringConfigurationTypeDef = TypedDict(
    "_OptionalIntelligentTieringConfigurationTypeDef",
    {"Filter": "IntelligentTieringFilterTypeDef"},
    total=False,
)

class IntelligentTieringConfigurationTypeDef(
    _RequiredIntelligentTieringConfigurationTypeDef, _OptionalIntelligentTieringConfigurationTypeDef
):
    pass

IntelligentTieringFilterTypeDef = TypedDict(
    "IntelligentTieringFilterTypeDef",
    {"Prefix": str, "Tag": "TagTypeDef", "And": "IntelligentTieringAndOperatorTypeDef"},
    total=False,
)

_RequiredInventoryConfigurationTypeDef = TypedDict(
    "_RequiredInventoryConfigurationTypeDef",
    {
        "Destination": "InventoryDestinationTypeDef",
        "IsEnabled": bool,
        "Id": str,
        "IncludedObjectVersions": InventoryIncludedObjectVersions,
        "Schedule": "InventoryScheduleTypeDef",
    },
)
_OptionalInventoryConfigurationTypeDef = TypedDict(
    "_OptionalInventoryConfigurationTypeDef",
    {"Filter": "InventoryFilterTypeDef", "OptionalFields": List[InventoryOptionalField]},
    total=False,
)

class InventoryConfigurationTypeDef(
    _RequiredInventoryConfigurationTypeDef, _OptionalInventoryConfigurationTypeDef
):
    pass

InventoryDestinationTypeDef = TypedDict(
    "InventoryDestinationTypeDef", {"S3BucketDestination": "InventoryS3BucketDestinationTypeDef"}
)

InventoryEncryptionTypeDef = TypedDict(
    "InventoryEncryptionTypeDef", {"SSES3": Dict[str, Any], "SSEKMS": "SSEKMSTypeDef"}, total=False
)

InventoryFilterTypeDef = TypedDict("InventoryFilterTypeDef", {"Prefix": str})

_RequiredInventoryS3BucketDestinationTypeDef = TypedDict(
    "_RequiredInventoryS3BucketDestinationTypeDef", {"Bucket": str, "Format": InventoryFormat}
)
_OptionalInventoryS3BucketDestinationTypeDef = TypedDict(
    "_OptionalInventoryS3BucketDestinationTypeDef",
    {"AccountId": str, "Prefix": str, "Encryption": "InventoryEncryptionTypeDef"},
    total=False,
)

class InventoryS3BucketDestinationTypeDef(
    _RequiredInventoryS3BucketDestinationTypeDef, _OptionalInventoryS3BucketDestinationTypeDef
):
    pass

InventoryScheduleTypeDef = TypedDict("InventoryScheduleTypeDef", {"Frequency": InventoryFrequency})

JSONInputTypeDef = TypedDict("JSONInputTypeDef", {"Type": JSONType}, total=False)

JSONOutputTypeDef = TypedDict(
    "JSONOutputTypeDef",
    {"RecordDelimiter": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredLambdaFunctionConfigurationTypeDef = TypedDict(
    "_RequiredLambdaFunctionConfigurationTypeDef", {"LambdaFunctionArn": str, "Events": List[Event]}
)
_OptionalLambdaFunctionConfigurationTypeDef = TypedDict(
    "_OptionalLambdaFunctionConfigurationTypeDef",
    {"Id": str, "Filter": "NotificationConfigurationFilterTypeDef"},
    total=False,
)

class LambdaFunctionConfigurationTypeDef(
    _RequiredLambdaFunctionConfigurationTypeDef, _OptionalLambdaFunctionConfigurationTypeDef
):
    pass

LifecycleExpirationTypeDef = TypedDict(
    "LifecycleExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

LifecycleRuleAndOperatorTypeDef = TypedDict(
    "LifecycleRuleAndOperatorTypeDef", {"Prefix": str, "Tags": List["TagTypeDef"]}, total=False
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {"Prefix": str, "Tag": "TagTypeDef", "And": "LifecycleRuleAndOperatorTypeDef"},
    total=False,
)

_RequiredLifecycleRuleTypeDef = TypedDict(
    "_RequiredLifecycleRuleTypeDef", {"Status": ExpirationStatus}
)
_OptionalLifecycleRuleTypeDef = TypedDict(
    "_OptionalLifecycleRuleTypeDef",
    {
        "Expiration": "LifecycleExpirationTypeDef",
        "ID": str,
        "Prefix": str,
        "Filter": "LifecycleRuleFilterTypeDef",
        "Transitions": List["TransitionTypeDef"],
        "NoncurrentVersionTransitions": List["NoncurrentVersionTransitionTypeDef"],
        "NoncurrentVersionExpiration": "NoncurrentVersionExpirationTypeDef",
        "AbortIncompleteMultipartUpload": "AbortIncompleteMultipartUploadTypeDef",
    },
    total=False,
)

class LifecycleRuleTypeDef(_RequiredLifecycleRuleTypeDef, _OptionalLifecycleRuleTypeDef):
    pass

_RequiredLoggingEnabledTypeDef = TypedDict(
    "_RequiredLoggingEnabledTypeDef", {"TargetBucket": str, "TargetPrefix": str}
)
_OptionalLoggingEnabledTypeDef = TypedDict(
    "_OptionalLoggingEnabledTypeDef", {"TargetGrants": List["TargetGrantTypeDef"]}, total=False
)

class LoggingEnabledTypeDef(_RequiredLoggingEnabledTypeDef, _OptionalLoggingEnabledTypeDef):
    pass

MetadataEntryTypeDef = TypedDict("MetadataEntryTypeDef", {"Name": str, "Value": str}, total=False)

MetricsAndOperatorTypeDef = TypedDict(
    "MetricsAndOperatorTypeDef", {"Prefix": str, "Tags": List["TagTypeDef"]}, total=False
)

_RequiredMetricsConfigurationTypeDef = TypedDict(
    "_RequiredMetricsConfigurationTypeDef", {"Id": str}
)
_OptionalMetricsConfigurationTypeDef = TypedDict(
    "_OptionalMetricsConfigurationTypeDef", {"Filter": "MetricsFilterTypeDef"}, total=False
)

class MetricsConfigurationTypeDef(
    _RequiredMetricsConfigurationTypeDef, _OptionalMetricsConfigurationTypeDef
):
    pass

MetricsFilterTypeDef = TypedDict(
    "MetricsFilterTypeDef",
    {"Prefix": str, "Tag": "TagTypeDef", "And": "MetricsAndOperatorTypeDef"},
    total=False,
)

_RequiredMetricsTypeDef = TypedDict("_RequiredMetricsTypeDef", {"Status": MetricsStatus})
_OptionalMetricsTypeDef = TypedDict(
    "_OptionalMetricsTypeDef", {"EventThreshold": "ReplicationTimeValueTypeDef"}, total=False
)

class MetricsTypeDef(_RequiredMetricsTypeDef, _OptionalMetricsTypeDef):
    pass

MultipartUploadTypeDef = TypedDict(
    "MultipartUploadTypeDef",
    {
        "UploadId": str,
        "Key": str,
        "Initiated": datetime,
        "StorageClass": StorageClass,
        "Owner": "OwnerTypeDef",
        "Initiator": "InitiatorTypeDef",
    },
    total=False,
)

NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef", {"NoncurrentDays": int}, total=False
)

NoncurrentVersionTransitionTypeDef = TypedDict(
    "NoncurrentVersionTransitionTypeDef",
    {"NoncurrentDays": int, "StorageClass": TransitionStorageClass},
    total=False,
)

NotificationConfigurationFilterTypeDef = TypedDict(
    "NotificationConfigurationFilterTypeDef", {"Key": "S3KeyFilterTypeDef"}, total=False
)

_RequiredObjectIdentifierTypeDef = TypedDict("_RequiredObjectIdentifierTypeDef", {"Key": str})
_OptionalObjectIdentifierTypeDef = TypedDict(
    "_OptionalObjectIdentifierTypeDef", {"VersionId": str}, total=False
)

class ObjectIdentifierTypeDef(_RequiredObjectIdentifierTypeDef, _OptionalObjectIdentifierTypeDef):
    pass

ObjectLockConfigurationTypeDef = TypedDict(
    "ObjectLockConfigurationTypeDef",
    {"ObjectLockEnabled": ObjectLockEnabled, "Rule": "ObjectLockRuleTypeDef"},
    total=False,
)

ObjectLockLegalHoldTypeDef = TypedDict(
    "ObjectLockLegalHoldTypeDef", {"Status": ObjectLockLegalHoldStatus}, total=False
)

ObjectLockRetentionTypeDef = TypedDict(
    "ObjectLockRetentionTypeDef",
    {"Mode": ObjectLockRetentionMode, "RetainUntilDate": datetime},
    total=False,
)

ObjectLockRuleTypeDef = TypedDict(
    "ObjectLockRuleTypeDef", {"DefaultRetention": "DefaultRetentionTypeDef"}, total=False
)

ObjectTypeDef = TypedDict(
    "ObjectTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": ObjectStorageClass,
        "Owner": "OwnerTypeDef",
    },
    total=False,
)

ObjectVersionTypeDef = TypedDict(
    "ObjectVersionTypeDef",
    {
        "ETag": str,
        "Size": int,
        "StorageClass": ObjectVersionStorageClass,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
        "Owner": "OwnerTypeDef",
    },
    total=False,
)

OutputLocationTypeDef = TypedDict("OutputLocationTypeDef", {"S3": "S3LocationTypeDef"}, total=False)

OutputSerializationTypeDef = TypedDict(
    "OutputSerializationTypeDef",
    {"CSV": "CSVOutputTypeDef", "JSON": "JSONOutputTypeDef"},
    total=False,
)

OwnerTypeDef = TypedDict("OwnerTypeDef", {"DisplayName": str, "ID": str}, total=False)

OwnershipControlsRuleTypeDef = TypedDict(
    "OwnershipControlsRuleTypeDef", {"ObjectOwnership": ObjectOwnership}
)

OwnershipControlsTypeDef = TypedDict(
    "OwnershipControlsTypeDef", {"Rules": List["OwnershipControlsRuleTypeDef"]}
)

PartTypeDef = TypedDict(
    "PartTypeDef",
    {"PartNumber": int, "LastModified": datetime, "ETag": str, "Size": int},
    total=False,
)

PolicyStatusTypeDef = TypedDict("PolicyStatusTypeDef", {"IsPublic": bool}, total=False)

ProgressEventTypeDef = TypedDict(
    "ProgressEventTypeDef", {"Details": "ProgressTypeDef"}, total=False
)

ProgressTypeDef = TypedDict(
    "ProgressTypeDef",
    {"BytesScanned": int, "BytesProcessed": int, "BytesReturned": int},
    total=False,
)

PublicAccessBlockConfigurationTypeDef = TypedDict(
    "PublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

QueueConfigurationDeprecatedTypeDef = TypedDict(
    "QueueConfigurationDeprecatedTypeDef",
    {"Id": str, "Event": Event, "Events": List[Event], "Queue": str},
    total=False,
)

_RequiredQueueConfigurationTypeDef = TypedDict(
    "_RequiredQueueConfigurationTypeDef", {"QueueArn": str, "Events": List[Event]}
)
_OptionalQueueConfigurationTypeDef = TypedDict(
    "_OptionalQueueConfigurationTypeDef",
    {"Id": str, "Filter": "NotificationConfigurationFilterTypeDef"},
    total=False,
)

class QueueConfigurationTypeDef(
    _RequiredQueueConfigurationTypeDef, _OptionalQueueConfigurationTypeDef
):
    pass

RecordsEventTypeDef = TypedDict(
    "RecordsEventTypeDef", {"Payload": Union[bytes, IO[bytes]]}, total=False
)

_RequiredRedirectAllRequestsToTypeDef = TypedDict(
    "_RequiredRedirectAllRequestsToTypeDef", {"HostName": str}
)
_OptionalRedirectAllRequestsToTypeDef = TypedDict(
    "_OptionalRedirectAllRequestsToTypeDef", {"Protocol": ProtocolType}, total=False
)

class RedirectAllRequestsToTypeDef(
    _RequiredRedirectAllRequestsToTypeDef, _OptionalRedirectAllRequestsToTypeDef
):
    pass

RedirectTypeDef = TypedDict(
    "RedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": ProtocolType,
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

ReplicaModificationsTypeDef = TypedDict(
    "ReplicaModificationsTypeDef", {"Status": ReplicaModificationsStatus}
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef", {"Role": str, "Rules": List["ReplicationRuleTypeDef"]}
)

ReplicationRuleAndOperatorTypeDef = TypedDict(
    "ReplicationRuleAndOperatorTypeDef", {"Prefix": str, "Tags": List["TagTypeDef"]}, total=False
)

ReplicationRuleFilterTypeDef = TypedDict(
    "ReplicationRuleFilterTypeDef",
    {"Prefix": str, "Tag": "TagTypeDef", "And": "ReplicationRuleAndOperatorTypeDef"},
    total=False,
)

_RequiredReplicationRuleTypeDef = TypedDict(
    "_RequiredReplicationRuleTypeDef",
    {"Status": ReplicationRuleStatus, "Destination": "DestinationTypeDef"},
)
_OptionalReplicationRuleTypeDef = TypedDict(
    "_OptionalReplicationRuleTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": "ReplicationRuleFilterTypeDef",
        "SourceSelectionCriteria": "SourceSelectionCriteriaTypeDef",
        "ExistingObjectReplication": "ExistingObjectReplicationTypeDef",
        "DeleteMarkerReplication": "DeleteMarkerReplicationTypeDef",
    },
    total=False,
)

class ReplicationRuleTypeDef(_RequiredReplicationRuleTypeDef, _OptionalReplicationRuleTypeDef):
    pass

ReplicationTimeTypeDef = TypedDict(
    "ReplicationTimeTypeDef",
    {"Status": ReplicationTimeStatus, "Time": "ReplicationTimeValueTypeDef"},
)

ReplicationTimeValueTypeDef = TypedDict(
    "ReplicationTimeValueTypeDef", {"Minutes": int}, total=False
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredRoutingRuleTypeDef = TypedDict(
    "_RequiredRoutingRuleTypeDef", {"Redirect": "RedirectTypeDef"}
)
_OptionalRoutingRuleTypeDef = TypedDict(
    "_OptionalRoutingRuleTypeDef", {"Condition": "ConditionTypeDef"}, total=False
)

class RoutingRuleTypeDef(_RequiredRoutingRuleTypeDef, _OptionalRoutingRuleTypeDef):
    pass

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef", {"Prefix": str, "Status": ExpirationStatus}
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Expiration": "LifecycleExpirationTypeDef",
        "ID": str,
        "Transition": "TransitionTypeDef",
        "NoncurrentVersionTransition": "NoncurrentVersionTransitionTypeDef",
        "NoncurrentVersionExpiration": "NoncurrentVersionExpirationTypeDef",
        "AbortIncompleteMultipartUpload": "AbortIncompleteMultipartUploadTypeDef",
    },
    total=False,
)

class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass

S3KeyFilterTypeDef = TypedDict(
    "S3KeyFilterTypeDef", {"FilterRules": List["FilterRuleTypeDef"]}, total=False
)

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef", {"BucketName": str, "Prefix": str}
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Encryption": "EncryptionTypeDef",
        "CannedACL": ObjectCannedACL,
        "AccessControlList": List["GrantTypeDef"],
        "Tagging": "TaggingTypeDef",
        "UserMetadata": List["MetadataEntryTypeDef"],
        "StorageClass": StorageClass,
    },
    total=False,
)

class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass

SSEKMSTypeDef = TypedDict("SSEKMSTypeDef", {"KeyId": str})

SelectObjectContentEventStreamTypeDef = TypedDict(
    "SelectObjectContentEventStreamTypeDef",
    {
        "Records": "RecordsEventTypeDef",
        "Stats": "StatsEventTypeDef",
        "Progress": "ProgressEventTypeDef",
        "Cont": Dict[str, Any],
        "End": Dict[str, Any],
    },
    total=False,
)

SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": "InputSerializationTypeDef",
        "ExpressionType": ExpressionType,
        "Expression": str,
        "OutputSerialization": "OutputSerializationTypeDef",
    },
)

_RequiredServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_RequiredServerSideEncryptionByDefaultTypeDef", {"SSEAlgorithm": ServerSideEncryption}
)
_OptionalServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_OptionalServerSideEncryptionByDefaultTypeDef", {"KMSMasterKeyID": str}, total=False
)

class ServerSideEncryptionByDefaultTypeDef(
    _RequiredServerSideEncryptionByDefaultTypeDef, _OptionalServerSideEncryptionByDefaultTypeDef
):
    pass

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef", {"Rules": List["ServerSideEncryptionRuleTypeDef"]}
)

ServerSideEncryptionRuleTypeDef = TypedDict(
    "ServerSideEncryptionRuleTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": "ServerSideEncryptionByDefaultTypeDef",
        "BucketKeyEnabled": bool,
    },
    total=False,
)

SourceSelectionCriteriaTypeDef = TypedDict(
    "SourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": "SseKmsEncryptedObjectsTypeDef",
        "ReplicaModifications": "ReplicaModificationsTypeDef",
    },
    total=False,
)

SseKmsEncryptedObjectsTypeDef = TypedDict(
    "SseKmsEncryptedObjectsTypeDef", {"Status": SseKmsEncryptedObjectsStatus}
)

StatsEventTypeDef = TypedDict("StatsEventTypeDef", {"Details": "StatsTypeDef"}, total=False)

StatsTypeDef = TypedDict(
    "StatsTypeDef", {"BytesScanned": int, "BytesProcessed": int, "BytesReturned": int}, total=False
)

StorageClassAnalysisDataExportTypeDef = TypedDict(
    "StorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": StorageClassAnalysisSchemaVersion,
        "Destination": "AnalyticsExportDestinationTypeDef",
    },
)

StorageClassAnalysisTypeDef = TypedDict(
    "StorageClassAnalysisTypeDef",
    {"DataExport": "StorageClassAnalysisDataExportTypeDef"},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TaggingTypeDef = TypedDict("TaggingTypeDef", {"TagSet": List["TagTypeDef"]})

TargetGrantTypeDef = TypedDict(
    "TargetGrantTypeDef",
    {"Grantee": "GranteeTypeDef", "Permission": BucketLogsPermission},
    total=False,
)

TieringTypeDef = TypedDict(
    "TieringTypeDef", {"Days": int, "AccessTier": IntelligentTieringAccessTier}
)

TopicConfigurationDeprecatedTypeDef = TypedDict(
    "TopicConfigurationDeprecatedTypeDef",
    {"Id": str, "Events": List[Event], "Event": Event, "Topic": str},
    total=False,
)

_RequiredTopicConfigurationTypeDef = TypedDict(
    "_RequiredTopicConfigurationTypeDef", {"TopicArn": str, "Events": List[Event]}
)
_OptionalTopicConfigurationTypeDef = TypedDict(
    "_OptionalTopicConfigurationTypeDef",
    {"Id": str, "Filter": "NotificationConfigurationFilterTypeDef"},
    total=False,
)

class TopicConfigurationTypeDef(
    _RequiredTopicConfigurationTypeDef, _OptionalTopicConfigurationTypeDef
):
    pass

TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {"Date": datetime, "Days": int, "StorageClass": TransitionStorageClass},
    total=False,
)

AbortMultipartUploadOutputTypeDef = TypedDict(
    "AbortMultipartUploadOutputTypeDef",
    {"RequestCharged": RequestCharged, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AccelerateConfigurationTypeDef = TypedDict(
    "AccelerateConfigurationTypeDef", {"Status": BucketAccelerateStatus}, total=False
)

AccessControlPolicyTypeDef = TypedDict(
    "AccessControlPolicyTypeDef",
    {"Grants": List["GrantTypeDef"], "Owner": "OwnerTypeDef"},
    total=False,
)

BucketLifecycleConfigurationTypeDef = TypedDict(
    "BucketLifecycleConfigurationTypeDef", {"Rules": List["LifecycleRuleTypeDef"]}
)

BucketLoggingStatusTypeDef = TypedDict(
    "BucketLoggingStatusTypeDef", {"LoggingEnabled": "LoggingEnabledTypeDef"}, total=False
)

CORSConfigurationTypeDef = TypedDict(
    "CORSConfigurationTypeDef", {"CORSRules": List["CORSRuleTypeDef"]}
)

CompleteMultipartUploadOutputTypeDef = TypedDict(
    "CompleteMultipartUploadOutputTypeDef",
    {
        "Location": str,
        "Bucket": str,
        "Key": str,
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": ServerSideEncryption,
        "VersionId": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CompletedMultipartUploadTypeDef = TypedDict(
    "CompletedMultipartUploadTypeDef", {"Parts": List["CompletedPartTypeDef"]}, total=False
)

CopyObjectOutputTypeDef = TypedDict(
    "CopyObjectOutputTypeDef",
    {
        "CopyObjectResult": "CopyObjectResultTypeDef",
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": ServerSideEncryption,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredCopySourceTypeDef = TypedDict("_RequiredCopySourceTypeDef", {"Bucket": str, "Key": str})
_OptionalCopySourceTypeDef = TypedDict(
    "_OptionalCopySourceTypeDef", {"VersionId": str}, total=False
)

class CopySourceTypeDef(_RequiredCopySourceTypeDef, _OptionalCopySourceTypeDef):
    pass

CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {"LocationConstraint": BucketLocationConstraint},
    total=False,
)

CreateBucketOutputTypeDef = TypedDict(
    "CreateBucketOutputTypeDef",
    {"Location": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateMultipartUploadOutputTypeDef = TypedDict(
    "CreateMultipartUploadOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "ServerSideEncryption": ServerSideEncryption,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DeleteObjectOutputTypeDef = TypedDict(
    "DeleteObjectOutputTypeDef",
    {
        "DeleteMarker": bool,
        "VersionId": str,
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DeleteObjectTaggingOutputTypeDef = TypedDict(
    "DeleteObjectTaggingOutputTypeDef",
    {"VersionId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteObjectsOutputTypeDef = TypedDict(
    "DeleteObjectsOutputTypeDef",
    {
        "Deleted": List["DeletedObjectTypeDef"],
        "RequestCharged": RequestCharged,
        "Errors": List["ErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredDeleteTypeDef = TypedDict(
    "_RequiredDeleteTypeDef", {"Objects": List["ObjectIdentifierTypeDef"]}
)
_OptionalDeleteTypeDef = TypedDict("_OptionalDeleteTypeDef", {"Quiet": bool}, total=False)

class DeleteTypeDef(_RequiredDeleteTypeDef, _OptionalDeleteTypeDef):
    pass

GetBucketAccelerateConfigurationOutputTypeDef = TypedDict(
    "GetBucketAccelerateConfigurationOutputTypeDef",
    {"Status": BucketAccelerateStatus, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketAclOutputTypeDef = TypedDict(
    "GetBucketAclOutputTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetBucketAnalyticsConfigurationOutputTypeDef = TypedDict(
    "GetBucketAnalyticsConfigurationOutputTypeDef",
    {
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetBucketCorsOutputTypeDef = TypedDict(
    "GetBucketCorsOutputTypeDef",
    {"CORSRules": List["CORSRuleTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketEncryptionOutputTypeDef = TypedDict(
    "GetBucketEncryptionOutputTypeDef",
    {
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetBucketIntelligentTieringConfigurationOutputTypeDef = TypedDict(
    "GetBucketIntelligentTieringConfigurationOutputTypeDef",
    {
        "IntelligentTieringConfiguration": "IntelligentTieringConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetBucketInventoryConfigurationOutputTypeDef = TypedDict(
    "GetBucketInventoryConfigurationOutputTypeDef",
    {
        "InventoryConfiguration": "InventoryConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetBucketLifecycleConfigurationOutputTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationOutputTypeDef",
    {"Rules": List["LifecycleRuleTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketLifecycleOutputTypeDef = TypedDict(
    "GetBucketLifecycleOutputTypeDef",
    {"Rules": List["RuleTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketLocationOutputTypeDef = TypedDict(
    "GetBucketLocationOutputTypeDef",
    {"LocationConstraint": BucketLocationConstraint, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketLoggingOutputTypeDef = TypedDict(
    "GetBucketLoggingOutputTypeDef",
    {"LoggingEnabled": "LoggingEnabledTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketMetricsConfigurationOutputTypeDef = TypedDict(
    "GetBucketMetricsConfigurationOutputTypeDef",
    {"MetricsConfiguration": "MetricsConfigurationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketOwnershipControlsOutputTypeDef = TypedDict(
    "GetBucketOwnershipControlsOutputTypeDef",
    {"OwnershipControls": "OwnershipControlsTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketPolicyOutputTypeDef = TypedDict(
    "GetBucketPolicyOutputTypeDef",
    {"Policy": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketPolicyStatusOutputTypeDef = TypedDict(
    "GetBucketPolicyStatusOutputTypeDef",
    {"PolicyStatus": "PolicyStatusTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetBucketReplicationOutputTypeDef = TypedDict(
    "GetBucketReplicationOutputTypeDef",
    {
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetBucketRequestPaymentOutputTypeDef = TypedDict(
    "GetBucketRequestPaymentOutputTypeDef",
    {"Payer": Payer, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredGetBucketTaggingOutputTypeDef = TypedDict(
    "_RequiredGetBucketTaggingOutputTypeDef", {"TagSet": List["TagTypeDef"]}
)
_OptionalGetBucketTaggingOutputTypeDef = TypedDict(
    "_OptionalGetBucketTaggingOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)

class GetBucketTaggingOutputTypeDef(
    _RequiredGetBucketTaggingOutputTypeDef, _OptionalGetBucketTaggingOutputTypeDef
):
    pass

GetBucketVersioningOutputTypeDef = TypedDict(
    "GetBucketVersioningOutputTypeDef",
    {
        "Status": BucketVersioningStatus,
        "MFADelete": MFADeleteStatus,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetBucketWebsiteOutputTypeDef = TypedDict(
    "GetBucketWebsiteOutputTypeDef",
    {
        "RedirectAllRequestsTo": "RedirectAllRequestsToTypeDef",
        "IndexDocument": "IndexDocumentTypeDef",
        "ErrorDocument": "ErrorDocumentTypeDef",
        "RoutingRules": List["RoutingRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetObjectAclOutputTypeDef = TypedDict(
    "GetObjectAclOutputTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetObjectLegalHoldOutputTypeDef = TypedDict(
    "GetObjectLegalHoldOutputTypeDef",
    {"LegalHold": "ObjectLockLegalHoldTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetObjectLockConfigurationOutputTypeDef = TypedDict(
    "GetObjectLockConfigurationOutputTypeDef",
    {
        "ObjectLockConfiguration": "ObjectLockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetObjectOutputTypeDef = TypedDict(
    "GetObjectOutputTypeDef",
    {
        "Body": StreamingBody,
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": ServerSideEncryption,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "StorageClass": StorageClass,
        "RequestCharged": RequestCharged,
        "ReplicationStatus": ReplicationStatus,
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": ObjectLockMode,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatus,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetObjectRetentionOutputTypeDef = TypedDict(
    "GetObjectRetentionOutputTypeDef",
    {"Retention": "ObjectLockRetentionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredGetObjectTaggingOutputTypeDef = TypedDict(
    "_RequiredGetObjectTaggingOutputTypeDef", {"TagSet": List["TagTypeDef"]}
)
_OptionalGetObjectTaggingOutputTypeDef = TypedDict(
    "_OptionalGetObjectTaggingOutputTypeDef",
    {"VersionId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

class GetObjectTaggingOutputTypeDef(
    _RequiredGetObjectTaggingOutputTypeDef, _OptionalGetObjectTaggingOutputTypeDef
):
    pass

GetObjectTorrentOutputTypeDef = TypedDict(
    "GetObjectTorrentOutputTypeDef",
    {
        "Body": StreamingBody,
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetPublicAccessBlockOutputTypeDef = TypedDict(
    "GetPublicAccessBlockOutputTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

HeadObjectOutputTypeDef = TypedDict(
    "HeadObjectOutputTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "ArchiveStatus": ArchiveStatus,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": ServerSideEncryption,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "StorageClass": StorageClass,
        "RequestCharged": RequestCharged,
        "ReplicationStatus": ReplicationStatus,
        "PartsCount": int,
        "ObjectLockMode": ObjectLockMode,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatus,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef", {"Rules": List["RuleTypeDef"]}
)

ListBucketAnalyticsConfigurationsOutputTypeDef = TypedDict(
    "ListBucketAnalyticsConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "AnalyticsConfigurationList": List["AnalyticsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListBucketIntelligentTieringConfigurationsOutputTypeDef = TypedDict(
    "ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "IntelligentTieringConfigurationList": List["IntelligentTieringConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListBucketInventoryConfigurationsOutputTypeDef = TypedDict(
    "ListBucketInventoryConfigurationsOutputTypeDef",
    {
        "ContinuationToken": str,
        "InventoryConfigurationList": List["InventoryConfigurationTypeDef"],
        "IsTruncated": bool,
        "NextContinuationToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListBucketMetricsConfigurationsOutputTypeDef = TypedDict(
    "ListBucketMetricsConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "MetricsConfigurationList": List["MetricsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListBucketsOutputTypeDef = TypedDict(
    "ListBucketsOutputTypeDef",
    {
        "Buckets": List["BucketTypeDef"],
        "Owner": "OwnerTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListMultipartUploadsOutputTypeDef = TypedDict(
    "ListMultipartUploadsOutputTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "NextKeyMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "NextUploadIdMarker": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List["MultipartUploadTypeDef"],
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": EncodingType,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListObjectVersionsOutputTypeDef = TypedDict(
    "ListObjectVersionsOutputTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "NextKeyMarker": str,
        "NextVersionIdMarker": str,
        "Versions": List["ObjectVersionTypeDef"],
        "DeleteMarkers": List["DeleteMarkerEntryTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": EncodingType,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListObjectsOutputTypeDef = TypedDict(
    "ListObjectsOutputTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List["ObjectTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": EncodingType,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListObjectsV2OutputTypeDef = TypedDict(
    "ListObjectsV2OutputTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List["ObjectTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": EncodingType,
        "KeyCount": int,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "StartAfter": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListPartsOutputTypeDef = TypedDict(
    "ListPartsOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "NextPartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List["PartTypeDef"],
        "Initiator": "InitiatorTypeDef",
        "Owner": "OwnerTypeDef",
        "StorageClass": StorageClass,
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

NotificationConfigurationDeprecatedTypeDef = TypedDict(
    "NotificationConfigurationDeprecatedTypeDef",
    {
        "TopicConfiguration": "TopicConfigurationDeprecatedTypeDef",
        "QueueConfiguration": "QueueConfigurationDeprecatedTypeDef",
        "CloudFunctionConfiguration": "CloudFunctionConfigurationTypeDef",
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicConfigurations": List["TopicConfigurationTypeDef"],
        "QueueConfigurations": List["QueueConfigurationTypeDef"],
        "LambdaFunctionConfigurations": List["LambdaFunctionConfigurationTypeDef"],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutObjectAclOutputTypeDef = TypedDict(
    "PutObjectAclOutputTypeDef",
    {"RequestCharged": RequestCharged, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PutObjectLegalHoldOutputTypeDef = TypedDict(
    "PutObjectLegalHoldOutputTypeDef",
    {"RequestCharged": RequestCharged, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PutObjectLockConfigurationOutputTypeDef = TypedDict(
    "PutObjectLockConfigurationOutputTypeDef",
    {"RequestCharged": RequestCharged, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PutObjectOutputTypeDef = TypedDict(
    "PutObjectOutputTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": ServerSideEncryption,
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PutObjectRetentionOutputTypeDef = TypedDict(
    "PutObjectRetentionOutputTypeDef",
    {"RequestCharged": RequestCharged, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PutObjectTaggingOutputTypeDef = TypedDict(
    "PutObjectTaggingOutputTypeDef",
    {"VersionId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

RequestPaymentConfigurationTypeDef = TypedDict(
    "RequestPaymentConfigurationTypeDef", {"Payer": Payer}
)

RequestProgressTypeDef = TypedDict("RequestProgressTypeDef", {"Enabled": bool}, total=False)

RestoreObjectOutputTypeDef = TypedDict(
    "RestoreObjectOutputTypeDef",
    {
        "RequestCharged": RequestCharged,
        "RestoreOutputPath": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

RestoreRequestTypeDef = TypedDict(
    "RestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": "GlacierJobParametersTypeDef",
        "Type": RestoreRequestType,
        "Tier": Tier,
        "Description": str,
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
    },
    total=False,
)

ScanRangeTypeDef = TypedDict("ScanRangeTypeDef", {"Start": int, "End": int}, total=False)

SelectObjectContentOutputTypeDef = TypedDict(
    "SelectObjectContentOutputTypeDef",
    {"Payload": "SelectObjectContentEventStreamTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UploadPartCopyOutputTypeDef = TypedDict(
    "UploadPartCopyOutputTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": "CopyPartResultTypeDef",
        "ServerSideEncryption": ServerSideEncryption,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UploadPartOutputTypeDef = TypedDict(
    "UploadPartOutputTypeDef",
    {
        "ServerSideEncryption": ServerSideEncryption,
        "ETag": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": RequestCharged,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {"MFADelete": MFADelete, "Status": BucketVersioningStatus},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

WebsiteConfigurationTypeDef = TypedDict(
    "WebsiteConfigurationTypeDef",
    {
        "ErrorDocument": "ErrorDocumentTypeDef",
        "IndexDocument": "IndexDocumentTypeDef",
        "RedirectAllRequestsTo": "RedirectAllRequestsToTypeDef",
        "RoutingRules": List["RoutingRuleTypeDef"],
    },
    total=False,
)
