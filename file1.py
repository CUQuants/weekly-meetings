'''
Author: Diego Alvarez
Date: 7/8/2021
Purpose: Example Meeting Writeup
'''

#we need this to change things
import matplotlib

#this will give us dates
import datetime as dt

#this will let us pull data
import pandas_datareader as web

#this will let us plot data
import matplotlib.pyplot as plt

#end date is today which is where we want to pull from
end = dt.datetime.today()

#we want 10 years in the past by accessing the start attribute which is an integer
start = dt.datetime(end.year - 20, end.month, end.day)

#use pandas datareader to get the data
#we are using the ST. Louis Federal Reserve Database (FRED)
#we are getting the Effective Fed Funds which has the title FEDFUNDS
#pull from start to date which we already defined
df = web.DataReader("FEDFUNDS", "fred", start, end)

#graph making

#we want to edit the size of the graph and change the axis
fig, ax1 = plt.subplots(figsize = (24,10))

#now we want to plot our data
plt.plot(df)



