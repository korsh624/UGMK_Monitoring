from flask import Flask, render_template, request
from mysql.connector import connect
import dbmodel
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    conn = connect(

        user='gb_ugmk',

        password='XyqbS49JX-pP',

        host='mysql94.1gb.ru',

        database='gb_ugmk',
        ssl_disabled=True)
    cur = conn.cursor()
    cur.execute('SELECT * FROM monitor')
    bdinfo= cur.fetchall()
    print(bdinfo)
    conn.close()
    return render_template('admin.html',bdinfo=bdinfo)

@app.route('/testadmin')
def testadmin():
    return render_template('testadmin.html')



if __name__=="__main__":
    app.run(debug=True)