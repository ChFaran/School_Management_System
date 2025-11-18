import tkinter as tk
from tkinter import messagebox
from app.view.dashboard import open_dashboard

def login_screen():
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200")

    tk.Label(root, text="Username").pack(pady=5)
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Password").pack(pady=5)
    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()

    def validate_login():
        username = entry_user.get()
        password = entry_pass.get()
        if username == "admin" and password == "1234":
            root.destroy()
            open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    tk.Button(root, text="Login", command=validate_login).pack(pady=10)

    root.mainloop()