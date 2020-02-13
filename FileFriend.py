from tkinter import *

class FileFriend:
    def __init__(self, root_widget):
        self.root_widget = root_widget
    
    def launch_filefriend(self):
        global filefriend_app
        try:
            if filefriend_app.state() == "normal": filefriend_app.focus()
        except:
            filefriend_app = 