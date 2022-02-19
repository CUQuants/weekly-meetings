import pandas as pd

tech_daily_prices = pd.read_csv("tech_daily_prices.csv", index_col = 0)
tech_weekly_prices = pd.read_csv("tech_weekly_prices.csv", index_col = 0)

def clean_via_na(df):
    
    df = df.dropna(axis = 1, how = "all")
    df = df.dropna()
    
    return df

tech_daily_prices = clean_via_na(tech_daily_prices)
#tech_weekly_prices = clean_via_na(tech_weekly_prices)

tech_daily_prices.to_csv("tech_daily_prices.csv")
#tech_weekly_prices.to_csv("tech_weekly_prices.csv")