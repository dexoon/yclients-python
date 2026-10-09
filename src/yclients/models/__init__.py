"""Модели YCLIENTS API: общие + сгенерированные из спеки."""

from .common import ApiEnvelope, Page, ValidationErrorItem
from .schemas import *

__all__ = ["ApiEnvelope", "Page", "ValidationErrorItem"]
__all__ += [
    _name
    for _name in dir()
    if not _name.startswith("_") and _name not in __all__
]
