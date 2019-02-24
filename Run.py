import tweepy
import sys
import time
from random import randint
from getinfo import info

# Finding recently tweet within the seed word in seedword.txt and performing a quick text analysis.

####### Access Information (Tweepy Authenticate) ###############
consumer_key = 'TFeHlE1xHikM3DenxPk5oIscq'
consumer_secret = '1k5RjfYQXIrCajmNKjDDaNTbdvmRLJWOJEsvh5MBGZYT6UBDLV'
access_key = '2153338314-i3QyDm3M0DAArpvS6Vq2MQQHbjvfu1tcmAAlYzV'
access_secret = 'qoT0nT7pZVzD8ZXOl0XlSMdUOwMgxvvQ6RoHLenAEz0oe'
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
inputFile = 'Seedword.txt'
outputFile = 'Output.txt'
##########################################
with open(inputFile, 'r') as inFile:
    keywords = inFile.readlines()
    print(len(keywords), "seed words!")

with open(outputFile, 'w', encoding='utf8') as outFile:
    for keyword in keywords:
        print("Keyword : " + keyword)
        for tweet in tweepy.Cursor(api.search, q=keyword,
                                    include_entities=True,
                                    lang="en", tweet_mode='extended').items(20):  # 搜尋最近k筆包含字詞的推文
            if "retweeted_status" in dir(tweet):
                info(tweet.retweeted_status.id, tweet.retweeted_status.created_at, tweet.retweeted_status.full_text,outFile)

            else:
                info(tweet.id, tweet.created_at, tweet.full_text,outFile)
        randtime = randint(1, 5)
        #print("Sleep for " + str(randtime) + " seconds")
        time.sleep(randtime)
    outFile.close()
    print("Done")
