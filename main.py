from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('users.html')

@app.route('/login')
def login_front():
    return render_template('login.html')




@app.route('/result', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            print(1)
            email = request.form['email']
            password = request.form['password']
            print(2)
            with sql.connect("database.db") as con:
                print(3)
                cur = con.cursor()
                print(4)
                cur.execute("INSERT INTO users (email,password)VALUES(?, ?)",(email,password) )
                print(5)
                con.commit()
                #pin_col =cur.fetchall()
                print(6)
                msg = "evviva"
                print(7)

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/login_back', methods=['POST','GET'])
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
                msg = "login riuscito"
                return render_template("result.html", msg=msg)
            else:
                msg = "login fallito"
                return render_template("result.html", msg=msg)







@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from users")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)