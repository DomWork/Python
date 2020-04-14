import datetime as dt
new_years_day = dt.date(2020,1,1)
my_birthday = dt.date(2020,9,7)
days_between = my_birthday - new_years_day #this is a timedelta object from the timedate class
print()
print("Your 2020 birthday, ", my_birthday, "is", days_between.days, "after New Year", new_years_day)
#duration = dt.timedelta(days=120)
print()
print(days_between.days, " days after your birthday is", my_birthday + days_between)
#print(type(days_between))
today = dt.date.today()
days_to_birthday = my_birthday - today
print()
print("There are ", days_to_birthday.days, "until your birthday!")
print()
