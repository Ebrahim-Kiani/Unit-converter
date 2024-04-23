from tkinter import *
from tkinter import messagebox

import tkinter
from convertor_module import convertor

def call_convertor():
    unit1 = str(list_box_from.get(ACTIVE))
    unit2 = str(list_box_to.get(ACTIVE))
    arguman = int(entry_from.get())
    my_object = convertor(unit1, unit2, arguman)

    answer = my_object.convertor()

    entry_to.delete(0, END)
    entry_to.insert(END, answer)


def configure_window():
    # Configure columns and rows to expand and resize dynamically
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)


window = Tk()

# Configure window for responsiveness
configure_window()

# Making Labels
label_from = Label(window, text='From')
label_to = Label(window, text='To')

label_from.grid(row=0, column=0)
label_to.grid(row=0, column=1)

# End making Labels
#################
entry_from = Entry(window, fg='blue')
entry_to = Entry(window, fg='red')

entry_from.grid(row=1, column=0)
entry_to.grid(row=1, column=1)

###################
list_box_from = Listbox(window, exportselection=False)
list_box_to = Listbox(window, exportselection=True, fg='brown')

list_box_from.grid(row=2, column=0, sticky=N+S+E+W)
list_box_to.grid(row=2, column=1, sticky=N+S+E+W)
########################

#####################

list_box_from.insert(END, "Meter")
list_box_from.insert(END, "Centimeter")
list_box_from.insert(END, "Milimeter")
list_box_from.insert(END, "Yard")
list_box_from.insert(END, "Mile")

list_box_to.insert(END, "Meter")
list_box_to.insert(END, "Centimeter")
list_box_to.insert(END, "Milimeter")
list_box_to.insert(END, "Yard")
list_box_to.insert(END, "Mile")

#######################

################

button = Button(window, text='Calculate', command=call_convertor)

button.grid(row=3, columnspan=2, sticky=E+W)


#######################
window.mainloop()