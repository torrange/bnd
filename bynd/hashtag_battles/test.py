from sqlasync import database
from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
from battleadmin.models import Battle
from battleadmin.models import Hashtag
from twitter import *


class GetUserHandler(tornado.web.RequestHandler):
    def get(self):
	battles = queryset = Battle.objects.all()
        hashtags = Hashtag.objects.all()
	print hashtags
	self.write({"response":"OK"})

class Application(tornado.web.Application):
    def __init__(self):
	handlers =  [ (r"/", GetUserHandler),]
	settings = {}
	tornado.web.Application.__init__(self, handlers, **settings)


def main():
    auth = OAuth("722577635939889152-R5qyydnehjWRd9ZFwmK3K5PZEjg6MC3", 
	"Ig4EC87EzQxilIhedGUKM7jPZleUmJLFc0bHnJuuAjnfK",
	"pPCXeAvd9wv5WP9WlA1h52fWd",
	"62us2GYwyUniV9TtDavbTdlCjS3nw22N8bCiN41UwrnDGEc7iX")
    t = Twitter(auth=auth)
    settings = {} 
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


main()



