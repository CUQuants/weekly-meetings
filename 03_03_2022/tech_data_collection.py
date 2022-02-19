import pandas as pd
import yfinance as yf

tech_tickers = pd.read_excel("holdings-daily-us-en-xlk.xlsx")

#get tickers
tech_tickers = tech_tickers[tech_tickers.columns[0]].to_list()

#download the data
tech_daily_prices = yf.download(tech_tickers)['Close']
tech_daily_prices.to_csv("tech_daily_prices.csv")

tech_weekly_prices = yf.download(tech_tickers, interval = "1wk")['Close']
tech_weekly_prices.to_csv("tech_weekly_prices.csv")