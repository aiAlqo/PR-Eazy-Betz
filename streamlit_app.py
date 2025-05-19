import streamlit as st
import pandas as pd

# ---------- CONFIGURATION ----------
GITHUB_REPO = "YOUR_USERNAME/YOUR_REPO"  # UPDATE THIS
CSV_FILES = {
    "Match Day 1": "NRL1.csv",
    "Match Day 2": "NRL2.csv",  # Add more as needed
}
TAX_RATE = 0.13

# ---------- FUNCTIONS ----------
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df.columns = ["Track Code", "Race", "Match", "Category", "No", "Bet", "Odds"]
    df["Match"] = df["Match"].fillna(method="ffill")
    return df[df["Bet"].notna()]

def get_raw_github_url(filename):
    return f"https://raw.githubusercontent.com/aiAlqo/PR-Eazy-Betz/Data/NRL1_2.csv"

def calculate_returns(odds, amount):
    winnings = odds * amount
    tax = winnings * TAX_RATE
    net = winnings - tax
    return winnings, tax, net

# ---------- UI ----------
st.set_page_config(layout="wide")
st.title("🏉 NRL Multi-Bet Calculator (Match-Based)")

match_day = st.sidebar.selectbox("Select Match Day", list(CSV_FILES.keys()))
csv_url = get_raw_github_url(CSV_FILES[match_day])
df = load_data(csv_url)

bet_amount = st.sidebar.number_input("Enter Bet Amount", min_value=1.0, step=1.0)

# Group by Match (not Race)
grouped = df.groupby("Match")
selections = {}

st.subheader(f"Bets for: {match_day}")

for match, group in grouped:
    st.markdown(f"## Match: {match}")
    
    # Further group by Category within each match
    category_grouped = group.groupby("Category")
    
    for category, cat_group in category_grouped:
        st.markdown(f"**Category: {category}**")
        options = [(f"{row['Bet']} (Odds: {row['Odds']})", row['Odds'], f"{row['Track Code']} - {row['Race']} - {row['Match']} - {row['No']}") 
                   for _, row in cat_group.iterrows()]
        
        selected = st.radio(
            f"Choose for {category}",
            options,
            format_func=lambda x: x[0],
            key=f"{match}_{category}"
        )
        selections[f"{match} | {category}"] = selected

# ---------- OUTPUT ----------
st.sidebar.header("Your Selections + Winnings 💸")
total_winnings = 0
total_tax = 0
total_net = 0

for label, (bet_label, odds, bet_code) in selections.items():
    winnings, tax, net = calculate_returns(odds, bet_amount)
    total_winnings += winnings
    total_tax += tax
    total_net += net

    with st.sidebar:
        st.markdown(f"**{label}**")
        st.write(f"Selection: `{bet_code}`")
        st.write(f"Odds: `{odds}`")
        st.write(f"Win: `${winnings:.2f}` | Tax: `${tax:.2f}` | After Tax: `${net:.2f}`")

st.sidebar.markdown("---")
st.sidebar.subheader("Summary")
st.sidebar.write(f"Total Winnings: `${total_winnings:.2f}`")
st.sidebar.write(f"Total Tax: `${total_tax:.2f}`")
st.sidebar.write(f"Total Net Return: `${total_net:.2f}`")
