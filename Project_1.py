from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import read_write_file_algorithm as rd
import time
ckey='A7wThk54hZMHwPPUgz5ynivJc'
csecret='n1zJUs98zFRjquwi0NLctdjsFTleKebYiNpmWdtuQqzxeUvfOV'
atoken='1195073922-3BR3hH0Ls69h2GDLLBf7fE1JGNOtcChtlIqAnou'
asecret='FMHyEiPv39y2A9KDJAY4cEHPZmmBptuLNW8hyE6lKBurE'

class listener(StreamListener):
    def on_data(self, raw_data):
        try:
            #print(raw_data)
            rd.read_write_file('Trumps.txt',raw_data)
            return True
        except BaseException:
            print('Failed on data')
            time.sleep(5)
    def on_error(self, status_code):
        print(status)
auth=OAuthHandler(ckey,csecret) # This set the authentication parameters
auth.set_access_token(atoken,asecret) # This set the auth for the token
twitterStream=Stream(auth,listener()) #set the stream pass-through
twitterStream.filter(track=["Trump"])




