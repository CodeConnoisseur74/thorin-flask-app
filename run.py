import os
import json
from flask import Flask, render_template, request, flash
<<<<<<< HEAD
if os.path.exists("env.py"):
    import env
=======
>>>>>>> 067b7b2 (add missing files)

if os.path.exists("env.py"):
    import env

# variable 'app'
# first argument of th3e Flask class is 'name'
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# Decorator : A way of wrapping functions
# (pie-notation)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
<<<<<<< HEAD
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
=======
        flash(
            "Thanks {}, we have received your message!".format(
                request.form.get("name"))
        )
>>>>>>> 067b7b2 (add missing files)
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# '__main__' is default module
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )
