"""
Main interface for application-autoscaling service type definitions.

Usage::

    ```python
    from mypy_boto3_application_autoscaling.type_defs import AlarmTypeDef

    data: AlarmTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_application_autoscaling.literals import (
    AdjustmentType,
    MetricAggregationType,
    MetricStatistic,
    MetricType,
    PolicyType,
    ScalableDimension,
    ScalingActivityStatusCode,
    ServiceNamespace,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AlarmTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "MetricDimensionTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "ScalableTargetActionTypeDef",
    "ScalableTargetTypeDef",
    "ScalingActivityTypeDef",
    "ScalingPolicyTypeDef",
    "ScheduledActionTypeDef",
    "StepAdjustmentTypeDef",
    "StepScalingPolicyConfigurationTypeDef",
    "SuspendedStateTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    "DescribeScalableTargetsResponseTypeDef",
    "DescribeScalingActivitiesResponseTypeDef",
    "DescribeScalingPoliciesResponseTypeDef",
    "DescribeScheduledActionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutScalingPolicyResponseTypeDef",
)

AlarmTypeDef = TypedDict("AlarmTypeDef", {"AlarmName": str, "AlarmARN": str})

_RequiredCustomizedMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedMetricSpecificationTypeDef",
    {"MetricName": str, "Namespace": str, "Statistic": MetricStatistic},
)
_OptionalCustomizedMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedMetricSpecificationTypeDef",
    {"Dimensions": List["MetricDimensionTypeDef"], "Unit": str},
    total=False,
)

class CustomizedMetricSpecificationTypeDef(
    _RequiredCustomizedMetricSpecificationTypeDef, _OptionalCustomizedMetricSpecificationTypeDef
):
    pass

MetricDimensionTypeDef = TypedDict("MetricDimensionTypeDef", {"Name": str, "Value": str})

_RequiredPredefinedMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedMetricSpecificationTypeDef", {"PredefinedMetricType": MetricType}
)
_OptionalPredefinedMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedMetricSpecificationTypeDef", {"ResourceLabel": str}, total=False
)

class PredefinedMetricSpecificationTypeDef(
    _RequiredPredefinedMetricSpecificationTypeDef, _OptionalPredefinedMetricSpecificationTypeDef
):
    pass

ScalableTargetActionTypeDef = TypedDict(
    "ScalableTargetActionTypeDef", {"MinCapacity": int, "MaxCapacity": int}, total=False
)

_RequiredScalableTargetTypeDef = TypedDict(
    "_RequiredScalableTargetTypeDef",
    {
        "ServiceNamespace": ServiceNamespace,
        "ResourceId": str,
        "ScalableDimension": ScalableDimension,
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
    },
)
_OptionalScalableTargetTypeDef = TypedDict(
    "_OptionalScalableTargetTypeDef", {"SuspendedState": "SuspendedStateTypeDef"}, total=False
)

class ScalableTargetTypeDef(_RequiredScalableTargetTypeDef, _OptionalScalableTargetTypeDef):
    pass

_RequiredScalingActivityTypeDef = TypedDict(
    "_RequiredScalingActivityTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": ServiceNamespace,
        "ResourceId": str,
        "ScalableDimension": ScalableDimension,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": ScalingActivityStatusCode,
    },
)
_OptionalScalingActivityTypeDef = TypedDict(
    "_OptionalScalingActivityTypeDef",
    {"EndTime": datetime, "StatusMessage": str, "Details": str},
    total=False,
)

class ScalingActivityTypeDef(_RequiredScalingActivityTypeDef, _OptionalScalingActivityTypeDef):
    pass

_RequiredScalingPolicyTypeDef = TypedDict(
    "_RequiredScalingPolicyTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespace,
        "ResourceId": str,
        "ScalableDimension": ScalableDimension,
        "PolicyType": PolicyType,
        "CreationTime": datetime,
    },
)
_OptionalScalingPolicyTypeDef = TypedDict(
    "_OptionalScalingPolicyTypeDef",
    {
        "StepScalingPolicyConfiguration": "StepScalingPolicyConfigurationTypeDef",
        "TargetTrackingScalingPolicyConfiguration": "TargetTrackingScalingPolicyConfigurationTypeDef",
        "Alarms": List["AlarmTypeDef"],
    },
    total=False,
)

class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, _OptionalScalingPolicyTypeDef):
    pass

_RequiredScheduledActionTypeDef = TypedDict(
    "_RequiredScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": ServiceNamespace,
        "Schedule": str,
        "ResourceId": str,
        "CreationTime": datetime,
    },
)
_OptionalScheduledActionTypeDef = TypedDict(
    "_OptionalScheduledActionTypeDef",
    {
        "Timezone": str,
        "ScalableDimension": ScalableDimension,
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": "ScalableTargetActionTypeDef",
    },
    total=False,
)

class ScheduledActionTypeDef(_RequiredScheduledActionTypeDef, _OptionalScheduledActionTypeDef):
    pass

_RequiredStepAdjustmentTypeDef = TypedDict(
    "_RequiredStepAdjustmentTypeDef", {"ScalingAdjustment": int}
)
_OptionalStepAdjustmentTypeDef = TypedDict(
    "_OptionalStepAdjustmentTypeDef",
    {"MetricIntervalLowerBound": float, "MetricIntervalUpperBound": float},
    total=False,
)

class StepAdjustmentTypeDef(_RequiredStepAdjustmentTypeDef, _OptionalStepAdjustmentTypeDef):
    pass

StepScalingPolicyConfigurationTypeDef = TypedDict(
    "StepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": AdjustmentType,
        "StepAdjustments": List["StepAdjustmentTypeDef"],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": MetricAggregationType,
    },
    total=False,
)

SuspendedStateTypeDef = TypedDict(
    "SuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)

_RequiredTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingScalingPolicyConfigurationTypeDef", {"TargetValue": float}
)
_OptionalTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": "PredefinedMetricSpecificationTypeDef",
        "CustomizedMetricSpecification": "CustomizedMetricSpecificationTypeDef",
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)

class TargetTrackingScalingPolicyConfigurationTypeDef(
    _RequiredTargetTrackingScalingPolicyConfigurationTypeDef,
    _OptionalTargetTrackingScalingPolicyConfigurationTypeDef,
):
    pass

DescribeScalableTargetsResponseTypeDef = TypedDict(
    "DescribeScalableTargetsResponseTypeDef",
    {"ScalableTargets": List["ScalableTargetTypeDef"], "NextToken": str},
    total=False,
)

DescribeScalingActivitiesResponseTypeDef = TypedDict(
    "DescribeScalingActivitiesResponseTypeDef",
    {"ScalingActivities": List["ScalingActivityTypeDef"], "NextToken": str},
    total=False,
)

DescribeScalingPoliciesResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesResponseTypeDef",
    {"ScalingPolicies": List["ScalingPolicyTypeDef"], "NextToken": str},
    total=False,
)

DescribeScheduledActionsResponseTypeDef = TypedDict(
    "DescribeScheduledActionsResponseTypeDef",
    {"ScheduledActions": List["ScheduledActionTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredPutScalingPolicyResponseTypeDef = TypedDict(
    "_RequiredPutScalingPolicyResponseTypeDef", {"PolicyARN": str}
)
_OptionalPutScalingPolicyResponseTypeDef = TypedDict(
    "_OptionalPutScalingPolicyResponseTypeDef", {"Alarms": List["AlarmTypeDef"]}, total=False
)

class PutScalingPolicyResponseTypeDef(
    _RequiredPutScalingPolicyResponseTypeDef, _OptionalPutScalingPolicyResponseTypeDef
):
    pass
