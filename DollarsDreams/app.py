import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np


tickers = ['SPY','QQQ','SCHD']
opening_prices = [589.39, 514.3, 27.47]
current_prices = []
current_dates = []
for ticker in tickers:
    ticker_object = yf.Ticker(ticker)
    history = ticker_object.history(period="1d")
    current_price = np.round(history["Close"].iloc[-1], 2)
    current_date = history.index[-1].date()  # Get the date from the index
    current_prices.append(current_price)
    current_dates.append(current_date) 

df = pd.DataFrame({
    'Ticker': tickers,
    '2025 Opening Price': opening_prices,
    'Current Price': current_prices,
    'Current Price Date': current_dates
})

# df['Percent Gain'] = np.round(((df['Current Price'] - df['2025 Opening Price']) / df['2025 Opening Price']) * 100,2)
df['Percent Gain'] = np.round(((df['Current Price'] - df['2025 Opening Price']) / df['2025 Opening Price']) * 100,2)
df['Percent of Open'] = np.round((df['Current Price'] / df['2025 Opening Price']) * 100,2)
df['$10,000 Return'] = np.round((df['Current Price'] / df['2025 Opening Price'])*10000,2)


# Create two columns
col1, col2 = st.columns([3, 1])  # Adjust proportions as needed

# Add the title in the first column
with col1:
	st.title("Dollars and Dreams")
	st.write("The money leaves are at the top of the tree. Have you seen my neck?")

# Add the image in the second column
with col2:
	st.image("images/dollars_dreams_giraffe.png", caption="Long Neck Larry, the High Return Hunter", width=150)

st.markdown("---")

st.subheader("YTD ROI for SPY, QQQ, and SCHD")

dfStreamlit = df.copy()
dfStreamlit['2025 Opening Price'] = dfStreamlit['2025 Opening Price'].apply(lambda x: f'${x:.2f}')
dfStreamlit['Current Price'] = dfStreamlit['Current Price'].apply(lambda x: f'${x:.2f}')
dfStreamlit['Percent Gain'] = dfStreamlit['Percent Gain'].apply(lambda x: f'{x:.2f}%') 
dfStreamlit['Percent of Open'] = dfStreamlit['Percent of Open'].apply(lambda x: f'{x:.2f}%') 
dfStreamlit['$10,000 Return'] = dfStreamlit['$10,000 Return'].apply(lambda x: f'${x:,.2f}')

def color_percent_change(val):
    color = 'green' if val[0] != '-' else 'red'  # Check if the first character is '-'
    return f'color: {color}'

# Apply the styling
st.dataframe(dfStreamlit.style.applymap(color_percent_change, subset=['Percent Gain']), hide_index=True)



