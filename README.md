# Stock Market Scraper

## Overview
This **Stock Market Scraper** is a Python-powered, API-driven, machine-learning-enabled script that fetches, analyzes, and predicts stock market trends for the **top 100 global companies**. It leverages the **Yahoo Finance API (`yfinance`)** to pull extensive stock data, applies **time-series forecasting** using **Meta’s Prophet model**, and saves everything into a structured **CSV file** for further analysis. 

In simple terms: This script is like a personal stock market assistant that tirelessly scrapes, organizes, and predicts stock prices so you don’t have to!

## Features
- **Automated Data Retrieval**: Fetches real-time & historical stock market data from Yahoo Finance.
- **Comprehensive Company Insights**: Grabs essential financial details such as market cap, sector, industry, and price performance metrics.
- **Machine Learning Magic**: Uses `Prophet`, a forecasting model developed by Meta (formerly Facebook), to predict future stock prices.
- **Error Handling & Rate Limiting**: Prevents API rejection by smartly managing request frequency.
- **Timezone Normalization**: Fixes pesky time-zone issues in financial data.
- **Fully Automated Output**: Exports all the juicy data into a neat, structured `CSV` file.

## How It Works (aka "The Secret Sauce")
1. **Ticker List Creation**: The script starts with a curated list of the top 100 global stock tickers.
2. **Stock Data Extraction**:
   - It calls Yahoo Finance (`yfinance.Ticker`) to retrieve fundamental company details and historical stock prices.
   - Cleans the data and ensures proper formatting.
3. **Time-Series Forecasting**:
   - Transforms stock price history into a `Prophet`-compatible dataset.
   - Trains a `Prophet` model on the stock’s closing price history.
   - Generates a **365-day forecast** into the future.
4. **Error Handling & Sleep Mechanism**:
   - Implements `try-except` blocks to gracefully handle missing data.
   - Introduces **randomized sleep intervals** (`random.uniform(1,3)`) to avoid API rate limiting.
5. **CSV Generation**:
   - Merges stock details and forecasts into a well-organized **CSV file**.
   - Saves everything as `Top_100_Companies_Stock_Data.csv`.

## Columns in the Output CSV
- `Ticker`: Stock symbol
- `Company Name`: Full name of the company
- `Country`: Country where the company is based
- `Sector`: Business sector
- `Industry`: Business industry
- `Market Cap`: Total market capitalization
- `52-Week High`: Highest stock price in the last 52 weeks
- `52-Week Low`: Lowest stock price in the last 52 weeks
- `Dividend Yield`: Annual dividend percentage
- `P/E Ratio`: Price-to-Earnings ratio
- `Last Close Price`: Most recent stock closing price
- `Future Prediction (1yr)`: Predicted stock price one year ahead

## Installation
### Requirements
- Python 3.7+
- Required libraries:
  ```bash
  pip install pandas yfinance prophet
  ```

## Usage
### Run the script in Google Colab or locally
```bash
python stock_scraper.py
```
The script will generate `Top_100_Companies_Stock_Data.csv` in the same directory.

### Download CSV in Google Colab
If using Google Colab, download the file with:
```python
from google.colab import files
files.download('Top_100_Companies_Stock_Data.csv')
```

## Uploading to GitHub
1. **Download the CSV** (if running on Colab)
2. **Go to GitHub** and create a new repository
3. **Upload the CSV**: Click **"Add file" > "Upload files"**, select `Top_100_Companies_Stock_Data.csv`, and commit changes.

## Future Enhancements
- Add **sentiment analysis** using financial news to factor in market hype and panic.
- Include **technical indicators** like RSI, MACD, and Bollinger Bands for deeper insights.
- Optimize **Prophet model parameters** for even better accuracy.
- Implement **multi-threading** for faster execution.

## License
This project is licensed under the **MIT License**.

---

🚀 *This script is like having a data scientist, stock analyst, and financial wizard—all rolled into one Python file in 20 minutes. Happy investing!* 📈

