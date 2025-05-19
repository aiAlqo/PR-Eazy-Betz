import streamlit as st
import pandas as pd

# URL to raw CSV on GitHub (replace this with your actual URL)
CSV_URL = "https://raw.githubusercontent.com/aiAlqo/PR-Eazy-Betz/refs/heads/master/Data/NRL1_1.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df["Race"] = df["Race"].fillna(method="ffill")
    df.columns = ["Track Code", "Race", "No 1", "Team 1", "Odds 1", "No 2", "Team 2", "Odds 2"]
    df = df[df["Team 1"].notna() | df["Team 2"].notna()]
    return df

# Load the data
df = load_data(CSV_URL)

# Streamlit layout
st.set_page_config(layout="wide")
st.title("NRL Betting Selector")

# Group by Race
grouped = df.groupby("Race")
selections = {}

with st.sidebar:
    st.header("Your Selections")

# Display grouped race selections
for race, group in grouped:
    st.subheader(f"Race {int(race)}")
    options = []

    for _, row in group.iterrows():
        # Team 1 option
        if pd.notna(row["Team 1"]):
            label = f"Team 1: {row['Team 1']} (Odds: {row['Odds 1']})"
            code = f"{row['Track Code']} - {int(race)} - 1"
            options.append((label, code))

        # Team 2 option
        if pd.notna(row["Team 2"]):
            label = f"Team 2: {row['Team 2']} (Odds: {row['Odds 2']})"
            code = f"{row['Track Code']} - {int(race)} - 2"
            options.append((label, code))

    # Create race-specific radio buttons
    selected = st.radio(
        f"Select outcome for Race {int(race)}", 
        options, 
        format_func=lambda x: x[0], 
        key=f"race_{race}"
    )
    selections[race] = selected[1]

# Sidebar output
with st.sidebar:
    for race in sorted(selections.keys()):
        st.write(f"Race {int(race)}: `{selections[race]}`")
