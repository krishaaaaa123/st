import streamlit as st

def main():
    st.title("User Input Example")
    
    # Text input
    name = st.text_input("Enter your name")
    st.write(f"Hello, {name}!")
    
    # Number input
    age = st.number_input("Enter your age", min_value=0, max_value=150, value=25)
    st.write(f"You are {age} years old.")
    
    # Checkbox input
    agreement = st.checkbox("I agree to the terms and conditions")
    if agreement:
        st.write("You agreed to the terms and conditions.")
    else:
        st.write("Please agree to the terms and conditions.")
    
    # Dropdown select input
    options = ["Option 1", "Option 2", "Option 3"]
    chosen_option = st.selectbox("Choose an option", options)
    st.write(f"You selected: {chosen_option}")
    
if __name__ == "__main__":
    main()