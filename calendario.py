import calendar
import datetime

actual_year = datetime.date.today().year
actual_month = datetime.date.today().month


def show_month(year: int, month: int):
    print(calendar.month(year, month))


show_month(actual_year, actual_month)
