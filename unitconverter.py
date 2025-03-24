import streamlit as st

# Function to convert   Centimeters to inches, meters, and foot
def convert_units(value, from_unit, to_unit):
    if from_unit == "centimeters":
        if to_unit == "Inches":
            return value / 2.54  #  Centimeters to inches
        elif to_unit == "Feet":
            return value / 30.48  # centimeters to foot
        elif to_unit == "Meter":
            return value / 100 # centimeters to meter
        else:
            return "Invalid conversion"

# Streamlit interface
def app():
    st.title("Unit Converter")

    # Input value
    value = st.number_input("Enter value in Centimeters", min_value=0, formate=1)

    # Select conversion type
    from_unit = "centimeters"  # Fixed as we are always converting from centimeters
    to_unit = st.selectbox("Convert to", ["Inches", "Foot", "Meter"])

    # Conversion result
    if st.button("Convert"):
        if value > 0:
            result = convert_units(value, from_unit, to_unit)
            st.write(f"{value}centimeters is equal to{result}{to_Unit}")
        else:
            st.write("Please enter a valid value greater than 0.")
st.write(quotes[0])
