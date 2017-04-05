__author__ = 'Naheed'

__author__ = 'Naheed'

import tweepy
import time
import sched
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def scheduler():
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc):
        print "Doing stuff..."
        # do your stuff
        s.enter(60, 1, do_something, (sc,))

    s.enter(60, 1, do_something, (s,))
    s.run()

class scraper:
    def __init__(self,):
        ckey = "2hinHF2aTTB2yFmUGrRYOoyId"
        csecret = "EDOvYminHKHjgVZHCKIuZBrUDkteQZZhsAjP8hwtZFQAXEdGqQ"
        atoken = "123304916-L33J88KA0JidxixFhXgtimMdvdfbTBswPgk5eAlW"
        asecret = "W4s5ASRhEPIfNSamQBSvc4sUPqmqylP6tN299ObG9wvBc"

        OAUTH_KEYS = {'consumer_key': ckey, 'consumer_secret': csecret,
                      'access_token_key': atoken, 'access_token_secret': asecret}
        auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
        auth.secure = True
        auth.set_access_token(atoken, asecret)

        self.api = tweepy.API(auth)
        self.tweets = []

    def usimmigration(self):
        jsonreturned = self.api.trends_available()
        import json
        from pprint import pprint
        # jsonobj = json.loads(jsonreturned)
        pprint(jsonreturned)
        jsonreturned.get
        # places = self.api.geo_search(query="op90", granularity="country", rpp=100, page=5)
        # place_id = places[0].id
        #
        # tweets = self.api.search(q="place:%s" % place_id, lang='en', show_user=True)
        #
        # cricTweet = tweepy.Cursor(self.api.search, q='cricket', geocode="23.8103,90.4125,100km").items(200)
        # for tweet in cricTweet:
        #     print tweet.created_at, tweet.text, tweet.lang
        #
        # for tweet in tweets:
        #     # print tweet.id, tweet.created_at, tweet.text + " => " +  tweet.place.name if tweet.place else "Undefined place"
        #     tweet_string = 'id:' + str(tweet.id) + " time:" + str(
        #         tweet.created_at) + " location:" + tweet.place.name if tweet.place else "DEFAULT" + " content:" + tweet.text + '\n'
        #     # f.write(tweet_string.encode('utf8'))
        #     self.tweets.append(tweet_string)

    def debbietweets(self):

        places = self.api.geo_search(query="Australia", granularity="country", rpp=100, page=5)
        place_id = places[0].id

        tweets = self.api.search(q="place:%s" % place_id, lang='en', show_user=True)

        # cricTweet = tweepy.Cursor(self.api.search, q='cricket', geocode="23.8103,90.4125,100km").items(200)
        # for tweet in cricTweet:
        #     print tweet.created_at, tweet.text, tweet.lang
        #
        for tweet in tweets:
            print tweet.id, tweet.created_at, tweet.text + " => " +  tweet.place.name if tweet.place else "Undefined place"
            tweet_string = 'id:' + str(tweet.id) + " time:" + str(tweet.created_at) + " content:" + str(tweet.text.strip()) + " location:" + tweet.place.name if tweet.place else "DEFAULT" + '\n'
            # f.write(tweet_string.encode('utf8'))
            self.tweets.append(tweet_string)

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

        places = self.api.geo_search(query="Bangladesh", granularity="country",rpp = 100, page = 5)
        place_id = places[0].id

        tweets = self.api.search(q="place:%s" % place_id,lang = 'en',show_user = True)
        for tweet in tweets:
            # print tweet.id, tweet.created_at, tweet.text + " => " +  tweet.place.name if tweet.place else "Undefined place"
            tweet_string = 'id:'+str(tweet.id)+" time:"+str(tweet.created_at)+" location:"+tweet.place.name if tweet.place else "DEFAULT"+" content:"+tweet.text+'\n'
            # f.write(tweet_string.encode('utf8'))
            self.tweets.append(tweet_string)

if __name__ == "__main__":
    sr = scraper()
    sr.usimmigration()
    # count = 0
    # maxcount = 10000
    # with open("debbietweets.txt", "a") as f:
    #     while count < maxcount:
    #         sr = scraper()
    #         sr.debbietweets()
    #
    #         for tweet in sr.tweets:
    #             f.write(tweet)
    #             f.write('\n')
    #         count += len(sr.tweets)
    #         time.sleep(100)
    #         print "total: ",count
    #         print "---------------------------------------"
    # #
    #