from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response



def main():
    with Configurator() as config:
        ###  add url
        config.add_route('intro', '/')
        config.add_route('text', '/text')
        config.add_route('jobs', '/jobs')

        config.scan('views')

        application = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8000, application)
    server.serve_forever()

main()


############    second
#
# def intro(request):
#     return Response('Hi, My name is Junaid Khalid')
#

# def main():
#     with Configurator() as config:
#
#         config.add_route('intro', '/')
#         config.add_view(intro, route_name='intro')
#         application = config.make_wsgi_app()
#
#     # 8000 is the port number through which the requests of our app will be served
#     server = make_server('0.0.0.0', 8000, application)
#     server.serve_forever()
#
# main()





############  first



# from wsgiref.simple_server import make_server
# from pyramid.config import Configurator
# from pyramid.response import Response
#
#
#
# def hello_world(request):
#     return Response('Hello World!')
#
#
# if __name__ == '__main__':
#     with Configurator() as config:
#         config.add_route('hello', '/')
#         config.add_view(hello_world, route_name='hello')
#         app = config.make_wsgi_app()
#     server = make_server('0.0.0.0', 6543, app)
#     server.serve_forever()
#


