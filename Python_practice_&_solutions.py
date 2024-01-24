#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:


temperature = 50
if temperature < 50:
    print("go drink tea")
else:
    print("you buy ice cream")


# In[13]:


num = int(input("write your number here"))

if num%2 == 0:
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')


# In[7]:


num = int(input('Enter an integer: '))

if num % 2 == 0:
    print('The integer {} is even'. format(num))
else:
    print('The integer {} is odd'. format(num))
    


# In[15]:


# Write a program that asks the user to enter his or her name. The program should 
# respond with a message that says hello to the user, using his or her name.


# In[17]:


name = input('what is your name')

print(f'hi {name}, how are you?')


# In[18]:


# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.


# In[21]:


width = float(input('what is the width'))
length = float(input('what is the length'))

area= width*length

print(f'The area of the place is {area} cm square')


# In[22]:


length = float(input('Enter the length of the room in meters: '))
width =  float(input('Enter the width of the room in meters: '))

area = length * width

print('The area of the room is {} meters square.'.format(area))


# In[23]:


# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.


# In[30]:


length = float(input('Enter the length of the room in feet: '))
width = float(input('Enter the length of the room in feet: '))

area = ((length*width)/(43560))

print(f'The area of the field is {area} acres.')


# In[27]:


Square_Feet_Per_Acre = 43560

length = float(input('Enter the length of the field in feet: '))
width =  float(input('Enter the width of the field in feet: '))

area = round((length * width) / Square_Feet_Per_Acre,5)

print('The area of the field is {} acres.'. format(area))


# In[31]:


#In many jurisdictions a small deposit is added to drink containers to encourage people
#to recycle them. In one particular jurisdiction, drink containers holding one liter or
#less have a $0.10 deposit, and drink containers holding more than one liter have a
#$0.25 deposit.
#Write a program that reads the number of containers of each size from the user.
#Your program should continue by computing and displaying the refund that will be
#received for returning those containers. Format the output so that it includes a dollar
#sign and always displays exactly two decimal places.


# In[44]:


large = int(input('how many bottles is larger than one liter?'))
small = int(input('how many bottles is small than one liter?'))

deposit_small = 0.10
deposit_large = 0.25
      
refund=(deposit_small*small)+(deposit_large*large)

print(f'Your total refund is ${refund}, thank you for recycling.')


# In[45]:


less_deposit = 0.10
more_deposit = 0.25

less = float(input('How many drink containers holding one liter or less do you have? '))
more = float(input('How many drink containers holding more than one liter do you have? '))

refund = less_deposit * less + more_deposit * more

print('Your total refund will be $%.2f.' % refund)


# In[46]:


#Exercise 6:Tax and Tip 
#The program that you create for this exercise will begin by reading the cost of a meal
#ordered at a restaurant from the user. Then your program will compute the tax and
#tip for the meal. Use your local tax rate when computing the amount of tax owing.
#Compute the tip as 18 percent of the meal amount (without the tax). The output from
#your program should include the tax amount, the tip amount, and the grand total for
#the meal including both the tax and the tip. Format the output so that all of the values
#are displayed using two decimal places


# In[57]:


meal_price= float(input('write the meal price here.'))

tipped_price = meal_price*.18 + meal_price

tax = meal_price * 0.08

taxed_tipped_price = round(tipped_price + tax,3)

print(f'you owe ${taxed_tipped_price,2}, thank you for your business!')


# In[55]:


meal = float(input('What was the cost of your meal: '))

tax = 0.075 * meal
tip = 0.18 * meal 
grand_total = tax +  tip + meal

print('Tax $%.2f' % tax)
print('Tip $%.2f' % tip)
print('Grand Total $%.2f' % grand_total)

print('Tax is ${:.2f}, Tip is ${:.2f} and the Grand Total is ${:.2f}'. format(round(tax,2),round(tip,2),round(grand_total,2)))


# In[58]:


#An online retailer sells two products: widgets and gizmos. Each widget weighs 75
#grams. Each gizmo weighs 112 grams. Write a program that reads the number of
#widgets and the number of gizmos in an order from the user. Then your program
#should compute and display the total weight of the order.


# In[65]:


widget =75
gizmo = 112

total_widget=int(input('how many widget did you purchase?'))
total_gizmo=int(input('how many gizmo did you purchase?'))

total_weigth = widget*total_widget + gizmo * total_gizmo

print('total weigth of your purchase is {} grams'.format(total_weigth))


# In[66]:


#Exercise 9: Compound Interest
#Pretend that you have just opened a new savings account that earns 4 percent interest
#per year. The interest that you earn is paid at the end of the year, and is added
#to the balance of the savings account. Write a program that begins by reading the
#amount of money deposited into the account from the user. Then your program should
#compute and display the amount in the savings account after 1, 2, and 3 years. Display
#each amount so that it is rounded to 2 decimal places.


# In[67]:



# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.


# In[75]:


deposit_amount= int(input('what is your initial deposit amount?'))

yearly_interest = 0.04

money_after_1_year = deposit_amount * yearly_interest + deposit_amount

money_after_2_years = money_after_1_year * yearly_interest + money_after_1_year

money_after_3_years = money_after_2_years * yearly_interest + money_after_2_years

print(money_after_1_year)
print(money_after_2_years)
print(money_after_3_years)


# In[76]:


principal = float(input('How much money did you deposit? '))
interest = 0.04

year1 = (principal * interest) + principal 
year2 = (year1 * interest) + year1 
year3 = (year2 * interest) + year2

print('Your Balance after the first year is ${:.2f}'. format(round(year1,2)))
print('Your Balance after the second year is ${:.2f}'. format(round(year2,2)))
print('Your Balance after the third year is ${:.2f}'. format(round(year3,2)))


# In[77]:


#Exercise 10: Arithmetic
#Create a program that reads two integers, a and b, from the user. Your program should
#compute and display:
#• The sum of a and b
#• The difference when b is subtracted from a
#• The product of a and b
#• The quotient when a is divided by b
#• The remainder when a is divided by b
#• The result of log10a
#• The result of a^b
#'''


# In[82]:


a = int(input('write the "a" value'))

b = int(input('write the "b" value'))

sum = a+b

difference = a-b

product = a*b

quotient = a/b

remainder = a%b

power = a**b

print(sum)
print(difference)
print(product)
print(quotient)
print(remainder)
print(power)


# In[83]:


from math import log10

a = int(input('Please enter your first number: '))
b = int(input('Please enter your first number: '))

print('The sum of {} and {} is {}'. format(a, b, a+b))
print('The difference between {} and {} is {}'. format(a, b, a-b))
print('The product of {} and {} is {}'. format(a, b, a*b))
print('The quotient when {} is divided by {} is {}'. format(a, b, a//b))
print('The remainder when {} is divided by {} is {}'. format(a, b, a%b))
print('The result when the logarithm of {} is taken is {}'. format(a,log10(a)))
print('The result when {} is raised to the power of {} is {}'. format(a,b,a**b))


# In[85]:


#Exercise 13: Making Change
#Consider the software that runs on a self-checkout machine. One task that it must be
#able to perform is to determine how much change to provide when the shopper pays
#for a purchase with cash.


#Write a program that begins by reading a number of cents from the user as an
#integer. 

#Then your program should compute and display the denominations of the
#coins that should be used to give that amount of change to the shopper. The change
#should be given using as few coins as possible. Assume that the machine is loaded
#with pennies, nickels, dimes, quarters, loonies and toonies.


# In[100]:


total_cents =int(input('how mamy cents do you have'))


toonies = 200
loonies = 100
quarter =25
dime =10
nickel=5
penny =1

number_of_toonies = (total_cents // toonies, 'toonies')
total_cents = total_cents%toonies
print(number_of_toonies)

number_of_loonies = (total_cents // loonies, 'loonies')
total_cents = total_cents%loonies
print(number_of_loonies)

number_of_quarter = (total_cents // quarter, 'quarter')
total_cents = total_cents%quarter
print(number_of_quarter)

number_of_dime = (total_cents // dime, 'dime')
total_cents = total_cents%dime
print(number_of_dime)

number_of_nickel = (total_cents // nickel, 'nickel')
total_cents = total_cents%nickel
print(number_of_nickel)


number_of_penny = (total_cents // penny, 'penny')
total_cents = total_cents%penny
print(number_of_penny)


# In[99]:


cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5

cents = int(input('Enter the number of cents:  '))

print(' ', cents // cents_per_toonie, 'toonies')
cents = cents % cents_per_toonie

print(' ', cents // cents_per_loonie, 'loonies')
cents = cents % cents_per_loonie

print(' ', cents // cents_per_quarter, 'quarter')
cents = cents % cents_per_quarter

print(' ', cents // cents_per_dime, 'dime')
cents = cents % cents_per_dime

print(' ', cents // cents_per_nickel, 'nickel')
cents = cents % cents_per_nickel	

print('', cents, 'pennies')


# In[101]:


#Exercise 14: Height Units
#Many people think about their height in feet and inches, even in some countries that
#primarily use the metric system. Write a program that reads a number of feet from
#the user, followed by a number of inches. Once these values are read, your program
#should compute and display the equivalent number of centimeters.
#'''


# In[106]:



heigth_ft = int(input('feet?'))
heigth_in = int(input('inches?'))

heigth_cm = (heigth_ft * 12 * 2.54) + heigth_in * 2.54

print(heigth_cm)


# In[110]:


in_per_ft = 12
cm_per_in = 2.54

feet, inch =  input('Enter your height in feet and inches, seperate with a comma(,): ').split(',')

feet = int(feet)
inch = int(inch)
cm = ((feet * in_per_ft) + inch) * cm_per_in

print('Your height in centimerters is {} cm'.format(cm))


# In[111]:


# Constants for conversion
INCHES_PER_FOOT = 12
CM_PER_INCH = 2.54

# Input from the user
feet = int(input('Enter the number of feet: '))
inches = int(input('Enter the number of inches: '))

# Calculate the height in centimeters
total_inches = (feet * INCHES_PER_FOOT) + inches
height_in_cm = total_inches * CM_PER_INCH

# Display the result
print(f'The equivalent height is {height_in_cm:.2f} centimeters')


# In[112]:


#Exercise 15: Distance Units
#In this exercise, you will create a program that begins by reading a measurement
#in feet from the user. Then your program should display the equivalent distance in
#inches, yards and miles. Use the Internet to look up the necessary conversion factors
#if you don’t have them memorized.


# In[113]:


inches = int(input('Enter the number of inches: '))

feet = inches/12
yard = feet/3
miles = yard/1760

print(feet,yard,miles)


# In[114]:


#cozum yanlis ama code u incele

INCHES_PER_FOOT = 12
YARDS_PER_FOOT = 1 / 3
MILES_PER_FOOT = 1 / 5280

# Input from the user
feet = float(input('Enter a measurement in feet: '))

# Perform the conversions
inches = feet * INCHES_PER_FOOT
yards = feet * YARDS_PER_FOOT
miles = feet * MILES_PER_FOOT

# Display the results
print(f'Equivalent distance in inches: {inches:.2f} inches')
print(f'Equivalent distance in yards: {yards:.2f} yards')
print(f'Equivalent distance in miles: {miles:.5f} miles')


# In[ ]:


#Exercise 16: Area and Volume
#Write a program that begins by reading a radius, r, from the user. The program will
#continue by computing and displaying the area of a circle with radius r and the
#volume of a sphere with radius r. Use the pi constant in the math module in your
#calculations.


# In[115]:


r = float(input('what is the radius of the circle?'))

pi =3.14

area = pi * r**2

volume = 4/3*pi*r**3

print('The area of the cirle is {} and the volume of the sphere is {}.'.format(area,volume))


# In[116]:


import math

radius = float(input('Enter your radius: '))

circle = math.pi * (radius) ** 2
sphere = math.pi * 4/3 * (radius) ** 3

print('The Area of the circle with radius {} is {} meter squared'.format(radius,circle))
print('The Volume of the sphere with radius {} is {} meter cube'.format(radius,sphere))


# In[117]:


#The volume of a cylinder can be computed by multiplying the area of its circular
#base by its height. Write a program that reads the radius of the cylinder, along with
#its height, from the user and computes its volume. Display the result rounded to one
#decimal place.


# In[132]:


import math

r= int(input('write the radius'))
h = int(input('write the height'))

Volume = (math.pi) * (r**2) * h

print('The volume of the given cylinder equals {:.1f}'.format(Volume))


# In[133]:


import math 
radius = float(input('Enter the radius of the cylinder: '))
height = float(input('Enter the height of the cylinder: '))

area = math.pi * (radius ** 2)
volume = area * height

print('The volume of the cylinder is {:.1f}'.format(volume))


# In[134]:


#Create a program that determines how quickly an object is traveling when it hits the
#ground. The user will enter the height from which the object is dropped in meters (m).
#Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
#due to gravity is 9.8m/s2. You can use the formula vf2 = vi2 + 2ad to compute the
#final speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known


# In[137]:


h = float(input('write the height in meters'))
a = 9.8

final_speed =math.sqrt(2*a*h)

print('The final speed of the object is {:.2f} m/s'.format(final_speed))


# In[136]:


import math 

height = float(input('Enter the height from which the object drops in meters: '))
g = 9.8
vf = math.sqrt(2 * g * height)

print('The final velocity when the objects hits the ground is  {} m/s^2'. format(vf))


# ### IF Statement Exercises

# In[138]:


#   Even or Odd?
# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.


# In[141]:


number = int(input('write your number here'))

if number%2 ==1:
    print('odd')
else:
    print('even')


# In[143]:


#It is commonly said that one human year is equivalent to 7 dog years. However this
#simple conversion fails to recognize that dogs reach adulthood in approximately two
#years. As a result, some people believe that it is better to count each of the first two
#human years as 10.5 dog years, and then count each additional human year as 4 dog years.
#Write a program that implements the conversion from human years to dog years
#described in the previous paragraph. Ensure that your program works correctly for
#conversions of less than two human years and for conversions of two or more human
#years. Your program should display an appropriate error message if the user enters
#a negative number.


# In[147]:


age = int(input('what is your dogs age'))
                
if age<=2:
    new_age = age*10.5
else:
    new_age = 2*10.5 + (age-2)*4
    
print('Your dog is {:.1f})


# In[148]:


#In this exercise you will create a program that reads a letter of the alphabet from the
#user. If the user enters a, e, i, o or u then your program should display a message
#indicating that the entered letter is a vowel. If the user enters y then your program
#should display a message indicating that sometimes y is a vowel, and sometimes y is
#a consonant. Otherwise your program should display a message indicating that the
#letter is a consonant.


# In[153]:


# ilkin boyle .format kullanmistim error verdi

letter = input('write a letter from the alphabet')

if letter == ['a','e','i','o','u']:
    print('{} is a vowel').format(letter)
elif letter == ['y']:
    print('{} is a sometimes consonent sometimes vowel').format(letter)
else:
    print('{} is a consonent').format(letter)


# In[156]:


letter = input('Write a letter from the alphabet: ')

if letter in ['a', 'e', 'i', 'o', 'u']:
    print('{} is a vowel'.format(letter))
elif letter == 'y':
    print('{} is a sometimes consonant sometimes vowel'.format(letter))
else:
    print('{} is a consonant'.format(letter))


# In[157]:


#The length of a month varies from 28 to 31 days. In this exercise you will create
#a program that reads the name of a month from the user as a string. Then your
#program should display the number of days in that month. Display “28 or 29 days”
#for February so that leap years are addressed.


# In[162]:


month = input('Enter the current month: ').lower()

days_30  = ['september','april','june','november']
days_31 = ['january','march','may','july','august','october','december']

if month in days_30:
    print('this month has 30 calendar days')
elif month in days_31:
    print('this month has 31 calendar days')
else:
    print('february can be 28 or 29 days')


# In[175]:


month = input('Enter the current month: ').lower()

days_30  = ['september','april','june','november']
days_31 = ['january','march','may','july','august','october','december']

if month in days_30:
    print('this month has 30 calendar days in', month)
elif month in days_31:
    print('this month has 31 calendar days', month)
elif month == 'february':
    print('can be 28 or 29 days in', month)


# In[176]:


#The following table lists the sound level in decibels for several common noises.
#Write a program that reads a sound level in decibels from the user. If the user
#enters a decibel level that matches one of the noises in the table then your program
#should display a message containing only that noise. If the user enters a number
#of decibels between the noises listed then your program should display a message
#indicating which noises the level is between. Ensure that your program also generates
#reasonable output for a value smaller than the quietest noise in the table, and for a
#value larger than the loudest noise in the table.


# In[177]:


level = int(input('Enter the sound level in decibels(dB): '))

if level  == 130:
    print('That\'s sounds like a Jackhammer.')
elif level == 106: 
    print('That\'s sounds like a Gas Lawnmower.')
elif level == 70:
    print('That\'s sounds like an Alarm clock.')
elif level == 40:
    print('That\'s sounds like a Quiet room.')
elif  40 < level < 70:
    print('That sounds resides between a Quiet room and an Alarm clock.')
elif 70 < level < 106:
    print('That sounds resides between an Alarm clock and a Gas Lawnmower.') 
elif 106 < level < 130:
    print('That sounds resides between a Gas Lawnmower and a Jackhammer.')
elif level > 130:
    print('That\'s not bearable sound, turn it off or down.')
elif level < 40:
    print('That\'s realy quiet, you should sleep just fine.')


# In[178]:


#A triangle can be classified based on the lengths of its sides as equilateral, isosceles
#or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
#triangle has two sides that are the same length, and a third side that is a different
#length. If all of the sides have different lengths then the triangle is scalene.
#Write a program that reads the lengths of 3 sides of a triangle from the user.
#Display a message indicating the type of the triangle.


# In[185]:


a = float(input('what is the a lenght'))
b = float(input('what is the b lenght'))
c = float(input('what is the c lenght'))


if a == b==c:
    print('this triange is an equilateral')
elif a==b and b!=c:
    print('this triange is an isosceles')
elif a!=b and b!=c and a!=c:
    print('this triange is an scalene')


# In[186]:


s1 = float(input('Enter the length of the first side: '))
s2 = float(input('Enter the length of the second side: '))
s3 = float(input('Enter the length of the third side: '))

if s1 == s2 == s3:
    print('That\'s an Equilateral Triangle')
elif s1 == s2 or s1 == s3 or s2 == s3:
    print('That\'s an Isosceles Triangle')
else:
    print('That\'s an Obtuse triangle')


# In[196]:


#Canada has three national holidays which fall on the same dates each year.
#Holiday             Date
#New year’s day      January 1
#Canada day          July 1
#Christmas day       December 25
#Write a program that reads a month and day from the user. If the month and day
#match one of the holidays listed previously then your program should display the
#holiday’s name. Otherwise your program should indicate that the entered month and
#day do not correspond to a fixed-date holiday.


# In[199]:


month = input('Enter a month of the year: ').lower()
day = int(input('Enter a day of the month: '))


if month == 'january' and day == 1:
    print('New year’s day')
if month == 'july' and day == 1:
    print('Canada day')
if month == 'december' and day == 25:
    print('christmas day')


# In[200]:


month = input('Enter a month of the year: ').lower()
day = int(input('Enter a day of the month: '))

if month == 'january' and day == 1:
    holiday = 'New year’s day'
    print('The fixed date holiday which corresponds to the day and month you entered is {}'. format(holiday))
elif month == 'july' and day == 1:
    holiday = 'Canada day'
    print('The fixed date holiday which corresponds to the day and month you entered is {}'. format(holiday))
elif month == 'december' and day == 25:
    holiday = 'Christmas day'
    print('The fixed date holiday which corresponds to the day and month you entered is {}'. format(holiday))
else:
    print('Enter a valid fixed-date holiday')


# In[201]:


#Positions on a chess board are identified by a letter and a number. The letter identifies
#the column, while the number identifies the row, as shown below:
#Write a program that reads a position from the user. Use an if statement to determine 
#if the column begins with a black square or a white square. Then use modular
#arithmetic to report the color of the square in that row. For example, if the user enters
#a1 then your program should report that the square is black. If the user enters d5
#then your program should report that the square is white. Your program may assume
#that a valid position will always be entered. It does not need to perform any error checking.


# In[211]:


column = input('write a letter')
row = int(input('write a number'))

column = ['a','b','c','d','e','f','g','h']

row = 1,2,3,4,5,6,7,8

if column in ['a','c','e','g'] and row in [1,3,5,7]:
    print('this square is black')
else:
    print('this square is white')


# In[210]:


column = input('Write a letter: ')
row = int(input('Write a number: '))

valid_columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
valid_rows = [1, 2, 3, 4, 5, 6, 7, 8]

if column in valid_columns and row in valid_rows:
    if column in ['a', 'c', 'e', 'g'] and row in [1, 3, 5, 7]:
        print('This square is black.')
    else:
        print(f'The square {column}{row} is white.')
else:
    print('Invalid input. Please enter a valid column (a-h) and row (1-8).')


# In[212]:


position = input('Enter your position on the chess board e.g.(a7): ').lower()

letter = position[0]
number = int(position[1])
white  = ['a','c','e','g']

if number % 2 == 0 and letter in white:
    print('You\'re on a White square.')
else:
    print('You\'re on a Black square.')


# In[213]:


#The year is divided into four seasons: spring, summer, fall and winter. While the
#exact dates that the seasons change vary a little bit from year to year because of the
#way that the calendar is constructed, we will use the following dates for this exercise:
#Season  First day
#Spring  March 20
#Summer  June 21
#Fall    September 22
#Winter  December 21
#Create a program that reads a month and day from the user. The user will enter
#the name of the month as a string, followed by the day within the month as an
#integer. Then your program should display the season associated with the date that
#was entered.


# In[ ]:


month = input('enter a month')
day = int(input('enter a day'))

if 


# In[214]:


# Get user input for month and day
month = input('Enter the month: ').lower()
day = int(input('Enter the day: '))

# Check the season based on the provided dates
if (month == 'march' and day >= 20) or (month == 'april' or month == 'may'):
    season = 'Spring'
elif (month == 'june' and day >= 21) or (month == 'july' or month == 'august'):
    season = 'Summer'
elif (month == 'september' and day >= 22) or (month == 'october' or month == 'november'):
    season = 'Fall'
elif (month == 'december' and day >= 21) or (month == 'january' or month == 'february'):
    season = 'Winter'
else:
    season = 'Invalid input'

# Display the result
if season != 'Invalid input':
    print(f'The season for {month} {day} is {season}.')
else:
    print('Invalid input. Please enter a valid month and day.')


# In[2]:


#The horoscopes commonly reported in newspapers use the position of the sun at the
#time of one’s birth to try and predict the future. This system of astrology divides the
#year into twelve zodiac signs, as outline in the table below:
#Zodiac sign                 Date range
#Capricorn                   December 22 to January 19
#Aquarius                    January 20 to February 18
#Pisces                      February 19 to March 20
#Aries                       March 21 to April 19
#Taurus                      April 20 to May 20
#Gemini                      May 21 to June 20
#Cancer                      June 21 to July 22
#Leo                         July 23 to August 22
#Virgo                       August 23 to September 22
#Libra                       September 23 to October 22
#Scorpio                     October 23 to November 21
#Sagittarius                            November 22 to December 21
#Write a program that asks the user to enter his or her month and day of birth. Then 
#your program should report the user’s zodiac sign as part of an appropriate output
#message.


# In[3]:


#Write a program that asks the user to enter his or her month and day of birth. Then 
#your program should report the user’s zodiac sign as part of an appropriate output
#message


# In[4]:


# Example dates for illustration
start = "2023-01-01"
end = "2023-12-31"
date = "2023-06-15"

# Convert strings to datetime objects if necessary
start = datetime.strptime(start, "%Y-%m-%d")
end = datetime.strptime(end, "%Y-%m-%d")
date = datetime.strptime(date, "%Y-%m-%d")

# Check if the date is within the range
if start <= date <= end:
    print("The date is in between.")
else:
    print("No!")
         


# In[7]:


month = input('Enter your birth month: ').lower()
day = int(input('Enter your day of the birth: '))

if month == 'december' and 22 <= day <= 31 or month == 'january' and 1 <= day <= 19:
    print('Your zodiac sign is Capricon')
elif month == 'january' and  20 <= day <= 31 or month == 'february' and 1 <= day <= 18:
    print('Your zodiac sign is Aquarius ')
elif month == 'february' and  19 <= day <= 29 or month == 'march' and 1 <= day <= 20:
    print('Your zodiac sign is Pisces')
elif month == 'march' and  21 <= day <= 31 or month == 'april' and 1 <= day <= 19:
    print('Your zodiac sign is Aries')
elif month == 'april' and  20 <= day <= 30 or month == 'may' and 1 <= day <= 20:
    print('Your zodiac sign is Taurus')
elif month == 'may' and  21 <= day <= 31 or month == 'june' and 1 <= day <= 20:
    print('Your zodiac sign is Gemini')
elif month == 'june' and  21 <= day <= 30 or month == 'july' and  1 <= day <= 22 :
    print('Your zodiac sign is Cancer')
elif month == 'july' and  23 <= day <= 31 or month == 'august' and 1 <= day <= 22:
    print('Your zodiac sign is Leo')
elif month == 'august' and  23 <= day <= 31 or month == 'september' and 1 <= day <= 22:
    print('Your zodiac sign is Virgo')
elif month == 'september' and  23 <= day <= 30 or month == 'october' and 1 <= day <= 22:
    print('Your zodiac sign is Libra')
elif month == 'october' and  23 <= day <= 31 or month == 'november' and 1 <= day <= 21:
    print('Your zodiac sign is Scorpio')
elif month == 'november' and  22 <= day <= 30 or month == 'december' and 1 <= day <= 21:
    print('Your zodiac sign is  Sagittarius')


# In[8]:


The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
shown in the table below. The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the hare.
Year Animal
2000 Dragon
2001 Snake
2002 Horse
2003 Sheep
2004 Monkey
2005 Rooster
2006 Dog
2007 Pig
2008 Rat
2009 Ox
2010 Tiger
2011 Hare
Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table.


# In[17]:


year = int(input('write your birth year here '))

if year%12 == 8:
    print(f'the year {year} was the dragon year in chinese calendar')
if year%12 == 9:
    print('snake')
if year%12 == 10:
    print('horse')
if year%12 == 11:
    print('sheep')
if year%12 == 0:
    print('monkey')
if year%12 == 1:
    print('rooster')
if year%12 == 2:
    print('dog')
if year%12 == 3:
    print('pig')
if year%12 == 4:
    print('rat')
if year%12 == 5:
    print('ox')
if year%12 == 6:
    print('tiger')
if year%12 == 7:
    print('hare')


# In[18]:


The following table contains earthquake magnitude ranges on the Richter scale and
their descriptors:
Magnitude                   Descriptor
Less than 2.0               Micro
2.0 to less than 3.0        Very minor
3.0 to less than 4.0        Minor
4.0 to less than 5.0        Light
5.0 to less than 6.0        Moderate
6.0 to less than 7.0        Strong
7.0 to less than 8.0        Major
8.0 to less than 10.0       Great
10.0 or more                Meteoric
Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake.


# In[23]:


magnitude = float(input('what is the magnitude of the earthquake    '))

if magnitude<2.0:
    print('Micro')
if 2.0<=magnitude<3.0:
    print('Very Minor')
if 3.0<=magnitude<4.0:
    print('Minor')
if 4.0<=magnitude<5.0:
    print('Light')
if 6.0<=magnitude<7.0:
    print('Moderate')
if 6.0<=magnitude<7.0:
    print('Strong')
if 7.0<=magnitude<8.0:
    print('major')
if 8.0<=magnitude<10.0:
    print('Great')
if magnitude>10.0:
    print('meteoric')


# In[24]:


magnitude = float(input('Enter te magnitude of the earthquake using Richter\'s scale: '))

if 2 < magnitude:
    des = 'Micro'
elif 2 <= magnitude < 3:
    des = 'Very minor'
elif 3 <= magnitude < 3:
    des = 'Minor'
elif 4 <= magnitude < 3:
    des = 'Light'
elif 5 <= magnitude < 3:
    des = 'Moderate'
elif 6 <= magnitude < 3:
    des = 'Strong'
elif 7 <= magnitude < 3:
    des = 'Major'
elif 8 <= magnitude < 3:
    des = 'Great'
elif 10 <= magnitude:
    des = 'Metroric'

print('A mangnitude {} earthquake is considered to be a a {} earthquake'. format(magnitude, des))


# In[25]:


# Get user input for magnitude
magnitude = float(input('Enter the earthquake magnitude: '))

# Determine the earthquake descriptor
if magnitude < 2.0:
    descriptor = 'Micro'
elif 2.0 <= magnitude < 3.0:
    descriptor = 'Very minor'
elif 3.0 <= magnitude < 4.0:
    descriptor = 'Minor'
elif 4.0 <= magnitude < 5.0:
    descriptor = 'Light'
elif 5.0 <= magnitude < 6.0:
    descriptor = 'Moderate'
elif 6.0 <= magnitude < 7.0:
    descriptor = 'Strong'
elif 7.0 <= magnitude < 8.0:
    descriptor = 'Major'
elif 8.0 <= magnitude < 10.0:
    descriptor = 'Great'
else:
    descriptor = 'Meteoric'

# Display the result
print(f'A magnitude {magnitude} earthquake is considered to be a {descriptor} earthquake.')


# In[26]:


A univariate quadratic function has the form f (x) = ax2 + bx + c, where a, b and
c are constants, and a is non-zero. The roots of a quadratic function can be found
by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A
quadratic function may have 0, 1 or 2 real roots. These roots can be computed using
the quadratic formula, shown below: root = −b ± √b2 − 4ac / 2a
The portion of the expression under the square root sign is called the discriminant.
If the discriminant is negative then the quadratic equation does not have any real roots.
If the discriminant is 0, then the equation has one real root. Otherwise the equation
has two real roots, and the expression must be evaluated twice, once using a plus
sign, and once using a minus sign, when computing the numerator.
Write a program that computes the real roots of a quadratic function. Your program
should begin by prompting the user for the values of a, b and c. Then it should display
a message indicating the number of real roots, along with the values of the real roots


# In[27]:


At a particular university, letter grades are mapped to grade points in the following manner:
Letter Grade points
A+      4.0
A       4.0
A−      3.7
B+      3.3
B       3.0
B−      2.7
C+      2.3
C       2.0
C−      1.7
D+      1.3
D       1.0
F       0
Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure


# In[6]:


grade = input('what is your letter grade')
des = 0
if grade== 'A+':
    des = 4.0
if grade== 'A':
    des = 4.0
if grade== 'A-':
    des = 3.7
if grade== 'B+':
    des = 3.3
if grade== 'B':
    des = 3.0
if grade== 'B-':
    des = 2.7
if grade== 'C+':
    des = 2.3
if grade== 'C':
    des = 2.0
if grade== 'C-':
    des = 1.7
if grade== 'D+':
    des = 1.3
if grade== 'D':
    des = 1.0
if grade== 'F':
    des = 0.0
print(f'your grade is {grade} equvalent to {des}')


# In[ ]:


At a particular company, employees are rated at the end of each year. The rating scale
begins at 0.0, with higher values indicating better performance and resulting in larger
raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
with each rating is shown in the following table. The amount of an employee’s raise
is $2400.00 multiplied by their rating.
Rating              Meaning
0.0                 Unacceptable performance
0.4                 Acceptable performance
0.6 or more         Meritorious performance
Write a program that reads a rating from the user and indicates whether the performance was unacceptable, 
acceptable or meritorious. The amount of the employee’s raise should also be reported. 
Your program should display an appropriate error message if an invalid rating is entered.


# In[17]:


rating = float(input("what is the employee's rating :  "))

bonus = 2400*rating

if rating== 0.0:
    des = 'Unacceptable performance'
    message = 'work more'
if rating == 0.4:
    des = 'Acceptable performance'
    message = 'Good Job'
if rating >= 0.6:
    des = 'Meritorious performance'
    message = 'Amazing Job'
    
print(f'your rating is {rating} which means {des}, {message}!!! you will get {bonus}')


# 
# 

# In[ ]:




