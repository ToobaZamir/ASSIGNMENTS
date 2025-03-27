import streamlit as st

st.title("Unit Converter App")
st.write("Choose a unit converter that's accurate, easy to use, and covers the units you need.")
st.markdown("### Converts Length, Mass And Time ")
st.write("Welcome! Select a category, enter a value and get the converted result ")

category = st.selectbox("Select a Categoty", ["Length", "Mass", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometer to Metre":
            return value * 1000
        elif unit == "Metre to Kilometer":
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
        elif unit == "Pound to kilogram":
            return value / 2.205
        elif unit == "Pound to Ounce":
            return value * 16
        elif unit == "Pound to Milligram":
            return value * 453600
        elif unit == "Pound to Stone":
            return value / 14
        elif unit == "Ounce to kilogram":
            return value /35.274
        elif unit == "Gram to Microgram":
            return value * 1e+6

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
        
if category == "Length":
    unit = st.selectbox("📏 Select Converter", ["Kilometer to Metre","Metre to Kilometer","Metre to Centimetre","Centimetre to Milimetre","Inch to Foot","Foot to Mile","Centimetre to Inche","Inch to Centimetre"])
elif category == "Mass":
    unit = st.selectbox("⚖️ Select Converter", ["Kilogram to Gram","Gram to Milligram","Pound to Kilogram","Pound to Ounce","Pound to Miligram","Pound to Stone","Ounce to Kilogram","Gram to Microgram"])
elif category == "Time":
    unit = st.selectbox("⏱️ Select Converter", ["Second to Minute","Minute to Hour","Minute to Day","Hour to Second","Hour to Day","Week to Hour","Day to Week"])

value = st.number_input("Enter The Value To Convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
