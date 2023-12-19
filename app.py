from flask import Flask, render_template, request
from dbmodel import DBmanager
from db import sql_name, sql_host, sql_pass, sql_login
app = Flask(__name__)

@app.route("/")
def home():
    base = DBmanager(sql_host, sql_login, sql_pass, sql_name)
    return render_template('index.html')

@app.route("/user")
def user():
    return render_template('user.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__=="__main__":
    app.run(debug=True)