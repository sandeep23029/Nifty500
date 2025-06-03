import streamlit as st
import pandas as pd

# Simple password protection
password = st.text_input("Enter password", type="password")
if password != "1234":
    st.warning("Wrong password")
    st.stop()

st.title("NIFTY 500 Monthly Screener")

# Read CSV
df = pd.read_csv("nifty500_monthly.csv")
st.dataframe(df)
