"""
Main interface for iotdeviceadvisor service literal definitions.

Usage::

    ```python
    from mypy_boto3_iotdeviceadvisor.literals import Status

    data: Status = "CANCELED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Status", "SuiteRunStatus")


Status = Literal["CANCELED", "ERROR", "FAIL", "PASS", "PASS_WITH_WARNINGS", "PENDING", "RUNNING"]
SuiteRunStatus = Literal[
    "CANCELED", "ERROR", "FAIL", "PASS", "PASS_WITH_WARNINGS", "PENDING", "RUNNING"
]
