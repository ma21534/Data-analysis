#Description: Variable to represent the base hours and overtime multiplier
#Date:10/15/2020
#Name: Bir

#Define two named constant
BASE_HOURS = 40    #BASE HOURS PER WEEK
OT_MULTIPLIER = 1.5  #overtime multiplier

#Get the hours worked and hourley pay rate
hours = float(input('Enter no. of hours worked:'))
pay_rate = float(input('Enter the hourly pay rate:'))

#Calculate and display gross pay
if hours > BASE_HOURS:
    #Calculate gross pay with OT
    #First, get the no. of OT hours worked
    overtime_hours = hours - BASE_HOURS

    #calculate amount of OT
    OT_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    #Calculate the gross pay
    gross_pay = BASE_HOURS * pay_rate + OT_pay
else:
    #Calculate the gross pay as usual without overtime
    gross_pay = hours*pay_rate
#Display the gross pay
print('The gross pay is:', format(gross_pay, ',.2f'), sep = '')


