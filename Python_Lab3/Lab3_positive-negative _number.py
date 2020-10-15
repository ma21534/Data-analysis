#Description: Determine positive or negative number
#Date:10/15/2020
#Name: Bir

#Define constant variable
BASE_NO = 0

#Ask user to enter the number
nu = int(input('Enter a number:'))

#Determine positive or negative number by if and else condition
if nu > BASE_NO:
         print(nu, 'is a Positive number.')
elif nu == 0:
    print(nu, ' is a Zero')
else:
        print(nu, 'is a Negative number.')
    
    
