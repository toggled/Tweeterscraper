__author__ = 'Naheed'

import preprocessor as p
import re,sys

class Tweetcollection:
    def __init__(self,tweets):
        self.tweets = tweets
        p.set_options(p.OPT.SMILEY, p.OPT.NUMBER, p.OPT.EMOJI,p.OPT.MENTION,p.OPT.URL,p.OPT.RESERVED)

    def cleantweet(self,tweet):
        # try:
        #     parsed_tweet = p.parse(tweet)
        # except:
        #     print parsed_tweet
        cleanedtweets = p.clean(tweet).split()
        # for url in p.parse(tweet).urls:
        #     cleanedtweets.append(url)
        return cleanedtweets

    def getcleantweets(self):
        self.cleanedtweets = []
        for tweet in self.tweets:
            self.cleanedtweets.append(self.cleantweet(tweet))

        return self.cleanedtweets

class TweetsPreprocessor:
    def __init__(self,filename):
        self.loc = []
        self.cont = []
        self.id = []
        self.timestamp = []
        with open(filename, "r") as f:
            lines = ' '.join(f.readlines())

            matchObj = re.findall(r'(id:)(\w+)', lines)
            for id in matchObj:
                self.id.append(id[1])

            matchObj = re.findall(r'(time:)(\w+\-\w+\-\w+ \w+\:\w+\:\w+)', lines)
            for time in matchObj:
                self.timestamp.append(time[1])
                # print time
            temp_cont = lines.split(" location:")
            for id, sth in enumerate(temp_cont):
                if id == 0:
                    con = sth.split("content:")[-1]
                    self.cont.append(con)
                else:
                    if id != len(temp_cont) - 1:
                        self.cont.append(sth.split("content:")[-1])
                    self.loc.append(sth.split(" id:")[0].strip())
            # print len(loc), loc
            # print len(cont), cont
    def gettweetsasdict(self):
        return dict(zip(self.id,zip(self.timestamp,self.loc,self.cont)))

    def getonlytweets(self):
        # print self.id[0],self.cont[0]
        return dict(zip(self.id,self.cont))

if __name__ == "__main__":
    # tp = TweetsPreprocessor('debbietweets.txt')
    tp = TweetsPreprocessor('sgtrend.txt')
    # tp = TweetsPreprocessor('Indiatweets.txt')
    tweets = tp.getonlytweets()
    print len(tweets)
    cleanedtweets = Tweetcollection(tweets.values()).getcleantweets()
    data =  zip(tweets.keys(),cleanedtweets)
    # with open('australia.txt','w') as f:
    # with open('bd.txt', 'w') as f:
    with open('sgtweets.txt', 'w') as f:
        for id,tweet in data:
            # print id,tweet
            twt = ""
            for t in tweet:
                # if isinstance(t, str):
                try:
                    twt+=(str(t)+" ")
                except:
                    continue
            # print twt
            st = "\"uid\" : \"" + id +"\" "+"\"content\" :"+" \""+twt+"\""+'\n'
            f.write(st.decode('utf-8'))
    print "tweets total: " ,len(data)