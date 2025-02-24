import pandas as pd
import yfinance as yf
from prophet import Prophet
from time import sleep
import random

# List of Top 100 Global Companies 
tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'BRK-B', 'META', 'NVDA', 'JPM', 'V', 'JNJ', 'WMT', 'PG', 'UNH', 'HD', 'MA',
    'DIS', 'PYPL', 'BAC', 'NFLX', 'ADBE', 'XOM', 'PFE', 'KO', 'NKE', 'PEP', 'MRNA', 'CSCO', 'ORCL', 'ABT', 'INTC', 'IBM',
    'T', 'CVX', 'LLY', 'BMY', 'COST', 'MCD', 'TMO', 'HON', 'LOW', 'RTX', 'UPS', 'CAT', 'SBUX', 'MS', 'GS', 'LMT', 'MDT',
    'BLK', 'SCHW', 'BA', 'ISRG', 'CVS', 'F', 'GM', 'SO', 'DE', 'PLD', 'AMAT', 'ZTS', 'GE', 'USB', 'DUK', 'PNC', 'NOW', 'TGT',
    'MO', 'BK', 'CL', 'MMM', 'ADI', 'GILD', 'CSX', 'EL', 'DHR', 'SYK', 'NSC', 'MMC', 'MET', 'ECL', 'HUM', 'CB', 'AON', 'SPGI',
    'ICE', 'CI', 'TFC', 'ADP', 'ITW', 'CME', 'ROP', 'AIG', 'EW', 'FIS', 'PH', 'APD', 'AEP', 'PSX', 'EMR', 'FDX', 'SHW', 'KLAC'
]

# Function to fetch company details & stock history
def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period='max')
        
        # Remove timezone from index
        hist = hist.tz_localize(None)
        
        # Prepare Data for Forecasting
        df = hist[['Close']].reset_index()
        df.columns = ['ds', 'y']
        df['ds'] = df['ds'].dt.tz_localize(None)  # Ensure no timezone
        
        # Train Prophet Model for Future Prediction
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=365)  # Predict 1 year ahead
        future['ds'] = future['ds'].dt.tz_localize(None)  # Ensure no timezone
        forecast = model.predict(future)
        
        return {
            'Ticker': ticker,
            'Company Name': info.get('longName', 'N/A'),
            'Country': info.get('country', 'N/A'),
            'Sector': info.get('sector', 'N/A'),
            'Industry': info.get('industry', 'N/A'),
            'Market Cap': info.get('marketCap', 'N/A'),
            '52-Week High': info.get('fiftyTwoWeekHigh', 'N/A'),
            '52-Week Low': info.get('fiftyTwoWeekLow', 'N/A'),
            'Dividend Yield': info.get('dividendYield', 'N/A'),
            'P/E Ratio': info.get('trailingPE', 'N/A'),
            'Last Close Price': hist['Close'].iloc[-1] if not hist.empty else 'N/A',
            'Future Prediction (1yr)': forecast[['ds', 'yhat']].tail(1).values.tolist()[0] if not forecast.empty else 'N/A'
        }
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return None

# Scrape data for all companies
data = []
for ticker in tickers:
    stock_data = fetch_stock_data(ticker)
    if stock_data:
        data.append(stock_data)
    sleep(random.uniform(1, 3))  # Prevent rate limiting

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('Top_100_Companies_Stock_Data.csv', index=False)

print("Data collection complete. Check the CSV file.yahooooo!")
