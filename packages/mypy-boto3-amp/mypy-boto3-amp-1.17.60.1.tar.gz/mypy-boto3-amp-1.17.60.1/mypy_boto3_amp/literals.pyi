"""
Main interface for amp service literal definitions.

Usage::

    ```python
    from mypy_boto3_amp.literals import ListWorkspacesPaginatorName

    data: ListWorkspacesPaginatorName = "list_workspaces"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListWorkspacesPaginatorName", "WorkspaceStatusCode")

ListWorkspacesPaginatorName = Literal["list_workspaces"]
WorkspaceStatusCode = Literal["ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATING"]
