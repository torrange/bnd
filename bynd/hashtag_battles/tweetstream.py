from tornado.concurrent import futures
from battleadmin.models import Hashtag
from twitter import *
import time
import bayespell

auth = OAuth("722577635939889152-R5qyydnehjWRd9ZFwmK3K5PZEjg6MC3",
    "Ig4EC87EzQxilIhedGUKM7jPZleUmJLFc0bHnJuuAjnfK",
    "pPCXeAvd9wv5WP9WlA1h52fWd",
    "62us2GYwyUniV9TtDavbTdlCjS3nw22N8bCiN41UwrnDGEc7iX")

twitter_stream = TwitterStream(auth=auth)
hashtags = [str(h.tag) for h in Hashtag.objects.all()]

thread_queue = []
thread_pool = futures.ThreadPoolExecutor(8)

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


def makejobs(hashtags, thread_pool):
    for hashtag in hashtags:
        print "creating job for: %s" % hashtag
        x = thread_pool.submit(hashtag_stream, hashtag)
        thread_queue.append(hashtag)


def check_new_tags(hashtags, thread_pool):
    hashtags = hashtags
    while True:
        print "checking for new tags..."
        _hashtags = [str(h.tag) for h in Hashtag.objects.all()]
        if hashtags == _hashtags:
            time.sleep(3)
            pass
        else:
            new_jobs = []
            delete_jobs = []
            for h in _hashtags:
                if h not in thread_queue:
                    new_jobs.append(h)
            if len(new_jobs) >= 1:
                print new_jobs
                makejobs(new_jobs)
            hashtags = _hashtags
            time.sleep(3)
        continue



def main():
    thread_pool.submit(makejobs, hashtags, thread_pool)
    thread_pool.submit(check_new_tags, hashtags, thread_pool)

main()

if __name__=="__main__":
    main()