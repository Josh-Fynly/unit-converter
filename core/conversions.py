# core/conversions.py

from core.exceptions import UnsupportedUnitError, InvalidValueError


def convert_length(value, from_unit, to_unit):
    """
    Convert between length units.
    Base unit: meters
    """
    if value < 0:
        raise InvalidValueError("Length value cannot be negative.")

    factors = {
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }

    if from_unit not in factors or to_unit not in factors:
        raise UnsupportedUnitError("Unsupported length unit.")

    meters = value * factors[from_unit]
    return meters / factors[to_unit]


def convert_weight(value, from_unit, to_unit):
    """
    Convert between weight units.
    Base unit: grams
    """
    if value < 0:
        raise InvalidValueError("Weight value cannot be negative.")

    factors = {
        "Grams": 1.0,
        "Kilograms": 1000.0,
        "Pounds": 453.592,
        "Ounces": 28.3495,
    }

    if from_unit not in factors or to_unit not in factors:
        raise UnsupportedUnitError("Unsupported weight unit.")

    grams = value * factors[from_unit]
    return grams / factors[to_unit]


def convert_temp(value, from_unit, to_unit):
    """
    Convert between temperature units.
    Internally converts via Celsius.
    """
    valid_units = {"Celsius", "Fahrenheit", "Kelvin"}

    if from_unit not in valid_units or to_unit not in valid_units:
        raise UnsupportedUnitError("Unsupported temperature unit.")

    if from_unit == to_unit:
        return value

    # Convert input to Celsius
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:  # Celsius
        celsius = value

    # Convert Celsius to target
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9 / 5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15