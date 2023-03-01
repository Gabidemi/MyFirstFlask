from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("todo.html.jinja", my_variable= todolist
    )

todolist=["I want to get 90+", "I want to gain a huge collection in a CCG", "I want to also get a lot of genshin characters"]

@app.route("/add", methods=['POST'])
def add():
    new_todo = request.form['new_todo']
    todolist.append(new_todo)
    return redirect(request.referrer)
    return new_todo
   

