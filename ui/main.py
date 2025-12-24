# ui/main.py

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from core import conversions as cv  # Core logic import

# ----------------------
# Page Configuration
# ----------------------
st.set_page_config(page_title="Unit Converter", page_icon="⚖️", layout="centered")

st.title("⚖️ Universal Unit Converter")
st.write("### Professional conversion tool")

category = st.sidebar.selectbox("Select Category", ["Length", "Weight", "Temperature"])
st.header(f"{category} Converter")

value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if category == "Length":
    units = ["Meters", "Kilometers", "Feet", "Miles"]
elif category == "Weight":
    units = ["Grams", "Kilograms", "Pounds", "Ounces"]
else:
    units = ["Celsius", "Fahrenheit", "Kelvin"]

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", units)
with col2:
    to_unit = st.selectbox("To", units)

if st.button("Convert Now"):
    try:
        if category == "Length":
            result = cv.convert_length(value, from_unit, to_unit)
        elif category == "Weight":
            result = cv.convert_weight(value, from_unit, to_unit)
        else:
            result = cv.convert_temp(value, from_unit, to_unit)

        st.success(f"**{value} {from_unit}** is equal to **{result:.4f} {to_unit}**")
    except Exception as e:
        st.error(f"Conversion failed: {e}")