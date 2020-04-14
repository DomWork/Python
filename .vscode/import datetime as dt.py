import datetime as dt
today = dt.date.today()
last_of_teens = dt.date(2020,2,21)

print()
print("Today")
print(today)
print()
print ("The 21st day of February 2020")
print(last_of_teens)                        #year, month, day
print(last_of_teens.day)                    #day
print(last_of_teens.month)                  #month
print(last_of_teens.year)                   #year
print(f"{last_of_teens:%A, %d %B, %Y}")     #day of week, comma, date, month name, comma, full year
print(f"{last_of_teens:%d %b %y}")          #date, short month name, short year
print(f"{last_of_teens:%d %m %y}")          #date, month number, short year
print()