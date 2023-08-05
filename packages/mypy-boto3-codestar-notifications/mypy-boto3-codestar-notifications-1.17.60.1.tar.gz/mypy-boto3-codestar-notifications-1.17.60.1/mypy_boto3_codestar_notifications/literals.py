"""
Main interface for codestar-notifications service literal definitions.

Usage::

    ```python
    from mypy_boto3_codestar_notifications.literals import DetailType

    data: DetailType = "BASIC"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DetailType",
    "ListEventTypesFilterName",
    "ListEventTypesPaginatorName",
    "ListNotificationRulesFilterName",
    "ListNotificationRulesPaginatorName",
    "ListTargetsFilterName",
    "ListTargetsPaginatorName",
    "NotificationRuleStatus",
    "TargetStatus",
)


DetailType = Literal["BASIC", "FULL"]
ListEventTypesFilterName = Literal["RESOURCE_TYPE", "SERVICE_NAME"]
ListEventTypesPaginatorName = Literal["list_event_types"]
ListNotificationRulesFilterName = Literal[
    "CREATED_BY", "EVENT_TYPE_ID", "RESOURCE", "TARGET_ADDRESS"
]
ListNotificationRulesPaginatorName = Literal["list_notification_rules"]
ListTargetsFilterName = Literal["TARGET_ADDRESS", "TARGET_STATUS", "TARGET_TYPE"]
ListTargetsPaginatorName = Literal["list_targets"]
NotificationRuleStatus = Literal["DISABLED", "ENABLED"]
TargetStatus = Literal["ACTIVE", "DEACTIVATED", "INACTIVE", "PENDING", "UNREACHABLE"]
