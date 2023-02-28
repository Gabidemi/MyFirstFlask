from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #Tells our slash that this is the homepage
def index():
    return render_template("home.html.jinja", my_variable="Never Gonna Give You Up-~",my_list=["apples", "bananas", "Oranges"]
    )


@app.route("/ping")
def ping():
    return"<p>pong</p>"

@app.route("/hello/<name>") #This is the link for it to display your name on the site
def hello(name):
    return f"<p>Hello, {name} !</p>"