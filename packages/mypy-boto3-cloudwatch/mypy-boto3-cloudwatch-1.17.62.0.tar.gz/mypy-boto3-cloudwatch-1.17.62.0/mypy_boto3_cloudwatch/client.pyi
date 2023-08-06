"""
Main interface for cloudwatch service client

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudwatch import CloudWatchClient

    client: CloudWatchClient = boto3.client("cloudwatch")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_cloudwatch.literals import (
    AlarmExistsWaiterName,
    AlarmType,
    ComparisonOperator,
    CompositeAlarmExistsWaiterName,
    DescribeAlarmHistoryPaginatorName,
    DescribeAlarmsPaginatorName,
    GetMetricDataPaginatorName,
    HistoryItemType,
    ListDashboardsPaginatorName,
    ListMetricsPaginatorName,
    MetricStreamOutputFormat,
    RecentlyActive,
    ScanBy,
    StandardUnit,
    StateValue,
    Statistic,
)
from mypy_boto3_cloudwatch.paginator import (
    DescribeAlarmHistoryPaginator,
    DescribeAlarmsPaginator,
    GetMetricDataPaginator,
    ListDashboardsPaginator,
    ListMetricsPaginator,
)
from mypy_boto3_cloudwatch.type_defs import (
    AnomalyDetectorConfigurationTypeDef,
    DeleteInsightRulesOutputTypeDef,
    DescribeAlarmHistoryOutputTypeDef,
    DescribeAlarmsForMetricOutputTypeDef,
    DescribeAlarmsOutputTypeDef,
    DescribeAnomalyDetectorsOutputTypeDef,
    DescribeInsightRulesOutputTypeDef,
    DimensionFilterTypeDef,
    DimensionTypeDef,
    DisableInsightRulesOutputTypeDef,
    EnableInsightRulesOutputTypeDef,
    GetDashboardOutputTypeDef,
    GetInsightRuleReportOutputTypeDef,
    GetMetricDataOutputTypeDef,
    GetMetricStatisticsOutputTypeDef,
    GetMetricStreamOutputTypeDef,
    GetMetricWidgetImageOutputTypeDef,
    LabelOptionsTypeDef,
    ListDashboardsOutputTypeDef,
    ListMetricsOutputTypeDef,
    ListMetricStreamsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    MetricDataQueryTypeDef,
    MetricDatumTypeDef,
    MetricStreamFilterTypeDef,
    PutDashboardOutputTypeDef,
    PutMetricStreamOutputTypeDef,
    TagTypeDef,
)
from mypy_boto3_cloudwatch.waiter import AlarmExistsWaiter, CompositeAlarmExistsWaiter

__all__ = ("CloudWatchClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DashboardInvalidInputError: Type[BotocoreClientError]
    DashboardNotFoundError: Type[BotocoreClientError]
    InternalServiceFault: Type[BotocoreClientError]
    InvalidFormatFault: Type[BotocoreClientError]
    InvalidNextToken: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LimitExceededFault: Type[BotocoreClientError]
    MissingRequiredParameterException: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class CloudWatchClient:
    """
    [CloudWatch.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.can_paginate)
        """
    def delete_alarms(self, AlarmNames: List[str]) -> None:
        """
        [Client.delete_alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.delete_alarms)
        """
    def delete_anomaly_detector(
        self,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: List["DimensionTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.delete_anomaly_detector)
        """
    def delete_dashboards(self, DashboardNames: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.delete_dashboards)
        """
    def delete_insight_rules(self, RuleNames: List[str]) -> DeleteInsightRulesOutputTypeDef:
        """
        [Client.delete_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.delete_insight_rules)
        """
    def delete_metric_stream(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_metric_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.delete_metric_stream)
        """
    def describe_alarm_history(
        self,
        AlarmName: str = None,
        AlarmTypes: List[AlarmType] = None,
        HistoryItemType: HistoryItemType = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
        ScanBy: ScanBy = None,
    ) -> DescribeAlarmHistoryOutputTypeDef:
        """
        [Client.describe_alarm_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarm_history)
        """
    def describe_alarms(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        AlarmTypes: List[AlarmType] = None,
        ChildrenOfAlarmName: str = None,
        ParentsOfAlarmName: str = None,
        StateValue: StateValue = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> DescribeAlarmsOutputTypeDef:
        """
        [Client.describe_alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarms)
        """
    def describe_alarms_for_metric(
        self,
        MetricName: str,
        Namespace: str,
        Statistic: Statistic = None,
        ExtendedStatistic: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
        Period: int = None,
        Unit: StandardUnit = None,
    ) -> DescribeAlarmsForMetricOutputTypeDef:
        """
        [Client.describe_alarms_for_metric documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarms_for_metric)
        """
    def describe_anomaly_detectors(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
    ) -> DescribeAnomalyDetectorsOutputTypeDef:
        """
        [Client.describe_anomaly_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.describe_anomaly_detectors)
        """
    def describe_insight_rules(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeInsightRulesOutputTypeDef:
        """
        [Client.describe_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.describe_insight_rules)
        """
    def disable_alarm_actions(self, AlarmNames: List[str]) -> None:
        """
        [Client.disable_alarm_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.disable_alarm_actions)
        """
    def disable_insight_rules(self, RuleNames: List[str]) -> DisableInsightRulesOutputTypeDef:
        """
        [Client.disable_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.disable_insight_rules)
        """
    def enable_alarm_actions(self, AlarmNames: List[str]) -> None:
        """
        [Client.enable_alarm_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.enable_alarm_actions)
        """
    def enable_insight_rules(self, RuleNames: List[str]) -> EnableInsightRulesOutputTypeDef:
        """
        [Client.enable_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.enable_insight_rules)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.generate_presigned_url)
        """
    def get_dashboard(self, DashboardName: str) -> GetDashboardOutputTypeDef:
        """
        [Client.get_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.get_dashboard)
        """
    def get_insight_rule_report(
        self,
        RuleName: str,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        MaxContributorCount: int = None,
        Metrics: List[str] = None,
        OrderBy: str = None,
    ) -> GetInsightRuleReportOutputTypeDef:
        """
        [Client.get_insight_rule_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.get_insight_rule_report)
        """
    def get_metric_data(
        self,
        MetricDataQueries: List["MetricDataQueryTypeDef"],
        StartTime: datetime,
        EndTime: datetime,
        NextToken: str = None,
        ScanBy: ScanBy = None,
        MaxDatapoints: int = None,
        LabelOptions: LabelOptionsTypeDef = None,
    ) -> GetMetricDataOutputTypeDef:
        """
        [Client.get_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_data)
        """
    def get_metric_statistics(
        self,
        Namespace: str,
        MetricName: str,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: List["DimensionTypeDef"] = None,
        Statistics: List[Statistic] = None,
        ExtendedStatistics: List[str] = None,
        Unit: StandardUnit = None,
    ) -> GetMetricStatisticsOutputTypeDef:
        """
        [Client.get_metric_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_statistics)
        """
    def get_metric_stream(self, Name: str) -> GetMetricStreamOutputTypeDef:
        """
        [Client.get_metric_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_stream)
        """
    def get_metric_widget_image(
        self, MetricWidget: str, OutputFormat: str = None
    ) -> GetMetricWidgetImageOutputTypeDef:
        """
        [Client.get_metric_widget_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_widget_image)
        """
    def list_dashboards(
        self, DashboardNamePrefix: str = None, NextToken: str = None
    ) -> ListDashboardsOutputTypeDef:
        """
        [Client.list_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.list_dashboards)
        """
    def list_metric_streams(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListMetricStreamsOutputTypeDef:
        """
        [Client.list_metric_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.list_metric_streams)
        """
    def list_metrics(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[DimensionFilterTypeDef] = None,
        NextToken: str = None,
        RecentlyActive: RecentlyActive = None,
    ) -> ListMetricsOutputTypeDef:
        """
        [Client.list_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.list_metrics)
        """
    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.list_tags_for_resource)
        """
    def put_anomaly_detector(
        self,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: List["DimensionTypeDef"] = None,
        Configuration: "AnomalyDetectorConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.put_anomaly_detector)
        """
    def put_composite_alarm(
        self,
        AlarmName: str,
        AlarmRule: str,
        ActionsEnabled: bool = None,
        AlarmActions: List[str] = None,
        AlarmDescription: str = None,
        InsufficientDataActions: List[str] = None,
        OKActions: List[str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> None:
        """
        [Client.put_composite_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.put_composite_alarm)
        """
    def put_dashboard(self, DashboardName: str, DashboardBody: str) -> PutDashboardOutputTypeDef:
        """
        [Client.put_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.put_dashboard)
        """
    def put_insight_rule(
        self,
        RuleName: str,
        RuleDefinition: str,
        RuleState: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_insight_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.put_insight_rule)
        """
    def put_metric_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: ComparisonOperator,
        AlarmDescription: str = None,
        ActionsEnabled: bool = None,
        OKActions: List[str] = None,
        AlarmActions: List[str] = None,
        InsufficientDataActions: List[str] = None,
        MetricName: str = None,
        Namespace: str = None,
        Statistic: Statistic = None,
        ExtendedStatistic: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
        Period: int = None,
        Unit: StandardUnit = None,
        DatapointsToAlarm: int = None,
        Threshold: float = None,
        TreatMissingData: str = None,
        EvaluateLowSampleCountPercentile: str = None,
        Metrics: List["MetricDataQueryTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        ThresholdMetricId: str = None,
    ) -> None:
        """
        [Client.put_metric_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_alarm)
        """
    def put_metric_data(self, Namespace: str, MetricData: List[MetricDatumTypeDef]) -> None:
        """
        [Client.put_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data)
        """
    def put_metric_stream(
        self,
        Name: str,
        FirehoseArn: str,
        RoleArn: str,
        OutputFormat: MetricStreamOutputFormat,
        IncludeFilters: List["MetricStreamFilterTypeDef"] = None,
        ExcludeFilters: List["MetricStreamFilterTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> PutMetricStreamOutputTypeDef:
        """
        [Client.put_metric_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_stream)
        """
    def set_alarm_state(
        self, AlarmName: str, StateValue: StateValue, StateReason: str, StateReasonData: str = None
    ) -> None:
        """
        [Client.set_alarm_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.set_alarm_state)
        """
    def start_metric_streams(self, Names: List[str]) -> Dict[str, Any]:
        """
        [Client.start_metric_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.start_metric_streams)
        """
    def stop_metric_streams(self, Names: List[str]) -> Dict[str, Any]:
        """
        [Client.stop_metric_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.stop_metric_streams)
        """
    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.tag_resource)
        """
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Client.untag_resource)
        """
    @overload
    def get_paginator(
        self, operation_name: DescribeAlarmHistoryPaginatorName
    ) -> DescribeAlarmHistoryPaginator:
        """
        [Paginator.DescribeAlarmHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarmHistory)
        """
    @overload
    def get_paginator(self, operation_name: DescribeAlarmsPaginatorName) -> DescribeAlarmsPaginator:
        """
        [Paginator.DescribeAlarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarms)
        """
    @overload
    def get_paginator(self, operation_name: GetMetricDataPaginatorName) -> GetMetricDataPaginator:
        """
        [Paginator.GetMetricData documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Paginator.GetMetricData)
        """
    @overload
    def get_paginator(self, operation_name: ListDashboardsPaginatorName) -> ListDashboardsPaginator:
        """
        [Paginator.ListDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Paginator.ListDashboards)
        """
    @overload
    def get_paginator(self, operation_name: ListMetricsPaginatorName) -> ListMetricsPaginator:
        """
        [Paginator.ListMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Paginator.ListMetrics)
        """
    @overload
    def get_waiter(self, waiter_name: AlarmExistsWaiterName) -> AlarmExistsWaiter:
        """
        [Waiter.AlarmExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Waiter.AlarmExists)
        """
    @overload
    def get_waiter(self, waiter_name: CompositeAlarmExistsWaiterName) -> CompositeAlarmExistsWaiter:
        """
        [Waiter.CompositeAlarmExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/cloudwatch.html#CloudWatch.Waiter.CompositeAlarmExists)
        """
