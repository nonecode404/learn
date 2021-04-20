from flask import *
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.args.get('name', 'Flask')
    return "<h1>Hello,%s!<h1>" % name, 201
    #return redirect('https://baidu.com/')

@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d!</p>' % (2021 - year)
colors = [ "blue" , 'white', 'red']

@app.route('/colors/<any(%s):color>' % str(colors)[1:-1])
def three_colors(color):
    return '<p>color</p>'

@app.route('/hi')
def hi():
    return redirect(url_for('hello'))

@app.before_request
def do_something():
    pass

@app.route('/404')
def not_found():
    abort(404)

user = {
    'username' : 'Grey Li',
    'bio' : 'A boy ',
}

movies = [
    {'name':'My Neighbor Totoro','year': '1988'},
    {'name':'Three','year': '1988'},
    {'name':'Four','year': '1998'},
    {'name':'Five','year': '1989'},
    {'name':'Six','year': '1990'},
    {'name':'Seven','year': '2018'},
]

@app.route('/watchlist')
def watchlist():
    return render_template("watchlist.html", user=user, movies=movies)