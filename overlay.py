import tkinter as tk
from tkinter import ttk
import serverTime, floatingWindow, Config

root = floatingWindow.App()

ServerTime = tk.StringVar(value=serverTime.getServerTime(Config.default_settings), name="ServerTime")

root.title("Genshin Todo Calendar")
root.geometry("500x500+200+400")
# Focus to config window when app started
root.lift()

ComboBoxForm: dict[str, list] = {
    "Server": list(serverTime.ServerTimezones.keys()),
    "Language": ["English", "Turkish", "Japanese"]
}

settings = {}
combos = {}
i=0
  
def ComboboxSelected(e):
    ServerTime.set(serverTime.getServerTime(settings))

for lab, boxValues in ComboBoxForm.items():
    i+=1
    label=tk.Label(root, text=lab).grid(row=i, column=0)
    settings[lab] = tk.StringVar(name=lab)
    comb=ttk.Combobox(root, width=27, values=boxValues, textvariable=settings[lab])
    combos[lab] = comb
    comb.bind("<<ComboboxSelected>>", ComboboxSelected) 
    comb.grid(row=i, column=1)

for key, value in Config.default_settings.items():
    settings[key].set(value)
    combos[key].set(value)

@root.floater.add_widget
def date(parent):
    return tk.Label(parent, textvariable=ServerTime, fg="white", bg="black")

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