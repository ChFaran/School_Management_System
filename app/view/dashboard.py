import tkinter as tk

def open_dashboard():
    dash = tk.Tk()
    dash.title("Dashboard")
    dash.geometry("400x300")

    tk.Label(dash, text="Welcome to the School Dashboard!", font=("Arial", 14)).pack(pady=20)
    tk.Button(dash, text="Exit", command=dash.destroy).pack(pady=10)

    dash.mainloop()