from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')



@app.route("/hardinfo", methods=['GET'])
def hardinfo():
    data = request.args.get('station')
    return render_template('hardinfo.html', data=data)




if __name__=="__main__":
    app.run(debug=True)