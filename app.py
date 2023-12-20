from flask import Flask, render_template, request
app = Flask(__name__)
from dbmodel import DBmanager
from db import sql_name, sql_host, sql_pass,   sql_login
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/user")
def user():
    return render_template('user.html')

@app.route("/hardinfo", methods=['GET'])
def hardinfo():
    data = request.args.get('station')
    return render_template('index.html', data=data)

@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/blank')
def blank():
    return render_template('blank.html')


@app.route('/specifythereason')
def specifythereason():
    base=DBmanager(sql_host,sql_login,sql_pass,sql_name)
    data=base.fetchall('''SELECT * FROM `reasons_for_stopping`''')
    print(data)
    arr=[]
    for el in data:
        arr.append(el[1])
    print(arr)
    return render_template('testadmin.html', arr=arr)

@app.route('/read_form', methods=['POST'] )
def read_form():
    data=request.form
    print(data)
    return render_template('done.html')



if __name__=="__main__":
    app.run(debug=True)