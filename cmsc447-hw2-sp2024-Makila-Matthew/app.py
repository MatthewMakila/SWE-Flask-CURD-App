from flask import Flask, render_template, request, url_for, abort, redirect, flash
import sqlite3
 
app = Flask(__name__)

# my secret key
app.config['SECRET_KEY'] = 'after 7 - sara smile'

# my methods
# connect to sqlite
def get_db_connection():
    connect = sqlite3.connect('user_data.db')
    connect.row_factory = sqlite3.Row
    return connect

# grab a user's id for create/delete
def get_user(user_id):
    connect = get_db_connection()
    user = connect.execute('SELECT * FROM users WHERE id = ?',
                           (user_id,)).fetchone()
    connect.close()
    if user is None:
        abort(404) # user did not exist
    return user

# searching for users
def search_users(query):
    connect = get_db_connection()
    # ensures we can get a user with any matching part of name or a complete ID!
    users = connect.execute("SELECT * FROM users WHERE user_name LIKE ? OR id = ?", 
                            ('%' + query + '%', query)).fetchall()
    connect.close()
    return users


#######################App Routing##############################
# app routes to pages for functionality
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

        # add the new user into the db
        connect = get_db_connection()
        connect.execute('INSERT INTO users (user_name, id, points) VALUES (?, ?, ?)',
                    (name, id, points))
        connect.commit()
        connect.close()
        return redirect(url_for('index')) # auto-send back to home upon success
    
    return render_template('create_user.html')

# the search/lookup page
@app.route('/search_user/', methods=('GET', 'POST'))
def search_user():
    connect = get_db_connection()
    users = connect.execute('SELECT * FROM users').fetchall()
    connect.close()

    if request.method == 'POST':
        query = request.form['query']
        users = search_users(query)
        return render_template('search_user.html', users=users, query=query)
    
    return render_template('search_user.html', users=users)

# edit a user's info
@app.route('/<int:id>/edit_user/', methods=('GET', 'POST'))
def edit_user(id):
    user = get_user(id)

    if request.method == 'POST':
        name = request.form['user_name']
        points = request.form['points']

        # make the edit from user and redirect back home
        connect = get_db_connection()
        connect.execute('UPDATE users SET user_name = ?, points = ?'
                    ' WHERE id = ?',
                    (name, points, id))
        connect.commit()
        connect.close()
        return redirect(url_for('index'))

    return render_template('edit_user.html', user=user)

# delete a user
@app.route('/<int:id>/delete_user/', methods=('POST',))
def delete_user(id):
    user = get_user(id)
    connect = get_db_connection()
    connect.execute('DELETE FROM users WHERE id = ?', (id,))
    connect.commit()
    connect.close()
    
    # let them know deletion worked and return home
    flash('"{}" was removed from the database :O'.format(user['user_name']))
    
    return redirect(url_for('index'))
