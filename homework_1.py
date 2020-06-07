#Raad Barnett 1231583
current_date = input("Enter the current date in (mm/dd/yyyy)")
date_of_birth = input("Enter the date of birth in (mm/dd/yyyy)")

cur_month = int(current_date.split("/")[0])
cur_day = int(current_date.split("/")[1])
cur_year = int(current_date.split("/")[2])

birth_month = int(date_of_birth.split("/")[0])
birth_day = int(date_of_birth.split("/")[1])
birth_year = int(date_of_birth.split("/")[2])


print("Birthday calculator")
print("Current day")
print("Month: ",cur_month)
print("Day: ",cur_day)
print("Year: ",cur_year)
print("Birthday")
print("Month: ",birth_month)
print("Day: ",birth_day)
print("Year: ",birth_year)

print("You are {0} years old.".format(cur_year-birth_year))

# import datetime
# print(datetime.datetime.now())
