import streamlit as st
# Initial imports
import panel as pn
import os
from pathlib import Path
import requests
import pandas as pd
import datetime as dt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from yahoofinancials import YahooFinancials
import json
from newsapi.newsapi_client import NewsApiClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
pn.extension("plotly")
from panel.interact import interact
import hvplot.pandas
import plotly.express as px

# Load .env enviroment variables
load_dotenv()

# Set News API Key
newsapi = NewsApiClient(api_key=os.environ["NEWS_API"])
#api_newsdata = NewsDataApiClient(apikey="newsdata")

# Set Alpaca API key and secret
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

api = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version='v2')

# Loading Functions
# Use newsapi client to get most relevant 20 headlines per day in the past month
def get_headlines(keyword,fdate,edate):
    all_headlines = []
    all_contents = []
    all_dates = [] 
    # string conversion of dates passed in to function
    fdate_str=str(fdate.strftime("%Y-%m-%d"))
    edate_str=str(edate.strftime("%Y-%m-%d"))

    print(f"Fetching news about '{keyword}'")
    print("*" * 30)
    #while date > end_date:
    print(f"retrieving news from: {fdate} - {edate}")
    articles = newsapi.get_everything(
        q=keyword,
        # from_param=str(date)[:10],
        # to=str(date)[:10],
        from_param=fdate_str,
        to=edate_str,
        language="en",
        sort_by="relevancy",
        page=1,
    )
    headlines = []
    contents = []
    for i in range(0, len(articles["articles"])):
        headlines.append(articles["articles"][i]["title"])
        contents.append(articles["articles"][i]["content"])
    all_headlines.append(headlines)
    all_contents.append(contents)
    all_dates.append(fdate)
    #date = date - timedelta(weeks=1)
    return all_headlines, all_dates, all_contents

# Create function that computes average compound sentiment of headlines for each day
def headline_sentiment_summarizer_avg(data,sdate):
    df=data.copy()
    sentiment = []
    sentiment_pos = []
    sentiment_neg = []
    for day in data:
        day_score = []
        day_positive = []
        day_negative = []
        for h in day:
            
            if h == None:
                continue
            else:
                day_score.append(sid.polarity_scores(h)["compound"])
                day_positive.append(sid.polarity_scores(h)["pos"])
                day_negative.append(sid.polarity_scores(h)["neg"])
        sentiment.append(sum(day_score) / len(day_score))
        sentiment_pos.append(sum(day_positive) / len(day_positive))
        sentiment_neg.append(sum(day_negative) / len(day_negative))
    d={"c0":sentiment,"p0":sentiment_pos,"n0":sentiment_neg,"Date":str(sdate.strftime("%Y-%m-%d"))}
    sentiment_df=pd.DataFrame(data=d).set_index("Date")
    return sentiment_df #, sentiment_pos, sentiment_neg

#call and set API from yahoo financials - crude oil price
yahoo_financials = YahooFinancials('CL=F')
crude_prices=(yahoo_financials.get_historical_price_data("2020-06-01", "2022-06-01", "weekly"))

#set json object and write crrude prices to json
json_object= json.dumps(crude_prices['CL=F']['prices'], indent = 4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object) 
    
#read json
crude_prices = pd.read_json('sample.json')
#create dataframe for crude prices 
crude_prices_df = pd.DataFrame(crude_prices)
#drop unneeded columns 
crude_prices_df.drop(['date','high','low','open','adjclose'],axis=1, inplace = True)
#rename columns and set index of dataframe on date
crude_prices_df.rename(columns = {'close':'Crude Close', 'volume':'Crude Volume','formatted_date':'Date'}, inplace = True)
crude_prices_df.set_index('Date', inplace = True)
#call yahoo financial to get gold prices 
yahoo_financials = YahooFinancials('GC=F')
gold_prices=(yahoo_financials.get_historical_price_data("2020-06-01", "2022-06-01", "weekly"))
#set json object and write gold prices to json
json_object= json.dumps(gold_prices['GC=F']['prices'], indent = 4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
gold_prices = pd.read_json('sample.json')
#convert gold prices to dataframe
gold_prices_df = pd.DataFrame(gold_prices)
#drop unneeded columns from the data frame
gold_prices_df.drop(['date','high','low','open','adjclose'],axis=1, inplace = True)
#rename columns and set index to date 
gold_prices_df.rename(columns = {'close':'Gold Close', 'volume':'Gold Volume','formatted_date':'Date'}, inplace = True)
gold_prices_df.set_index('Date', inplace = True)
#call api for SPY s and p 500 data
yahoo_financials = YahooFinancials('SPY')
SPY_prices=(yahoo_financials.get_historical_price_data("2020-06-01", "2022-06-01", "weekly"))
#set json object and write data 
json_object= json.dumps(SPY_prices['SPY']['prices'], indent = 4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
#read the json data
SPY_prices = pd.read_json('sample.json')
#convert json to a data frame
SPY_prices_df = pd.DataFrame(SPY_prices)
#drop unneedeeed columns, rename columns and set index to date 
SPY_prices_df.drop(['date','high','low','open','adjclose'],axis=1, inplace = True)
SPY_prices_df.rename(columns = {'close':'SPY Close', 'formatted_date':'Date','volume':'SPY Volume'}, inplace = True)
SPY_prices_df.set_index('Date', inplace = True)
#call api and get bitcoin prices 
yahoo_financials = YahooFinancials('BTC-USD')
BTC_prices=(yahoo_financials.get_historical_price_data("2020-06-01", "2022-06-01", "weekly"))
#set sson object and write data
json_object= json.dumps(BTC_prices['BTC-USD']['prices'], indent = 4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
#create Btc data frame
BTC_prices_df = pd.DataFrame(BTC_prices)
#drop undeeded columns, rename columns set index of data frame to date
BTC_prices_df.drop(['date','high','low','open','adjclose'],axis=1, inplace = True)
BTC_prices_df.rename(columns = {'close':'BTC Close', 'volume':'BTC Volume','formatted_date':'Date'}, inplace = True)
BTC_prices_df.set_index('Date', inplace = True)
# call yahoo financial api for eth data
yahoo_financials = YahooFinancials('ETH-USD')
ETH_prices=(yahoo_financials.get_historical_price_data("2020-06-01", "2022-06-01", "weekly"))
#print(ETH_prices)
#set json obect write data to json
json_object= json.dumps(ETH_prices['ETH-USD']['prices'], indent = 4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
#read json data
ETH_prices = pd.read_json('sample.json')
#create eath data frame
ETH_prices_df = pd.DataFrame(ETH_prices)
#drop unneeded columns, rename columns, set index to date
ETH_prices_df.drop(['date','high','low','open','adjclose'],axis=1, inplace = True)
ETH_prices_df.rename(columns = {'close':'ETH Close', 'volume':'ETH Volume','formatted_date':'Date'}, inplace = True)
ETH_prices_df.set_index('Date', inplace = True)

st.write("#Oracle of Nonsense")
st.write("Crude Asset Features Loaded")
st.write("Gold Asset Features Loaded")
st.write("S&P500 (SPY) Asset Features Loaded")
st.write("Bitcoin (BTC) Asset Features Loaded")
st.write("Ethereum (ETH) Asset Features Loaded")
         
