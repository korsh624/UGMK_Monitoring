from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/testadmin')
def testadmin():
    return render_template('testadmin.html')



if __name__=="__main__":
    app.run(debug=True)