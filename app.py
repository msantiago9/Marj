import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import render_template, redirect, session, request, jsonify
from flask.helpers import url_for
from jinja2.exceptions import TemplateNotFound

load_dotenv(find_dotenv())

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SESSION_COOKIE_SECURE"] = True


@app.before_first_request
def initialize_session_variables():
    print("First init")
    if not session.get("size"):
        session["size"] = "normal"
    if not session.get("theme"):
        session["theme"] = "dark"


@app.route("/")
def index():
    if not session["size"] or not session["theme"]:
        initialize_session_variables()
    return render_template("index.html", size=session["size"], theme=session["theme"])


@app.route("/java/<id>")
def tutorial_page(id):
    try:
        template = render_template(
            f"tutorials/{id}.html",
            prev=int(id) - 1,
            next=int(id) + 1,
            size=session["size"],
            theme=session["theme"],
        )
        return template
    except TemplateNotFound:
        return redirect(url_for("index"))


@app.route("/size", methods=["POST"])
def size_toggle():
    size = request.json.get("size")
    print(size)
    session["size"] = size
    return jsonify({"response": 200})


@app.route("/theme", methods=["POST"])
def theme_toggle():
    theme = request.json.get("theme")
    session["theme"] = theme
    return jsonify({"response": 200})


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
