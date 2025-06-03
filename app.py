import streamlit as st
import pandas as pd

<<<<<<< HEAD
st.title("Nifty 500 Monthly Data Screener")

# CSV file load karo
df = pd.read_csv("nifty500_monthly_data.csv")

# Stock select karne ke liye dropdown
stocks = st.multiselect("Select Stocks", options=df['Symbol'].unique())

if stocks:
    filtered_df = df[df['Symbol'].isin(stocks)]
    st.dataframe(filtered_df)
else:
    st.write("Please select one or more stocks to see the data.")
=======
# Simple password protection
password = st.text_input("Enter password", type="password")
if password != "1234":
    st.warning("Wrong password")
    st.stop()

st.title("NIFTY 500 Monthly Screener")

# Read CSV
df = pd.read_csv("nifty500_monthly.csv")
st.dataframe(df)
>>>>>>> 9879cb416b315ce76e1fff83aa0c2fffe57c9ee5
