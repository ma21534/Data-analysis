#!/usr/bin/env python
# coding: utf-8

# # Homework 1 (20 pts)
# 
# ## Due Date: 10/13/2020 ( Tuesday 11:59PM)
# 
# Save Notebook file as :HW1_21534_Bir.ipynb
# 
# Email to: jzhang@eastwest.edu
# 
# Subject: CI280 Homework 1 

# Ch02 Input, Output
# 
# Problem 1: Computer present value ( Input , compute and output: 2 points)
# 
# present_value = future_value / ( 1.0 + rate) ** years

# In[1]:


# Problem 1: (2 pts)

# Input (1 point)
future_value = 0
p_value = 0
years = 0

future_value = float(input("Enter future value:"))
interest_rate = float(input("Enter interest rate:"))
years = int(input('Enter no. of year:'))
# Compute (1 point)
p_value =  future_value / ( 1.0 + interest_rate) ** years

# Output 
print('Present value:', format(p_value, '.2f'))


# Ch03 Decision -- if ... else ...
# 
# Problem 2: Software Sales (Page 154) ( 5 pts)
# A softare company sells a package that retais for $99. Quantity discounts are given according to following table:
#     Quantity     Discount
#     10 - 19       10%
#     20 - 49       20%
#     50 - 99       30%
#     100 or more   40%
#     
# Write a program that ask the uer to enter number of packages, and display the dicount rate, discount and total pay.
# 
#     Declare constant variables -- 1 pt
#     Input                      -- 1 pt
#     Compute discount rate      -- 2 pts
#     Compute other              -- 1 pt
#     -----------------------------------
#     Total points                  5 pts

# In[2]:


# Problem 2: (5 pts)

# Get input
package = int(input("Enter number of package purchased: "))
mp = 99
if package < 10:
    discount = 0 
elif package < 20:
    discount = 10 
elif package < 50:
    discount = 20  

elif package < 100:
    discount = 30 
else:
    discount = 40 

# Compute
original_price = mp*package
discountamount = (discount/100)*original_price
Total_cost = original_price - discountamount

print('===Summary=========')
print('Number of package purchased:', package)
print('Discount rate:', format(discount, '.1f'), "%")
print('Original price', "$", format(original_price, '.1f'))
print('Your Discount Saving:', "$", format(discountamount, '.1f'))
print('Cost after Discount:' , "$", format(Total_cost, '.1f'))




# Ch04 Loop
# 
# Problem 3: Tuition Increase ( 3 pts)
# At one college, the tuition for a full-time student is $8000 per semsestr. 
# The college will incease the tuituin by 3% per year for next five years.
# Write a program to display the projected tuition amount for the next five years
# 
#     Declare constant variables 
#     loop and Compute           -- 2 pts
#     Display format             -- 1 pts
#     -----------------------------------
#     Total points                  3 pts

# In[3]:


# Problem 3: (3 pts)

tuition = 8000
INCREASE_RATE = 0.03
print('Projected Tuition for the next five years')
print('Year \t\t Tuition')
print('--------------------------')
for year in range(1, 6):
     tuition += (3/100) * tuition
     print(str(year) + "\t\t $" + format(tuition, ".2f"))
    


      







# Ch05 Function
# 
# Problem 4: ( 4 pts)
# Write a function to generate random numbers, and keep a count how many are even numbers, and how many are odd numbers,
# and return two counts
# 
# Generate 100 random numbers to show the ratio.
# Generate 1000 random numbers to show the ratio.
# Generate 10000 random numbers to show the ratio.
# 
# Hints: 
# Use random.randint(0,x) to generate a random number
# Use num%2 == 0 to check is it is even number
# 
#     Define function: 3 pts
#     Invoke function: 1 pts
#     Total: 4 pts

# In[4]:


# Problem 4 (6 pts)
import random

# Define the function here
def countNo(x):
    even = 0
    odd = 0
    for i in range(1,x+1):
        num = random.randint(0,100)
        if num%2 == 0:
            even=even+1
        else:
            odd=odd+1
    return even,odd

#ratio for 100 random numbers
x=100
even,odd=countNo(x)
print(float(even/odd))

#ratio for 1000 random numbers
x=1000
even,odd=countNo(x)
print(float(even/odd))

#ratio for 10000 random numbers
x=10000
even,odd=countNo(x)
print(float(even/odd))     
        






