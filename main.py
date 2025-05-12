import sqlite3

conn = sqlite3.connect('sql_learning.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY aUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# Insert a record
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Bob', 25))
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Charlie', 35))

# Commit the changes
conn.commit()

# Fetch all users from the table
cursor.execute("SELECT * FROM users")

# Fetch all rows
rows = cursor.fetchall()
for row in rows:
    print(row)

    # cursor.executemany() function used to insert multiple records at once
more_users = [
    ('David', 28),
    ('Eve', 22),
    ('Frank', 40)
]
cursor.executemany('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', more_users)

#fetchall() function used to fetch all records from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit the changes
cursor.close()
conn.close()


 
