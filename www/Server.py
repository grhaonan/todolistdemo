__author__ = 'gr_haonan'
import os.path
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options

define ("port", default=8000, help="run on the given port", type=int)
define ("mysql_host",default="127.0.0.1:3306",help="db host")
define ("mysql_database", default="todolist",help="db name")
define ("mysql_user",default="root",help="db user")
define ("mysql_password",default="liucong_3689",help="db password")

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__),"templates")
STATIC_PATH =os.path.join(os.path.dirname(__file__),"static")


class IndexHandler(tornado.web.RequestHandler):


    def get(self):
        #PreArgument=self.get_argument('greeting', 'Hello')
        #self.write(PreArgument + ', I am Dustin')
        self.render('ToDoListHome.html')




# Define different handler to handle response
class ToDoApplication(tornado.web.Application):
    def __init__(self):
        handlers =[
            (r"/",IndexHandler)
            #Define more handlers
        ]

        path_settings = dict(
            template_path= TEMPLATE_PATH,
            static_path=STATIC_PATH
        )
        tornado.web.Application.__init__(self, handlers, **path_settings)
        self.db = torndb.Connection(
            host = options.mysql_host,
            database = options.mysql_database,
            user = options.mysql_user,
            password = options.mysql_password
        )



#Define main: SetUp the HTTP Server and listen to predefined port to wait for http request

def main():
    tornado.options.parse_command_line()
    #app=tornado.web.Application(handlers=[(r"/",IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(ToDoApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

# Make sure the code can only be exacuated by local base
if __name__=="__main__":
    main()
