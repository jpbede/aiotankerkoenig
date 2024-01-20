"""Exceptions for the aiotankerkoenig client."""
from __future__ import annotations


class TankerkoenigError(Exception):
    """Base exception class for all exceptions raised by this library."""


class TankerkoenigConnectionError(TankerkoenigError):
    """Raised when a connection error occurs."""


class TankerkoenigInvalidKeyError(TankerkoenigError):
    """Raised when the API key is invalid."""
