import streamlit as str
import pandas as pd 
import os
import io import bytes[notice] T
import streamlit as st

# Home Page
st.title("Growth Mindset Challenge")
st.write("Welcome! Let's develop a growth mindset through challenges and learning.")

# Growth Mindset Quiz
st.subheader("Are you in a Growth Mindset?")
question = st.radio(
    "How do you feel about challenges?",
    ("I avoid challenges", "I embrace challenges and learn from them")
)

if question == "I embrace challenges and learn from them":
    st.success("Great! You're on the right track.")
else:
    st.warning("Don't worry! Challenges help you grow.")

# Set Learning Goals
st.subheader("Set Your Learning Goals")
goal = st.text_input("What is your learning goal for this month?")
if goal:
    st.success(f"Your goal is set: {goal}")

# Show Motivational Quotes
st.subheader("Stay Inspired!")
quotes = ["Believe you can and you're halfway there" - Theodore Roosevelt",
          "It's not about being the best. It's about being better than you were yesterday."]
st.write(quotes[0])
