# notification_service.py
import tkinter as tk
from tkinter import messagebox

def show_popup(message="Script completed successfully!"):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Notification", message)
    root.destroy()  # Close the popup
