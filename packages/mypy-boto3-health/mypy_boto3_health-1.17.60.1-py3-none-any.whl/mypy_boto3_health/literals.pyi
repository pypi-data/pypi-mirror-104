"""
Main interface for health service literal definitions.

Usage::

    ```python
    from mypy_boto3_health.literals import DescribeAffectedAccountsForOrganizationPaginatorName

    data: DescribeAffectedAccountsForOrganizationPaginatorName = "describe_affected_accounts_for_organization"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeAffectedAccountsForOrganizationPaginatorName",
    "DescribeAffectedEntitiesForOrganizationPaginatorName",
    "DescribeAffectedEntitiesPaginatorName",
    "DescribeEventAggregatesPaginatorName",
    "DescribeEventTypesPaginatorName",
    "DescribeEventsForOrganizationPaginatorName",
    "DescribeEventsPaginatorName",
    "entityStatusCode",
    "eventAggregateField",
    "eventScopeCode",
    "eventStatusCode",
    "eventTypeCategory",
)

DescribeAffectedAccountsForOrganizationPaginatorName = Literal[
    "describe_affected_accounts_for_organization"
]
DescribeAffectedEntitiesForOrganizationPaginatorName = Literal[
    "describe_affected_entities_for_organization"
]
DescribeAffectedEntitiesPaginatorName = Literal["describe_affected_entities"]
DescribeEventAggregatesPaginatorName = Literal["describe_event_aggregates"]
DescribeEventTypesPaginatorName = Literal["describe_event_types"]
DescribeEventsForOrganizationPaginatorName = Literal["describe_events_for_organization"]
DescribeEventsPaginatorName = Literal["describe_events"]
entityStatusCode = Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]
eventAggregateField = Literal["eventTypeCategory"]
eventScopeCode = Literal["ACCOUNT_SPECIFIC", "NONE", "PUBLIC"]
eventStatusCode = Literal["closed", "open", "upcoming"]
eventTypeCategory = Literal["accountNotification", "investigation", "issue", "scheduledChange"]
