# In[2]:


import tweepy
from textblob import TextBlob
import csv
import re
import sys
import pandas as pd


# In[3]:


consumer_key = 'xxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxx'
access_token_key= 'xxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxx'


# In[4]:


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)


# In[14]:


api=tweepy.API(auth)
pubic_tweets=api.search('realDonaldTrump')
unwanted_words=[]
symbols=[]
data=[]


# In[15]:


for tweet in pubic_tweets:
    text=tweet.text
    textWords=text.split()
   
    cleanedTweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", text).split())
    print (cleanedTweet)
    analysis= TextBlob(cleanedTweet)
    print (analysis.sentiment)
    print()
    
    polarity = 'Positive'
    if(analysis.sentiment.polarity < 0):
        polarity = 'Negative'
    if(0<=analysis.sentiment.polarity <=0.2):
        polarity = 'Neutral'
   
    dic={}
    dic['Sentiment']=polarity
    dic['Tweet']=cleanedTweet
    data.append(dic)
    df=pd.DataFrame(data)
    df.to_csv('Result.csv')
    
    




