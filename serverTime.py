import datetime
import locale
from pytz import timezone

ServerTimezones = {
    "America": "Etc/GMT+5",
    "Europe": "Etc/GMT+1",
    "Asia": "Etc/GMT-8"
}

locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')

now = datetime.datetime.now(timezone(ServerTimezones["Asia"]))
date = now.strftime("%x %a").encode(locale.getlocale()[1], "backslashreplace").decode()
