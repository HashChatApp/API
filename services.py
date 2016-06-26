import tweepy

class TwitterService:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(self.auth)

    def getTrends(self, lat=-1, lon=-1):
        if lat == -1 or lon == -1 or lat == None or lon == None:
            # No location available, get worldwide trends
            return self.api.trends_place(id=1)

        id = self.api.trends_closest(lat=lat, long=lon)[0]["woeid"]
        return self.api.trends_place(id=id)

    def get_authorization_url(self):
        try:
            return self.auth.get_authorization_url()
        except tweepy.TweepError:
            print 'Error! Failed to get request token.'

        return nil
