import datetime, locale, Config
from pytz import timezone
import tkinter as tk

ServerTimezones = {
    "America": "Etc/GMT+5",
    "Europe": "Etc/GMT+1",
    "Asia": "Etc/GMT-8"
}

def getServerTime(serv, loc):
    print(serv)
    print(loc)
    locale.setlocale(locale.LC_TIME, f"{Config.get_locale_code(loc)}.UTF-8")
    now = datetime.datetime.now(timezone(ServerTimezones[serv]))
    return now.strftime("%x %a").encode(locale.getlocale()[1], "backslashreplace").decode()
