from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

# simply a test for Flask import
 
app = Flask(__name__)

def get_db_connection():
    connect = sqlite3.connect('user_data.db')
    connect.row_factory = sqlite3.Row
    return connect

@app.route('/')
def index():
    connect = get_db_connection()
    users = connect.execute('SELECT * FROM users').fetchall()
    connect.close()
    return render_template('index.html', users=users)

# creating new users
@app.route('/create_user/', methods=('GET', 'POST'))
def create_user():
    # user attempts to make new user
    if request.method == 'POST':
        name = request.form['user_name']
        id = request.form['id']
        points = request.form['points']
        print(name, id, points)

        # add the new user into the db
        connect = get_db_connection()
        connect.execute('INSERT INTO users (user_name, id, points) VALUES (?, ?, ?)',
                    (name, id, points))
        connect.commit()
        connect.close()
        return redirect(url_for('index')) # auto-send back to home upon success
    
    return render_template('create_user.html')

# the search/lookup page
@app.route('/search_user/')
def search_user():
    connect = get_db_connection()
    users = connect.execute('SELECT * FROM users').fetchall()
    connect.close()
    return render_template('search_user.html', users=users)
