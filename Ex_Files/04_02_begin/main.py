
from distutils.log import debug
from flask import Flask

app = Flask(__name__)
# enclosing the name with two underscores is called dunderscores


@app.route("/")
def hello():
    return "Hello World"


app.run(debug=True)
