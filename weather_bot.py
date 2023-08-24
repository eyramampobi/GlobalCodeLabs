import tweepy
import pyowm
import time

consumer_key = "hnYHufNnz07m93lKvbhzjf2nQ"
consumer_secret = "Kr0Jp9rXlG0bnJmas4DMhW78mhLnxv2Fm0noZchE80eBVJfIAV"
access_token = "1694718644331421697-s9lxX3MOzj8D5guGrSZI9tJYhbSIbv"
access_token_secret = "HTp8Kmkc7rrlZGEJN6kBEv9oCXDEp2bfa3fbZLdPTyRB6"

auth = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
                     access_token=access_token, access_token_secret=access_token_secret)


owm = pyowm.OWM('1e2c5b9103431398f3e092ae93b6a865')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('London')

w = observation.weather
tweet_interval = 20

condition = int(w.temperature('celsius')["temp"])
while True:
    if condition >= 5 and condition <= 20:
        auth.create_tweet(text="❄️")
    elif condition >= -10 and condition <= 5:
        auth.create_tweet(text="❄️")
    elif condition > 20:
        auth.create_tweet(text="☀️")
   
    
    else:
       auth.create_tweet(text="You are not human")
    time.sleep(tweet_interval)
        