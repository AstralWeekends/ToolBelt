from tkinter import *
import pyperclip

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
            box_label.grid(row=1, column=3, sticky = S+W, pady = 5)

            copy_button_left = Button(master = superduper_app, text = 'Copy', wraplength = 1, height=7)
            copy_button_left.grid(row=2, column=2, rowspan=2,sticky = N)
            copy_button_left.config(command = lambda: pyperclip.copy(text_box_left.get(1.0, END)))

            clear_button_left = Button(master = superduper_app, text = 'Clear', wraplength = 1, height=7)
            clear_button_left.grid(row=3, column=2,sticky = S)
            clear_button_left.config(command = lambda: text_box_left.delete(1.0, END))

            text_box_left = Text(master = superduper_app, width=30, height=15, relief=SUNKEN)
            text_box_left.grid(row=2, column=3, rowspan=2, sticky = N)

            mid_separator = Label(master = superduper_app, text="----->")
            mid_separator.grid(row=2, column=4, rowspan=2, padx=10)

            text_box_right = Text(master = superduper_app, width=30, height=15, relief=SUNKEN)
            text_box_right.grid(row=2, column=5, rowspan=2, sticky = N)

            copy_button_right = Button(master = superduper_app, text = 'Copy', wraplength = 1, height=15)
            copy_button_right.grid(row=2, column=6, rowspan = 2)
            copy_button_right.config(command = lambda: pyperclip.copy(text_box_right.get(1.0, END)))

            command_label = Label(master = superduper_app, text = "Select Command:")
            command_label.grid(row=4, column = 3, sticky = E)

            command = StringVar(superduper_app)
            command.set("Remove Dups")
            command_dropdown = OptionMenu(superduper_app, command, "Remove Dups", "Extract Dups", "Count Dups by Value")
            command_dropdown.grid(row=4, column=4, pady=5, sticky = W, columnspan=2)

            execute_button = Button(master = superduper_app, text = "Execute")
            execute_button.grid(row = 5, column = 4, pady=5, sticky = N+S+E+W)
            execute_button.config(command = lambda: command_router(command.get()))

            quit_button = Button(master = superduper_app, text = "Quit", command = superduper_app.destroy)
            quit_button.grid(row = 6, column = 4, pady=5, sticky = N+S+E+W)

            right_separator = Frame(master = superduper_app, width=50)
            right_separator.grid(row=0, column=7)

            #Take selected command and route to appropriate function aftering converting to a list.
            def command_router(command):

                data_in = text_box_left.get(1.0, END)
                list_in = data_in.split(sep = '\n')
                text_box_right.delete(1.0, END)

                if command == "Remove Dups":
                    result = remove_dups(list_in)
                    return(result)
                
                if command == "Extract Dups":
                    result = extract_dups(list_in)
                    return(result)

                if command == "Count Dups by Value":
                    result = count_dups_by_value(list_in)
                    return(result)

            
            def remove_dups(list_in):
                #remove dups from list
                listified_no_dups = list(dict.fromkeys(list_in))
                #return list as a string to text_box_right
                return(text_box_right.insert(1.0, '\n'.join(listified_no_dups)))

            def extract_dups(list_in):
                list_out = []
                for item in list_in:
                    if list_in.count(item) > 1:
                        if item not in list_out:
                            list_out.append(item)
                return(text_box_right.insert(1.0, '\n'.join(list_out)))
            
            def count_dups_by_value(list_in):
                list_out = []
                counts = {item: list_in.count(item) for item in list_in if list_in.count(item) > 1 and item != ''}
                for k in counts:
                    str1 = str(k) + " - " + str(counts.get(k))
                    list_out.append(str1)
                return(text_box_right.insert(1.0, '\n'.join(list_out)))







            