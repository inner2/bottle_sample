from bottle import route, run, template, request


# localhost
@route('/')
def title():
    # call views/title.tpl
    return template('title')

# localhost:8080/show
@route('/show', method='GET')
def men():
    # GETパラメータの取得(username, men)
    username = request.query.username
    men = request.query.men

    # Controller部 =======================================
    if (username == ""):
        username = "名無しさん"

    if men in {"ramen"}:
        menname = "ラーメン"
    elif men in {"soba"}:
        menname = "そば"
    elif men in {"udon"}:
        menname = "うどん"
    else:
        menname = "Error!!"

    # View部 =============================================
    # views/show.tplを呼ぶ
    return template('show', name=username, men=menname)


run(host='localhost', port=8080, debug=True, reloader=True)