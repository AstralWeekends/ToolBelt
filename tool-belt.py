from tkinter import *
from PIL import Image,ImageTk
import pyperclip
from appmethods import *
from sqlizer import launch_sqlizer

root = Tk()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
root.title("ToolBelt - version 0.1")

#Application Button Icons
sqlizer_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/sqlizer.png")
file_friend_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/filefriend.png")
super_duper_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/superduper.png")
regex_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/regexlib.png")

# Application Buttons
sqlizer_button = Button(master = root, image = sqlizer_icon, command = lambda: launch_sqlizer(root)).grid(row=0, column=1, padx=3, pady=1)
file_friend_button = Button(master = root, image = file_friend_icon).grid(row=0, column=2, padx=3, pady=1)
super_duper_button = Button(master = root, image = super_duper_icon).grid(row=1, column=1, padx=3, pady=1)
regex_button = Button(master = root, image = regex_icon).grid(row=1, column=2, padx=3, pady=1)

root.mainloop()