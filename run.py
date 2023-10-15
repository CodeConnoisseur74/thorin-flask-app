import os
from flask import Flask


# variable 'app'
# first argument of th3e Flask class is 'name'
app = Flask(__name__)


# Decorator : A way of wrapping functions
# (pie-notation)
@app.route("/")
def index():
    return "Hello, World"


# '__main__' is default module
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
