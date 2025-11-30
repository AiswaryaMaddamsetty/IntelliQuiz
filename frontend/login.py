import tkinter as tk
from tkinter import messagebox
import sqlite3

# ------------------------- Functions -------------------------
def login():
    username = entry_user.get()
    password = entry_pass.get()
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return
    try:
        conn = sqlite3.connect("backend/quiz_app.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if cursor.fetchone():
            messagebox.showinfo("Success", f"Welcome, {username}!")
            root.destroy()  # close login window
            from frontend import home     # open home window

        else:
            messagebox.showerror("Error", "Invalid credentials")
    except Exception as e:
        messagebox.showerror("Error", f"Database error: {e}")
    finally:
        conn.close()

def register():
    username = entry_user.get()
    password = entry_pass.get()
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return
    try:
        conn = sqlite3.connect("backend/quiz_app.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration Successful! You can now login.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    finally:
        conn.close()

# ------------------------- Main Window -------------------------
root = tk.Tk()
root.title("Quiz Maker - Login")
root.geometry("500x400")  # Bigger window
root.configure(bg="#f0f0f0")  # Light grey background
root.resizable(False, False)

# ------------------------- Header Frame -------------------------
header_frame = tk.Frame(root, bg="#4a90e2", height=80)
header_frame.pack(fill="x")
header_label = tk.Label(header_frame, text="Welcome to Quiz Maker", bg="#4a90e2",
                        fg="white", font=("Helvetica", 20, "bold"))
header_label.pack(pady=20)

# ------------------------- Login Frame -------------------------
frame = tk.Frame(root, bg="#f0f0f0", padx=30, pady=30)
frame.pack(pady=20)

tk.Label(frame, text="Username:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=10)
entry_user = tk.Entry(frame, font=("Helvetica", 12), width=25)
entry_user.grid(row=0, column=1, pady=10)

tk.Label(frame, text="Password:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", pady=10)
entry_pass = tk.Entry(frame, font=("Helvetica", 12), width=25, show="*")
entry_pass.grid(row=1, column=1, pady=10)

# ------------------------- Buttons -------------------------
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

login_btn = tk.Button(btn_frame, text="Login", width=12, bg="#4a90e2", fg="white", font=("Helvetica", 12, "bold"),
                      command=login)
login_btn.grid(row=0, column=0, padx=10)

register_btn = tk.Button(btn_frame, text="Register", width=12, bg="#50e3c2", fg="white", font=("Helvetica", 12, "bold"),
                         command=register)
register_btn.grid(row=0, column=1, padx=10)

root.mainloop()
