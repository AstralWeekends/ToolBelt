from tkinter import *
from PIL import Image,ImageTk
from sqlizer import *
from FileFriend import *

root = Tk()                         
root.resizable(width = 0, height = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
root.title("t  o  o  l  b  e  l  t  : :  v  e  r  s  i  o  n  0.2")

sqlizer_app = Sqlizer(root)
filefriend_app = FileFriend(root)

#Application Button Icons
sqlizer_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/sqlizer.png")
file_friend_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/filefriend.png")
super_duper_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/superduper.png")
regex_icon = PhotoImage(file = "/srv/git/repos/ToolBelt/icons/regexlib.png")

# Application Buttons
sqlizer_button = Button(master = root, image = sqlizer_icon, command = lambda: sqlizer_app.launch_sqlizer()).grid(row=0, column=1, padx=3, pady=1)
file_friend_button = Button(master = root, image = file_friend_icon, command = lambda: filefriend_app.launch_filefriend()).grid(row=0, column=2, padx=3, pady=1)
super_duper_button = Button(master = root, image = super_duper_icon).grid(row=1, column=1, padx=3, pady=1)
regex_button = Button(master = root, image = regex_icon).grid(row=1, column=2, padx=3, pady=1)

root.mainloop()