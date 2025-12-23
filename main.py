# main.py
import streamlit as st
import conversions as cv  # We import our logic file

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="⚖️")

st.title("⚖️ Universal Unit Converter")
st.write("### Professional conversion tool")

# Sidebar for category selection
category = st.sidebar.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Main Area
st.header(f"{category} Converter")

# Input value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Define units based on category
if category == "Length":
    units = ["Meters", "Kilometers", "Feet", "Miles"]
elif category == "Weight":
    units = ["Grams", "Kilograms", "Pounds", "Ounces"]
else:
    units = ["Celsius", "Fahrenheit", "Kelvin"]

# Layout: Two columns for "From" and "To" (Looks great on mobile)
col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From", units)

with col2:
    to_unit = st.selectbox("To", units)

# The Trigger
if st.button("Convert Now", type="primary"):
    result = 0
    if category == "Length":
        result = cv.convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        result = cv.convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        result = cv.convert_temp(value, from_unit, to_unit)
    
    st.success(f"**{value} {from_unit}** is equal to **{result:.4f} {to_unit}**")


