import os
import sys

sys.path.append('/var/www/kiteeatingtree.org/application')

os.environ['PYTHON_EGG_CACHE'] = '/var/www/kiteeatingtree.org/.python-egg'

def application(environ, start_response):
    status = '200 OK'
    output = 'Heyman!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

