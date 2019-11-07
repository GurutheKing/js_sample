# pi = 3.14
# print(pi, 'is the value of pi')
# first_num =int(input("Enter the first number: "))
# second_num =int(input("Enter the second number: "))
# print("The total of bum1 and num2 : ",first_num+second_num)
# print("The multi of bum1 and num2 : ", first_num*second_num)
from datetime import datetime, timedelta
# the current date si stored in teh variable current_date
today = datetime.now()
one_day = timedelta(days=1)
yesterday = today- one_day
# prints the current date
print("The current date is: ",today.day)
print("Yesterday's date =: ", yesterday.day)
#last week
this_week = datetime.now()
one_week =timedelta(weeks=1)
last_week = this_week-one_week
# prints the current week
print("The current date is: ",this_week.month)
print("last week's date =: ", last_week.month)
#num_days =31
#print("the total number of days in october is ", num_days)
#print("THE TOTAL NUMBER OF DAYS IN DECEMBER IS " + str(num_days))