import tweepy
import json

# enter the corresponding information from your twitter application:
consumer_key = 'ftpSZnEi0f3JnoaBXtCg2BxH0'
# keep the quotes, replace this with your consumer key
consumer_secret = 'VX2zyXVqyhYGVsj5doIOho8VEjqQKPXrChENchyBKnzU1tWQVJ'
# keep the quotes, replace this with your consumer secret key
access_key = '796182382286163968-fc9ewRIC4gNhVRAz6ZYw0QkaDBwE2W2'
# keep the quotes, replace this with your access token
access_secret = 'QZa7h3Grix7PAVFThrsgKBa3Ic40f0wyRTSKsUGKb6m7i'
# keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        self.count = 0

    def on_connect(self):
        print("Connection established!!")

    def on_disconnect(self, notice):
        print("Connection lost!! : ", notice)

    def on_data(self, data):
        content = json.loads(data)
        if "direct_message" in content:
            print content
        return True

    def on_direct_message(self, status):
        print("Enter on_direct_message")
        print status
        return True

    def on_error(self, status):
        print (statuses)

if __name__ == "__main__":
    l = MyStreamListener()
    stream = tweepy.Stream(auth, l)
    stream.userstream()
