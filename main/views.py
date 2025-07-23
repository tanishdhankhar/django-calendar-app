from django.shortcuts import render
import calendar
from datetime import datetime

def calendar_view(request):
    show_calendar = False
    html_calendar = ""
    month = datetime.now().month
    year = datetime.now().year

    if request.method == "POST":
        show_calendar = True
        cal = calendar.HTMLCalendar(calendar.SUNDAY)
        html_calendar = cal.formatmonth(year, month)

    return render(request, "main/calendar.html", {
        "show_calendar": show_calendar,
        "calendar": html_calendar,
        "month": calendar.month_name[month],
        "year": year
    })
