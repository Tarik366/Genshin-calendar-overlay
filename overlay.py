import tkinter as tk
import datetime
import locale
import serverTime
from pytz import timezone
from insertText import insert_with_fallback

locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')

root = tk.Tk()

root.option_add("*Font", "Genshin-Impact 16")

root.title("Always On Top")

now = datetime.datetime.now(timezone(serverTime.ServerTimezones["Asia"]))
date = now.strftime("%x %a").encode(locale.getlocale()[1], "backslashreplace").decode()

# Make the window transparent (optional)
root.attributes('-alpha', 0.8)

# Set the window to always be on top
root.attributes('-topmost', True)

root.overrideredirect(1)

print(date)
label = tk.Label(root, text=date, font=("Noto Sans", 16, "bold"))
label.pack(pady=10)

listbox = tk.Listbox(height = 10, 
                  width = 15, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Default_SC-85W",
                  fg = "yellow")

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

listbox.pack()

root.mainloop()