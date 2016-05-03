import json
'''

with open('Trumps.txt', 'r') as trumpfile:
    for stream in trumpfile:
        tweet=json.JSONDecoder(stream)
        #tweet=json.loads(stream,encoding='utf-8')
        print(tweet['text'])
        #print(stream)

tweets =[]
with open('Trumps.txt', 'r') as trumpfile:
    for stream in trumpfile:
        try:
            tweets.append(json.loads(stream))
        except:
            pass
    print(len(tweets))
    #print(tweets[1])
tweeted=json.loads(tweets)
for line in tweeted:
    print(line['text'])

'''
with open('Trumps.txt', 'r') as trumpfile:
    for stream in trumpfile:
        tweet=json.dumps(stream)
        tweet_text=json.loads(tweet['text'])
        print(tweet_text)


