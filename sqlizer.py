#test2
from tkinter import *
import pyperclip

class Sqlizer:

    def __init__(self, root_widget):
        self.root_widget = root_widget

    def launch_sqlizer(self):
        global sqlizer_app
        try:
            if sqlizer_app.state() == "normal": sqlizer_app.focus()
        except:
            sqlizer_app = Toplevel(master = self.root_widget)
            sqlizer_app.resizable(width = 0, height = 0)
            sqlizer_app.title("s q l i z e r")
            sqlizer_app.transient(master = self.root_widget)


            left_separator = Frame(master = sqlizer_app, width=50)
            left_separator.grid(row=0, column=1)

            box_label = Label(master = sqlizer_app, text="Enter a list:")
            box_label.grid(row=1, column=2, pady=10)

            text_box = Text(master = sqlizer_app, width=30, height=10, relief=SUNKEN)
            text_box.grid(row=2, column=2, columnspan=3)

            format_copy_button = Button(master = sqlizer_app, text = "Format + Copy")
            format_copy_button.config(command = lambda: [self.formatcopy(text_box.get(1.0, END), FormatSelection.get()), self.changetext(text_box)])
            format_copy_button.grid(row=3, column=3, pady=5)

            clear_button = Button(master = sqlizer_app, text = "Clear", command = lambda: text_box.delete(1.0, END))
            clear_button.grid(row=4, column=3, pady=5)

            quit_button = Button(master = sqlizer_app, text = "Quit", command = sqlizer_app.destroy)
            quit_button.grid(row=5, column=3, pady=5)
            
            # Radio Button Setup. SSMS = option 1, SQL Browser = option 2
            FormatSelection = IntVar()
            FormatSelection.set(1)
            radio_ssms = Radiobutton(master = sqlizer_app, text = "SQL Server", variable = FormatSelection, value = 1, highlightthickness = 0)
            radio_ssms.grid(row=6, column=2, pady=20)
            radio_sqlbrowser = Radiobutton(master = sqlizer_app, text = "SQL Browser", variable = FormatSelection, value = 2, highlightthickness = 0)
            radio_sqlbrowser.grid(row=6, column=4, pady=20)
            right_separator = Frame(master = sqlizer_app, width=50).grid(row=0, column=5)

            #Color configuration for elements above:
            
            #Application Background
            sqlizer_app.config(bg="#00ccff")
            #Application Button Background
            format_copy_button.config(bg="#ff8080")
            clear_button.config(bg="#ff8080")
            quit_button.config(bg="#ff8080")
            radio_ssms.config(bg="#00ccff")
            radio_sqlbrowser.config(bg="#00ccff")
            #Label Background
            box_label.config(bg="#00ccff")

    # Summary: Take a list, formats using 1 of 2 options and copies to clipboard.
    # Option 1 = SSMS [,,,] & Option 2 = SQL Browser [('','','')]
    def formatcopy(self, inputlist: 'str', formatoption: 'int') -> str:

        listified = inputlist.split(sep = '\n')
        list_nospace = [i for i in listified if i != '']

        if formatoption == 1:
            listresult1 = ("('" + "','".join(list_nospace) + "')")
            pyperclip.copy(listresult1)
        if formatoption == 2:
            listresult2 = (",".join(list_nospace))
            pyperclip.copy(listresult2)
        return

    def changetext(self, textbox):
        textbox.delete(1.0, END)
        textbox.insert(1.0, pyperclip.paste())
        return