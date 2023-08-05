"""
Main interface for kinesis service type definitions.

Usage::

    ```python
    from mypy_boto3_kinesis.type_defs import ChildShardTypeDef

    data: ChildShardTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_kinesis.literals import (
    ConsumerStatus,
    EncryptionType,
    MetricsName,
    ShardFilterType,
    ShardIteratorType,
    StreamStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChildShardTypeDef",
    "ConsumerDescriptionTypeDef",
    "ConsumerTypeDef",
    "EnhancedMetricsTypeDef",
    "HashKeyRangeTypeDef",
    "InternalFailureExceptionTypeDef",
    "KMSAccessDeniedExceptionTypeDef",
    "KMSDisabledExceptionTypeDef",
    "KMSInvalidStateExceptionTypeDef",
    "KMSNotFoundExceptionTypeDef",
    "KMSOptInRequiredTypeDef",
    "KMSThrottlingExceptionTypeDef",
    "PutRecordsResultEntryTypeDef",
    "RecordTypeDef",
    "ResourceInUseExceptionTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "ResponseMetadata",
    "SequenceNumberRangeTypeDef",
    "ShardTypeDef",
    "StreamDescriptionSummaryTypeDef",
    "StreamDescriptionTypeDef",
    "SubscribeToShardEventStreamTypeDef",
    "SubscribeToShardEventTypeDef",
    "TagTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeStreamConsumerOutputTypeDef",
    "DescribeStreamOutputTypeDef",
    "DescribeStreamSummaryOutputTypeDef",
    "EnhancedMonitoringOutputTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorOutputTypeDef",
    "ListShardsOutputTypeDef",
    "ListStreamConsumersOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutRecordOutputTypeDef",
    "PutRecordsOutputTypeDef",
    "PutRecordsRequestEntryTypeDef",
    "RegisterStreamConsumerOutputTypeDef",
    "ShardFilterTypeDef",
    "StartingPositionTypeDef",
    "SubscribeToShardOutputTypeDef",
    "UpdateShardCountOutputTypeDef",
    "WaiterConfigTypeDef",
)

ChildShardTypeDef = TypedDict(
    "ChildShardTypeDef",
    {"ShardId": str, "ParentShards": List[str], "HashKeyRange": "HashKeyRangeTypeDef"},
)

ConsumerDescriptionTypeDef = TypedDict(
    "ConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatus,
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
)

ConsumerTypeDef = TypedDict(
    "ConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatus,
        "ConsumerCreationTimestamp": datetime,
    },
)

EnhancedMetricsTypeDef = TypedDict(
    "EnhancedMetricsTypeDef", {"ShardLevelMetrics": List[MetricsName]}, total=False
)

HashKeyRangeTypeDef = TypedDict(
    "HashKeyRangeTypeDef", {"StartingHashKey": str, "EndingHashKey": str}
)

InternalFailureExceptionTypeDef = TypedDict(
    "InternalFailureExceptionTypeDef", {"message": str}, total=False
)

KMSAccessDeniedExceptionTypeDef = TypedDict(
    "KMSAccessDeniedExceptionTypeDef", {"message": str}, total=False
)

KMSDisabledExceptionTypeDef = TypedDict(
    "KMSDisabledExceptionTypeDef", {"message": str}, total=False
)

KMSInvalidStateExceptionTypeDef = TypedDict(
    "KMSInvalidStateExceptionTypeDef", {"message": str}, total=False
)

KMSNotFoundExceptionTypeDef = TypedDict(
    "KMSNotFoundExceptionTypeDef", {"message": str}, total=False
)

KMSOptInRequiredTypeDef = TypedDict("KMSOptInRequiredTypeDef", {"message": str}, total=False)

KMSThrottlingExceptionTypeDef = TypedDict(
    "KMSThrottlingExceptionTypeDef", {"message": str}, total=False
)

PutRecordsResultEntryTypeDef = TypedDict(
    "PutRecordsResultEntryTypeDef",
    {"SequenceNumber": str, "ShardId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

_RequiredRecordTypeDef = TypedDict(
    "_RequiredRecordTypeDef",
    {"SequenceNumber": str, "Data": Union[bytes, IO[bytes]], "PartitionKey": str},
)
_OptionalRecordTypeDef = TypedDict(
    "_OptionalRecordTypeDef",
    {"ApproximateArrivalTimestamp": datetime, "EncryptionType": EncryptionType},
    total=False,
)


class RecordTypeDef(_RequiredRecordTypeDef, _OptionalRecordTypeDef):
    pass


ResourceInUseExceptionTypeDef = TypedDict(
    "ResourceInUseExceptionTypeDef", {"message": str}, total=False
)

ResourceNotFoundExceptionTypeDef = TypedDict(
    "ResourceNotFoundExceptionTypeDef", {"message": str}, total=False
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

_RequiredSequenceNumberRangeTypeDef = TypedDict(
    "_RequiredSequenceNumberRangeTypeDef", {"StartingSequenceNumber": str}
)
_OptionalSequenceNumberRangeTypeDef = TypedDict(
    "_OptionalSequenceNumberRangeTypeDef", {"EndingSequenceNumber": str}, total=False
)


class SequenceNumberRangeTypeDef(
    _RequiredSequenceNumberRangeTypeDef, _OptionalSequenceNumberRangeTypeDef
):
    pass


_RequiredShardTypeDef = TypedDict(
    "_RequiredShardTypeDef",
    {
        "ShardId": str,
        "HashKeyRange": "HashKeyRangeTypeDef",
        "SequenceNumberRange": "SequenceNumberRangeTypeDef",
    },
)
_OptionalShardTypeDef = TypedDict(
    "_OptionalShardTypeDef", {"ParentShardId": str, "AdjacentParentShardId": str}, total=False
)


class ShardTypeDef(_RequiredShardTypeDef, _OptionalShardTypeDef):
    pass


_RequiredStreamDescriptionSummaryTypeDef = TypedDict(
    "_RequiredStreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatus,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
        "OpenShardCount": int,
    },
)
_OptionalStreamDescriptionSummaryTypeDef = TypedDict(
    "_OptionalStreamDescriptionSummaryTypeDef",
    {"EncryptionType": EncryptionType, "KeyId": str, "ConsumerCount": int},
    total=False,
)


class StreamDescriptionSummaryTypeDef(
    _RequiredStreamDescriptionSummaryTypeDef, _OptionalStreamDescriptionSummaryTypeDef
):
    pass


_RequiredStreamDescriptionTypeDef = TypedDict(
    "_RequiredStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatus,
        "Shards": List["ShardTypeDef"],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
    },
)
_OptionalStreamDescriptionTypeDef = TypedDict(
    "_OptionalStreamDescriptionTypeDef",
    {"EncryptionType": EncryptionType, "KeyId": str},
    total=False,
)


class StreamDescriptionTypeDef(
    _RequiredStreamDescriptionTypeDef, _OptionalStreamDescriptionTypeDef
):
    pass


_RequiredSubscribeToShardEventStreamTypeDef = TypedDict(
    "_RequiredSubscribeToShardEventStreamTypeDef",
    {"SubscribeToShardEvent": "SubscribeToShardEventTypeDef"},
)
_OptionalSubscribeToShardEventStreamTypeDef = TypedDict(
    "_OptionalSubscribeToShardEventStreamTypeDef",
    {
        "ResourceNotFoundException": "ResourceNotFoundExceptionTypeDef",
        "ResourceInUseException": "ResourceInUseExceptionTypeDef",
        "KMSDisabledException": "KMSDisabledExceptionTypeDef",
        "KMSInvalidStateException": "KMSInvalidStateExceptionTypeDef",
        "KMSAccessDeniedException": "KMSAccessDeniedExceptionTypeDef",
        "KMSNotFoundException": "KMSNotFoundExceptionTypeDef",
        "KMSOptInRequired": "KMSOptInRequiredTypeDef",
        "KMSThrottlingException": "KMSThrottlingExceptionTypeDef",
        "InternalFailureException": "InternalFailureExceptionTypeDef",
    },
    total=False,
)


class SubscribeToShardEventStreamTypeDef(
    _RequiredSubscribeToShardEventStreamTypeDef, _OptionalSubscribeToShardEventStreamTypeDef
):
    pass


_RequiredSubscribeToShardEventTypeDef = TypedDict(
    "_RequiredSubscribeToShardEventTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "ContinuationSequenceNumber": str,
        "MillisBehindLatest": int,
    },
)
_OptionalSubscribeToShardEventTypeDef = TypedDict(
    "_OptionalSubscribeToShardEventTypeDef", {"ChildShards": List["ChildShardTypeDef"]}, total=False
)


class SubscribeToShardEventTypeDef(
    _RequiredSubscribeToShardEventTypeDef, _OptionalSubscribeToShardEventTypeDef
):
    pass


_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


_RequiredDescribeLimitsOutputTypeDef = TypedDict(
    "_RequiredDescribeLimitsOutputTypeDef", {"ShardLimit": int, "OpenShardCount": int}
)
_OptionalDescribeLimitsOutputTypeDef = TypedDict(
    "_OptionalDescribeLimitsOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DescribeLimitsOutputTypeDef(
    _RequiredDescribeLimitsOutputTypeDef, _OptionalDescribeLimitsOutputTypeDef
):
    pass


_RequiredDescribeStreamConsumerOutputTypeDef = TypedDict(
    "_RequiredDescribeStreamConsumerOutputTypeDef",
    {"ConsumerDescription": "ConsumerDescriptionTypeDef"},
)
_OptionalDescribeStreamConsumerOutputTypeDef = TypedDict(
    "_OptionalDescribeStreamConsumerOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeStreamConsumerOutputTypeDef(
    _RequiredDescribeStreamConsumerOutputTypeDef, _OptionalDescribeStreamConsumerOutputTypeDef
):
    pass


_RequiredDescribeStreamOutputTypeDef = TypedDict(
    "_RequiredDescribeStreamOutputTypeDef", {"StreamDescription": "StreamDescriptionTypeDef"}
)
_OptionalDescribeStreamOutputTypeDef = TypedDict(
    "_OptionalDescribeStreamOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DescribeStreamOutputTypeDef(
    _RequiredDescribeStreamOutputTypeDef, _OptionalDescribeStreamOutputTypeDef
):
    pass


_RequiredDescribeStreamSummaryOutputTypeDef = TypedDict(
    "_RequiredDescribeStreamSummaryOutputTypeDef",
    {"StreamDescriptionSummary": "StreamDescriptionSummaryTypeDef"},
)
_OptionalDescribeStreamSummaryOutputTypeDef = TypedDict(
    "_OptionalDescribeStreamSummaryOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeStreamSummaryOutputTypeDef(
    _RequiredDescribeStreamSummaryOutputTypeDef, _OptionalDescribeStreamSummaryOutputTypeDef
):
    pass


EnhancedMonitoringOutputTypeDef = TypedDict(
    "EnhancedMonitoringOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[MetricsName],
        "DesiredShardLevelMetrics": List[MetricsName],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredGetRecordsOutputTypeDef = TypedDict(
    "_RequiredGetRecordsOutputTypeDef", {"Records": List["RecordTypeDef"]}
)
_OptionalGetRecordsOutputTypeDef = TypedDict(
    "_OptionalGetRecordsOutputTypeDef",
    {
        "NextShardIterator": str,
        "MillisBehindLatest": int,
        "ChildShards": List["ChildShardTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class GetRecordsOutputTypeDef(_RequiredGetRecordsOutputTypeDef, _OptionalGetRecordsOutputTypeDef):
    pass


GetShardIteratorOutputTypeDef = TypedDict(
    "GetShardIteratorOutputTypeDef",
    {"ShardIterator": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListShardsOutputTypeDef = TypedDict(
    "ListShardsOutputTypeDef",
    {"Shards": List["ShardTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListStreamConsumersOutputTypeDef = TypedDict(
    "ListStreamConsumersOutputTypeDef",
    {
        "Consumers": List["ConsumerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredListStreamsOutputTypeDef = TypedDict(
    "_RequiredListStreamsOutputTypeDef", {"StreamNames": List[str], "HasMoreStreams": bool}
)
_OptionalListStreamsOutputTypeDef = TypedDict(
    "_OptionalListStreamsOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class ListStreamsOutputTypeDef(
    _RequiredListStreamsOutputTypeDef, _OptionalListStreamsOutputTypeDef
):
    pass


_RequiredListTagsForStreamOutputTypeDef = TypedDict(
    "_RequiredListTagsForStreamOutputTypeDef", {"Tags": List["TagTypeDef"], "HasMoreTags": bool}
)
_OptionalListTagsForStreamOutputTypeDef = TypedDict(
    "_OptionalListTagsForStreamOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class ListTagsForStreamOutputTypeDef(
    _RequiredListTagsForStreamOutputTypeDef, _OptionalListTagsForStreamOutputTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredPutRecordOutputTypeDef = TypedDict(
    "_RequiredPutRecordOutputTypeDef", {"ShardId": str, "SequenceNumber": str}
)
_OptionalPutRecordOutputTypeDef = TypedDict(
    "_OptionalPutRecordOutputTypeDef",
    {"EncryptionType": EncryptionType, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class PutRecordOutputTypeDef(_RequiredPutRecordOutputTypeDef, _OptionalPutRecordOutputTypeDef):
    pass


_RequiredPutRecordsOutputTypeDef = TypedDict(
    "_RequiredPutRecordsOutputTypeDef", {"Records": List["PutRecordsResultEntryTypeDef"]}
)
_OptionalPutRecordsOutputTypeDef = TypedDict(
    "_OptionalPutRecordsOutputTypeDef",
    {
        "FailedRecordCount": int,
        "EncryptionType": EncryptionType,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class PutRecordsOutputTypeDef(_RequiredPutRecordsOutputTypeDef, _OptionalPutRecordsOutputTypeDef):
    pass


_RequiredPutRecordsRequestEntryTypeDef = TypedDict(
    "_RequiredPutRecordsRequestEntryTypeDef", {"Data": Union[bytes, IO[bytes]], "PartitionKey": str}
)
_OptionalPutRecordsRequestEntryTypeDef = TypedDict(
    "_OptionalPutRecordsRequestEntryTypeDef", {"ExplicitHashKey": str}, total=False
)


class PutRecordsRequestEntryTypeDef(
    _RequiredPutRecordsRequestEntryTypeDef, _OptionalPutRecordsRequestEntryTypeDef
):
    pass


_RequiredRegisterStreamConsumerOutputTypeDef = TypedDict(
    "_RequiredRegisterStreamConsumerOutputTypeDef", {"Consumer": "ConsumerTypeDef"}
)
_OptionalRegisterStreamConsumerOutputTypeDef = TypedDict(
    "_OptionalRegisterStreamConsumerOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class RegisterStreamConsumerOutputTypeDef(
    _RequiredRegisterStreamConsumerOutputTypeDef, _OptionalRegisterStreamConsumerOutputTypeDef
):
    pass


_RequiredShardFilterTypeDef = TypedDict("_RequiredShardFilterTypeDef", {"Type": ShardFilterType})
_OptionalShardFilterTypeDef = TypedDict(
    "_OptionalShardFilterTypeDef", {"ShardId": str, "Timestamp": datetime}, total=False
)


class ShardFilterTypeDef(_RequiredShardFilterTypeDef, _OptionalShardFilterTypeDef):
    pass


_RequiredStartingPositionTypeDef = TypedDict(
    "_RequiredStartingPositionTypeDef", {"Type": ShardIteratorType}
)
_OptionalStartingPositionTypeDef = TypedDict(
    "_OptionalStartingPositionTypeDef", {"SequenceNumber": str, "Timestamp": datetime}, total=False
)


class StartingPositionTypeDef(_RequiredStartingPositionTypeDef, _OptionalStartingPositionTypeDef):
    pass


_RequiredSubscribeToShardOutputTypeDef = TypedDict(
    "_RequiredSubscribeToShardOutputTypeDef", {"EventStream": "SubscribeToShardEventStreamTypeDef"}
)
_OptionalSubscribeToShardOutputTypeDef = TypedDict(
    "_OptionalSubscribeToShardOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class SubscribeToShardOutputTypeDef(
    _RequiredSubscribeToShardOutputTypeDef, _OptionalSubscribeToShardOutputTypeDef
):
    pass


UpdateShardCountOutputTypeDef = TypedDict(
    "UpdateShardCountOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardCount": int,
        "TargetShardCount": int,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
