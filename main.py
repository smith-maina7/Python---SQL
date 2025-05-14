import sqlite3

conn = sqlite3.connect('sql_learning.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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


# updating a record"

cursor.execute('''
    SELECT id
    FROM users
    WHERE name = ?
''', ('Alice',))  
result = cursor.fetchone()
if result:
    user_id = result[0]
    cursor.execute(''' 
        UPDATE users
        SET name = ?
        WHERE id = ?
    ''', ('Alice Smith', user_id))  
    conn.commit()
    print("Record updated successfully")
else:
    print("User not found")

 #Deleting a record

cursor.execute("SELECT id FROM users WHERE name =?", ('Bob',))
result = cursor.fetchone()

if result:
    user_id = result[0]
    cursor.execute('''
        DELETE FROM users
        WHERE id = ?''', (user_id,))
    conn.commit()
    print("Record deleted successfully")
else:
    print("User not found")

# Fetch all users from the table
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)
#Close the connection

# cursor.execute("DELETE FROM users")
# conn.commit()
# # Fetch all users from the table
# cursor.execute("SELECT * FROM users")
# for row in cursor.fetchall():
#     print(row)
cursor.close()
conn.close()


 
