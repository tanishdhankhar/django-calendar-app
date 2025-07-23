from django.shortcuts import render
import calendar
from datetime import datetime

def calendar_view(request):
    import calendar
    from datetime import datetime

    # Get month and year from GET parameters, or default to current
    month = request.GET.get('month')
    year = request.GET.get('year')
    now = datetime.now()
    if month is not None and year is not None:
        try:
            month = int(month)
            year = int(year)
        except ValueError:
            month = now.month
            year = now.year
    else:
        month = now.month
        year = now.year

    show_calendar = True  # Always show calendar now
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendar = cal.formatmonth(year, month)

    # Calculate previous and next month/year
    prev_month = month - 1
    prev_year = year
    if prev_month < 1:
        prev_month = 12
        prev_year -= 1
    next_month = month + 1
    next_year = year
    if next_month > 12:
        next_month = 1
        next_year += 1

    return render(request, "main/calendar.html", {
        "show_calendar": show_calendar,
        "calendar": html_calendar,
        "month": calendar.month_name[month],
        "month_num": month,
        "year": year,
        "prev_month": prev_month,
        "prev_year": prev_year,
        "next_month": next_month,
        "next_year": next_year,
        "all_months": list(enumerate(calendar.month_name))[1:],
    })
