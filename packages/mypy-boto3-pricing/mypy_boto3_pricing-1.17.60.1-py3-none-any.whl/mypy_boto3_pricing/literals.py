"""
Main interface for pricing service literal definitions.

Usage::

    ```python
    from mypy_boto3_pricing.literals import DescribeServicesPaginatorName

    data: DescribeServicesPaginatorName = "describe_services"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeServicesPaginatorName",
    "FilterType",
    "GetAttributeValuesPaginatorName",
    "GetProductsPaginatorName",
)


DescribeServicesPaginatorName = Literal["describe_services"]
FilterType = Literal["TERM_MATCH"]
GetAttributeValuesPaginatorName = Literal["get_attribute_values"]
GetProductsPaginatorName = Literal["get_products"]
