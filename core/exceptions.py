# core/exceptions.py

class ConversionError(Exception):
    """Base exception for conversion errors."""
    pass


class UnsupportedUnitError(ConversionError):
    """Raised when an unsupported unit is requested."""
    pass


class InvalidValueError(ConversionError):
    """Raised when an invalid value is provided for conversion."""
    pass