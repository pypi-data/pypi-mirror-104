"""
Main interface for macie service literal definitions.

Usage::

    ```python
    from mypy_boto3_macie.literals import ListMemberAccountsPaginatorName

    data: ListMemberAccountsPaginatorName = "list_member_accounts"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListMemberAccountsPaginatorName",
    "ListS3ResourcesPaginatorName",
    "S3ContinuousClassificationType",
    "S3OneTimeClassificationType",
)

ListMemberAccountsPaginatorName = Literal["list_member_accounts"]
ListS3ResourcesPaginatorName = Literal["list_s3_resources"]
S3ContinuousClassificationType = Literal["FULL"]
S3OneTimeClassificationType = Literal["FULL", "NONE"]
