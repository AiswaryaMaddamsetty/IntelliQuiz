import os
import sqlite3
import tkinter as tk
from tkinter import messagebox

# ----------------------- Initialize Database -----------------------
def init_database():
    """Ensure database and tables exist before app starts."""
    db_path = os.path.join("backend", "quiz_app.db")
    if not os.path.exists(db_path):
        import backend.database  # This will auto-create tables
        print("✅ Database initialized successfully.")
    else:
        print("ℹ️ Database already exists. Skipping initialization.")

# ----------------------- Launch Login Page -----------------------
def open_login_window():
    """Import and launch the login window."""
    try:
        from frontend import login
        print("🚀 Launching Quiz Maker Login Window...")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open login window: {e}")

# ----------------------- Main Entry -----------------------
if __name__ == "__main__":
    init_database()
    open_login_window()
