import calendar
import datetime

actual_year = datetime.date.today().year
actual_month = datetime.date.today().month

events_dict = {}


def show_month(year: int, month: int):
    print(calendar.month(year, month))


def add_event(year, month, day, event):
    try:
        date = datetime.datetime(year, month, day)
    except:
        print("introduce una fecha válida bro")
    if not date in events_dict:
        events_dict[date] = []
    events_dict[date].append(event)


show_month(actual_year, actual_month)
