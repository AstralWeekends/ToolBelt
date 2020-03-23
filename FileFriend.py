from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import difflib
import webbrowser


class FileFriend:

    def __init__(self, root_widget):
        self.root_widget = root_widget

    def launch_filefriend(self):
        global filefriend_app
        try:
            if filefriend_app.state() == "normal": filefriend_app.focus()
        except:
            filefriend_app = Toplevel(master = self.root_widget)
            filefriend_app.resizable(width = 0, height = 0)
            filefriend_app.title("f i l e f r i e n d")

            left_separator = Frame(master = filefriend_app, width = 50)
            left_separator.grid(row = 0, column = 1)

            file1_button = Button(master = filefriend_app, text = "File 1")
            file1_button.config(command = lambda: self.openfile(filepath1))
            file1_button.grid(row = 1, column = 2)

            file2_button = Button(master = filefriend_app, text = "File 2")
            file2_button.config(command = lambda: self.openfile(filepath2))
            file2_button.grid(row = 2, column = 2)

            filepath1 = StringVar()
            file1_entry = Entry(master = filefriend_app, width = 40)
            file1_entry.config(textvariable = filepath1)
            file1_entry.grid(row = 1, column = 3, padx = 5)

            filepath2 = StringVar()
            file2_entry = Entry(master = filefriend_app, width = 40)
            file2_entry.config(textvariable = filepath2)
            file2_entry.grid(row = 2, column = 3, padx = 5)

            instr_text = Label(master = filefriend_app, text = "Select 2 files to compare:")
            instr_text.grid(row = 0, column = 3)

            compare_button = Button(master = filefriend_app, text = "Compare")
            compare_button.config(command = lambda: self.comparefiles(filepath1, filepath2))
            compare_button.grid(row = 3, column = 3, pady = 5)

            right_separator = Frame(master = filefriend_app, width = 50)
            right_separator.grid(row = 0, column = 4)

    def openfile(self, filepath):
        
        ftypes = [
            ('Text Files', '*.txt *.xml *.csv *.rpt *.html')
        ]
        self.filename = filedialog.askopenfilename(initialdir = "/home/alecslyter/Documents/Python/test_input",
                                                   title = "Select a File", filetypes = ftypes)
        try:
            if self.filename != '':
                filepath.set(self.filename)
                return self.filename
        except:
            messagebox.showerror(title = "Error", message = "Could not open file.")

    def comparefiles(self, file1, file2):
        if file1.get() == '' or file2.get() == '':
            messagebox.showerror(title = "Error", message = "Please enter a file in both boxes.")
        else:
            with open(file1.get()) as f1:
                file1_content = f1.readlines()
            with open(file2.get()) as f2:
                file2_content = f2.readlines()

            self.save_file = filedialog.asksaveasfile(mode="w", title = "Save As...",
                                                      filetypes = [('HTML', '*.html')],
                                                      defaultextension = ".html")

            while hasattr(self.save_file, 'name'):
                diff_file = difflib.HtmlDiff().make_file(file1_content, file2_content)
                with open(self.save_file.name, 'w') as output:
                    output.write(diff_file)
                    break