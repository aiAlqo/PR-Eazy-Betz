import streamlit as st
import pandas as pd

# ---------- CONFIGURATION ----------
GITHUB_REPO = "aiAlqo/PR-Eazy-Betz"
CSV_FILES = {
    "Match Day 1": "NRL1.csv",
    "Match Day 2": "NRL2.csv",  # Add more as needed
}
TAX_RATE = 0.13

# ---------- FUNCTIONS ----------
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df.columns = ["Track Code", "Race", "No 1", "Team 1", "Odds 1", "No 2", "Team 2", "Odds 2"]
    df["Race"] = df["Race"].fillna(method="ffill")
    return df[df["Team 1"].notna() | df["Team 2"].notna()]

def get_raw_github_url(filename):
    return f"https://raw.githubusercontent.com/aiAlqo/PR-Eazy-Betz/data/NRL1_1.csv"

def calculate_returns(odds, amount):
    winnings = odds * amount
    tax = winnings * TAX_RATE
    net = winnings - tax
    return winnings, tax, net

# ---------- UI ----------
st.set_page_config(layout="wide")
st.title("🏉 NRL Multi-Match Betting Calculator")

match_day = st.sidebar.selectbox("Select Match Day", list(CSV_FILES.keys()))
csv_url = get_raw_github_url(CSV_FILES[match_day])
df = load_data(csv_url)

bet_amount = st.sidebar.number_input("Enter Bet Amount", min_value=1.0, step=1.0)

# Group by Race and collect selections
grouped = df.groupby("Race")
selections = {}

st.subheader(f"Available Bets – {match_day}")

for race, group in grouped:
    st.markdown(f"### Race {int(race)}")
    options = []
    for _, row in group.iterrows():
        if pd.notna(row["Team 1"]):
            label = f"{row['Team 1']} (Odds: {row['Odds 1']})"
            options.append((label, row["Odds 1"], f"{row['Track Code']} - {int(race)} - {int(row['No 1'])}"))

        if pd.notna(row["Team 2"]):
            label = f"{row['Team 2']} (Odds: {row['Odds 2']})"
            options.append((label, row["Odds 2"], f"{row['Track Code']} - {int(race)} - {int(row['No 2'])}"))

    selected = st.radio(
        f"Choose outcome for Race {int(race)}",
        options,
        format_func=lambda x: x[0],
        key=f"race_{race}"
    )
    selections[race] = selected

# ---------- OUTPUT ----------
st.sidebar.header("Your Selections + Winnings 💰")
total_winnings = 0
total_tax = 0
total_net = 0

for race, (label, odds, code) in selections.items():
    winnings, tax, net = calculate_returns(odds, bet_amount)
    total_winnings += winnings
    total_tax += tax
    total_net += net

    with st.sidebar:
        st.markdown(f"**Race {int(race)}**")
        st.write(f"Selection: `{code}`")
        st.write(f"Odds: `{odds}`")
        st.write(f"Win: `${winnings:.2f}` | Tax: `${tax:.2f}` | After Tax: `${net:.2f}`")

st.sidebar.markdown("---")
st.sidebar.subheader("Summary")
st.sidebar.write(f"Total Potential Winnings: `${total_winnings:.2f}`")
st.sidebar.write(f"Total Tax Deducted: `${total_tax:.2f}`")
st
