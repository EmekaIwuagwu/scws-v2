"""
Utility modules
"""

from .logger import logger, setup_logging, get_logger
from .errors import (
    AppError,
    ADBConnectionError,
    ADBDeviceNotFoundError,
    ADBDeviceUnauthorizedError,
    ADBDeviceOfflineError,
    ScrcpyDeployError,
    ScrcpyStartError,
    ScrcpyServerCrashError,
    StreamNotFoundError,
    StreamAlreadyActiveError,
    ValidationError,
    NotFoundError,
)

__all__ = [
    "logger",
    "setup_logging",
    "get_logger",
    "AppError",
    "ADBConnectionError",
    "ADBDeviceNotFoundError",
    "ADBDeviceUnauthorizedError",
    "ADBDeviceOfflineError",
    "ScrcpyDeployError",
    "ScrcpyStartError",
    "ScrcpyServerCrashError",
    "StreamNotFoundError",
    "StreamAlreadyActiveError",
    "ValidationError",
    "NotFoundError",
]
