import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎯 PR Eazy Betz", layout="wide")

st.title("📊 Generic 12x32 Table")

# Create dummy data
rows = 32
cols = 12

# Placeholder table headers
column_names = [f"Column {j+1}" for j in range(cols)]

# Define selectable options
options_col5 = ['']
options_col9 = ['']

# Table layout using columns
with st.expander('NRL (National Rugby League)'):
    st.write("### Match No.1")
