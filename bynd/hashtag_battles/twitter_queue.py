from tornado.concurrent import futures
from battleadmin.models import Hashtag
from twitter import *
import time
import bayespell
import zmq
import thread


def hashtag_stream(hashtags, auth):
    print "listening for %s" % ",".join(hashtags)
    twitter_stream = TwitterStream(auth=auth)
    iterator = twitter_stream.statuses.filter(track=",".join(hashtags))
    while True:
        print "started thread worker for %s" % ",".join(hashtags)
        for tweet in iterator:
            try: 
                hashtag = "#"
                try:
                    for htag in hashtags:
                        if htag in str(tweet["text"]):
                            hashtag = str(htag)
                            err_count = bayespell.errors(tweet["text"])
                    print hashtag, err_count
                    if hashtag != "#": 
                        hashtag_object = Hashtag.objects.get(tag=hashtag)
                        hashtag_object.typos = hashtag_object.typos + err_count
                        hashtag_object.save()
                except:
                    pass
                continue
            except:
                time.sleep(3)
                twitter_stream = TwitterStream(auth=auth)
                iterator = twitter_stream.statuses.filter(track=",".join(hashtags))
                continue
            if die == 1:
                False



def main():
    auth = OAuth("722577635939889152-R5qyydnehjWRd9ZFwmK3K5PZEjg6MC3",
             "Ig4EC87EzQxilIhedGUKM7jPZleUmJLFc0bHnJuuAjnfK",
             "pPCXeAvd9wv5WP9WlA1h52fWd",
             "62us2GYwyUniV9TtDavbTdlCjS3nw22N8bCiN41UwrnDGEc7iX")
    thread_queue = []
    hashtags = [str(h.tag) for h in Hashtag.objects.all()]
    print "creating thread for: %s" % hashtags
    x = thread.start_new_thread(hashtag_stream, (hashtags, auth))
    thread_queue.append(x)
    ctx = zmq.Context()
    socket = ctx.socket(zmq.SUB)
    socket.bind("tcp://0.0.0.0:6000")
    socket.setsockopt(zmq.SUBSCRIBE, "job::")
    print "listening..."
    while True:
        msg = socket.recv()
        msg = msg.split("::")[-1]
        if msg in hashtags:
            print "%s updated" % msg
        else:
            print "%s created. creating job..." % msg
            hashtags.append(msg)
            global die
            die = 1
            x = thread.start_new_thread(hashtag_stream, (hashtags, auth))
            thread_queue.append(x)
            die = 0
        continue

main()
