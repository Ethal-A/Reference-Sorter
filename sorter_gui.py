import tkinter as tk
from tkinter import messagebox
import os
import re

# Parameters
app_width = 700
app_height = 700

def sort_references(references):
    '''
    @param references: a list of references
    
    @returns list of references in sorted alphabetical order

    Ignores all non-latin characters (sorts only bazed on a-z and A-Z)
    '''
    # Ignore all non-latin characters and sort
    references = sorted(references, key=lambda x: re.sub('[^A-Za-z]+', '', x).lower())
    
    # filter references
    filtered_references = ""
    for ref in references:
        # Check if empty string or just new line
        if (len(ref) == 0 or ref == "\n"):
            continue
        filtered_references += ref + ('\n\n' if ref != references[len(references) - 1] else '')
    return filtered_references

root = tk.Tk()
# TODO, make screen not resize-able and remove the full screen option
root.maxsize(app_width, app_height)
root.minsize(app_width, app_height)

# Defining GUI layout
canvas = tk.Canvas(root, height=app_height, width=app_width, bg="#263D42")
canvas.pack(pady=10)

# Frame (inside) layout
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

text_box = tk.Text(canvas, height=40, fg="white", bg="#263D42")
text_box.pack()

def help_clicked():
    messagebox.showinfo(title='Help', message="")

def sort_clicked():
    '''
    Gets current text, sorts it and replaced the current text with the sorted text.
    '''
    # Get the references
    references = text_box.get("1.0", tk.END).split('\n')

    # Sort the references
    references = sort_references(references)

    text_box.replace("1.0", tk.END, references)

sort_button = tk.Button(root, text="Sort", padx=50, pady=5, fg="white", bg="#263D42", command=sort_clicked)
sort_button.place(x=(app_width / 2 - 50), y=660)

help_button = tk.Button(root, text="Help", padx=20, pady=5, fg="white", bg="#263D42", command=help_clicked)
help_button.place(x=27,y=660)

# Loop to run continously
root.mainloop()