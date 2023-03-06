from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)

connection = pymysql.connect(
    host="10.100.33.60",
    user="gabidemi",
    password="244655536",
    database="gabidemi_todos",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

@app.route("/")
def index():
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM `Todos`")

    result = cursor.fetchall()

    print(result[1])
    return render_template("todo.html.jinja", my_variable= result
    )

todolist=["I want to get 90+", "I want to gain a huge collection in a CCG", "I want to also get a lot of genshin characters"]

@app.route("/add", methods=['POST'])
def add():
    new_todo = request.form['new_todo']
    todolist.append(new_todo)
    return redirect(request.referrer)
    return new_todo
   

