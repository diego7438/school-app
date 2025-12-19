import sqlite3
import os

# This points to the location where our app will create the database.
# It's inside a folder called 'instance' that Flask manages.
DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'my_windward_app.sqlite')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

# Ensure the instance folder exists
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

# Connect to the database (this will create it if it doesn't exist)
connection = sqlite3.connect(DATABASE_PATH)

# Open and execute the schema file
# This runs the SQL commands in schema.sql to create tables
with open(SCHEMA_PATH) as f:
    connection.executescript(f.read())

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Database initialized successfully at:", DATABASE_PATH)
