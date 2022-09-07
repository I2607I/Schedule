import datetime
def type_current_week():
    tod = datetime.date.today()
    year = tod.year
    month = tod.month
    day = tod.day
    week = datetime.date(year,month,day).isocalendar()[1]
    if week % 2 == 0:
        return 'чётная'
    else:
        return 'нечётная'
