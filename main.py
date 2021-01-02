from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource, Api, reqparse
from classes.image_recognized import ImageRecognized
from PIL import Image
import sqlite3 as sql
import os
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def login_front():
    return render_template('index.html')

"""@app.route('/enternew')
def new_student():
    return render_template('users.html')\


@app.route('/signin', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users (email,password)VALUES(?, ?)",(email,password) )
                con.commit()

        except:
            con.rollback()
            return

        finally:
            return redirect('/upload')
            
#La funzione sopra serve ad aggiungere la pagina di registrazione"""



@app.route('/upload_photo', methods=['POST','GET'])
def login_back():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with sql.connect('database.db') as con:
            cur = con.cursor()
            cur.execute('SELECT email, password FROM users WHERE email = ? AND password = ?',(email,password))
            con.commit()
            control = cur.fetchall()
            if control != []:
                return upload_front(author = True)
            else:
                return redirect('/login_failed')

@app.route('/login_failed')
def login_failed():
    return render_template("login_failed.html")

#Sopra le funzioni relative al login

"""
@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    rows = cur.fetchall()
    return render_template("list.html", rows=rows)

La funzione sopra è inaccessibile agli utenti e serve a controllare il database"""



UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_back', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect('/')
        files = request.files.getlist('files[]')
        photo_id = 0
        results = {}
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                photo = "instance/uploads/" + filename
                photo_res = ImageRecognized.image_recognized(photo)
                print(photo_res)
                os.remove(app.config['UPLOAD_FOLDER'] + "/" + filename)
                photo_id = photo_id +1
                photo_id_st = str(photo_id)
                results["Photo" + photo_id_st] = photo_res
            else:
                return redirect('/upload_failed')
        return render_template('upload.html', value=results)


@app.route('/upload_failed')
def upload_failed():
    return render_template("upload_failed.html")

def upload_front(author=''):
    if author == True:
        return render_template("upload.html")
    else:
        return redirect("/")

#sopra le funzioni che gestiscono l'upload dei files e mandano la risposta al frontend


if __name__ == '__main__':
    app.run(debug=True)

