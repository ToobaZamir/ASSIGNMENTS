import streamlit as st

st.title("Unit Converter App")
st.write("Choose a unit converter that's accurate, easy to use, and covers the units you need.")
st.markdown("### Converts Length, Mass And Time ")
st.write("Welcome! Select a category, enter a value and get the converted result ")

category = st.selectbox("Select a Categoty", ["Length", "Mass", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Metre":
            return value * 1000
        elif unit == "Metre to Kilometers":
            return value / 0.001
        elif unit == "Metre to Centimetre":
            return value * 100
        elif unit == "Centimetre to Milimetre":
            return value * 10
        elif unit == "Inch to Foot":
            return value / 12
        elif unit == "Foot to Mile":
            return value / 5280
        elif unit == "Centimetre to Inch":
            return value / 2.54
        elif unit == "Inch to Centimetre":
            return value *2.54


    elif category == "Mass":
        if unit == "Kilogram to Gram":
            return value *1000
        elif unit == "Gram to Milligram":
            return value *1000
        elif unit == "Milligram to Microgram":
            return value * 1000
        elif unit == "Microgaram to kilogram":
            return value  / 1e+9
        elif unit == "Pounds to kilogram":
            return value / 2.205
        elif unit == "Pounds to Ounce":
            return value * 16
        elif unit == "Pounds to Milligram":
            return value * 453600
        elif unit == "Pounds to Stone":
            return value / 14
        elif unit == "Ounce to kilogram":
            return value /35.274
        elif unit == "Gram to Microgram":
            return value * 1e+6
        elif unit == "Milligram to kilogram":
            return value / 1e+6



    elif category == "Time":
        if unit == "Second to Minute":
            return value / 60
        elif unit == "Minute to Hour":
            return value / 60
        elif unit == "Minute to Day":
            return value / 1440
        elif unit == "Hour to Second":
            return value * 3600
        elif unit == "Hour to Day":
            return value / 24
        elif unit == "Week to Hour":
            return value * 168
        elif unit == "Day to Week":
            return value / 7
    return 0
if category == "Length":
    unit = st.selectbox("📏 Select Converter", ["Kilometers to Metre","Metre to Kilometers","Centimetre to Milimetre","Inch to Foot","Foot to Mile","Centimetre to Inche","Inch to Centimetre"])
elif category == "Mass":
    unit = st.selectbox("⚖️ Select Converter", ["Kilograms to Gram", "Miligram to Micrograms","Microgaram to Kilogram","Pounds to Ounce","Pounds to Miligram","Pounds  to Stone","Ounce to Kilogram","Gram to Microgram","Milligram to Kilogram",])
        
elif category == "Time":
    unit = st.selectbox("⏱️ Select Converter", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter The Value To Convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
