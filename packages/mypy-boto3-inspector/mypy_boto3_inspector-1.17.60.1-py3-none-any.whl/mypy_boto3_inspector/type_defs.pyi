"""
Main interface for inspector service type definitions.

Usage::

    ```python
    from mypy_boto3_inspector.type_defs import AgentPreviewTypeDef

    data: AgentPreviewTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_inspector.literals import (
    AgentHealth,
    AgentHealthCode,
    AssessmentRunNotificationSnsStatusCode,
    AssessmentRunState,
    AssetType,
    FailedItemErrorCode,
    InspectorEvent,
    PreviewStatus,
    ReportStatus,
    ScopeType,
    Severity,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AgentPreviewTypeDef",
    "AssessmentRunAgentTypeDef",
    "AssessmentRunNotificationTypeDef",
    "AssessmentRunStateChangeTypeDef",
    "AssessmentRunTypeDef",
    "AssessmentTargetTypeDef",
    "AssessmentTemplateTypeDef",
    "AssetAttributesTypeDef",
    "AttributeTypeDef",
    "DurationRangeTypeDef",
    "EventSubscriptionTypeDef",
    "ExclusionPreviewTypeDef",
    "ExclusionTypeDef",
    "FailedItemDetailsTypeDef",
    "FindingTypeDef",
    "InspectorServiceAttributesTypeDef",
    "NetworkInterfaceTypeDef",
    "PrivateIpTypeDef",
    "ResourceGroupTagTypeDef",
    "ResourceGroupTypeDef",
    "RulesPackageTypeDef",
    "ScopeTypeDef",
    "SecurityGroupTypeDef",
    "SubscriptionTypeDef",
    "TagTypeDef",
    "TelemetryMetadataTypeDef",
    "TimestampRangeTypeDef",
    "AddAttributesToFindingsResponseTypeDef",
    "AgentFilterTypeDef",
    "AssessmentRunFilterTypeDef",
    "AssessmentTargetFilterTypeDef",
    "AssessmentTemplateFilterTypeDef",
    "CreateAssessmentTargetResponseTypeDef",
    "CreateAssessmentTemplateResponseTypeDef",
    "CreateExclusionsPreviewResponseTypeDef",
    "CreateResourceGroupResponseTypeDef",
    "DescribeAssessmentRunsResponseTypeDef",
    "DescribeAssessmentTargetsResponseTypeDef",
    "DescribeAssessmentTemplatesResponseTypeDef",
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    "DescribeExclusionsResponseTypeDef",
    "DescribeFindingsResponseTypeDef",
    "DescribeResourceGroupsResponseTypeDef",
    "DescribeRulesPackagesResponseTypeDef",
    "FindingFilterTypeDef",
    "GetAssessmentReportResponseTypeDef",
    "GetExclusionsPreviewResponseTypeDef",
    "GetTelemetryMetadataResponseTypeDef",
    "ListAssessmentRunAgentsResponseTypeDef",
    "ListAssessmentRunsResponseTypeDef",
    "ListAssessmentTargetsResponseTypeDef",
    "ListAssessmentTemplatesResponseTypeDef",
    "ListEventSubscriptionsResponseTypeDef",
    "ListExclusionsResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListRulesPackagesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PreviewAgentsResponseTypeDef",
    "RemoveAttributesFromFindingsResponseTypeDef",
    "StartAssessmentRunResponseTypeDef",
)

_RequiredAgentPreviewTypeDef = TypedDict("_RequiredAgentPreviewTypeDef", {"agentId": str})
_OptionalAgentPreviewTypeDef = TypedDict(
    "_OptionalAgentPreviewTypeDef",
    {
        "hostname": str,
        "autoScalingGroup": str,
        "agentHealth": AgentHealth,
        "agentVersion": str,
        "operatingSystem": str,
        "kernelVersion": str,
        "ipv4Address": str,
    },
    total=False,
)

class AgentPreviewTypeDef(_RequiredAgentPreviewTypeDef, _OptionalAgentPreviewTypeDef):
    pass

_RequiredAssessmentRunAgentTypeDef = TypedDict(
    "_RequiredAssessmentRunAgentTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": AgentHealth,
        "agentHealthCode": AgentHealthCode,
        "telemetryMetadata": List["TelemetryMetadataTypeDef"],
    },
)
_OptionalAssessmentRunAgentTypeDef = TypedDict(
    "_OptionalAssessmentRunAgentTypeDef",
    {"agentHealthDetails": str, "autoScalingGroup": str},
    total=False,
)

class AssessmentRunAgentTypeDef(
    _RequiredAssessmentRunAgentTypeDef, _OptionalAssessmentRunAgentTypeDef
):
    pass

_RequiredAssessmentRunNotificationTypeDef = TypedDict(
    "_RequiredAssessmentRunNotificationTypeDef",
    {"date": datetime, "event": InspectorEvent, "error": bool},
)
_OptionalAssessmentRunNotificationTypeDef = TypedDict(
    "_OptionalAssessmentRunNotificationTypeDef",
    {
        "message": str,
        "snsTopicArn": str,
        "snsPublishStatusCode": AssessmentRunNotificationSnsStatusCode,
    },
    total=False,
)

class AssessmentRunNotificationTypeDef(
    _RequiredAssessmentRunNotificationTypeDef, _OptionalAssessmentRunNotificationTypeDef
):
    pass

AssessmentRunStateChangeTypeDef = TypedDict(
    "AssessmentRunStateChangeTypeDef", {"stateChangedAt": datetime, "state": AssessmentRunState}
)

_RequiredAssessmentRunTypeDef = TypedDict(
    "_RequiredAssessmentRunTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTemplateArn": str,
        "state": AssessmentRunState,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List["AttributeTypeDef"],
        "createdAt": datetime,
        "stateChangedAt": datetime,
        "dataCollected": bool,
        "stateChanges": List["AssessmentRunStateChangeTypeDef"],
        "notifications": List["AssessmentRunNotificationTypeDef"],
        "findingCounts": Dict[Severity, int],
    },
)
_OptionalAssessmentRunTypeDef = TypedDict(
    "_OptionalAssessmentRunTypeDef", {"startedAt": datetime, "completedAt": datetime}, total=False
)

class AssessmentRunTypeDef(_RequiredAssessmentRunTypeDef, _OptionalAssessmentRunTypeDef):
    pass

_RequiredAssessmentTargetTypeDef = TypedDict(
    "_RequiredAssessmentTargetTypeDef",
    {"arn": str, "name": str, "createdAt": datetime, "updatedAt": datetime},
)
_OptionalAssessmentTargetTypeDef = TypedDict(
    "_OptionalAssessmentTargetTypeDef", {"resourceGroupArn": str}, total=False
)

class AssessmentTargetTypeDef(_RequiredAssessmentTargetTypeDef, _OptionalAssessmentTargetTypeDef):
    pass

_RequiredAssessmentTemplateTypeDef = TypedDict(
    "_RequiredAssessmentTemplateTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTargetArn": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List["AttributeTypeDef"],
        "assessmentRunCount": int,
        "createdAt": datetime,
    },
)
_OptionalAssessmentTemplateTypeDef = TypedDict(
    "_OptionalAssessmentTemplateTypeDef", {"lastAssessmentRunArn": str}, total=False
)

class AssessmentTemplateTypeDef(
    _RequiredAssessmentTemplateTypeDef, _OptionalAssessmentTemplateTypeDef
):
    pass

_RequiredAssetAttributesTypeDef = TypedDict(
    "_RequiredAssetAttributesTypeDef", {"schemaVersion": int}
)
_OptionalAssetAttributesTypeDef = TypedDict(
    "_OptionalAssetAttributesTypeDef",
    {
        "agentId": str,
        "autoScalingGroup": str,
        "amiId": str,
        "hostname": str,
        "ipv4Addresses": List[str],
        "tags": List["TagTypeDef"],
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
    },
    total=False,
)

class AssetAttributesTypeDef(_RequiredAssetAttributesTypeDef, _OptionalAssetAttributesTypeDef):
    pass

_RequiredAttributeTypeDef = TypedDict("_RequiredAttributeTypeDef", {"key": str})
_OptionalAttributeTypeDef = TypedDict("_OptionalAttributeTypeDef", {"value": str}, total=False)

class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass

DurationRangeTypeDef = TypedDict(
    "DurationRangeTypeDef", {"minSeconds": int, "maxSeconds": int}, total=False
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef", {"event": InspectorEvent, "subscribedAt": datetime}
)

_RequiredExclusionPreviewTypeDef = TypedDict(
    "_RequiredExclusionPreviewTypeDef",
    {"title": str, "description": str, "recommendation": str, "scopes": List["ScopeTypeDef"]},
)
_OptionalExclusionPreviewTypeDef = TypedDict(
    "_OptionalExclusionPreviewTypeDef", {"attributes": List["AttributeTypeDef"]}, total=False
)

class ExclusionPreviewTypeDef(_RequiredExclusionPreviewTypeDef, _OptionalExclusionPreviewTypeDef):
    pass

_RequiredExclusionTypeDef = TypedDict(
    "_RequiredExclusionTypeDef",
    {
        "arn": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List["ScopeTypeDef"],
    },
)
_OptionalExclusionTypeDef = TypedDict(
    "_OptionalExclusionTypeDef", {"attributes": List["AttributeTypeDef"]}, total=False
)

class ExclusionTypeDef(_RequiredExclusionTypeDef, _OptionalExclusionTypeDef):
    pass

FailedItemDetailsTypeDef = TypedDict(
    "FailedItemDetailsTypeDef", {"failureCode": FailedItemErrorCode, "retryable": bool}
)

_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "arn": str,
        "attributes": List["AttributeTypeDef"],
        "userAttributes": List["AttributeTypeDef"],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "schemaVersion": int,
        "service": str,
        "serviceAttributes": "InspectorServiceAttributesTypeDef",
        "assetType": AssetType,
        "assetAttributes": "AssetAttributesTypeDef",
        "id": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "severity": Severity,
        "numericSeverity": float,
        "confidence": int,
        "indicatorOfCompromise": bool,
    },
    total=False,
)

class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass

_RequiredInspectorServiceAttributesTypeDef = TypedDict(
    "_RequiredInspectorServiceAttributesTypeDef", {"schemaVersion": int}
)
_OptionalInspectorServiceAttributesTypeDef = TypedDict(
    "_OptionalInspectorServiceAttributesTypeDef",
    {"assessmentRunArn": str, "rulesPackageArn": str},
    total=False,
)

class InspectorServiceAttributesTypeDef(
    _RequiredInspectorServiceAttributesTypeDef, _OptionalInspectorServiceAttributesTypeDef
):
    pass

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "networkInterfaceId": str,
        "subnetId": str,
        "vpcId": str,
        "privateDnsName": str,
        "privateIpAddress": str,
        "privateIpAddresses": List["PrivateIpTypeDef"],
        "publicDnsName": str,
        "publicIp": str,
        "ipv6Addresses": List[str],
        "securityGroups": List["SecurityGroupTypeDef"],
    },
    total=False,
)

PrivateIpTypeDef = TypedDict(
    "PrivateIpTypeDef", {"privateDnsName": str, "privateIpAddress": str}, total=False
)

_RequiredResourceGroupTagTypeDef = TypedDict("_RequiredResourceGroupTagTypeDef", {"key": str})
_OptionalResourceGroupTagTypeDef = TypedDict(
    "_OptionalResourceGroupTagTypeDef", {"value": str}, total=False
)

class ResourceGroupTagTypeDef(_RequiredResourceGroupTagTypeDef, _OptionalResourceGroupTagTypeDef):
    pass

ResourceGroupTypeDef = TypedDict(
    "ResourceGroupTypeDef",
    {"arn": str, "tags": List["ResourceGroupTagTypeDef"], "createdAt": datetime},
)

_RequiredRulesPackageTypeDef = TypedDict(
    "_RequiredRulesPackageTypeDef", {"arn": str, "name": str, "version": str, "provider": str}
)
_OptionalRulesPackageTypeDef = TypedDict(
    "_OptionalRulesPackageTypeDef", {"description": str}, total=False
)

class RulesPackageTypeDef(_RequiredRulesPackageTypeDef, _OptionalRulesPackageTypeDef):
    pass

ScopeTypeDef = TypedDict("ScopeTypeDef", {"key": ScopeType, "value": str}, total=False)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef", {"groupName": str, "groupId": str}, total=False
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {"resourceArn": str, "topicArn": str, "eventSubscriptions": List["EventSubscriptionTypeDef"]},
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"value": str}, total=False)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

_RequiredTelemetryMetadataTypeDef = TypedDict(
    "_RequiredTelemetryMetadataTypeDef", {"messageType": str, "count": int}
)
_OptionalTelemetryMetadataTypeDef = TypedDict(
    "_OptionalTelemetryMetadataTypeDef", {"dataSize": int}, total=False
)

class TelemetryMetadataTypeDef(
    _RequiredTelemetryMetadataTypeDef, _OptionalTelemetryMetadataTypeDef
):
    pass

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef", {"beginDate": datetime, "endDate": datetime}, total=False
)

AddAttributesToFindingsResponseTypeDef = TypedDict(
    "AddAttributesToFindingsResponseTypeDef", {"failedItems": Dict[str, "FailedItemDetailsTypeDef"]}
)

AgentFilterTypeDef = TypedDict(
    "AgentFilterTypeDef",
    {"agentHealths": List[AgentHealth], "agentHealthCodes": List[AgentHealthCode]},
)

AssessmentRunFilterTypeDef = TypedDict(
    "AssessmentRunFilterTypeDef",
    {
        "namePattern": str,
        "states": List[AssessmentRunState],
        "durationRange": "DurationRangeTypeDef",
        "rulesPackageArns": List[str],
        "startTimeRange": "TimestampRangeTypeDef",
        "completionTimeRange": "TimestampRangeTypeDef",
        "stateChangeTimeRange": "TimestampRangeTypeDef",
    },
    total=False,
)

AssessmentTargetFilterTypeDef = TypedDict(
    "AssessmentTargetFilterTypeDef", {"assessmentTargetNamePattern": str}, total=False
)

AssessmentTemplateFilterTypeDef = TypedDict(
    "AssessmentTemplateFilterTypeDef",
    {"namePattern": str, "durationRange": "DurationRangeTypeDef", "rulesPackageArns": List[str]},
    total=False,
)

CreateAssessmentTargetResponseTypeDef = TypedDict(
    "CreateAssessmentTargetResponseTypeDef", {"assessmentTargetArn": str}
)

CreateAssessmentTemplateResponseTypeDef = TypedDict(
    "CreateAssessmentTemplateResponseTypeDef", {"assessmentTemplateArn": str}
)

CreateExclusionsPreviewResponseTypeDef = TypedDict(
    "CreateExclusionsPreviewResponseTypeDef", {"previewToken": str}
)

CreateResourceGroupResponseTypeDef = TypedDict(
    "CreateResourceGroupResponseTypeDef", {"resourceGroupArn": str}
)

DescribeAssessmentRunsResponseTypeDef = TypedDict(
    "DescribeAssessmentRunsResponseTypeDef",
    {
        "assessmentRuns": List["AssessmentRunTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
    },
)

DescribeAssessmentTargetsResponseTypeDef = TypedDict(
    "DescribeAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargets": List["AssessmentTargetTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
    },
)

DescribeAssessmentTemplatesResponseTypeDef = TypedDict(
    "DescribeAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplates": List["AssessmentTemplateTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
    },
)

DescribeCrossAccountAccessRoleResponseTypeDef = TypedDict(
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    {"roleArn": str, "valid": bool, "registeredAt": datetime},
)

DescribeExclusionsResponseTypeDef = TypedDict(
    "DescribeExclusionsResponseTypeDef",
    {
        "exclusions": Dict[str, "ExclusionTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
    },
)

DescribeFindingsResponseTypeDef = TypedDict(
    "DescribeFindingsResponseTypeDef",
    {"findings": List["FindingTypeDef"], "failedItems": Dict[str, "FailedItemDetailsTypeDef"]},
)

DescribeResourceGroupsResponseTypeDef = TypedDict(
    "DescribeResourceGroupsResponseTypeDef",
    {
        "resourceGroups": List["ResourceGroupTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
    },
)

DescribeRulesPackagesResponseTypeDef = TypedDict(
    "DescribeRulesPackagesResponseTypeDef",
    {
        "rulesPackages": List["RulesPackageTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
    },
)

FindingFilterTypeDef = TypedDict(
    "FindingFilterTypeDef",
    {
        "agentIds": List[str],
        "autoScalingGroups": List[str],
        "ruleNames": List[str],
        "severities": List[Severity],
        "rulesPackageArns": List[str],
        "attributes": List["AttributeTypeDef"],
        "userAttributes": List["AttributeTypeDef"],
        "creationTimeRange": "TimestampRangeTypeDef",
    },
    total=False,
)

_RequiredGetAssessmentReportResponseTypeDef = TypedDict(
    "_RequiredGetAssessmentReportResponseTypeDef", {"status": ReportStatus}
)
_OptionalGetAssessmentReportResponseTypeDef = TypedDict(
    "_OptionalGetAssessmentReportResponseTypeDef", {"url": str}, total=False
)

class GetAssessmentReportResponseTypeDef(
    _RequiredGetAssessmentReportResponseTypeDef, _OptionalGetAssessmentReportResponseTypeDef
):
    pass

_RequiredGetExclusionsPreviewResponseTypeDef = TypedDict(
    "_RequiredGetExclusionsPreviewResponseTypeDef", {"previewStatus": PreviewStatus}
)
_OptionalGetExclusionsPreviewResponseTypeDef = TypedDict(
    "_OptionalGetExclusionsPreviewResponseTypeDef",
    {"exclusionPreviews": List["ExclusionPreviewTypeDef"], "nextToken": str},
    total=False,
)

class GetExclusionsPreviewResponseTypeDef(
    _RequiredGetExclusionsPreviewResponseTypeDef, _OptionalGetExclusionsPreviewResponseTypeDef
):
    pass

GetTelemetryMetadataResponseTypeDef = TypedDict(
    "GetTelemetryMetadataResponseTypeDef", {"telemetryMetadata": List["TelemetryMetadataTypeDef"]}
)

_RequiredListAssessmentRunAgentsResponseTypeDef = TypedDict(
    "_RequiredListAssessmentRunAgentsResponseTypeDef",
    {"assessmentRunAgents": List["AssessmentRunAgentTypeDef"]},
)
_OptionalListAssessmentRunAgentsResponseTypeDef = TypedDict(
    "_OptionalListAssessmentRunAgentsResponseTypeDef", {"nextToken": str}, total=False
)

class ListAssessmentRunAgentsResponseTypeDef(
    _RequiredListAssessmentRunAgentsResponseTypeDef, _OptionalListAssessmentRunAgentsResponseTypeDef
):
    pass

_RequiredListAssessmentRunsResponseTypeDef = TypedDict(
    "_RequiredListAssessmentRunsResponseTypeDef", {"assessmentRunArns": List[str]}
)
_OptionalListAssessmentRunsResponseTypeDef = TypedDict(
    "_OptionalListAssessmentRunsResponseTypeDef", {"nextToken": str}, total=False
)

class ListAssessmentRunsResponseTypeDef(
    _RequiredListAssessmentRunsResponseTypeDef, _OptionalListAssessmentRunsResponseTypeDef
):
    pass

_RequiredListAssessmentTargetsResponseTypeDef = TypedDict(
    "_RequiredListAssessmentTargetsResponseTypeDef", {"assessmentTargetArns": List[str]}
)
_OptionalListAssessmentTargetsResponseTypeDef = TypedDict(
    "_OptionalListAssessmentTargetsResponseTypeDef", {"nextToken": str}, total=False
)

class ListAssessmentTargetsResponseTypeDef(
    _RequiredListAssessmentTargetsResponseTypeDef, _OptionalListAssessmentTargetsResponseTypeDef
):
    pass

_RequiredListAssessmentTemplatesResponseTypeDef = TypedDict(
    "_RequiredListAssessmentTemplatesResponseTypeDef", {"assessmentTemplateArns": List[str]}
)
_OptionalListAssessmentTemplatesResponseTypeDef = TypedDict(
    "_OptionalListAssessmentTemplatesResponseTypeDef", {"nextToken": str}, total=False
)

class ListAssessmentTemplatesResponseTypeDef(
    _RequiredListAssessmentTemplatesResponseTypeDef, _OptionalListAssessmentTemplatesResponseTypeDef
):
    pass

_RequiredListEventSubscriptionsResponseTypeDef = TypedDict(
    "_RequiredListEventSubscriptionsResponseTypeDef", {"subscriptions": List["SubscriptionTypeDef"]}
)
_OptionalListEventSubscriptionsResponseTypeDef = TypedDict(
    "_OptionalListEventSubscriptionsResponseTypeDef", {"nextToken": str}, total=False
)

class ListEventSubscriptionsResponseTypeDef(
    _RequiredListEventSubscriptionsResponseTypeDef, _OptionalListEventSubscriptionsResponseTypeDef
):
    pass

_RequiredListExclusionsResponseTypeDef = TypedDict(
    "_RequiredListExclusionsResponseTypeDef", {"exclusionArns": List[str]}
)
_OptionalListExclusionsResponseTypeDef = TypedDict(
    "_OptionalListExclusionsResponseTypeDef", {"nextToken": str}, total=False
)

class ListExclusionsResponseTypeDef(
    _RequiredListExclusionsResponseTypeDef, _OptionalListExclusionsResponseTypeDef
):
    pass

_RequiredListFindingsResponseTypeDef = TypedDict(
    "_RequiredListFindingsResponseTypeDef", {"findingArns": List[str]}
)
_OptionalListFindingsResponseTypeDef = TypedDict(
    "_OptionalListFindingsResponseTypeDef", {"nextToken": str}, total=False
)

class ListFindingsResponseTypeDef(
    _RequiredListFindingsResponseTypeDef, _OptionalListFindingsResponseTypeDef
):
    pass

_RequiredListRulesPackagesResponseTypeDef = TypedDict(
    "_RequiredListRulesPackagesResponseTypeDef", {"rulesPackageArns": List[str]}
)
_OptionalListRulesPackagesResponseTypeDef = TypedDict(
    "_OptionalListRulesPackagesResponseTypeDef", {"nextToken": str}, total=False
)

class ListRulesPackagesResponseTypeDef(
    _RequiredListRulesPackagesResponseTypeDef, _OptionalListRulesPackagesResponseTypeDef
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": List["TagTypeDef"]}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredPreviewAgentsResponseTypeDef = TypedDict(
    "_RequiredPreviewAgentsResponseTypeDef", {"agentPreviews": List["AgentPreviewTypeDef"]}
)
_OptionalPreviewAgentsResponseTypeDef = TypedDict(
    "_OptionalPreviewAgentsResponseTypeDef", {"nextToken": str}, total=False
)

class PreviewAgentsResponseTypeDef(
    _RequiredPreviewAgentsResponseTypeDef, _OptionalPreviewAgentsResponseTypeDef
):
    pass

RemoveAttributesFromFindingsResponseTypeDef = TypedDict(
    "RemoveAttributesFromFindingsResponseTypeDef",
    {"failedItems": Dict[str, "FailedItemDetailsTypeDef"]},
)

StartAssessmentRunResponseTypeDef = TypedDict(
    "StartAssessmentRunResponseTypeDef", {"assessmentRunArn": str}
)
