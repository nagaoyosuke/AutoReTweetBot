import json
import config
import tweepy
import os

from requests_oauthlib import OAuth1Session
CK = os.environ["CONSUMER_KEY"]
CS = os.environ["CONSUMER_SECRET_KEY"]
AT = os.environ["ACCESS_TOKEN"]
ATS = os.environ["ACCESS_TOKEN_SECRET"]

''' ローカル
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET_KEY
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
'''

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
#APIインスタンスを作成
api = tweepy.API(auth)

q = "RT AND プレゼント AND exclude:nativeretweets AND min_retweets:1000" #ここに検索キーワードを設定
count = 5
search_results = api.search(q=q, lang='ja' ,count=count)
for result in search_results:
    username = result.user._json['screen_name']
    user_id = result.id #ツイートのstatusオブジェクトから、ツイートidを取得
    print(user_id)
    user = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
    print(user)
    tweet = result.text
    print(tweet)
    time = result.created_at
    print(time)
 
    try:
        api.create_friendship(username)
        print(username)
        print("をフォローしました")
    except:
        print("もうすでにフォローしている")

    try:
        api.retweet(user_id)
        print("をRTしました")
    except:
        print("もうすでにRTしている")
print("##################")
