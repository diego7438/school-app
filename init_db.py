import sqlite3
import os
import psycopg2

# This points to the location where our app will create the database.
# It's inside a folder called 'instance' that Flask manages.
DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'my_windward_app.sqlite')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

# Ensure the instance folder exists
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

def get_db_connection():
    # If we are on Render, DATABASE_URL will exist
    if os.environ.get('DATABASE_URL'):
        return psycopg2.connect(os.environ.get('DATABASE_URL'))
    # Otherwise, use SQLite
    return sqlite3.connect(DATABASE_PATH)

connection = get_db_connection()

with open(SCHEMA_PATH) as f:
    schema_sql = f.read()

    if os.environ.get('DATABASE_URL'):
        # Postgres compatibility: Replace SQLite's AUTOINCREMENT with Postgres's SERIAL
        schema_sql = schema_sql.replace("INTEGER PRIMARY KEY AUTOINCREMENT", "SERIAL PRIMARY KEY")
        with connection.cursor() as cur:
            cur.execute(schema_sql)
    else:
        connection.executescript(schema_sql)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Database initialized successfully at:", DATABASE_PATH)
