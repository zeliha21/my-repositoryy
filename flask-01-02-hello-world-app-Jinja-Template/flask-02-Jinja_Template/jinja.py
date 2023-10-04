# Using Jinja templates
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number=10, number2=20)

@app.route("/number/<string:num1>/<string:num2>")
def custom(num1,num2):
    if num1.isdigit() and num2.isdigit():
        return render_template("index.html",number1=num1,num2=num2)
    else:
        return "Invalid numbers"
    
# Create a function named number which sends number num1 and num2 and sum of them to 
# the body.html. Assign a URL route the number function with decorator @app.route('/sum').
@app.route("/sum/<string:a>/<string:b>")
def number(a, b):
    if a.isdigit() and b.isdigit():
        total = int(a) + int(b)
        html_code = render_template("body.html", num1=a, num2=b, sum=total)
        return html_code
    else:
        return "Invalid numbers to add together"
app.run(debug=False)