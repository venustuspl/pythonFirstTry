import jinja2
from flask import Flask, render_template, request, session
import MyDataSource as mds
app = Flask(__name__)
app.config["SECRET_KEY"]='moje_haslo'


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'



#Python has a built-in variable called __name__ that records the name of the currently running module or script.

@app.route('/index')
def hello_template():
    return render_template("index.html", first_name="Tomek", last_name="K.")

#Jinja to lekki silnik szablonów, który pozwala na tworzenie dynamicznych stron internetowych za pomocą języka Python
@app.route("/products")
def products():
    return render_template("products.html", products=mds.getAll())

@app.route("/my_session")
def my_session():
    print('adding user to session')
    session['account_manager']='Mr. Smith'
    print('logged user:' + session['account_manager'])
    return "";

if __name__ == '__main__':
    app.run(debug=True, port=80);

