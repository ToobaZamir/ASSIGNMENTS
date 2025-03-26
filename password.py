import re
import streamlit as st

st.title("Password Strength Checker🔑") 
st.write("Is your password strong enough to protect you?Discover the ultimate Password Checker app!Instantly evalute your password's strength and make sure you,re secured against threats.Stay safe online with a password that,s tough to crake")

st.markdown("""
 ## Check and improve your password🔐!""")
# function to check password strenght
password= st.text_input("Enter your password",type="password")

value= 0

feedback= []

if password:
    if len (password)>= 8:
        value +=1

    else:
        feedback.append("❌ Password should be *atleast 8 character long*.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        value += 1
    
    else:
        feedback.append("❌ password should contain both uppercase(A-Z and lowercase(a-z)letters")

    if re.search(r"\d",password):
        value +=1

    else:
        feedback.append("❌password should contain atleast one digit")
    
    
    if re.search(r"[@#$%^&*!]",password):
        value += 1
    else:
        feedback.append("❌Password should contain at least one special character[@#$%^&*!]")
    
    if value == 4:
        st.success("✅strong password - your password is  secure.")
    elif value == 3:
        feedback.append("🟡Your password is medium strength. it could be stronger")
    else: 
        feedback.append("🔴your password is week .Please make it stronger")



    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter a password to get started")