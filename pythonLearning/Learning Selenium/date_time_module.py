import datetime

today_dateTime = datetime.datetime.today()
print(today_dateTime)
today_date = datetime.datetime.today().date()
print(today_date)
current_time = datetime.datetime.today().time()
print(current_time)

new_formate = today_dateTime.strftime("%Y/%m/%d %H:%M:%S:%f")
print(new_formate)
