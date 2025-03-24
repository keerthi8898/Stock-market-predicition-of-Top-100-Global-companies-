import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Data 
data = [
    {"ticker": "AAPL", "companyName": "Apple Inc.", "country": "United States", "sector": "Technology", "industry": "Consumer Electronics", "marketCap": 3.68868E+12, "weekHigh52": 260.1, "weekLow52": 164.08, "dividendYield": 0.41, "peRatio": 38.91442, "lastClosePrice": 245.5500031, "futurePrediction": 237.54958048083708},
    {"ticker": "MSFT", "companyName": "Microsoft Corporation", "country": "United States", "sector": "Technology", "industry": "Software - Infrastructure", "marketCap": 3.03522E+12, "weekHigh52": 468.35, "weekLow52": 385.58, "dividendYield": 0.81, "peRatio": 32.90008, "lastClosePrice": 408.2099915, "futurePrediction": 464.1058130853018},
    {"ticker": "GOOGL", "companyName": "Alphabet Inc.", "country": "United States", "sector": "Communication Services", "industry": "Internet Content & Information", "marketCap": 2.2006E+12, "weekHigh52": 207.05, "weekLow52": 130.67, "dividendYield": 0.45, "peRatio": 22.318012, "lastClosePrice": 179.6600037, "futurePrediction": 180.18789865279092},
    {"ticker": "AMZN", "companyName": "Amazon.com, Inc.", "country": "United States", "sector": "Consumer Cyclical", "industry": "Internet Retail", "marketCap": 2.29525E+12, "weekHigh52": 242.52, "weekLow52": 151.61, "dividendYield": None, "peRatio": 39.235508, "lastClosePrice": 216.5800018, "futurePrediction": 190.01008761572507},
    {"ticker": "TSLA", "companyName": "Tesla, Inc.", "country": "United States", "sector": "Consumer Cyclical", "industry": "Auto Manufacturers", "marketCap": 1.08654E+12, "weekHigh52": 488.54, "weekLow52": 138.8, "dividendYield": None, "peRatio": 166.40393, "lastClosePrice": 337.7999878, "futurePrediction": 235.59336777954766},
    {"ticker": "BRK-B", "companyName": "Berkshire Hathaway Inc.", "country": "United States", "sector": "Financial Services", "industry": "Insurance - Diversified", "marketCap": 1.03271E+12, "weekHigh52": 491.67, "weekLow52": 395.66, "dividendYield": None, "peRatio": 9.6812935, "lastClosePrice": 478.7399902, "futurePrediction": 482.0646313537554},
    {"ticker": "META", "companyName": "Meta Platforms, Inc.", "country": "United States", "sector": "Communication Services", "industry": "Internet Content & Information", "marketCap": 1.73188E+12, "weekHigh52": 740.91, "weekLow52": 414.5, "dividendYield": 0.31, "peRatio": 28.648365, "lastClosePrice": 683.5499878, "futurePrediction": 869.0416121242142},
    {"ticker": "NVDA", "companyName": "NVIDIA Corporation", "country": "United States", "sector": "Technology", "industry": "Semiconductors", "marketCap": 3.29133E+12, "weekHigh52": 153.13, "weekLow52": 75.606, "dividendYield": 0.03, "peRatio": 53.120556, "lastClosePrice": 134.4299927, "futurePrediction": 114.57833052714092},
    {"ticker": "JPM", "companyName": "JPMorgan Chase & Co.", "country": "United States", "sector": "Financial Services", "industry": "Banks - Diversified", "marketCap": 7.38844E+11, "weekHigh52": 280.25, "weekLow52": 179.2, "dividendYield": 1.89, "peRatio": 13.386018, "lastClosePrice": 264.2399902, "futurePrediction": 202.34480122519582},
    {"ticker": "V", "companyName": "Visa Inc.", "country": "United States", "sector": "Financial Services", "industry": "Credit Services", "marketCap": 6.72318E+11, "weekHigh52": 357.15, "weekLow52": 252.7, "dividendYield": 0.68, "peRatio": 35.09869, "lastClosePrice": 348.5299988, "futurePrediction": 324.3575638963133},
    {"ticker": "JNJ", "companyName": "Johnson & Johnson", "country": "United States", "sector": "Healthcare", "industry": "Drug Manufacturers - General", "marketCap": 3.90757E+11, "weekHigh52": 168.85, "weekLow52": 140.68, "dividendYield": 3.06, "peRatio": 28.031088, "lastClosePrice": 162.3000031, "futurePrediction": 181.54688598892707},
    {"ticker": "WMT", "companyName": "Walmart Inc.", "country": "United States", "sector": "Consumer Defensive", "industry": "Discount Stores", "marketCap": 7.61405E+11, "weekHigh52": 105.3, "weekLow52": 58.18, "dividendYield": 0.99, "peRatio": 39.3278, "lastClosePrice": 94.77999878, "futurePrediction": 68.13749496579901},
    {"ticker": "PG", "companyName": "The Procter & Gamble Company", "country": "United States", "sector": "Consumer Defensive", "industry": "Household & Personal Products", "marketCap": 3.99164E+11, "weekHigh52": 180.43, "weekLow52": 153.52, "dividendYield": 2.37, "peRatio": 27.106686, "lastClosePrice": 170.2299957, "futurePrediction": 167.24024673016885},
    {"ticker": "UNH", "companyName": "UnitedHealth Group Incorporated", "country": "United States", "sector": "Healthcare", "industry": "Healthcare Plans", "marketCap": 4.29239E+11, "weekHigh52": 630.73, "weekLow52": 436.38, "dividendYield": 1.8, "peRatio": 30.033485, "lastClosePrice": 466.4200134, "futurePrediction": 633.254272226302},
    {"ticker": "HD", "companyName": "The Home Depot, Inc.", "country": "United States", "sector": "Consumer Cyclical", "industry": "Home Improvement Retail", "marketCap": 3.82743E+11, "weekHigh52": 439.37, "weekLow52": 323.77, "dividendYield": 2.34, "peRatio": 26.17527, "lastClosePrice": 385.2999878, "futurePrediction": 410.73528125860184},
    {"ticker": "MA", "companyName": "Mastercard Incorporated", "country": "United States", "sector": "Financial Services", "industry": "Credit Services", "marketCap": 5.08286E+11, "weekHigh52": 576.94, "weekLow52": 428.86, "dividendYield": 0.55, "peRatio": 40.166428, "lastClosePrice": 557.5100098, "futurePrediction": 531.9135130466001},
    {"ticker": "DIS", "companyName": "The Walt Disney Company", "country": "United States", "sector": "Communication Services", "industry": "Entertainment", "marketCap": 1.96434E+11, "weekHigh52": 123.74, "weekLow52": 83.91, "dividendYield": 0.92, "peRatio": 35.279224, "lastClosePrice": 108.6600037, "futurePrediction": 143.8355819274115},
    {"ticker": "PYPL", "companyName": "PayPal Holdings, Inc.", "country": "United States", "sector": "Financial Services", "industry": "Credit Services", "marketCap": 74143686656, "weekHigh52": 93.66, "weekLow52": 56.97, "dividendYield": None, "peRatio": 18.78446, "lastClosePrice": 74.94999695, "futurePrediction": 79.09920600530185},
    {"ticker": "BAC", "companyName": "Bank of America Corporation", "country": "United States", "sector": "Financial Services", "industry": "Banks - Diversified", "marketCap": 3.41043E+11, "weekHigh52": 48.08, "weekLow52": 33.53, "dividendYield": 2.32, "peRatio": 13.959502, "lastClosePrice": 44.81000137, "futurePrediction": 42.752446447482534},
    {"ticker": "NFLX", "companyName": "Netflix, Inc.", "country": "United States", "sector": "Communication Services", "industry": "Entertainment", "marketCap": 4.29104E+11, "weekHigh52": 1064.5, "weekLow52": 542.01, "dividendYield": None, "peRatio": 50.511078, "lastClosePrice": 1003.150024, "futurePrediction": 655.7770220238489},
    {"ticker": "ADBE", "companyName": "Adobe Inc.", "country": "United States", "sector": "Technology", "industry": "Software - Application", "marketCap": 1.93412E+11, "weekHigh52": 587.75, "weekLow52": 403.75, "dividendYield": None, "peRatio": 35.97733, "lastClosePrice": 444.3200073, "futurePrediction": 634.8536661045515},
    {"ticker": "XOM", "companyName": "Exxon Mobil Corporation", "country": "United States", "sector": "Energy", "industry": "Oil & Gas Integrated", "marketCap": 4.80299E+11, "weekHigh52": 126.34, "weekLow52": 103.05, "dividendYield": 3.58, "peRatio": 14.118623, "lastClosePrice": 110.6900024, "futurePrediction": 91.18859473833228},
    {"ticker": "PFE", "companyName": "Pfizer Inc.", "country": "United States", "sector": "Healthcare", "industry": "Drug Manufacturers - General", "marketCap": 1.49042E+11, "weekHigh52": 31.54, "weekLow52": 24.48, "dividendYield": 6.54, "peRatio": 18.652483, "lastClosePrice": 26.29999924, "futurePrediction": 38.30045399815284},
    {"ticker": "KO", "companyName": "The Coca-Cola Company", "country": "United States", "sector": "Consumer Defensive", "industry": "Beverages - Non-Alcoholic", "marketCap": 3.06876E+11, "weekHigh52": 73.53, "weekLow52": 57.93, "dividendYield": 2.72, "peRatio": 29.004065, "lastClosePrice": 71.34999847, "futurePrediction": 64.57847500745187},
    {"ticker": "NKE", "companyName": "NIKE, Inc.", "country": "United States", "sector": "Consumer Cyclical", "industry": "Footwear & Accessories", "marketCap": 1.13153E+11, "weekHigh52": 106.1, "weekLow52": 68.62, "dividendYield": 2.09, "peRatio": 23.61111, "lastClosePrice": 76.5, "futurePrediction": 131.39937013953937},
    {"ticker": "PEP", "companyName": "PepsiCo, Inc.", "country": "United States", "sector": "Consumer Defensive", "industry": "Beverages - Non-Alcoholic", "marketCap": 2.10525E+11, "weekHigh52": 183.41, "weekLow52": 141.51, "dividendYield": 3.53, "peRatio": 22.086332, "lastClosePrice": 153.5, "futurePrediction": 187.29728537534643}
]

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
df.head()  # Display the first few rows of the DataFrame
# 1. Market Cap by Sector (Pie Chart)
sector_data = df.groupby('sector')['marketCap'].sum() / 1e12  # Convert to trillions
sector_pie_data = sector_data.sort_values(ascending=False)

fig_pie = px.pie(
    names=sector_pie_data.index, values=sector_pie_data, 
    title="Market Cap by Sector (in Trillions $)", 
    labels={'value': 'Market Cap ($ Trillions)', 'names': 'Sector'}
)
fig_pie.show()

# 2. Top 10 Companies by Market Cap (Bar Chart)
top_10_companies = df.sort_values(by='marketCap', ascending=False).head(10)
top_10_companies['marketCap'] /= 1e12  # Convert to trillions
fig_bar = px.bar(
    top_10_companies, x='ticker', y='marketCap', 
    title="Top 10 Companies by Market Cap (in Trillions $)",
    labels={'marketCap': 'Market Cap ($ Trillions)', 'ticker': 'Company'}
)
fig_bar.show()

# 3. Top Growth Stocks (Bar Chart)
df['percentChange'] = ((df['futurePrediction'] - df['lastClosePrice']) / df['lastClosePrice']) * 100
top_growth_stocks = df[df['percentChange'] > 0].sort_values(by='percentChange', ascending=False).head(8)
fig_growth = px.bar(
    top_growth_stocks, x='ticker', y='percentChange', color='percentChange', 
    title="Top Growth Stocks", 
    labels={'percentChange': '% Growth Potential', 'ticker': 'Company'}
)
fig_growth.show()

# 4. Bottom Decline Stocks (Bar Chart)
bottom_stocks = df[df['percentChange'] < 0].sort_values(by='percentChange').head(8)
fig_decline = px.bar(
    bottom_stocks, x='ticker', y='percentChange', color='percentChange', 
    title="Predicted Declining Stocks", 
    labels={'percentChange': '% Expected Decline', 'ticker': 'Company'}
)
fig_decline.show()

# 5. P/E Ratio vs Dividend Yield Scatter Plot (Bubble Chart)
fig_scatter = px.scatter(
    df, x='peRatio', y='dividendYield', size='marketCap', color='sector', 
    hover_name='ticker', size_max=60,
    title="P/E Ratio vs Dividend Yield",
    labels={'peRatio': 'P/E Ratio', 'dividendYield': 'Dividend Yield (%)'}
)
fig_scatter.show()

# 6. Market Cap Treemap (Treemap)
fig_treemap = px.treemap(
    top_10_companies, path=['ticker'], values='marketCap',
    title="Top 10 Companies Market Cap Treemap",
    color='marketCap', hover_data=['companyName'],
    color_continuous_scale='Viridis'
)
fig_treemap.show()

# 7. Current Price vs Future Prediction (Bar Chart)
fig_price_prediction = px.bar(
    top_10_companies, x='ticker', y=['lastClosePrice', 'futurePrediction'],
    title="Current Price vs Future Prediction (Top 10 Companies)",
    labels={'value': 'Price ($)', 'ticker': 'Company'}
)
fig_price_prediction.show()
