import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎯 PR Eazy Betz", layout="wide")

st.title("📊 Generic 12x32 Table")

# Create dummy data
rows = 32
cols = 12

data = [[f"Row {i+1}, Col {j+1}" for j in range(cols)} for i in range(rows)]
column_names = [f"Column {j+1}" for j in range(cols)]

df = pd.DataFrame(data, columns=column_names)

#Display the table
st.dataframe(df, use_container_width=True)
