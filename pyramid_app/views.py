from pyramid.response import Response
from pyramid.view import view_config
import json
from wsgiref.simple_server import make_server
from pyramid.config import Configurator



@view_config(route_name='intro')
def home_page(request):
    header = '<h2 style="text-align: center;">Home Page</h2>'
    body = '<br><br><p style="text-align: center; font-family: verdana; color: blue;">Hi, My name is Junaid Khalid.</p>'
    body += '<p style="text-align: center; font-family: verdana;"> This is my portfolio website.</p>'
    footer = '<p style="text-align: center; font-family: verdana;">Checkout my <a href="/jobs">previous jobs</a>.</p>'


    return Response(header + body + footer)



@view_config(route_name='begin')
def job_history1(request):
    ctx = {
        "Teacher": "Ulug'bek Valiyev",
        "ball": 5
    }
    json_body = json.dumps(ctx)
    return Response(body=json_body, content_type='application/json', charset='utf-8')


    #return Response(ctx)

@view_config(route_name='jobs')
def job_history(request):
    header = '<h2 style="text-align: center;">Job History</h2>'
    job1 = '<p style="text-align: center; font-family: verdana;">Jr. Software Developer at XYZ</p>'

    return Response(header + job1)




# def main():
#     with Configurator() as config:
#         config.add_route('intro', '/')
#         config.add_route('begin', '/begin')
#         config.add_route('jobs', '/jobs')
#         config.scan()
#         app = config.make_wsgi_app()
#     return app
#
#
# if __name__ == '__main__':
#     app = main()
#     server = make_server('0.0.0.0', 8080, app)
#     print("Server running at http://localhost:8080")
#     server.serve_forever()
#

