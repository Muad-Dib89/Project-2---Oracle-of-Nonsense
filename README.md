# Project-2---Oracle-of-Nonsense
Project 2 
#Dashboard of economic sentiment on different asset classes

This project allows us to make future predictions of the value of various assets using historical data, media setiment and the power of machine learning. We can use these predictions to follow market trends and to anticipate asset values. After gathering data from various sources, we cleaned and processed this data for processing by our NLP and Machine Learning algorithims. After processing, we visualized the data and our predictions for analysis and presentation.  

#	Data sources
For our data, we used various  Yahoo Finance API calls. Historical prices dating back 2 years were pulled. Weekly pricing data was obtained
-	Crypto Currency prices and volumes (BitCoin and Ethereum) 
-	Stock Market closing prices and volumes (SPY)
-	Crude Oil prices and volumes (CL+F)
-	Gold prices and volumes  (CR=F)

For NLP and sentiment Analysis the NEWS API was utilized. 
- Top 100 articcles pulled on a weekly window over the last 2 years
- Custome function built to determine weekly sentiment score for each asset.

# Machine Learning 
Fitting data Window  
- Defining Features(sentiment score) and Target (price/market direction)   
- Scaling the data: StandardScalar (Normally distributed)   
- Created 2 Machine Learning Algorithms  
LSTM Neural network with 2 layers. Sentiment score to predict SPY price  
“Adam” optimizer incorporates momentum and exponential weighted averages  
LTSM Neural network with 2 layers. Sentiment score to predict directionality of the SPY  
Sigmoid activation, binary cross entropy (True/False)   


 # Deliverables:

We aim to provide a standard analysis and to display key metrics. To do so, we will use natural language processing (NLP) to run a sentiment analysis on key words involved with the asset classes chosen. This will provide us with output word counts and positive, neutral or negative sentiments associated with each asset. Our machine learning component will classify the sentiment data (positive, neutral, negative) and calculate a future prediction of sentiment.

Our deliverables include:
-	NLP sentiment scores (Mark Staten)
-	A Machine Learning predictive algorithim (Jacob Edelbrock,  Mark Staten)
-	Asset class and predicted values data frames and visualizations (Gerald Howard and Jacob Edelbrock)
-	Power point presentation (Gerald Howard)
-	Read Me file (Gerald Howard)

# Overview of Code Structure in Notebook

* Loading most if not all Libraries needed or plan to use
* Loading the environment settings
* Defining Functions to pull news items and to calculate the sentiment scores
 - headline_sentiment_summarizer_avg(data,sdate)
 - get_headlines(keyword,fdate,edate)
* Pulling in Asset Values into the Dataframe from yahoo financials
* Combining Asset Data into a single dataframe and setting index to DateTime, Adding feature using pandas lambda function to create a binary determination on last two weeks of data based on price for each asset class
* Commented out loop code: Pull News api data for 2 years. This is using a paid plan and to minimize cost we do not run unless our saved sentiment scores get corrupted
* Saved Sentiment scores to csv files so we dont have to keep pulling the news data using api calls
* Load all sentiment scores to a single pandas dataframe
* Create a Price Model (SPY) based on sentiment data ( We planned on all assets but did not complete that portion of the project idea )
![Sentiment Price Model Loss Function curve](/RegressionMSE_sentimentPriceModel.png)
![Sentiment Price Model Loss Function curve](/Regression_SentimentPrice_RealvsPredicted.png)

* Created a Model (SPY) to predict market direction
![Sentiment Price Model Loss Function curve](/sigmoid_sentiment_marketdirection.png)
