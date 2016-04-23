#from tornado.concurrent import futures
#from battleadmin.models import Hashtag
from twitter import *
import time
import bayespell
import zmq
import thread


def hashtag_stream(hashtags):
    #hashtag = str(hashtag)
    #hashtag_object = Hashtag.objects.get(tag=hashtag)
    print "listening for %s" % ",".join(hashtags)
    twitter_stream = TwitterStream(auth=auth)
    iterator = twitter_stream.statuses.filter(track=",".join(hashtags))
    while True:
        print "started thread worker for %s" % ",".join(hashtags)
        for tweet in iterator:
            try: 
                #print tweet.keys()
                hashtag = "#"
                try:
                    for htag in hashtags:
                        if htag in str(tweet["text"]):
                            hashtag = str(htag)
                    err_count = bayespell.errors(tweet["text"])
                    print hashtag, err_count
                    #hashtag_object = Hashtag.objects.get(tag=hashtag)
                    #hashtag_object.typos = hashtag_object.typos + err_count
                    #hashtag_object.save()
                    
                except:
                    pass

                continue
            except:
                print "raise!"
                time.sleep(3)
                twitter_stream = TwitterStream(auth=auth)
                iterator = twitter_stream.statuses.filter(track=",".join(hashtags))
                continue

                

auth = OAuth("722577635939889152-R5qyydnehjWRd9ZFwmK3K5PZEjg6MC3",
             "Ig4EC87EzQxilIhedGUKM7jPZleUmJLFc0bHnJuuAjnfK",
             "pPCXeAvd9wv5WP9WlA1h52fWd",
             "62us2GYwyUniV9TtDavbTdlCjS3nw22N8bCiN41UwrnDGEc7iX")



def makejob(hashtags):
    print "creating job for: %s" % hashtags
    x = thread.start_new_thread(hashtag_stream, (hashtags,))
    thread_queue.append(x)


                
def main(makejob):
    thread_queue = []
    #hashtags = [str(h.tag) for h in Hashtag.objects.all()]
    hashtags = ["#Shakespeare400", "#StGeorgesDay"]
    #makejob(hashtags)
    print "creating thread for: %s" % hashtags
    x = thread.start_new_thread(hashtag_stream, (hashtags,))
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
            print "%s not in thread_queue" % msg
            hashtags.append(msg)
            x = thread.start_new_thread(hashtag_stream, (hashtags,))
            thread_queue.append(x)
            #makejob(msg)
        continue

main(makejob)
