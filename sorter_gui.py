import tkinter as tk
import webbrowser
import re

# Parameters
background_colour = '#263D42'
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
    filtered_references = ''
    for ref in references:
        # Check if empty string or just new line
        if (len(ref) == 0 or ref == '\n'):
            continue
        filtered_references += ref + ('\n\n' if ref != references[len(references) - 1] else '')
    return filtered_references

# Setting window parameters
root = tk.Tk()
root.title('Reference Sorter')

# Set icon
img = tk.PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

root.minsize(app_width, app_height)
root.resizable(False, False)

# Defining GUI layout
canvas = tk.Canvas(root, height=app_height, width=app_width, bg=background_colour)
canvas.pack(pady=10)

# Input
text_box = tk.Text(canvas, height=40, fg='white', bg=background_colour)
text_box.pack()

def help_clicked():
    webbrowser.open('https://github.com/Ethal-Askander/Reference-Sorter/blob/main/README.md', new=1)

def sort_clicked():
    '''
    Gets current text, sorts it and replaced the current text with the sorted text.
    '''
    # Get the references
    references = text_box.get('1.0', tk.END).split('\n')

    # Sort the references
    references = sort_references(references)

    text_box.replace('1.0', tk.END, references)

sort_button = tk.Button(root, text='Sort', padx=50, pady=5, fg='white', bg=background_colour, command=sort_clicked)
sort_button.place(x=(app_width / 2 - 50), y=660)

help_button = tk.Button(root, text='Help', padx=20, pady=5, fg='white', bg=background_colour, command=help_clicked)
help_button.place(x=27,y=660)

# Loop to run continously
root.mainloop()