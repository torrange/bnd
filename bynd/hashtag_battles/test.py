from sqlasync import database
from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
from battleadmin.models import Battle
from battleadmin.models import Hashtag

class GetUserHandler(tornado.web.RequestHandler):
    def get(self):
	battles = queryset = Battle.objects.all()
        hashtags = Hashtag.objects.all()
	self.write({"response":"OK"})

class Application(tornado.web.Application):
    def __init__(self):
	handlers =  [ (r"/", GetUserHandler),]
	settings = {}
	tornado.web.Application.__init__(self, handlers, **settings)


def main():
    settings = {} 
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
