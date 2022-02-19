import pandas as pd
import yfinance as yf

#read csv
crypto_tickers = pd.read_excel("cyrpto_data.xlsx")

#get tickers
crypto_tickers = crypto_tickers[crypto_tickers.columns[0]].to_list()

#download the data
crypto_daily_prices = yf.download(crypto_tickers)['Close']
crypto_daily_prices.to_csv("crypto_daily_prices.csv")

crypto_weekly_prices = yf.download(crypto_tickers, interval = "1wk")['Close']
crypto_weekly_prices.to_csv("crypto_weekly_prices.csv")