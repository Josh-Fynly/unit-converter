# conversions.py

def convert_length(value, from_unit, to_unit):
    # We convert everything to Meters first, then to the target
    factors = {
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Feet": 0.3048,
        "Miles": 1609.34
    }
    # logic: (value * from_factor) / to_factor
    meters = value * factors[from_unit]
    return meters / factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Base unit: Grams
    factors = {
        "Grams": 1.0,
        "Kilograms": 1000.0,
        "Pounds": 453.592,
        "Ounces": 28.3495
    }
    grams = value * factors[from_unit]
    return grams / factors[to_unit]

def convert_temp(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Convert input to Celsius
    celsius = value
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
        
    # Convert Celsius to target
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15

