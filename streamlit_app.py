import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎯 PR Eazy Betz", layout="wide")

import streamlit as st
import pandas as pd

# Create a 9-column, 3-row dataframe
df = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [False, False, False],  # Checkbox column (3rd)
        "D": [7, 8, 9],
        "E": [10, 11, 12],
        "F": [False, False, False],  # Checkbox column (6th)
        "G": [13, 14, 15],
        "H": [16, 17, 18],
        "I": [19, 20, 21],
    }
)

# Configure columns 3 and 6 as checkboxes
column_config = {
    "C": st.column_config.CheckboxColumn("Select C"),
    "F": st.column_config.CheckboxColumn("Select F"),
}

# Make only the checkbox columns editable
st.data_editor(
    df,
    column_config=column_config,
    disabled=["A", "B", "D", "E", "G", "H", "I"],
    hide_index=True,
)


# Guide preparations
with st.sidebar:
  st.header('Tipping Guide')
