"""
Main interface for iot-jobs-data service type definitions.

Usage::

    ```python
    from mypy_boto3_iot_jobs_data.type_defs import JobExecutionStateTypeDef

    data: JobExecutionStateTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_iot_jobs_data.literals import JobExecutionStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "JobExecutionStateTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "DescribeJobExecutionResponseTypeDef",
    "GetPendingJobExecutionsResponseTypeDef",
    "StartNextPendingJobExecutionResponseTypeDef",
    "UpdateJobExecutionResponseTypeDef",
)

JobExecutionStateTypeDef = TypedDict(
    "JobExecutionStateTypeDef",
    {"status": JobExecutionStatus, "statusDetails": Dict[str, str], "versionNumber": int},
    total=False,
)

JobExecutionSummaryTypeDef = TypedDict(
    "JobExecutionSummaryTypeDef",
    {
        "jobId": str,
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "versionNumber": int,
        "executionNumber": int,
    },
    total=False,
)

JobExecutionTypeDef = TypedDict(
    "JobExecutionTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": JobExecutionStatus,
        "statusDetails": Dict[str, str],
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "approximateSecondsBeforeTimedOut": int,
        "versionNumber": int,
        "executionNumber": int,
        "jobDocument": str,
    },
    total=False,
)

DescribeJobExecutionResponseTypeDef = TypedDict(
    "DescribeJobExecutionResponseTypeDef", {"execution": "JobExecutionTypeDef"}, total=False
)

GetPendingJobExecutionsResponseTypeDef = TypedDict(
    "GetPendingJobExecutionsResponseTypeDef",
    {
        "inProgressJobs": List["JobExecutionSummaryTypeDef"],
        "queuedJobs": List["JobExecutionSummaryTypeDef"],
    },
    total=False,
)

StartNextPendingJobExecutionResponseTypeDef = TypedDict(
    "StartNextPendingJobExecutionResponseTypeDef", {"execution": "JobExecutionTypeDef"}, total=False
)

UpdateJobExecutionResponseTypeDef = TypedDict(
    "UpdateJobExecutionResponseTypeDef",
    {"executionState": "JobExecutionStateTypeDef", "jobDocument": str},
    total=False,
)
