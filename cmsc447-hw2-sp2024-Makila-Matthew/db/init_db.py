import sqlite3

connect = sqlite3.connect('user_data.db')

with open('C:/Users/matth/Documents/VSCODE/SWE_HW2/cmsc447-hw2-sp2024-Makila-Matthew/db/schema.sql') as f:
    connect.executescript(f.read())

cur = connect.cursor()
init_names = ['Steve Smith', 'Jian Wong', 'Chris Peterson', 'Sai Patel', 
              'Andrew Whitehead', 'Lynn Roberts', 'Robert Sanders']
init_ids = [211, 122, 213, 524, 425, 626, 287]
init_points = [80, 92, 91, 94, 99, 90, 75]

for i in range(len(init_names)):
    cur.execute("INSERT INTO users (user_name, id, points) VALUES (?, ?, ?)",
            (init_names[i], init_ids[i], init_points[i]))

connect.commit()
connect.close()
