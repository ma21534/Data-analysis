#Description: Test three scores and display their average, congratulate if average> high score 95.
#Date:10/15/2020
#Name: Bir
#Define constant variable. HIGH SCORE named constant holds value that is considered high score
HIGH_SCORE = 95

#INput 3 test score
test1 = int(input('Enter the score for test 1:'))
test2 = int(input('Enter the score for test 2:'))
test3 = int(input('Enter the score for test 3:'))

#Calculate average score
average = (test1 + test2 + test3)/3

#Print average score 
print('The average score is:', average)

#Congratulate if average is > high score.
if average >= HIGH_SCORE:   #control/decision structure
    print('Congratulations!')
    print('That is a great average')

