"""
Main interface for codeguruprofiler service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_codeguruprofiler import CodeGuruProfilerClient
    from mypy_boto3_codeguruprofiler.paginator import (
        ListProfileTimesPaginator,
    )

    client: CodeGuruProfilerClient = boto3.client("codeguruprofiler")

    list_profile_times_paginator: ListProfileTimesPaginator = client.get_paginator("list_profile_times")
    ```
"""
from datetime import datetime
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codeguruprofiler.literals import AggregationPeriod, OrderBy
from mypy_boto3_codeguruprofiler.type_defs import (
    ListProfileTimesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListProfileTimesPaginator",)


class ListProfileTimesPaginator(Boto3Paginator):
    """
    [Paginator.ListProfileTimes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguruprofiler.html#CodeGuruProfiler.Paginator.ListProfileTimes)
    """

    def paginate(
        self,
        endTime: datetime,
        period: AggregationPeriod,
        profilingGroupName: str,
        startTime: datetime,
        orderBy: OrderBy = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListProfileTimesResponseTypeDef]:
        """
        [ListProfileTimes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguruprofiler.html#CodeGuruProfiler.Paginator.ListProfileTimes.paginate)
        """
