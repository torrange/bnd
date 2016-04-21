from battleadmin.models import Hashtag
from twitter import *
import bayespell
import threading
import time


class TweetThreading(object):

    def __init__(self, hashtag, interval=1):
        self.interval = interval
	self.hashtag = hashtag
        thread = threading.Thread(target=self.stream_processor, args=(self.hashtag))
        thread.daemon = True
        thread.start()

    def stream_processor(self, hashtag):
	iterator = twitter_stream.statuses.filter(track=hashtag)
        hashtag_object = Hashtag.objects.get(tag=hashtag)
        while True:
	    for tweet in iterator:
		try:
		    err_count = bayespell.errors(tweet["text"].replace(hashtag, "")
		    print err_count)
		    hashtag_object.typos = hashtag_object.typos + err_count
		    hashtag_object.save()
		    continue
		except:
		    print "raise!"
		    time.sleep(5)
		    iterator = twitter_stream.statuses.filter(track=hashtag)
		    continue

		    

















auth = OAuth("722577635939889152-R5qyydnehjWRd9ZFwmK3K5PZEjg6MC3", 
    "Ig4EC87EzQxilIhedGUKM7jPZleUmJLFc0bHnJuuAjnfK",
    "pPCXeAvd9wv5WP9WlA1h52fWd",
    "62us2GYwyUniV9TtDavbTdlCjS3nw22N8bCiN41UwrnDGEc7iX")

twitter_stream = TwitterStream(auth=auth)
hashtags = [TweetThreader(ht.tag) for ht in Hashtag.objects.all()]

#for hashtag_tuple in hashtags:











def hashtag_stream_processor(hashtag):
    iterator = twitter_stream.statuses.filter(track=hashtag)
    hashtag_object = Hashtag.objects.get(tag=hashtag)
    for tweet in iterator:
	err_count = bayespell.errors(tweet["text"].replace(hashtag, ""))
	hashtag_object.typos = hashtag_object.typos + err_count
	hashtag_object.save()
	continue
    return 
