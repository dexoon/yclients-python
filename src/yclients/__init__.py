"""Асинхронный типизированный клиент YCLIENTS REST API."""

from .client import YclientsClient
from .exceptions import (
    YclientsApiError,
    YclientsAuthError,
    YclientsError,
    YclientsForbiddenError,
    YclientsNotFoundError,
    YclientsRateLimitError,
    YclientsServerError,
    YclientsTransportError,
    YclientsValidationError,
)
from .models.common import Page

__version__ = "0.1.0"

__all__ = [
    "Page",
    "YclientsApiError",
    "YclientsAuthError",
    "YclientsClient",
    "YclientsError",
    "YclientsForbiddenError",
    "YclientsNotFoundError",
    "YclientsRateLimitError",
    "YclientsServerError",
    "YclientsTransportError",
    "YclientsValidationError",
    "__version__",
]
