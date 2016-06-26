import tweepy

class TwitterService:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def getTrends(self, lat=-1, lon=-1):
        if lat == -1 or lon == -1 or lat == None or lon == None:
            # No location available, get worldwide trends
            return self.api.trends_place(id=1)

        id = self.api.trends_closest(lat=lat, long=lon)[0]["woeid"]
        return self.api.trends_place(id=id)
