import twint
import json
import boto3
from datetime import datetime

comprehend_client = boto3.client('comprehend')


def scraping_twitter(event):
    str_body = event['body']
    body = json.loads(str_body)
    search = body['search'].split(",")
    username = body['username']
    c = twint.Config()
    c.Since = body['from']
    c.Until = datetime.today().strftime('%Y-%m-%d')
    if search:
        c.Search = search
    c.Limit = body['limit']
    if username:
        c.Username = username
    c.Store_object = True
    twint.run.Search(c)
    tw_list = twint.output.tweets_list

    tweets = []
    for x in range(len(tw_list)):
        tweet_info = vars(tw_list[x])
        sentiment = analyse_tweet(tweet_info['tweet'])
        tweet_info['sentiment'] = sentiment['Sentiment']
        tweet_info['score'] = sentiment['SentimentScore']
        tweets.append(tweet_info)

    return tweets


def analyse_tweet(tweet):
    response = comprehend_client.detect_sentiment(
        Text=tweet,
        LanguageCode='es'
    )
    return response

