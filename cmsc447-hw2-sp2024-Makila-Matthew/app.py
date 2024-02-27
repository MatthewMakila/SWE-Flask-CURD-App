from flask import Flask, render_template
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

@app.route('/create_user')
def create_user():
    connect = get_db_connection()
    users = connect.execute('SELECT * FROM users').fetchall()
    connect.close()
    return render_template('create_user.html', users=users)

"""
@app.route('/search_user')
def create_user():
    connect = get_db_connection()
    users = connect.execute('SELECT * FROM users').fetchall()
    connect.close()
    return render_template('search_user.html', users=users)
"""