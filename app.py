from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api, Resource, reqparse, abort

#this file is the core of the app, the one who connect html pages   

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type = str, help="String required", required=True)
video_put_args.add_argument("views", type = int, help="String required")
video_put_args.add_argument("likes", type = int, help="String required")

@app.route('/index', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != '#Team4':
            error = 'Invalid credentials'
        else:
            return redirect(url_for('landing_page'))
    return render_template('index.html', error=error)

@app.route("/landing")
def landing_page():
    return render_template("landing-page.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/result")
def result():
    return render_template("result.html")
        
# All the html pages have to be developed into the "templates" folder in order to make them available to the app.py
if __name__ == "__main__":
    app.run(debug=True)
