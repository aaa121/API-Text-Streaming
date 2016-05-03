# This cleans the streamed feeds in Project_1b.py by adding favourite and retweet counts
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import read_write_file_algorithm as rd
import time
import sys
from http.client import IncompleteRead
ckey='A7wThk54hZMHwPPUgz5ynivJc'
csecret='n1zJUs98zFRjquwi0NLctdjsFTleKebYiNpmWdtuQqzxeUvfOV'
atoken='1195073922-3BR3hH0Ls69h2GDLLBf7fE1JGNOtcChtlIqAnou'
asecret='FMHyEiPv39y2A9KDJAY4cEHPZmmBptuLNW8hyE6lKBurE'

stop = 1000000
count=0
step=1
for i in range(0,stop,step):
    count+=1
    # print(count)
    print(i)
    class listener(StreamListener):
        def on_data(self, raw_data):
            try:
                #print(raw_data)
                tweet=raw_data.split(',"text":"')[1].split('","source')[0]
                # Note before the element in the text is comma followed by "text":".  The [1]
                # indicates the element to the right after : Also, the actual tweet ends with
                # (","source), then [0] indicates the text to the left.
                feed_time = str(time.time())  # The whole date can be input but unix timestamp is better
                # The unix time can be converted to human readable time in excel using (=(A1/ 86400) + 25569+(GMT/24))
                # GMT is the country's GMT. For instance, New Zealand standard time is +12 UTC
                retweet = raw_data.split(',"retweet_count":')[1].split(',"favorite_count":')[0] # Nuber of retweet
                likes = raw_data.split(',"favorite_count":')[1].split(',"entities":')[0] #Number of likes
                save_feed = feed_time + "," + retweet + "," + likes + "," + tweet
                # If better for the tweet to come last because of double/nested tweets cases
                # For the purpose of csv seperate by comma otherwise, use :::
                rd.read_write_file('Trump_Indiana.csv',save_feed+"\n")
                return True
            except (BaseException, AttributeError, IncompleteRead, ConnectionError):
                print(time.ctime(),'\tFailed on data')
                rd.read_write_file('Failure_log2.txt',time.ctime()+'\tFailed on data\n')
                time.sleep(5)
        def on_error(self, status_code):
            print(time.ctime, "\tEncountered Error with Status Code:\t",status_code,"\n",sys.stderr)
            return True
            print(time.ctime(),"\t Restarting Stream")


    auth=OAuthHandler(ckey,csecret) # This set the authentication parameters
    auth.set_access_token(atoken,asecret) # This set the auth for the token
    try:
        twitterStream=Stream(auth,listener()) #set the stream pass-through
        twitterStream.filter(track=["Trump"])

    except (BaseException, AttributeError, IncompleteRead, ConnectionError):
        # time.sleep(2)
        pass
print(count)