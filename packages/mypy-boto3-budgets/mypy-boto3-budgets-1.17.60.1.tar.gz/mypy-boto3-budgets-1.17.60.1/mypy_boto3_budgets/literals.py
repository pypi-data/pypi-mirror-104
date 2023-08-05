"""
Main interface for budgets service literal definitions.

Usage::

    ```python
    from mypy_boto3_budgets.literals import ActionStatus

    data: ActionStatus = "EXECUTION_FAILURE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionStatus",
    "ActionSubType",
    "ActionType",
    "ApprovalModel",
    "BudgetType",
    "ComparisonOperator",
    "DescribeBudgetActionHistoriesPaginatorName",
    "DescribeBudgetActionsForAccountPaginatorName",
    "DescribeBudgetActionsForBudgetPaginatorName",
    "DescribeBudgetPerformanceHistoryPaginatorName",
    "DescribeBudgetsPaginatorName",
    "DescribeNotificationsForBudgetPaginatorName",
    "DescribeSubscribersForNotificationPaginatorName",
    "EventType",
    "ExecutionType",
    "NotificationState",
    "NotificationType",
    "SubscriptionType",
    "ThresholdType",
    "TimeUnit",
)


ActionStatus = Literal[
    "EXECUTION_FAILURE",
    "EXECUTION_IN_PROGRESS",
    "EXECUTION_SUCCESS",
    "PENDING",
    "RESET_FAILURE",
    "RESET_IN_PROGRESS",
    "REVERSE_FAILURE",
    "REVERSE_IN_PROGRESS",
    "REVERSE_SUCCESS",
    "STANDBY",
]
ActionSubType = Literal["STOP_EC2_INSTANCES", "STOP_RDS_INSTANCES"]
ActionType = Literal["APPLY_IAM_POLICY", "APPLY_SCP_POLICY", "RUN_SSM_DOCUMENTS"]
ApprovalModel = Literal["AUTOMATIC", "MANUAL"]
BudgetType = Literal[
    "COST",
    "RI_COVERAGE",
    "RI_UTILIZATION",
    "SAVINGS_PLANS_COVERAGE",
    "SAVINGS_PLANS_UTILIZATION",
    "USAGE",
]
ComparisonOperator = Literal["EQUAL_TO", "GREATER_THAN", "LESS_THAN"]
DescribeBudgetActionHistoriesPaginatorName = Literal["describe_budget_action_histories"]
DescribeBudgetActionsForAccountPaginatorName = Literal["describe_budget_actions_for_account"]
DescribeBudgetActionsForBudgetPaginatorName = Literal["describe_budget_actions_for_budget"]
DescribeBudgetPerformanceHistoryPaginatorName = Literal["describe_budget_performance_history"]
DescribeBudgetsPaginatorName = Literal["describe_budgets"]
DescribeNotificationsForBudgetPaginatorName = Literal["describe_notifications_for_budget"]
DescribeSubscribersForNotificationPaginatorName = Literal["describe_subscribers_for_notification"]
EventType = Literal["CREATE_ACTION", "DELETE_ACTION", "EXECUTE_ACTION", "SYSTEM", "UPDATE_ACTION"]
ExecutionType = Literal[
    "APPROVE_BUDGET_ACTION", "RESET_BUDGET_ACTION", "RETRY_BUDGET_ACTION", "REVERSE_BUDGET_ACTION"
]
NotificationState = Literal["ALARM", "OK"]
NotificationType = Literal["ACTUAL", "FORECASTED"]
SubscriptionType = Literal["EMAIL", "SNS"]
ThresholdType = Literal["ABSOLUTE_VALUE", "PERCENTAGE"]
TimeUnit = Literal["ANNUALLY", "DAILY", "MONTHLY", "QUARTERLY"]
