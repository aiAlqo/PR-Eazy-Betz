import streamlit as st
import pandas as pd

# Load CSV data
df = pd.read_csv("https://github.com/aiAlqo/PR-Eazy-Betz/blob/master/Data/NRL_Round8_Tipping_Guide.csv")

# Group the data by 'Match' and create separate dataframes
grouped = df.groupby("Match")

st.title("NRL Round 8 Tipping Guide")

for match_title, match_df in grouped:
    # Drop the 'Match' column as instructed
    display_df = match_df.drop(columns=["Match"])
    
    # Display a title for each match
    st.header(match_title)

    # Show each row with a checkbox
    for index, row in display_df.iterrows():
        # Generate label for the checkbox
        label = f"{row.to_dict()}"
        st.checkbox(label=label, key=f"{match_title}_{index}")
