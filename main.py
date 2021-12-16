import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.sidebar.markdown("""# Siamak Mushakhian 
Data Scientist
""")
st.sidebar.text_input("Email:")
st.sidebar.text_input("Password:", type='password')
st.sidebar.button("Log in")

st.write("""
# Stock Price Application
""")

cols = st.columns(2)

# define the ticker symbol
tickerSymbol = cols[0].text_input("Symbol:", 'GOOG')
st.markdown(f'Shown are the **stock closing** price and **volume** of **{tickerSymbol}**')

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

period_list = ['1d', '5d']
selected_period = cols[0].selectbox("Period:", period_list)

interval_list = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
selected_interval = cols[1].selectbox("Interval", interval_list)

today = datetime.date.today()
yesterday = today + datetime.timedelta(days=-10)
start_date = cols[0].date_input('Start date', yesterday)
end_date = cols[1].date_input('End date', today)
if start_date > end_date:
    st.error("Error: End date must fall after start date")

# get the historical prices for this ticker
tickerDf = tickerData.history(interval=selected_interval, start=start_date, end=end_date)
# Open High Low Close Volume Dividends Stock Splits

chart_list = ['Open', 'High', 'Low', 'Close', 'Volume']
selected_charts = st.multiselect("Charts", chart_list)

if st.button("Show"):
    for chart in selected_charts:
        st.write(f"## {chart}")
        st.line_chart(tickerDf[chart])
