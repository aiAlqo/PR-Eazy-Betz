import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎯 PR Eazy Betz", layout="wide")

st.title("📊 Generic 12x32 Table")

# Create dummy data
rows = 32
cols = 12

data = [[f"Row {i+1}, Col {j+1}" for j in range(cols)] for i in range(rows)]
column_names = [f"Column {j+1}" for j in range(cols)]

df = pd.DataFrame(data, columns=column_names)

# Define selectable options
options_col5 = ['']
options_col9 = ['']

# Table layout using columns
with st.expander('NRL (National Rugby League)'):
    st.dataframe(df, use_container_width=True)

# Sample data
data = {
    'Item': ['Apples', 'Bananas', 'Cherries'],
    'Price per unit': [1.5, 0.8, 2.0],
    'Available Qty': [100, 200, 150]
}
df = pd.DataFrame(data)

st.title("Interactive Table Selector")

# Display table with checkboxes
st.subheader("Select items:")
selected_items = []

for i, row in df.iterrows():
    if st.checkbox(f"{row['Item']} (${row['Price per unit']}/unit)", key=row['Item']):
        qty = st.number_input(f"Enter quantity for {row['Item']} (max {row['Available Qty']}):", 
                              min_value=0, 
                              max_value=row['Available Qty'], 
                              key=f"qty_{row['Item']}")
        selected_items.append({
            'Item': row['Item'],
            'Unit Price': row['Price per unit'],
            'Quantity': qty,
            'Total': qty * row['Price per unit']
        })

# Show result
if selected_items:
    st.subheader("Your Selection Summary")
    result_df = pd.DataFrame(selected_items)
    st.dataframe(result_df)

    grand_total = result_df['Total'].sum()
    st.success(f"**Grand Total: ${grand_total:.2f}**")
else:
    st.info("Select at least one item to see calculations.")

# Guide preparations
with st.sidebar:
  st.header('Tipping Guide')
