from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'



#Python has a built-in variable called __name__ that records the name of the currently running module or script.

@app.route('/index')
def hello_template():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=80);