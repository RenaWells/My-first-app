# Import tkinter and simpledialog
import tkinter as tk
from tkinter import simpledialog

# Define the root window
ROOT = tk.Tk()

# Define input dialog


# Define the input dialog
USER_INP = simpledialog.askstring(title="My first app",
                                  prompt="Do you like iced tea ?:")

# Print the user input
print("Hello Thxs for trying out my first app", USER_INP)
