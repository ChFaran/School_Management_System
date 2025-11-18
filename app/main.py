import tkinter as tk
from app.views.login import LoginWindow
from app.utils.database import Database


class SchoolManagementApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("School Management System")
        self.root.geometry("1200x800")

        # Initialize database
        self.db = Database()

        # Apply styling
        from app.utils.style import apply_style
        apply_style()

        # Start with login window
        self.show_login()

    def show_login(self):
        """Clear current window and show login"""
        for widget in self.root.winfo_children():
            widget.destroy()
        LoginWindow(self.root, self)

    def run(self):
        """Start the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = SchoolManagementApp()
    app.run()