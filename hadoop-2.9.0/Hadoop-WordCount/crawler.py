import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'WbaP94BKvPV0onNipttz8GxJh'
consumer_secret = 'sA3vrhAaUeHNKWDUHsbyURjRhjNIXrzw4Ns1buSnxIvrST4L42'
access_token = '2691538652-PLw61qVoUYHcAE2HiFN0FunRC9tVAcy5PgYC6nO'
access_token_secret = 'MjCh36tExJBtASapozPnlB3T2dhOZbqjLwzqTw0EsSYVO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('tendencias.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="corrupto",count=100, lang="es", since="2018-01-01").items():
    #print ("hola")
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

print ("finished")
