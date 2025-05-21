import streamlit as st
import pandas as pd

# Load the correct raw CSV
csv_url = "https://raw.githubusercontent.com/aiAlqo/PR-Eazy-Betz/master/Data/NRL_Round8_Tipping_Guide.csv"
df = pd.read_csv(csv_url, engine="python", on_bad_lines='skip')

# Check for the 'Match' column
if "Match" not in df.columns:
    st.error("Missing expected column: 'Match'")
    st.write("Available columns:", df.columns.tolist())
    st.dataframe(df.head())
    st.stop()

# Group by match
grouped = df.groupby("Match")

st.title("NRL Round 8 Tipping Guide")

# Loop through each match
for match_title, match_df in grouped:
    st.subheader(match_title)

    # Drop the Match column for display
    display_df = match_df.drop(columns=["Match"], errors='ignore')

    # Display each row as a "checkbox + table row"
    for idx, row in display_df.iterrows():
        with st.container():
            cols = st.columns([0.1, 2])  # One column for checkbox, one for table row
            with cols[0]:
                st.checkbox("", key=f"{match_title}_{idx}")
            with cols[1]:
                # Display the row like a table row
                st.markdown(" | ".join(f"**{col}**: {val}" for col, val in row.items()))
