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

# Machine Learningn 
Fitting data Window
Defining Features(sentiment score) and Target (price/market direction) 
Scaling the data: StandardScalar (Normally distributed) 
Created 2 Machine Learning Algorithms
LSTM Neural network with 2 layers. Sentiment score to predict SPY price
“Adam” optimizer incorporates momentum and exponential weighted averages
LTSM Neural network with 2 layers. Sentiment score to predict directionality of the SPY
Sigmoid activation, binary cross entropy (True/False) 


 # Deliverables:

We aim to provide a standard analysis and to display key metrics. To do so, we will use natural language processing (NLP) to run a sentiment analysis on key words involved with the asset classes chosen. This will provide us with output word counts and positive, neutral or negative sentiments associated with each asset. Our machine learning component will classify the sentiment data (positive, neutral, negative) and calculate a future prediction of sentiment.

Our deliverables include:
-	NLP sentiment scores (mark Staten)
-	An interactive dashboard (Mark Staten)
-	A Machine Learning predictive algorithim (Jacob Edelbrock)
-	Asset class and predicted values data frames and visualizations (Gerald Howard and Jacob Edelbrock)
-	Power point presentation (Gerald Howard)
-	Read Me file (Gerald Howard)









 

