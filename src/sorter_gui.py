import tkinter as tk
from tkinter.constants import WORD
import webbrowser
import re

# References: 
# Background colour hex '#263D42' is from the following tkinter tutorial video: https://www.youtube.com/watch?v=jE-SpRI3K5g&t=551s
# Sorting latin characters ignoring all special characters (the 1 line code that does it): https://stackoverflow.com/questions/13589560/how-to-sort-list-of-string-without-considering-special-characters-and-with-case
class Sorter:
    def __init__(self, app_width=700, app_height=700, background_colour='#263D42', cursor='white'):
        # Set parameters
        self.app_width = app_width
        self.app_height = app_height
        self.background_colour = background_colour

        # Setup window
        self.root = tk.Tk()
        self.root.minsize(app_width, app_height)
        self.root.resizable(False, False)
        
        # Set title and icon
        # Note that the file location doesn't work when exporting the script as an executable. So instead, the source code of the image is provided using https://www.motobit.com/util/base64-decoder-encoder.asp.
        # Alternatively:
        # img = tk.PhotoImage(file='../images/icon.png')
        data = '''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
ZdFo/gtjVjsJHoDhWAAAAABJRU5ErkJggg=='''
        self.root.title('Reference Sorter')
        img = tk.PhotoImage(data=data)
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        # Defining input text box
        self.canvas = tk.Canvas(self.root, height=app_height, width=app_width, bg=background_colour)
        self.canvas.pack(pady=10)
        self.text_box = tk.Text(self.canvas, height=40, fg='white', bg=background_colour, insertbackground=cursor, insertwidth=3, undo=True, wrap=WORD)
        self.text_box.pack()

        # Defining buttons
        self.sort_button = tk.Button(self.root, text='Sort', padx=50, pady=5, fg='white', bg=background_colour, command=self.sort_clicked)
        self.sort_button.place(x=(app_width / 2 - 50), y=660)

        self.help_button = tk.Button(self.root, text='Help', padx=20, pady=5, fg='white', bg=background_colour, command=self.help_clicked)
        self.help_button.place(x=27,y=660)

        # Change colour buttons
        self.colour1 = tk.Button(self.root, padx=20, pady=5, bg='black', command=lambda : self.set_colours(bg='black', cursor='white'))
        self.colour1.place(x=(app_width/2 + 150 - 28), y=660)

        self.colour2 = tk.Button(self.root, padx=20, pady=5, bg='#263D42', command=lambda : self.set_colours(bg='#263D42', cursor='white'))
        self.colour2.place(x=(app_width/2 + 200 - 28), y=660)

        self.colour3 = tk.Button(self.root, padx=20, pady=5, bg='#063970', command=lambda : self.set_colours(bg='#063970', cursor='white'))
        self.colour3.place(x=(app_width/2 + 250 - 28), y=660)

        self.colour4 = tk.Button(self.root, padx=20, pady=5, bg='#2596be', command=lambda : self.set_colours(bg='#2596be', cursor='white'))
        self.colour4.place(x=(app_width/2 + 300 - 28), y=660)

        # Loop to run continously (runs application)
        self.root.mainloop()
    
    def sort_references(self, references):
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

    def help_clicked(self):
        '''
        Opens up the GitHub README.md for this application
        '''
        webbrowser.open('https://github.com/Ethal-Askander/Reference-Sorter/blob/main/README.md', new=1)

    def sort_clicked(self):
        '''
        Gets current text, sorts it and replaced the current text with the sorted text.
        '''
        # Get the references
        references = self.text_box.get('1.0', tk.END).split('\n')

        # Sort the references
        references = self.sort_references(references)

        self.text_box.replace('1.0', tk.END, references)

    def set_colours(self, fg='white', bg='#263D42', cursor='white'):
        '''
        @param colour

        Changes the background colour of all items on the window to the given colour
        '''
        self.background_colour = bg
        self.canvas.configure(bg=bg)
        self.text_box.configure(fg=fg, bg=bg, insertbackground=cursor)
        self.sort_button.configure(fg=fg, bg=bg,)
        self.help_button.configure(fg=fg, bg=bg,)

# Run Application
Sorter()