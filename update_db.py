import sqlite3
import os


# path to your databse

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'my_windward_app.sqlite')

con = sqlite3.connect(DATABASE_PATH)
cur = con.cursor()

try:
    cur.execute("ALTER TABLE users ADD COLUMN grade TEXT")
    print("Successfully added 'grade' column to users table!")
except sqlite3.OperationalError:
    print("Column 'grade' already exists.")

con.commit()
con.close()