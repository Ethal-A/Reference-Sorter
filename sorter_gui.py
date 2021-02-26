import tkinter as tk
from tkinter import filedialog, Text
import os

def sort_references(references):
    '''
    @param references: a list of references
    
    @returns list of references in sorted alphabetical order

    Ignores all non-latin characters (sorts only bazed on a-z and A-Z)
    '''
    # Ignore all non-latin characters and sort
    references = sorted(references, key=lambda x: re.sub('[^A-Za-z]+', '', x).lower())
    return references

root = tk.Tk()
root.maxsize(700, 700)
root.minsize(700, 700)

# Defining GUI layout
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack(pady=10)

# Frame (inside) layout
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

text_box = tk.Text(canvas, height=40, fg="black", bg="white")
text_box.pack()

sort_button = tk.Button(root, text="Sort", padx=100, pady=5, fg="white", bg="#263D42")
sort_button.pack()

# Loop to run continously
root.mainloop()