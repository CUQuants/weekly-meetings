import datetime as dt
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

#get todays date
end = dt.datetime.today()

#get 10 years from now by accessing todays year attribute
start = dt.datetime(end.year - 20, end.month, end.day)

#these are the tickers that we are going to use
tickers = ["^GSPC", "AAPL"]

#This is for renaming the columns in the dataframe
names = ["AAPL_returns", "SPX_returns"]

#download the data using yahoo finance tool 
#we want adjusted closed because that accounts for stock splits and dividends
#get the percent change which is the returns of the daily return of the stock
#we want to drop all values that aren't numbers (first value becomes a nan with pct_change)

df = yf.download(tickers, start, end)['Adj Close'].pct_change().dropna()

#rename columns
df.columns = names

plt.figure(figsize = (5,7))

#we are trying to fit our data with 2 components 
pca = PCA(n_components=2).fit(df)

#we are comparing the 
plt.scatter(df['AAPL_returns'], df['SPX_returns'], alpha=.3,)

#pca.components_ is the attribute that keeps the vector which is an array
#pca.explained_variance_ tells us how much of the variation of the data is explained by the component

#are using the enumarate which loops through and keeps an index
#the i is for the index and and the (comp, var) is for the pca.components_, pca.explained_variance_
#the zip is similar to a for loop but it is faster

for i, (comp, var) in enumerate(zip(pca.components_, pca.explained_variance_)):
    
    #multiply the component by its variance we put the 200 in for scaling
    #its variance will show how much of this component plays
    
    comp = comp * var * 200
    
    #then plot the component as a vector
    plt.plot([0, comp[0]], [0, comp[1]], color=f"C{i + 2}", linewidth=5)

#for more plotting
plt.gca().set(title="Daily AAPL Returns vs SPX returns", xlabel='AAPL', ylabel='SPX')



