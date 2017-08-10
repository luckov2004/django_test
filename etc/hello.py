CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web' #'/path/to/my/app',
   # 'python': '/usr/bin/python',
    'args': (
       '--bind=0.0.0.0:8080',
       '--workers=',
       '--timeout=60',
       'hello.app',

    ),
}
#def hello(environ, start_response):
#	body = [(i + '\n') for i in environ['QUERY_STRING'].split('&')]
#	start_response ('200 OK', [('Content-Type', 'text/plain')]
#	return body
