import tkinter as tk
import serverTime
import floatingWindow

root = floatingWindow.App()

root.title("Genshin Todo Calendar")

@root.floater.add_widget
def date(parent):
    return tk.Label(parent, text=serverTime.date, font=("Noto Sans", 16, "bold"), fg="white", bg="black")

@root.floater.add_widget
def overlay(parent):
    listbox = tk.Listbox(parent, height = 10, 
                  width = 15, 
                  bg = "black",
                  activestyle = 'dotbox', 
                  font = "Default_SC-85W",
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