"""
Main interface for rds-data service literal definitions.

Usage::

    ```python
    from mypy_boto3_rds_data.literals import DecimalReturnType

    data: DecimalReturnType = "DOUBLE_OR_LONG"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DecimalReturnType", "TypeHint")


DecimalReturnType = Literal["DOUBLE_OR_LONG", "STRING"]
TypeHint = Literal["DATE", "DECIMAL", "JSON", "TIME", "TIMESTAMP", "UUID"]
