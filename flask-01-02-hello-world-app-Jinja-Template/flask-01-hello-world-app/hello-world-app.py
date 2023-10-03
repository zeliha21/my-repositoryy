# Hello World App

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World</h1>"



@app.route("/second")
def second():
    return "<h2>This is the second page</h2>"

@app.route('/third/subthird')
def third():
    return "This is the subpage of third page"

@app.route("/forth/<string:id>")
def forth(id):
    if id.isdigit():
        return f"The id of this page is(id)"
    else:
        return f"Not a valid page id!"

app.run(debug=False)