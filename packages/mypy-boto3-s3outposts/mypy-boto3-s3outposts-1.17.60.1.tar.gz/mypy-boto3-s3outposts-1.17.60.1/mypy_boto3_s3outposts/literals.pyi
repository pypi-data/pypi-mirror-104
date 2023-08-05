"""
Main interface for s3outposts service literal definitions.

Usage::

    ```python
    from mypy_boto3_s3outposts.literals import EndpointStatus

    data: EndpointStatus = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EndpointStatus", "ListEndpointsPaginatorName")

EndpointStatus = Literal["AVAILABLE", "PENDING"]
ListEndpointsPaginatorName = Literal["list_endpoints"]
