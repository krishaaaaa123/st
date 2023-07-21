import streamlit as st

def is_valid_name(name):
    # Regular expression to check if the name contains only letters and spaces
    return bool(name.strip().isalpha())

def is_valid_age(age):
    # Check if the age is between 1 and 99 (inclusive)
    return 1 <= age <= 99

def app(name, age):
    st.title("User Input Example")

    # Check if the name is valid
    if not is_valid_name(name):
        st.error("Please enter a valid name (letters only, no numbers or special characters).")
    else:
        st.write(f"Hello, {name}!")

    # Check if the age is valid
    if not is_valid_age(age):
        st.error("Please enter a valid age (between 1 and 99).")
    else:
        st.write(f"You are {age} years old.")

