import pytest
import unittest
import re
import streamlit as st
import os
import streamlit.testing as TestClient

import test_main




   
class TestUserInput(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(main.main)

    def test_name_input(self):
        with self.client:
            self.client.text_input("Enter your name", value="John")
            result = self.client.get_query_params()["value"]
            self.assertEqual(result, "John")

    def test_age_input(self):
        with self.client:
            self.client.number_input("Enter your age", value=30)
            result = self.client.get_query_params()["value"]
            self.assertEqual(result, "30")

    def test_name_input_validation(self):
        with self.client:
            self.client.text_input("Enter your name", value="John Doe")
            result = self.client.get_query_params()["value"]
            if not re.match(r'^[A-Z][a-zA-Z\s]{0,29}$', result):
                st.error("Please type your name again")
            self.assertTrue(re.match(r'^[A-Z][a-zA-Z\s]{0,29}$', result))

    def test_age_input_validation(self):
        with self.client:
            self.client.number_input("Enter your age", value=30)
            result = self.client.get_query_params()["value"]
            if not re.match(r'^[1-9][0-9]$', str(result)):
                st.error("Please enter a valid age (1-99)")
            self.assertTrue(re.match(r'^[1-9][0-9]$', str(result)))

if __name__ == '__test_main__':
    pytest.test_main()

    
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