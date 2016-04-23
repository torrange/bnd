from tornado.concurrent import futures
from battleadmin.models import Hashtag
from twitter import *
import time
import bayespell
import zmq
import thread


def hashtag_stream(hashtag):
    hashtag = str(hashtag)
    iterator = twitter_stream.statuses.filter(track=hashtag)
    hashtag_object = Hashtag.objects.get(tag=hashtag)
    print "created job for %s" % hashtag
    while True:
        for tweet in iterator:
             try:
                  err_count = bayespell.errors(tweet["text"].replace(hashtag, ""))
                  print err_count
                  hashtag_object.typos = hashtag_object.typos + err_count
                  hashtag_object.save()
                  continue
             except:
                 print "raise!"
                 time.sleep(3)
                 iterator = twitter_stream.statuses.filter(track=hashtag)
                 continue

                

auth = OAuth("722577635939889152-R5qyydnehjWRd9ZFwmK3K5PZEjg6MC3",
             "Ig4EC87EzQxilIhedGUKM7jPZleUmJLFc0bHnJuuAjnfK",
             "pPCXeAvd9wv5WP9WlA1h52fWd",
             "62us2GYwyUniV9TtDavbTdlCjS3nw22N8bCiN41UwrnDGEc7iX")

twitter_stream = TwitterStream(auth=auth)
hashtags = [str(h.tag) for h in Hashtag.objects.all()]
thread_queue = []

def makejobs(hashtags):
    for hashtag in hashtags:
        print "creating job for: %s" % hashtag
        thread.start_new_thread(hashtag_stream, (hashtag,))
        thread_queue.append(hashtag)

def makejob(hashtag):
    print "creating job for: %s" % hashtag
    thread.start_new_thread(hashtag_stream, (hashtag,))
    thread_queue.append(hashtag)


                
def main(makejobs, makejob):    
    makejobs(hashtags)
    ctx = zmq.Context()
    socket = ctx.socket(zmq.SUB)
    socket.bind("tcp://0.0.0.0:6000")
    socket.setsockopt(zmq.SUBSCRIBE, "job::")
    print "listening..."
    while True:
        msg = socket.recv()
        msg = msg.split("::")[-1]
        if msg in thread_queue:
            print "%s in thread_queue" % msg
        else:
            print "%s not in thread_queue" % msg
            makejob(msg)
        continue

main(makejobs, makejob)

if __name__=="__main__":
    main()