#CI280 Lab02 – List daily sales of one week 
# Bir Mahato
# Date:10/8/2020

#Write a program that asks the user to enter a store’s sales for each day of the week
#Variables
total_sales = 0.0
Days = 7
#Initialize lists
daily_sales = [0.0]* Days
days_of_week = ['Sunday', 'Monday', 'Tuesday',  'Wednesday', 'Thursday', 'Friday','Saturday']


for i in range(7):
    daily_sales[i] = float(input('Enter the sales for' + days_of_week[i] + ':' ))





#Display weekly sales
print('Weekly Sales')
print('------------')


for index in range(7):
    print(days_of_week [index], ':$', format(daily_sales[index], ',.2f'))



#Calculation

for number in daily_sales:
    total_sales += number
Average_sales = sum(daily_sales)/len(daily_sales)    
max_sales = max(daily_sales)
max_index = daily_sales.index(max_sales)

min_sales = min(daily_sales)
min_index = daily_sales.index(min_sales)

#Display weekly sales Summary
print()
print('Weekly sales Summary')
print('------------')
print('Total sales', format(total_sales, ',.2f'))
print('Average sales: $', format(Average_sales, ',.2f'))
print('The Highest sales is in', days_of_week[max_index], format(max_sales, ',.2f'))
print('The lowest sales is in', days_of_week[min_index], format(min_sales, ',.2f'))


