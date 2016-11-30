from bottle import route, run, template, request


# localhost
@route('/')
def index():
    # call views/title.tpl
    return template('index')

run(host='localhost', port=8080, debug=True, reloader=True)