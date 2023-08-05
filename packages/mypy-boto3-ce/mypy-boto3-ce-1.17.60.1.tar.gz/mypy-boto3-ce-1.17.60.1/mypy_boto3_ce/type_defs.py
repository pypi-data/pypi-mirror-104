"""
Main interface for ce service type definitions.

Usage::

    ```python
    from mypy_boto3_ce.type_defs import AnomalyMonitorTypeDef

    data: AnomalyMonitorTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from mypy_boto3_ce.literals import (
    AccountScope,
    AnomalyFeedbackType,
    AnomalySubscriptionFrequency,
    CostCategoryInheritedValueDimensionName,
    CostCategoryRuleType,
    CostCategoryRuleVersion,
    CostCategoryStatus,
    CostCategoryStatusComponent,
    Dimension,
    GroupDefinitionType,
    LookbackPeriodInDays,
    MatchOption,
    MonitorDimension,
    MonitorType,
    NumericOperator,
    OfferingClass,
    PaymentOption,
    RecommendationTarget,
    RightsizingType,
    SortOrder,
    SubscriberStatus,
    SubscriberType,
    SupportedSavingsPlansType,
    TermInYears,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnomalyMonitorTypeDef",
    "AnomalyScoreTypeDef",
    "AnomalySubscriptionTypeDef",
    "AnomalyTypeDef",
    "CostCategoryInheritedValueDimensionTypeDef",
    "CostCategoryProcessingStatusTypeDef",
    "CostCategoryReferenceTypeDef",
    "CostCategoryRuleTypeDef",
    "CostCategoryTypeDef",
    "CostCategoryValuesTypeDef",
    "CoverageByTimeTypeDef",
    "CoverageCostTypeDef",
    "CoverageHoursTypeDef",
    "CoverageNormalizedUnitsTypeDef",
    "CoverageTypeDef",
    "CurrentInstanceTypeDef",
    "DateIntervalTypeDef",
    "DimensionValuesTypeDef",
    "DimensionValuesWithAttributesTypeDef",
    "EBSResourceUtilizationTypeDef",
    "EC2InstanceDetailsTypeDef",
    "EC2ResourceDetailsTypeDef",
    "EC2ResourceUtilizationTypeDef",
    "EC2SpecificationTypeDef",
    "ESInstanceDetailsTypeDef",
    "ElastiCacheInstanceDetailsTypeDef",
    "ForecastResultTypeDef",
    "GroupDefinitionTypeDef",
    "GroupTypeDef",
    "ImpactTypeDef",
    "InstanceDetailsTypeDef",
    "MetricValueTypeDef",
    "ModifyRecommendationDetailTypeDef",
    "RDSInstanceDetailsTypeDef",
    "RedshiftInstanceDetailsTypeDef",
    "ReservationAggregatesTypeDef",
    "ReservationCoverageGroupTypeDef",
    "ReservationPurchaseRecommendationDetailTypeDef",
    "ReservationPurchaseRecommendationMetadataTypeDef",
    "ReservationPurchaseRecommendationSummaryTypeDef",
    "ReservationPurchaseRecommendationTypeDef",
    "ReservationUtilizationGroupTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceUtilizationTypeDef",
    "ResultByTimeTypeDef",
    "RightsizingRecommendationConfigurationTypeDef",
    "RightsizingRecommendationMetadataTypeDef",
    "RightsizingRecommendationSummaryTypeDef",
    "RightsizingRecommendationTypeDef",
    "RootCauseTypeDef",
    "SavingsPlansAmortizedCommitmentTypeDef",
    "SavingsPlansCoverageDataTypeDef",
    "SavingsPlansCoverageTypeDef",
    "SavingsPlansDetailsTypeDef",
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    "SavingsPlansPurchaseRecommendationTypeDef",
    "SavingsPlansSavingsTypeDef",
    "SavingsPlansUtilizationAggregatesTypeDef",
    "SavingsPlansUtilizationByTimeTypeDef",
    "SavingsPlansUtilizationDetailTypeDef",
    "SavingsPlansUtilizationTypeDef",
    "ServiceSpecificationTypeDef",
    "SubscriberTypeDef",
    "TagValuesTypeDef",
    "TargetInstanceTypeDef",
    "TerminateRecommendationDetailTypeDef",
    "UtilizationByTimeTypeDef",
    "AnomalyDateIntervalTypeDef",
    "CreateAnomalyMonitorResponseTypeDef",
    "CreateAnomalySubscriptionResponseTypeDef",
    "CreateCostCategoryDefinitionResponseTypeDef",
    "DeleteCostCategoryDefinitionResponseTypeDef",
    "DescribeCostCategoryDefinitionResponseTypeDef",
    "ExpressionTypeDef",
    "GetAnomaliesResponseTypeDef",
    "GetAnomalyMonitorsResponseTypeDef",
    "GetAnomalySubscriptionsResponseTypeDef",
    "GetCostAndUsageResponseTypeDef",
    "GetCostAndUsageWithResourcesResponseTypeDef",
    "GetCostCategoriesResponseTypeDef",
    "GetCostForecastResponseTypeDef",
    "GetDimensionValuesResponseTypeDef",
    "GetReservationCoverageResponseTypeDef",
    "GetReservationPurchaseRecommendationResponseTypeDef",
    "GetReservationUtilizationResponseTypeDef",
    "GetRightsizingRecommendationResponseTypeDef",
    "GetSavingsPlansCoverageResponseTypeDef",
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    "GetSavingsPlansUtilizationDetailsResponseTypeDef",
    "GetSavingsPlansUtilizationResponseTypeDef",
    "GetTagsResponseTypeDef",
    "GetUsageForecastResponseTypeDef",
    "ListCostCategoryDefinitionsResponseTypeDef",
    "ProvideAnomalyFeedbackResponseTypeDef",
    "SortDefinitionTypeDef",
    "TotalImpactFilterTypeDef",
    "UpdateAnomalyMonitorResponseTypeDef",
    "UpdateAnomalySubscriptionResponseTypeDef",
    "UpdateCostCategoryDefinitionResponseTypeDef",
)

_RequiredAnomalyMonitorTypeDef = TypedDict(
    "_RequiredAnomalyMonitorTypeDef", {"MonitorName": str, "MonitorType": MonitorType}
)
_OptionalAnomalyMonitorTypeDef = TypedDict(
    "_OptionalAnomalyMonitorTypeDef",
    {
        "MonitorArn": str,
        "CreationDate": str,
        "LastUpdatedDate": str,
        "LastEvaluatedDate": str,
        "MonitorDimension": MonitorDimension,
        "MonitorSpecification": Dict[str, Any],
        "DimensionalValueCount": int,
    },
    total=False,
)


class AnomalyMonitorTypeDef(_RequiredAnomalyMonitorTypeDef, _OptionalAnomalyMonitorTypeDef):
    pass


AnomalyScoreTypeDef = TypedDict("AnomalyScoreTypeDef", {"MaxScore": float, "CurrentScore": float})

_RequiredAnomalySubscriptionTypeDef = TypedDict(
    "_RequiredAnomalySubscriptionTypeDef",
    {
        "MonitorArnList": List[str],
        "Subscribers": List["SubscriberTypeDef"],
        "Threshold": float,
        "Frequency": AnomalySubscriptionFrequency,
        "SubscriptionName": str,
    },
)
_OptionalAnomalySubscriptionTypeDef = TypedDict(
    "_OptionalAnomalySubscriptionTypeDef", {"SubscriptionArn": str, "AccountId": str}, total=False
)


class AnomalySubscriptionTypeDef(
    _RequiredAnomalySubscriptionTypeDef, _OptionalAnomalySubscriptionTypeDef
):
    pass


_RequiredAnomalyTypeDef = TypedDict(
    "_RequiredAnomalyTypeDef",
    {
        "AnomalyId": str,
        "AnomalyScore": "AnomalyScoreTypeDef",
        "Impact": "ImpactTypeDef",
        "MonitorArn": str,
    },
)
_OptionalAnomalyTypeDef = TypedDict(
    "_OptionalAnomalyTypeDef",
    {
        "AnomalyStartDate": str,
        "AnomalyEndDate": str,
        "DimensionValue": str,
        "RootCauses": List["RootCauseTypeDef"],
        "Feedback": AnomalyFeedbackType,
    },
    total=False,
)


class AnomalyTypeDef(_RequiredAnomalyTypeDef, _OptionalAnomalyTypeDef):
    pass


CostCategoryInheritedValueDimensionTypeDef = TypedDict(
    "CostCategoryInheritedValueDimensionTypeDef",
    {"DimensionName": CostCategoryInheritedValueDimensionName, "DimensionKey": str},
    total=False,
)

CostCategoryProcessingStatusTypeDef = TypedDict(
    "CostCategoryProcessingStatusTypeDef",
    {"Component": CostCategoryStatusComponent, "Status": CostCategoryStatus},
    total=False,
)

CostCategoryReferenceTypeDef = TypedDict(
    "CostCategoryReferenceTypeDef",
    {
        "CostCategoryArn": str,
        "Name": str,
        "EffectiveStart": str,
        "EffectiveEnd": str,
        "NumberOfRules": int,
        "ProcessingStatus": List["CostCategoryProcessingStatusTypeDef"],
        "Values": List[str],
        "DefaultValue": str,
    },
    total=False,
)

CostCategoryRuleTypeDef = TypedDict(
    "CostCategoryRuleTypeDef",
    {
        "Value": str,
        "Rule": Dict[str, Any],
        "InheritedValue": "CostCategoryInheritedValueDimensionTypeDef",
        "Type": CostCategoryRuleType,
    },
    total=False,
)

_RequiredCostCategoryTypeDef = TypedDict(
    "_RequiredCostCategoryTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "Name": str,
        "RuleVersion": CostCategoryRuleVersion,
        "Rules": List["CostCategoryRuleTypeDef"],
    },
)
_OptionalCostCategoryTypeDef = TypedDict(
    "_OptionalCostCategoryTypeDef",
    {
        "EffectiveEnd": str,
        "ProcessingStatus": List["CostCategoryProcessingStatusTypeDef"],
        "DefaultValue": str,
    },
    total=False,
)


class CostCategoryTypeDef(_RequiredCostCategoryTypeDef, _OptionalCostCategoryTypeDef):
    pass


CostCategoryValuesTypeDef = TypedDict(
    "CostCategoryValuesTypeDef",
    {"Key": str, "Values": List[str], "MatchOptions": List[MatchOption]},
    total=False,
)

CoverageByTimeTypeDef = TypedDict(
    "CoverageByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Groups": List["ReservationCoverageGroupTypeDef"],
        "Total": "CoverageTypeDef",
    },
    total=False,
)

CoverageCostTypeDef = TypedDict("CoverageCostTypeDef", {"OnDemandCost": str}, total=False)

CoverageHoursTypeDef = TypedDict(
    "CoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)

CoverageNormalizedUnitsTypeDef = TypedDict(
    "CoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)

CoverageTypeDef = TypedDict(
    "CoverageTypeDef",
    {
        "CoverageHours": "CoverageHoursTypeDef",
        "CoverageNormalizedUnits": "CoverageNormalizedUnitsTypeDef",
        "CoverageCost": "CoverageCostTypeDef",
    },
    total=False,
)

CurrentInstanceTypeDef = TypedDict(
    "CurrentInstanceTypeDef",
    {
        "ResourceId": str,
        "InstanceName": str,
        "Tags": List["TagValuesTypeDef"],
        "ResourceDetails": "ResourceDetailsTypeDef",
        "ResourceUtilization": "ResourceUtilizationTypeDef",
        "ReservationCoveredHoursInLookbackPeriod": str,
        "SavingsPlansCoveredHoursInLookbackPeriod": str,
        "OnDemandHoursInLookbackPeriod": str,
        "TotalRunningHoursInLookbackPeriod": str,
        "MonthlyCost": str,
        "CurrencyCode": str,
    },
    total=False,
)

DateIntervalTypeDef = TypedDict("DateIntervalTypeDef", {"Start": str, "End": str})

DimensionValuesTypeDef = TypedDict(
    "DimensionValuesTypeDef",
    {"Key": Dimension, "Values": List[str], "MatchOptions": List[MatchOption]},
    total=False,
)

DimensionValuesWithAttributesTypeDef = TypedDict(
    "DimensionValuesWithAttributesTypeDef",
    {"Value": str, "Attributes": Dict[str, str]},
    total=False,
)

EBSResourceUtilizationTypeDef = TypedDict(
    "EBSResourceUtilizationTypeDef",
    {
        "EbsReadOpsPerSecond": str,
        "EbsWriteOpsPerSecond": str,
        "EbsReadBytesPerSecond": str,
        "EbsWriteBytesPerSecond": str,
    },
    total=False,
)

EC2InstanceDetailsTypeDef = TypedDict(
    "EC2InstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "AvailabilityZone": str,
        "Platform": str,
        "Tenancy": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

EC2ResourceDetailsTypeDef = TypedDict(
    "EC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": str,
        "InstanceType": str,
        "Platform": str,
        "Region": str,
        "Sku": str,
        "Memory": str,
        "NetworkPerformance": str,
        "Storage": str,
        "Vcpu": str,
    },
    total=False,
)

EC2ResourceUtilizationTypeDef = TypedDict(
    "EC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": str,
        "MaxMemoryUtilizationPercentage": str,
        "MaxStorageUtilizationPercentage": str,
        "EBSResourceUtilization": "EBSResourceUtilizationTypeDef",
    },
    total=False,
)

EC2SpecificationTypeDef = TypedDict(
    "EC2SpecificationTypeDef", {"OfferingClass": OfferingClass}, total=False
)

ESInstanceDetailsTypeDef = TypedDict(
    "ESInstanceDetailsTypeDef",
    {
        "InstanceClass": str,
        "InstanceSize": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ElastiCacheInstanceDetailsTypeDef = TypedDict(
    "ElastiCacheInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "ProductDescription": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ForecastResultTypeDef = TypedDict(
    "ForecastResultTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "MeanValue": str,
        "PredictionIntervalLowerBound": str,
        "PredictionIntervalUpperBound": str,
    },
    total=False,
)

GroupDefinitionTypeDef = TypedDict(
    "GroupDefinitionTypeDef", {"Type": GroupDefinitionType, "Key": str}, total=False
)

GroupTypeDef = TypedDict(
    "GroupTypeDef", {"Keys": List[str], "Metrics": Dict[str, "MetricValueTypeDef"]}, total=False
)

_RequiredImpactTypeDef = TypedDict("_RequiredImpactTypeDef", {"MaxImpact": float})
_OptionalImpactTypeDef = TypedDict("_OptionalImpactTypeDef", {"TotalImpact": float}, total=False)


class ImpactTypeDef(_RequiredImpactTypeDef, _OptionalImpactTypeDef):
    pass


InstanceDetailsTypeDef = TypedDict(
    "InstanceDetailsTypeDef",
    {
        "EC2InstanceDetails": "EC2InstanceDetailsTypeDef",
        "RDSInstanceDetails": "RDSInstanceDetailsTypeDef",
        "RedshiftInstanceDetails": "RedshiftInstanceDetailsTypeDef",
        "ElastiCacheInstanceDetails": "ElastiCacheInstanceDetailsTypeDef",
        "ESInstanceDetails": "ESInstanceDetailsTypeDef",
    },
    total=False,
)

MetricValueTypeDef = TypedDict("MetricValueTypeDef", {"Amount": str, "Unit": str}, total=False)

ModifyRecommendationDetailTypeDef = TypedDict(
    "ModifyRecommendationDetailTypeDef",
    {"TargetInstances": List["TargetInstanceTypeDef"]},
    total=False,
)

RDSInstanceDetailsTypeDef = TypedDict(
    "RDSInstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "DatabaseEngine": str,
        "DatabaseEdition": str,
        "DeploymentOption": str,
        "LicenseModel": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

RedshiftInstanceDetailsTypeDef = TypedDict(
    "RedshiftInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ReservationAggregatesTypeDef = TypedDict(
    "ReservationAggregatesTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
        "RICostForUnusedHours": str,
        "RealizedSavings": str,
        "UnrealizedSavings": str,
    },
    total=False,
)

ReservationCoverageGroupTypeDef = TypedDict(
    "ReservationCoverageGroupTypeDef",
    {"Attributes": Dict[str, str], "Coverage": "CoverageTypeDef"},
    total=False,
)

ReservationPurchaseRecommendationDetailTypeDef = TypedDict(
    "ReservationPurchaseRecommendationDetailTypeDef",
    {
        "AccountId": str,
        "InstanceDetails": "InstanceDetailsTypeDef",
        "RecommendedNumberOfInstancesToPurchase": str,
        "RecommendedNormalizedUnitsToPurchase": str,
        "MinimumNumberOfInstancesUsedPerHour": str,
        "MinimumNormalizedUnitsUsedPerHour": str,
        "MaximumNumberOfInstancesUsedPerHour": str,
        "MaximumNormalizedUnitsUsedPerHour": str,
        "AverageNumberOfInstancesUsedPerHour": str,
        "AverageNormalizedUnitsUsedPerHour": str,
        "AverageUtilization": str,
        "EstimatedBreakEvenInMonths": str,
        "CurrencyCode": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedMonthlySavingsPercentage": str,
        "EstimatedMonthlyOnDemandCost": str,
        "EstimatedReservationCostForLookbackPeriod": str,
        "UpfrontCost": str,
        "RecurringStandardMonthlyCost": str,
    },
    total=False,
)

ReservationPurchaseRecommendationMetadataTypeDef = TypedDict(
    "ReservationPurchaseRecommendationMetadataTypeDef",
    {"RecommendationId": str, "GenerationTimestamp": str},
    total=False,
)

ReservationPurchaseRecommendationSummaryTypeDef = TypedDict(
    "ReservationPurchaseRecommendationSummaryTypeDef",
    {
        "TotalEstimatedMonthlySavingsAmount": str,
        "TotalEstimatedMonthlySavingsPercentage": str,
        "CurrencyCode": str,
    },
    total=False,
)

ReservationPurchaseRecommendationTypeDef = TypedDict(
    "ReservationPurchaseRecommendationTypeDef",
    {
        "AccountScope": AccountScope,
        "LookbackPeriodInDays": LookbackPeriodInDays,
        "TermInYears": TermInYears,
        "PaymentOption": PaymentOption,
        "ServiceSpecification": "ServiceSpecificationTypeDef",
        "RecommendationDetails": List["ReservationPurchaseRecommendationDetailTypeDef"],
        "RecommendationSummary": "ReservationPurchaseRecommendationSummaryTypeDef",
    },
    total=False,
)

ReservationUtilizationGroupTypeDef = TypedDict(
    "ReservationUtilizationGroupTypeDef",
    {
        "Key": str,
        "Value": str,
        "Attributes": Dict[str, str],
        "Utilization": "ReservationAggregatesTypeDef",
    },
    total=False,
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef", {"EC2ResourceDetails": "EC2ResourceDetailsTypeDef"}, total=False
)

ResourceUtilizationTypeDef = TypedDict(
    "ResourceUtilizationTypeDef",
    {"EC2ResourceUtilization": "EC2ResourceUtilizationTypeDef"},
    total=False,
)

ResultByTimeTypeDef = TypedDict(
    "ResultByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Total": Dict[str, "MetricValueTypeDef"],
        "Groups": List["GroupTypeDef"],
        "Estimated": bool,
    },
    total=False,
)

RightsizingRecommendationConfigurationTypeDef = TypedDict(
    "RightsizingRecommendationConfigurationTypeDef",
    {"RecommendationTarget": RecommendationTarget, "BenefitsConsidered": bool},
)

RightsizingRecommendationMetadataTypeDef = TypedDict(
    "RightsizingRecommendationMetadataTypeDef",
    {
        "RecommendationId": str,
        "GenerationTimestamp": str,
        "LookbackPeriodInDays": LookbackPeriodInDays,
        "AdditionalMetadata": str,
    },
    total=False,
)

RightsizingRecommendationSummaryTypeDef = TypedDict(
    "RightsizingRecommendationSummaryTypeDef",
    {
        "TotalRecommendationCount": str,
        "EstimatedTotalMonthlySavingsAmount": str,
        "SavingsCurrencyCode": str,
        "SavingsPercentage": str,
    },
    total=False,
)

RightsizingRecommendationTypeDef = TypedDict(
    "RightsizingRecommendationTypeDef",
    {
        "AccountId": str,
        "CurrentInstance": "CurrentInstanceTypeDef",
        "RightsizingType": RightsizingType,
        "ModifyRecommendationDetail": "ModifyRecommendationDetailTypeDef",
        "TerminateRecommendationDetail": "TerminateRecommendationDetailTypeDef",
    },
    total=False,
)

RootCauseTypeDef = TypedDict(
    "RootCauseTypeDef",
    {"Service": str, "Region": str, "LinkedAccount": str, "UsageType": str},
    total=False,
)

SavingsPlansAmortizedCommitmentTypeDef = TypedDict(
    "SavingsPlansAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)

SavingsPlansCoverageDataTypeDef = TypedDict(
    "SavingsPlansCoverageDataTypeDef",
    {
        "SpendCoveredBySavingsPlans": str,
        "OnDemandCost": str,
        "TotalCost": str,
        "CoveragePercentage": str,
    },
    total=False,
)

SavingsPlansCoverageTypeDef = TypedDict(
    "SavingsPlansCoverageTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": "SavingsPlansCoverageDataTypeDef",
        "TimePeriod": "DateIntervalTypeDef",
    },
    total=False,
)

SavingsPlansDetailsTypeDef = TypedDict(
    "SavingsPlansDetailsTypeDef",
    {"Region": str, "InstanceFamily": str, "OfferingId": str},
    total=False,
)

SavingsPlansPurchaseRecommendationDetailTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    {
        "SavingsPlansDetails": "SavingsPlansDetailsTypeDef",
        "AccountId": str,
        "UpfrontCost": str,
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedSPCost": str,
        "EstimatedOnDemandCost": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
        "EstimatedSavingsAmount": str,
        "EstimatedSavingsPercentage": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedAverageUtilization": str,
        "EstimatedMonthlySavingsAmount": str,
        "CurrentMinimumHourlyOnDemandSpend": str,
        "CurrentMaximumHourlyOnDemandSpend": str,
        "CurrentAverageHourlyOnDemandSpend": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationMetadataTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    {"RecommendationId": str, "GenerationTimestamp": str, "AdditionalMetadata": str},
    total=False,
)

SavingsPlansPurchaseRecommendationSummaryTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    {
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedTotalCost": str,
        "CurrentOnDemandSpend": str,
        "EstimatedSavingsAmount": str,
        "TotalRecommendationCount": str,
        "DailyCommitmentToPurchase": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedSavingsPercentage": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationTypeDef",
    {
        "AccountScope": AccountScope,
        "SavingsPlansType": SupportedSavingsPlansType,
        "TermInYears": TermInYears,
        "PaymentOption": PaymentOption,
        "LookbackPeriodInDays": LookbackPeriodInDays,
        "SavingsPlansPurchaseRecommendationDetails": List[
            "SavingsPlansPurchaseRecommendationDetailTypeDef"
        ],
        "SavingsPlansPurchaseRecommendationSummary": "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    },
    total=False,
)

SavingsPlansSavingsTypeDef = TypedDict(
    "SavingsPlansSavingsTypeDef", {"NetSavings": str, "OnDemandCostEquivalent": str}, total=False
)

_RequiredSavingsPlansUtilizationAggregatesTypeDef = TypedDict(
    "_RequiredSavingsPlansUtilizationAggregatesTypeDef",
    {"Utilization": "SavingsPlansUtilizationTypeDef"},
)
_OptionalSavingsPlansUtilizationAggregatesTypeDef = TypedDict(
    "_OptionalSavingsPlansUtilizationAggregatesTypeDef",
    {
        "Savings": "SavingsPlansSavingsTypeDef",
        "AmortizedCommitment": "SavingsPlansAmortizedCommitmentTypeDef",
    },
    total=False,
)


class SavingsPlansUtilizationAggregatesTypeDef(
    _RequiredSavingsPlansUtilizationAggregatesTypeDef,
    _OptionalSavingsPlansUtilizationAggregatesTypeDef,
):
    pass


_RequiredSavingsPlansUtilizationByTimeTypeDef = TypedDict(
    "_RequiredSavingsPlansUtilizationByTimeTypeDef",
    {"TimePeriod": "DateIntervalTypeDef", "Utilization": "SavingsPlansUtilizationTypeDef"},
)
_OptionalSavingsPlansUtilizationByTimeTypeDef = TypedDict(
    "_OptionalSavingsPlansUtilizationByTimeTypeDef",
    {
        "Savings": "SavingsPlansSavingsTypeDef",
        "AmortizedCommitment": "SavingsPlansAmortizedCommitmentTypeDef",
    },
    total=False,
)


class SavingsPlansUtilizationByTimeTypeDef(
    _RequiredSavingsPlansUtilizationByTimeTypeDef, _OptionalSavingsPlansUtilizationByTimeTypeDef
):
    pass


SavingsPlansUtilizationDetailTypeDef = TypedDict(
    "SavingsPlansUtilizationDetailTypeDef",
    {
        "SavingsPlanArn": str,
        "Attributes": Dict[str, str],
        "Utilization": "SavingsPlansUtilizationTypeDef",
        "Savings": "SavingsPlansSavingsTypeDef",
        "AmortizedCommitment": "SavingsPlansAmortizedCommitmentTypeDef",
    },
    total=False,
)

SavingsPlansUtilizationTypeDef = TypedDict(
    "SavingsPlansUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)

ServiceSpecificationTypeDef = TypedDict(
    "ServiceSpecificationTypeDef", {"EC2Specification": "EC2SpecificationTypeDef"}, total=False
)

SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {"Address": str, "Type": SubscriberType, "Status": SubscriberStatus},
    total=False,
)

TagValuesTypeDef = TypedDict(
    "TagValuesTypeDef",
    {"Key": str, "Values": List[str], "MatchOptions": List[MatchOption]},
    total=False,
)

TargetInstanceTypeDef = TypedDict(
    "TargetInstanceTypeDef",
    {
        "EstimatedMonthlyCost": str,
        "EstimatedMonthlySavings": str,
        "CurrencyCode": str,
        "DefaultTargetInstance": bool,
        "ResourceDetails": "ResourceDetailsTypeDef",
        "ExpectedResourceUtilization": "ResourceUtilizationTypeDef",
    },
    total=False,
)

TerminateRecommendationDetailTypeDef = TypedDict(
    "TerminateRecommendationDetailTypeDef",
    {"EstimatedMonthlySavings": str, "CurrencyCode": str},
    total=False,
)

UtilizationByTimeTypeDef = TypedDict(
    "UtilizationByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Groups": List["ReservationUtilizationGroupTypeDef"],
        "Total": "ReservationAggregatesTypeDef",
    },
    total=False,
)

_RequiredAnomalyDateIntervalTypeDef = TypedDict(
    "_RequiredAnomalyDateIntervalTypeDef", {"StartDate": str}
)
_OptionalAnomalyDateIntervalTypeDef = TypedDict(
    "_OptionalAnomalyDateIntervalTypeDef", {"EndDate": str}, total=False
)


class AnomalyDateIntervalTypeDef(
    _RequiredAnomalyDateIntervalTypeDef, _OptionalAnomalyDateIntervalTypeDef
):
    pass


CreateAnomalyMonitorResponseTypeDef = TypedDict(
    "CreateAnomalyMonitorResponseTypeDef", {"MonitorArn": str}
)

CreateAnomalySubscriptionResponseTypeDef = TypedDict(
    "CreateAnomalySubscriptionResponseTypeDef", {"SubscriptionArn": str}
)

CreateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "CreateCostCategoryDefinitionResponseTypeDef",
    {"CostCategoryArn": str, "EffectiveStart": str},
    total=False,
)

DeleteCostCategoryDefinitionResponseTypeDef = TypedDict(
    "DeleteCostCategoryDefinitionResponseTypeDef",
    {"CostCategoryArn": str, "EffectiveEnd": str},
    total=False,
)

DescribeCostCategoryDefinitionResponseTypeDef = TypedDict(
    "DescribeCostCategoryDefinitionResponseTypeDef",
    {"CostCategory": "CostCategoryTypeDef"},
    total=False,
)

ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "Or": List[Dict[str, Any]],
        "And": List[Dict[str, Any]],
        "Not": Dict[str, Any],
        "Dimensions": "DimensionValuesTypeDef",
        "Tags": "TagValuesTypeDef",
        "CostCategories": "CostCategoryValuesTypeDef",
    },
    total=False,
)

_RequiredGetAnomaliesResponseTypeDef = TypedDict(
    "_RequiredGetAnomaliesResponseTypeDef", {"Anomalies": List["AnomalyTypeDef"]}
)
_OptionalGetAnomaliesResponseTypeDef = TypedDict(
    "_OptionalGetAnomaliesResponseTypeDef", {"NextPageToken": str}, total=False
)


class GetAnomaliesResponseTypeDef(
    _RequiredGetAnomaliesResponseTypeDef, _OptionalGetAnomaliesResponseTypeDef
):
    pass


_RequiredGetAnomalyMonitorsResponseTypeDef = TypedDict(
    "_RequiredGetAnomalyMonitorsResponseTypeDef", {"AnomalyMonitors": List["AnomalyMonitorTypeDef"]}
)
_OptionalGetAnomalyMonitorsResponseTypeDef = TypedDict(
    "_OptionalGetAnomalyMonitorsResponseTypeDef", {"NextPageToken": str}, total=False
)


class GetAnomalyMonitorsResponseTypeDef(
    _RequiredGetAnomalyMonitorsResponseTypeDef, _OptionalGetAnomalyMonitorsResponseTypeDef
):
    pass


_RequiredGetAnomalySubscriptionsResponseTypeDef = TypedDict(
    "_RequiredGetAnomalySubscriptionsResponseTypeDef",
    {"AnomalySubscriptions": List["AnomalySubscriptionTypeDef"]},
)
_OptionalGetAnomalySubscriptionsResponseTypeDef = TypedDict(
    "_OptionalGetAnomalySubscriptionsResponseTypeDef", {"NextPageToken": str}, total=False
)


class GetAnomalySubscriptionsResponseTypeDef(
    _RequiredGetAnomalySubscriptionsResponseTypeDef, _OptionalGetAnomalySubscriptionsResponseTypeDef
):
    pass


GetCostAndUsageResponseTypeDef = TypedDict(
    "GetCostAndUsageResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List["GroupDefinitionTypeDef"],
        "ResultsByTime": List["ResultByTimeTypeDef"],
        "DimensionValueAttributes": List["DimensionValuesWithAttributesTypeDef"],
    },
    total=False,
)

GetCostAndUsageWithResourcesResponseTypeDef = TypedDict(
    "GetCostAndUsageWithResourcesResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List["GroupDefinitionTypeDef"],
        "ResultsByTime": List["ResultByTimeTypeDef"],
        "DimensionValueAttributes": List["DimensionValuesWithAttributesTypeDef"],
    },
    total=False,
)

_RequiredGetCostCategoriesResponseTypeDef = TypedDict(
    "_RequiredGetCostCategoriesResponseTypeDef", {"ReturnSize": int, "TotalSize": int}
)
_OptionalGetCostCategoriesResponseTypeDef = TypedDict(
    "_OptionalGetCostCategoriesResponseTypeDef",
    {"NextPageToken": str, "CostCategoryNames": List[str], "CostCategoryValues": List[str]},
    total=False,
)


class GetCostCategoriesResponseTypeDef(
    _RequiredGetCostCategoriesResponseTypeDef, _OptionalGetCostCategoriesResponseTypeDef
):
    pass


GetCostForecastResponseTypeDef = TypedDict(
    "GetCostForecastResponseTypeDef",
    {"Total": "MetricValueTypeDef", "ForecastResultsByTime": List["ForecastResultTypeDef"]},
    total=False,
)

_RequiredGetDimensionValuesResponseTypeDef = TypedDict(
    "_RequiredGetDimensionValuesResponseTypeDef",
    {
        "DimensionValues": List["DimensionValuesWithAttributesTypeDef"],
        "ReturnSize": int,
        "TotalSize": int,
    },
)
_OptionalGetDimensionValuesResponseTypeDef = TypedDict(
    "_OptionalGetDimensionValuesResponseTypeDef", {"NextPageToken": str}, total=False
)


class GetDimensionValuesResponseTypeDef(
    _RequiredGetDimensionValuesResponseTypeDef, _OptionalGetDimensionValuesResponseTypeDef
):
    pass


_RequiredGetReservationCoverageResponseTypeDef = TypedDict(
    "_RequiredGetReservationCoverageResponseTypeDef",
    {"CoveragesByTime": List["CoverageByTimeTypeDef"]},
)
_OptionalGetReservationCoverageResponseTypeDef = TypedDict(
    "_OptionalGetReservationCoverageResponseTypeDef",
    {"Total": "CoverageTypeDef", "NextPageToken": str},
    total=False,
)


class GetReservationCoverageResponseTypeDef(
    _RequiredGetReservationCoverageResponseTypeDef, _OptionalGetReservationCoverageResponseTypeDef
):
    pass


GetReservationPurchaseRecommendationResponseTypeDef = TypedDict(
    "GetReservationPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": "ReservationPurchaseRecommendationMetadataTypeDef",
        "Recommendations": List["ReservationPurchaseRecommendationTypeDef"],
        "NextPageToken": str,
    },
    total=False,
)

_RequiredGetReservationUtilizationResponseTypeDef = TypedDict(
    "_RequiredGetReservationUtilizationResponseTypeDef",
    {"UtilizationsByTime": List["UtilizationByTimeTypeDef"]},
)
_OptionalGetReservationUtilizationResponseTypeDef = TypedDict(
    "_OptionalGetReservationUtilizationResponseTypeDef",
    {"Total": "ReservationAggregatesTypeDef", "NextPageToken": str},
    total=False,
)


class GetReservationUtilizationResponseTypeDef(
    _RequiredGetReservationUtilizationResponseTypeDef,
    _OptionalGetReservationUtilizationResponseTypeDef,
):
    pass


GetRightsizingRecommendationResponseTypeDef = TypedDict(
    "GetRightsizingRecommendationResponseTypeDef",
    {
        "Metadata": "RightsizingRecommendationMetadataTypeDef",
        "Summary": "RightsizingRecommendationSummaryTypeDef",
        "RightsizingRecommendations": List["RightsizingRecommendationTypeDef"],
        "NextPageToken": str,
        "Configuration": "RightsizingRecommendationConfigurationTypeDef",
    },
    total=False,
)

_RequiredGetSavingsPlansCoverageResponseTypeDef = TypedDict(
    "_RequiredGetSavingsPlansCoverageResponseTypeDef",
    {"SavingsPlansCoverages": List["SavingsPlansCoverageTypeDef"]},
)
_OptionalGetSavingsPlansCoverageResponseTypeDef = TypedDict(
    "_OptionalGetSavingsPlansCoverageResponseTypeDef", {"NextToken": str}, total=False
)


class GetSavingsPlansCoverageResponseTypeDef(
    _RequiredGetSavingsPlansCoverageResponseTypeDef, _OptionalGetSavingsPlansCoverageResponseTypeDef
):
    pass


GetSavingsPlansPurchaseRecommendationResponseTypeDef = TypedDict(
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": "SavingsPlansPurchaseRecommendationMetadataTypeDef",
        "SavingsPlansPurchaseRecommendation": "SavingsPlansPurchaseRecommendationTypeDef",
        "NextPageToken": str,
    },
    total=False,
)

_RequiredGetSavingsPlansUtilizationDetailsResponseTypeDef = TypedDict(
    "_RequiredGetSavingsPlansUtilizationDetailsResponseTypeDef",
    {
        "SavingsPlansUtilizationDetails": List["SavingsPlansUtilizationDetailTypeDef"],
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetSavingsPlansUtilizationDetailsResponseTypeDef = TypedDict(
    "_OptionalGetSavingsPlansUtilizationDetailsResponseTypeDef",
    {"Total": "SavingsPlansUtilizationAggregatesTypeDef", "NextToken": str},
    total=False,
)


class GetSavingsPlansUtilizationDetailsResponseTypeDef(
    _RequiredGetSavingsPlansUtilizationDetailsResponseTypeDef,
    _OptionalGetSavingsPlansUtilizationDetailsResponseTypeDef,
):
    pass


_RequiredGetSavingsPlansUtilizationResponseTypeDef = TypedDict(
    "_RequiredGetSavingsPlansUtilizationResponseTypeDef",
    {"Total": "SavingsPlansUtilizationAggregatesTypeDef"},
)
_OptionalGetSavingsPlansUtilizationResponseTypeDef = TypedDict(
    "_OptionalGetSavingsPlansUtilizationResponseTypeDef",
    {"SavingsPlansUtilizationsByTime": List["SavingsPlansUtilizationByTimeTypeDef"]},
    total=False,
)


class GetSavingsPlansUtilizationResponseTypeDef(
    _RequiredGetSavingsPlansUtilizationResponseTypeDef,
    _OptionalGetSavingsPlansUtilizationResponseTypeDef,
):
    pass


_RequiredGetTagsResponseTypeDef = TypedDict(
    "_RequiredGetTagsResponseTypeDef", {"Tags": List[str], "ReturnSize": int, "TotalSize": int}
)
_OptionalGetTagsResponseTypeDef = TypedDict(
    "_OptionalGetTagsResponseTypeDef", {"NextPageToken": str}, total=False
)


class GetTagsResponseTypeDef(_RequiredGetTagsResponseTypeDef, _OptionalGetTagsResponseTypeDef):
    pass


GetUsageForecastResponseTypeDef = TypedDict(
    "GetUsageForecastResponseTypeDef",
    {"Total": "MetricValueTypeDef", "ForecastResultsByTime": List["ForecastResultTypeDef"]},
    total=False,
)

ListCostCategoryDefinitionsResponseTypeDef = TypedDict(
    "ListCostCategoryDefinitionsResponseTypeDef",
    {"CostCategoryReferences": List["CostCategoryReferenceTypeDef"], "NextToken": str},
    total=False,
)

ProvideAnomalyFeedbackResponseTypeDef = TypedDict(
    "ProvideAnomalyFeedbackResponseTypeDef", {"AnomalyId": str}
)

_RequiredSortDefinitionTypeDef = TypedDict("_RequiredSortDefinitionTypeDef", {"Key": str})
_OptionalSortDefinitionTypeDef = TypedDict(
    "_OptionalSortDefinitionTypeDef", {"SortOrder": SortOrder}, total=False
)


class SortDefinitionTypeDef(_RequiredSortDefinitionTypeDef, _OptionalSortDefinitionTypeDef):
    pass


_RequiredTotalImpactFilterTypeDef = TypedDict(
    "_RequiredTotalImpactFilterTypeDef", {"NumericOperator": NumericOperator, "StartValue": float}
)
_OptionalTotalImpactFilterTypeDef = TypedDict(
    "_OptionalTotalImpactFilterTypeDef", {"EndValue": float}, total=False
)


class TotalImpactFilterTypeDef(
    _RequiredTotalImpactFilterTypeDef, _OptionalTotalImpactFilterTypeDef
):
    pass


UpdateAnomalyMonitorResponseTypeDef = TypedDict(
    "UpdateAnomalyMonitorResponseTypeDef", {"MonitorArn": str}
)

UpdateAnomalySubscriptionResponseTypeDef = TypedDict(
    "UpdateAnomalySubscriptionResponseTypeDef", {"SubscriptionArn": str}
)

UpdateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "UpdateCostCategoryDefinitionResponseTypeDef",
    {"CostCategoryArn": str, "EffectiveStart": str},
    total=False,
)
