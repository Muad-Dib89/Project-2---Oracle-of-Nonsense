# Project-2---Oracle-of-Nonsense
Project 2 
#Dashboard of economic sentiment on different asset classes

This project allows us to make future predictions of the value of various assets using historical data, media setiment and the power of machine learning. We can use these predictions to follow market trends and to anticipate asset values. After gathering data from various sources, we cleaned and processed this data for processing by our NLP and Machine Learning algorithims. After processing, we visualized the new data for analysis and presentation in order to make future predictions.  

Our deliverables include:
-	NLP sentiment scores (Mark Staten)
-	An interactive dashboard (Mark Staten)
-	A Machine Learning predictive algorithim (Jacob Edelbrock & mark Staten)
-	NLP sentiment scores (Mark Staten)
-	Asset class and predicted values data frames and visualizations (Gerald Howard and Jacob Edelbrock)
-	Power point presentation (Gerald Howard)
-	Read Me file (Gerald Howard)

#Data sources
For our data, we used various sources such as ALPACA and Yahoo Finance. We used these sources to extrapolate key metrics such as:
-	Crypto Currency prices (BitCoin and Ethereum) 
-	Stock Market closing prices
-	Crude Oil prices 
-	Gold prices 

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

# Summary:
    - Using All sentiment scores calculated from news item  to predict SPY price does not yield any useful metric
    - Using Sentiment scores to predict direction on overall accuracy starts to yield some useful insight as the accuracy overall seems to be improving
    
# Ways to potentially improve the models
    - Limit sentiment scores being used to the asset being evaluated on said sentiment scores
    - Overall prediction may improve with the addition of features other than sentiment
    - Improve the keywords used to pull in relevant news articles to provide better sentiment score
