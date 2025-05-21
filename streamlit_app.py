import streamlit as st
import pandas as pd

# Safe CSV loading
try:
    df = pd.read_csv("https://github.com/aiAlqo/PR-Eazy-Betz/blob/master/Data/NRL_Round8_Tipping_Guide.csv", engine="python", on_bad_lines='skip')
except pd.errors.ParserError as e:
    st.error(f"Error reading CSV: {e}")
    st.stop()

st.title("NRL Round 8 Tipping Guide")

# Display each match's data with checkboxes
for match_title, match_df in grouped:
    st.subheader(match_title)

    # Drop 'Match' column
    display_df = match_df.drop(columns=["Match"], errors='ignore')

    for idx, row in display_df.iterrows():
        label = " | ".join([f"{col}: {val}" for col, val in row.items()])
        st.checkbox(label, key=f"{match_title}_{idx}")
