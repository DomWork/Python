import datetime as dt
now_time = dt.datetime.now()
last_of_teens = dt.date(2020,2,21)

print()
print("What time is it?")
print(now_time)
print()
print ("Friendly now time")
print(f"{now_time:%I:%M %p}")                        #hour, minute, AM/PM
print(f"{now_time:%I:%M%p on %A, %d %B}")     #time AM/PM, day of week, comma, date, month name
print(f"{now_time: %H:%M}")          #24 hour clock hours:minutes
print(f"{now_time:%d/%m/%y, %H:%M}")          #date, month number, short year, 24 hour time
print(f"{now_time:%d/%m/%Y, %H:%M}")          #date, month number, long year, 24 hour time
print()