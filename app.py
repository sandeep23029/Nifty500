import streamlit as st
import pandas as pd

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
