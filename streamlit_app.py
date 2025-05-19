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

# Loop over rows
    for i in range(rows):
        cols_ui = st.columns(cols)

        for j in range(cols):
            if j == 4:  # Column 5 (index 4)
                with cols_ui[j]:
                    st.radio(f"row_{i}_col5", options_col5, key=f"r{i}_c5", label_visibility="collapsed")
            elif j == 8:  # Column 9 (index 8)
                with cols_ui[j]:
                    st.radio(f"row_{i}_col9", options_col9, key=f"r{i}_c9", label_visibility="collapsed")
            else:
                with cols_ui[j]:
                    st.text_input(f"", value=f"Row {i+1}, Col {j+1}", key=f"r{i}_c{j}", label_visibility="collapsed")
