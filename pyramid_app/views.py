#from pyramid.compat import escape
from pyramid.response import Response
from pyramid.view import view_config




@view_config(route_name='intro')
def home_page(request):
    header = '<h2 style="text-align: center;">Home Page</h2>'
    body = '<br><br><p style="text-align: center; font-family: verdana; color: blue;">Hi, My name is Junaid Khalid.</p>'
    body += '<p style="text-align: center; font-family: verdana;"> This is my portfolio website.</p>'
    footer = '<p style="text-align: center; font-family: verdana;">Checkout my <a href="/jobs">previous jobs</a>.</p>'


    return Response(header + body + footer)


@view_config(route_name='text')
def job_history1(request):
    ctx = {
        "Teacher":"Ulug'bek Valiyev",
        "ball": 5
    }


    return Response(ctx)

@view_config(route_name='jobs')
def job_history(request):
    header = '<h2 style="text-align: center;">Job History</h2>'
    job1 = '<p style="text-align: center; font-family: verdana;">Jr. Software Developer at XYZ</p>'

    return Response(header + job1)





