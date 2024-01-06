import random
import string
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

class Password:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x400")
        self.root.title("Password Generator App")
        self.root.configure(bg='beige')
        self.root.resizable(False, False)

        select_value = {"1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6",
                         "7" : "7", "8" : "8", "9" : "9", "10" : "10", "11" : "11", "12" : "12",
                         "13" : "13", "14" : "14", "15" : "15", "16" : "16", "17" : "17", "18" : "18",
                         "19" : "19", "20" : "20", "21" : "21", "22" : "22", "23" : "23", "24" : "24",
                         "25" : "25", "26" : "26", "27" : "27", "28" : "28", "29" : "29", "30" : "30",}

        # Function to make hover effect
        def on_enter(e):
            create_button['bg']='orange'
            create_button['fg']='black'

        def on_leave(e):
            create_button['bg']='green'
            create_button['fg']='white'

        title = Label(self.root, text="Generate Your Strong Password Here..!!", bg='beige', fg='black', font=('Arial', 15))
        title.pack(fill=X, pady=30)

        length = Label(self.root, text="Select the length of your Password: ", bg='beige', font=('Arial', 11))
        length.place(x="15", y="80")

        solid = IntVar()
        selector = Combobox(self.root, textvariable=solid, state='readonly')
        selector['values'] = [l for l in select_value.keys()]
        selector.current(7)
        selector.place(x="250", y="80")


        def generate_password():
            try:
                password_length = solid.get()
                small_letter = string.ascii_lowercase
                capital_letter = string.ascii_uppercase
                digits = string.digits
                special_character = string.punctuation
                all_list = []
                all_list.extend(list(small_letter))
                all_list.extend(list(capital_letter))
                all_list.extend(list(digits))
                all_list.extend(list(special_character))
                random.shuffle(all_list)
                password.set("".join(all_list[0:password_length]))
            except:
                messagebox.askretrycancel("A problem has been occured.", "Please Try Again..!!")
        # Creating buttons...
        create_button = Button(self.root, text="Generate Password", bg='green', fg='white', font=('Arial', 15), cursor='hand2', command=generate_password)
        create_button.bind("<Enter>", on_enter)
        create_button.bind("<Leave>", on_leave)
        create_button.pack(anchor='center', pady='50')

        res_label = Label(self.root, text="Generated Password :) ", bg='beige', font=('Arial', 13))
        res_label.pack()

        password=StringVar()
        res_entry = Entry(self.root, textvariable=password, font=('Arial', 15), state='readonly', fg='green')
        res_entry.pack()



    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    p = Password()
    p.run()
