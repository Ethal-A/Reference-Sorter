import tkinter as tk
import webbrowser
import re

class Sorter:
    def __init__(self, app_width=700, app_height=700, background_colour='#263D42'):
        # Set parameters
        self.app_width = app_width
        self.app_height = app_height
        self.background_colour = background_colour

        # Setup window
        self.root = tk.Tk()
        self.root.minsize(app_width, app_height)
        self.root.resizable(False, False)
        
        # Set title and icon
        self.root.title('Reference Sorter')
        img = tk.PhotoImage(file='images/icon.png')
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        # Defining input text box
        self.canvas = tk.Canvas(self.root, height=app_height, width=app_width, bg=background_colour)
        self.canvas.pack(pady=10)
        self.text_box = tk.Text(self.canvas, height=40, fg='white', bg=background_colour)
        self.text_box.pack()

        # Defining buttons
        self.sort_button = tk.Button(self.root, text='Sort', padx=50, pady=5, fg='white', bg=background_colour, command=self.sort_clicked)
        self.sort_button.place(x=(app_width / 2 - 50), y=660)

        self.help_button = tk.Button(self.root, text='Help', padx=20, pady=5, fg='white', bg=background_colour, command=self.help_clicked)
        self.help_button.place(x=27,y=660)

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

# Run Application
Sorter()