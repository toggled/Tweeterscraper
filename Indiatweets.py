__author__ = 'Naheed'

__author__ = 'Naheed'

import tweepy
import time


class scraper:
    def __init__(self,):
        ckey = "AaGSqW4HUqj79qBAnlP0ZM21m"
        csecret = "TsR8c0LAHyMpWWRLWWujVmTrEb9mFBN4r88ksFmYlKN3iUxq4c"
        atoken = "123304916-t6F3avk1z99NDpJ87kgNOBsLoPhfJAuOopYsLLfb"
        asecret = "CAWvcFgz5vMBHKuGRYWkmJO5T69GXwbQT7qyI3NFDbVLA"

        OAUTH_KEYS = {'consumer_key': ckey, 'consumer_secret': csecret,
                      'access_token_key': atoken, 'access_token_secret': asecret}
        auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
        auth.secure = True
        auth.set_access_token(atoken, asecret)

        self.api = tweepy.API(auth)
        self.tweets = []

    def extractcrickettweets(self):
        # cricTweet = tweepy.Cursor(self.api.search, q='cricket').items(10)
        # cricTweet = tweepy.Cursor(self.api.search, q='cricket', geocode="1.290270,103.851959,10km").items(100)
        cricTweet = tweepy.Cursor(self.api.search, q='cricket', geocode="23.8103,90.4125,100km").items(200)
        for tweet in cricTweet:
            print tweet.created_at, tweet.text, tweet.lang

    def extractcyclone(self):
        # cricTweet = tweepy.Cursor(self.api.search, q='cricket').items(10)
        # cricTweet = tweepy.Cursor(self.api.search, q='cricket', geocode="1.290270,103.851959,10km").items(100)
        # cricTweet = tweepy.Cursor(self.api.search, q='debbie', geocode="25.2744,133.7751,1500km",lang = 'en').items(200)
        # for tweet in cricTweet:
        #     print tweet.id, tweet.created_at, tweet.text, tweet.lang

        places = self.api.geo_search(query="India", granularity="country",rpp = 100)
        place_id = places[0].id

        tweets = self.api.search(q="place:%s" % place_id,lang = 'en',show_user = True)
        for tweet in tweets:
            # print tweet.id, tweet.created_at, tweet.text + " => " +  tweet.place.name if tweet.place else "Undefined place"
            tweet_string = 'id:'+str(tweet.id)+" time:"+str(tweet.created_at)+" content:"+str(tweet.text.encode('utf-8'))+" location:"+str(tweet.place.name) if tweet.place else "DEFAULT"+'\n'
            # f.write(tweet_string.encode('utf8'))
            self.tweets.append(tweet_string)

if __name__ == "__main__":

    # sr.extractcrickettweets()
    count = 0
    maxcount = 5000
    with open("indiatweets.txt", "a") as f:
        while count < maxcount:
            sr = scraper()
            sr.extractcyclone()

            for tweet in sr.tweets:
                print tweet
                f.write(tweet)
                f.write('\n')
            count += len(sr.tweets)
            time.sleep(100)
            print "total: ",count
            print "---------------------------------------"