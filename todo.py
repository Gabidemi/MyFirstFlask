from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "Ayo": generate_password_hash("BakuganIsMyChildhood#2009")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

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

    cursor.execute("SELECT * FROM `Todos` ORDER BY `Complete`ASC;")

    result = cursor.fetchall()

    print(result[1])
    return render_template("todo.html.jinja", my_variable= result
    )

todolist=["I want to get 90+", "I want to gain a huge collection in a CCG", "I want to also get a lot of genshin characters"]

@app.route("/add", methods=['POST'])
@auth.login_required
def add():
    new_todo = request.form['new_todo']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO `Todos`(`description`) VALUES('"+ new_todo  +"')")
    return redirect(request.referrer)
    return new_todo
   

@app.route("/complete", methods=["POST"])
@auth.login_required
def complete():
    todo_id = request.form['todo_id']
    cursor = connection.cursor()
    cursor.execute(f"UPDATE `Todos` SET `Complete` = 1 WHERE `Id` = {todo_id}")


    return redirect("/")


