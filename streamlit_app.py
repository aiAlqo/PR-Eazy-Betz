import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎯 PR Eazy Betz", layout="wide")

st.title("📊 Generic 12x32 Table")

# Create dummy data
rows = 32
cols = 12

# Sample column names
column_names = [f"Column {j+1}" for j in range(cols)]

# Placeholder data
data = [[f"R{i+1}C{j+1}" for j in range(cols)] for i in range(rows)]
df = pd.DataFrame(data, columns=column_names)

# Options for radio buttons
radio_options = ["-", "✔️", "❌"]

# Show interactive table row by row
st.write("### Select options for Column 5 and Column 9")

# Store user selections
selections = []

# Table header
header_cols = st.columns(cols)
for idx, col in enumerate(header_cols):
    col.markdown(f"**{column_names[idx]}**")

# Table rows
for i in range(rows):
    cols_streamlit = st.columns(cols)
    row_selections = []

    for j in range(cols):
        if j == 4 or j == 8:  # Col 5 and 9 (index starts at 0)
            choice = cols_streamlit[j].radio(
                label="",
                options=radio_options,
                index=0,
                key=f"row{i}_col{j}",
                label_visibility="collapsed",
                horizontal=True
            )
            row_selections.append(choice)
            cols_streamlit[j].markdown("")  # Optional: add a spacer
        else:
            cols_streamlit[j].markdown(df.iloc[i, j])
            row_selections.append(df.iloc[i, j])

    selections.append(row_selections)

# Optionally show selections
if st.button("Show Selections"):
    st.write("### Your Current Selections (Col 5 & 9):")
    for idx, row in enumerate(selections):
        st.write(f"Row {idx+1}: Col 5 → {row[4]}, Col 9 → {row[8]}")
