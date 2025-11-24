"""
Pydantic models for request/response schemas
"""

from .device import (
    ADBDevice,
    DeviceConnectionOptions,
    DeviceState,
    TransportType,
)
from .scrcpy import (
    AudioCodec,
    ScrcpyConfig,
    ScrcpyServerState,
    ScrcpyServerStatus,
    VideoCodec,
)
from .websocket import (
    AudioFrameData,
    ControlEvent,
    ControlEventType,
    DeviceInfoData,
    ErrorMessageData,
    StreamStatusData,
    VideoFrameData,
    WSMessage,
    WSMessageType,
)
from .api import (
    DeviceStats,
    ErrorResponse,
    HealthCheckResponse,
    MetricsResponse,
    StreamConfigUpdate,
    SuccessResponse,
)

__all__ = [
    # Device models
    "ADBDevice",
    "DeviceConnectionOptions",
    "DeviceState",
    "TransportType",
    # SCRCpy models
    "AudioCodec",
    "ScrcpyConfig",
    "ScrcpyServerState",
    "ScrcpyServerStatus",
    "VideoCodec",
    # WebSocket models
    "AudioFrameData",
    "ControlEvent",
    "ControlEventType",
    "DeviceInfoData",
    "ErrorMessageData",
    "StreamStatusData",
    "VideoFrameData",
    "WSMessage",
    "WSMessageType",
    # API models
    "DeviceStats",
    "ErrorResponse",
    "HealthCheckResponse",
    "MetricsResponse",
    "StreamConfigUpdate",
    "SuccessResponse",
]
