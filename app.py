import datetime

from flask import Flask, render_template, request
app = Flask(__name__)
from dbmodel import DBmanager
from db import sql_name, sql_host, sql_pass,   sql_login
@app.route("/")
def home():
    base = DBmanager(sql_host, sql_login, sql_pass, sql_name)
    data = base.fetchall('''SELECT * FROM `reasons_for_stopping`''')
    print(data)
    arr = []
    for el in data:
        arr.append(el[1])
    print(arr)
    return render_template('spec.html', arr=arr)


@app.route("/read_btn", methods=['POST'])
def read_btn():
    base = DBmanager(sql_host, sql_login, sql_pass, sql_name)
    data = base.fetchall('''SELECT * FROM `reasons_for_stopping`''')
    print(data)
    arr = []
    for el in data:
        arr.append(el[1])
    print(arr)
    btn=request.form

    print(btn)
    return render_template('spec.html', arr=arr)

@app.route("/user")
def user():
    return render_template('user.html')



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


@app.route('/spec')
def spec():
    base=DBmanager(sql_host,sql_login,sql_pass,sql_name)
    data=base.fetchall('''SELECT * FROM `reasons_for_stopping`''')
    print(data)
    arr=[]
    for el in data:
        arr.append(el[1])
    print(arr)
    return render_template('spec.html', arr=arr)





@app.route('/read_form', methods=['POST'] )
def read_form():
    data=request.form
    print(data)
    return render_template('done.html')

@app.route("/getok", methods=['GET'])
def getok():
    data = request.args.get('station')
    print(data)
    if data=="off":
        base=DBmanager(sql_host,sql_login,sql_pass,sql_name)
        time=datetime.datetime.now()
        base.query('''INSERT INTO monitor(time_off) VALUES(%s)''',(time,))
    if data=="on":
        base = DBmanager(sql_host, sql_login, sql_pass, sql_name)
        time = str(datetime.datetime.now())
        lastvalue='noset'
        base.query(f'''UPDATE monitor SET time_on = {time} WHERE time_on ={lastvalue}''')
    return render_template('getok.html', data=data)

@app.route("/hardinfo", methods=['GET'])
def hardinfo():
    data = request.args.get('station')
    return render_template('getok.html', data=data)


@app.route("/operator", methods=['GET'])
def operator():
    data = request.args.get("operator")
    print(data)
    return render_template('getok.html', data=data)



if __name__=="__main__":
    app.run(debug=True)