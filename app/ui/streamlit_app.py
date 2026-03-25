import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from app.main import run

st.title("E-commerce AI Agent")

query = st.text_input("Enter query")

if st.button("Search"):
    result = run(query)
    st.write(result)