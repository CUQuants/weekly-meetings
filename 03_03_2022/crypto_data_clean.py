import pandas as pd

crypto_daily_prices = pd.read_csv("crypto_daily_prices.csv", index_col = 0)
crypto_weekly_prices = pd.read_csv("crypto_weekly_prices.csv", index_col = 0)

def clean_via_na(df):
    
    df = df.dropna(axis = 1, how = "all")
    df = df.dropna()
    
    return df

crypto_daily_prices = clean_via_na(crypto_daily_prices)
crypto_weekly_prices = clean_via_na(crypto_weekly_prices)

crypto_daily_prices.to_csv("crypto_daily_prices.csv")
crypto_weekly_prices.to_csv("crypto_weekly_prices.csv")