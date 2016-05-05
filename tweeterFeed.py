#import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#consumer key, consumer secret, access token and access secret
ckey = "MA0aWTiDX7dYpgRrmJA0kwd8m"
csecret="xL2jH6JmhvkP7XM7KF6Zu158Y0V10MFS1mIjzCwaDhcxrZnWG4"
atoken = "264462320-ioT834SZt4HfkIutTsbgk7RU0cziisW0N7xKWnpo"
atokensecret="yynUtRkNwS0dQH665WCAmDhUl8gAiZXpXdHh7jjoNAYBv"


class listener(StreamListener):
	def on_data(self,data):
		all_data= json.loads(data)
		tweet = all_data["text"]
		print tweet
		return True

	def on_error(self,status):
		print status

auth= OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,atokensecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["marfin"])
