from tkinter import *

class SuperDuper:

    def __init__(self, root_widget):
        self.root_widget = root_widget
    
    def launch_superduper(self):
        global superduper_app
        try:
            if superduper_app.state() == "normal": superduper_app.focus()
        except:
            superduper_app = Toplevel(master = self.root_widget)
            superduper_app.resizable(width = 0, height = 0)
            superduper_app.title("s u p e r :: d u p e r !")
            superduper_app.transient(master = self.root_widget)

            left_separator = Frame(master = superduper_app, width=50)
            left_separator.grid(row=0, column=1)

            box_label = Label(master = superduper_app, text="Enter a list:")
            box_label.grid(row=1, column=2, pady=10)

            text_box = Text(master = superduper_app, width=30, height=10, relief=SUNKEN)
            text_box.grid(row=2, column=2, columnspan=3)