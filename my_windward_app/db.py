import sqlite3
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app, g

class CustomCursor(RealDictCursor):
    """A cursor that can store the last inserted ID."""
    pass

class PostgresWrapper:
    """
    A helper class that makes PostgreSQL look and act like SQLite.
    This allows us to switch databases without rewriting the whole app.
    """
    def __init__(self, db_url):
        self.conn = psycopg2.connect(db_url)

    def execute(self, sql, params=()):
        # 1. Translate placeholders: SQLite uses '?', Postgres uses '%s'
        sql = sql.replace('?', '%s')
        
        # 2. Create a cursor using our custom class
        cur = self.conn.cursor(cursor_factory=CustomCursor)
        
        # 3. Handle the "ID problem" (SQLite uses .lastrowid, Postgres needs RETURNING id)
        if sql.strip().upper().startswith("INSERT"):
            sql += " RETURNING id"
            cur.execute(sql, params)
            row = cur.fetchone()
            if row:
                # Store the ID on the cursor so auth.py can find it
                cur.lastrowid = row['id']
        else:
            cur.execute(sql, params)
            
        return cur

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

# this function connects to our database.db file and returns the connection
def get_db_connection():
    if 'db' not in g:
        # Check if we are on Render (DATABASE_URL will exist)
        if os.environ.get('DATABASE_URL'):
            g.db = PostgresWrapper(os.environ.get('DATABASE_URL'))
        else:
            # We are on your laptop (Local), use SQLite
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row

    return g.db