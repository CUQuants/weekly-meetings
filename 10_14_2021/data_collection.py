import random
import numpy as np
import pandas as pd
import yfinance as yf

#this gets 50 random tickers from S&P 500
def get_random_tickers(count):
    
    #read tickers from wikipedia
    tickers = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]['Symbol'].to_list()
    
    #shuffle tickers
    random.shuffle(tickers)
    
    #grab the first 50 or 1/10 of the S&P 500
    tickers = tickers[0:count]
    
    return tickers

def get_stats(tickers):
    
    #make a dataframe to output with the correct columns
    df = pd.DataFrame(0, index = np.arange(len(tickers)), columns = ["ticker", "ROA", "RPS"])
    
    #go through the tickers
    for i,j in enumerate(tickers):
        
        #output what ticker we are working on
        print("working on", j)
        
        #grab the information via yfinance
        ticker = yf.Ticker(j).info
        
        #then put the data into the dataframe
        df.loc[i, "ticker"] = j
        df.loc[i, "ROA"] = ticker.get("returnOnAssets")
        df.loc[i, "RPS"] = ticker.get("revenuePerShare")
        
    #clean the dataframe by putting  the ticker in the index
    df = df.set_index("ticker")
    return df

df = get_stats(get_random_tickers(200))
df.to_csv("SP500_ROA_RPS.csv")