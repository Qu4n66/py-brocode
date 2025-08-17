
import datetime


date = datetime.date(1999,2,28)
today = datetime.date.today()
time = datetime.time(9,40,0)
now = datetime.datetime.today()
now2 = now.strftime("%Y-%d-%B")

target_datetime = datetime.datetime(2010,1,2,12,30,1)
current_datetime = datetime.datetime.now()
if target_datetime  < current_datetime:
    print('Target date has passed')
else:
    print('Target day has not passed')