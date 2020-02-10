from tkinter import *
from PIL import Image,ImageTk
from appmethods import *

root = Tk()
root.title("ToolBelt - version 0.1")

#Sqlizer App
def launch_sqlizer():
    global sqlizer_app
    try:
        if sqlizer_app.state() == "normal": sqlizer_app.focus()
    except:
        sqlizer_app = Toplevel(master = root)
        sqlizer_app.title("s q l i z e r")

        left_separator = Frame(master = sqlizer_app, width=50)
        left_separator.grid(row=0, column=1)

        box_label = Label(master = sqlizer_app, text="Enter a list:")
        box_label.grid(row=1, column=2, pady=10)

        text_box = Text(master = sqlizer_app, width=30, height=10, relief=SUNKEN)
        text_box.grid(row=2, column=2, columnspan=3)

        format_copy_button = Button(master = sqlizer_app, text = "Format + Copy", command = lambda: formatcopy(text_box.get(1.0, END), FormatSelection.get()))
        format_copy_button.grid(row=3, column=3, pady=5)

        clear_button = Button(master = sqlizer_app, text = "Clear", command = lambda: text_box.delete(1.0, END))
        clear_button.grid(row=4, column=3, pady=5)

        quit_button = Button(master = sqlizer_app, text = "Quit", command = sqlizer_app.destroy)
        quit_button.grid(row=5, column=3, pady=5)
        
        # Radio Button Setup. SSMS = option 1, SQL Browser = option 2
        FormatSelection = IntVar()
        FormatSelection.set(1)
        radio_ssms = Radiobutton(master = sqlizer_app, text = "SQL Server", variable = FormatSelection, value = 1)
        radio_ssms.grid(row=6, column=2, pady=20)
        radio_sqlbrowser = Radiobutton(master = sqlizer_app, text = "SQL Browser", variable = FormatSelection, value = 2)
        radio_sqlbrowser.grid(row=6, column=4, pady=20)
        right_separator = Frame(master = sqlizer_app, width=50).grid(row=0, column=5)

#Application Button Icons
sqlizer_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/sqlizer.png")
file_friend_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/filefriend.png")
super_duper_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/superduper.png")
regex_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/regexlib.png")

# Application Buttons
sqlizer_button = Button(master = root, image = sqlizer_icon, command = launch_sqlizer).grid(row=0, column=1, padx=3, pady=1)
file_friend_button = Button(master = root, image = file_friend_icon).grid(row=0, column=2, padx=3, pady=1)
super_duper_button = Button(master = root, image = super_duper_icon).grid(row=0, column=3, padx=3, pady=1)
regex_button = Button(master = root, image = regex_icon).grid(row=0, column=4, padx=3, pady=1)

root.mainloop()