import sqlite3

conn = sqlite3.connect("quiz_app.db")
cursor = conn.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# Quiz history table
cursor.execute("""
CREATE TABLE IF NOT EXISTS quiz_history (
    quiz_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    difficulty TEXT,
    score INTEGER,
    date_taken DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

conn.commit()
conn.close()
