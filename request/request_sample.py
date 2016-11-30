from bottle import get, post, request
from bottle import route, run


# login form
@get('/login', method='GET')  # or @route('/login')
def login():
    username = request.query.get('user')
    password = request.query.get('pass')
    return '''
    <form action="/login" method="post">
            Username: <input name="username" type="text" value="{username}"/>
            Password: <input name="password" type="password" value="{password}"/>
            <input value="Login" type="submit" />
        </form>
    '''.format(username=username, password=password)


# login
@route('/login', method='POST')  # or @post('/post')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    return "{username} {password}".format(username=username, password=password)


run(host='localhost', port=8080, debug=True)