#!/usr/bin/env python
# coding: utf-8

# In[1]:


#CI280 Lab02 – List
# Bir Mahato
# Date:10/8/2020

#1)
numbers = [50, 20, 10,80,10]
print(numbers)
print(numbers[2])

max_value = max(numbers)
max_index = numbers.index(max_value)
print('max =' , max_value)
print(max_index)

min_value = min(numbers)
min_index = numbers.index(min_value)
print('min =' , min_value)
print(min_index)

print(' length =' , len(numbers))
print(' Element =' , numbers[len(numbers)-1])

#2
names =['Steven', 'Will', 'Alicia']
print(names)

print('--')
for name in names:
    print(name)
print('--')
index = 2
while index < len(names):
    print(names[index])
    index += 1

#3
num1 = list(range(0,20,5))
print(num1)

num2 = num1 *3
print(num2)

index = 0
while index < len(num1):
    num1[index] = num1[index]*3
    index += 1
print(num1)

print(sum(num1))
print(sum(num1)/len(num1))

#4) List slicing
numbers = list(range(0,101,10))
print(numbers)

print(numbers[:5])
print(numbers[2:5])
print(numbers[7:])
print(numbers[-3:])

#5) Commonly used method
cities = ['Chicago', 'Paris']
print(cities)

city_index = cities.index('Paris')
print(city_index)

cities.insert(1, 'New York')
print(cities)

cities.reverse()
print(cities)

cities.sort()
print(cities)

cities.remove('New York')
print(cities)


# In[2]:


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



# In[ ]:




