import tkinter as tk
from tkinter import ttk
import serverTime
import floatingWindow

root = floatingWindow.App()

root.title("Genshin Todo Calendar")
root.geometry("500x500+200+400")
# Focus to config window when app started
root.lift()

ComboBoxForm: dict[str, list] = {
    "Server": list(serverTime.ServerTimezones.keys()),
    "Language": ["English", "Turkish", "Japanese"]
}

i=0
for lab, boxValues in ComboBoxForm.items():
    i+=1
    tk.Label(root, text=lab).grid(row=i, column=0)
    ttk.Combobox(root, width=27, values=boxValues).grid(row=i, column=1)

@root.floater.add_widget
def date(parent):
    return tk.Label(parent, text=serverTime.date, fg="white", bg="black")

@root.floater.add_widget
def overlay(parent):
    listbox = tk.Listbox(parent, height = 10, 
                  width = 15, 
                  bg = "black",
                  activestyle = 'dotbox', 
                  fg = "white")

    Items = [
        "Furina kitap",
        "Esco kitap",
        "Skirk kitap",
        "Raiden kitap",
        "土",
        "balığk",
    ]
    i=0
    for item in Items:
        i+=1
        listbox.insert(i, item)

    return listbox

root.mainloop()