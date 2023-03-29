            ##### Python Beginner Reference #####

            ### Variables and Strings ###
'''Variables are used to store values. A string is a series of 
characters, surrounded by single or double quotes.'''

#Hello World
print("Hello world!")

#With a variable 
msg = "Hello world!"
print(msg)

#f-Strings (using variables in strings)
first_name = 'Albert'
last_name = 'Einstein'
full_name = f"{first_name} {last_name}"
print(full_name)


            ### Lists ###
'''A list stores a series of items in a particular order. You 
access items using an index, or within a loop.'''

#Make a list
bikes = ['Trek', 'Redline', 'Giant']

#Get first item in list
first_bike = bikes[0]

#Get last item in list
last_bike = bikes[-1]

#Looping through a list
for bike in bikes:
    print(bike)

#Adding items to lists
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')
print(bikes)

#Making numerical lists
squares = []
for x in range(1,11):
    squares.append(x**2)
print(squares)

#List comprehensions
squares = [x**2 for x in range(1,11)]
print(squares)

#Slicing a list
finishers = ['Sam', 'Bob', 'Ada','Bea']
first_two = finishers[:2]

#Copying a list
copy_of_bikes = bikes[:]

            ### Tuples ###
'''Tuples are similar to lists, but are immutable, meaning the items 
in a tuple can't be modified. '''

#Making a tuple
dimensions = (1920, 1080)

            ### If statements ###
'''If statements are used to test for particular conditions and
respond appropriately.'''

#Conditional tests
x == 42 #equals
x != 42 #not equal
x > 42 #greater than
x >= 42 #greater or equal to
x < 42 #less than
x <= 42 #less or equal to

#Conditional test with lists
'trek' in bikes
'surly' not in bikes

#Assigning boolean values
game_active = True
can_edit = False

#Simple if test
age = 20
if age >= 18:
    print("You can vote!")

#If-Elif-Else Statements
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15
print(f"You must pay ${ticket_price} for your ticket.")

            ### Dictionaries ###
'''Dictionaries store connections between pieces of 
information. Each item in a dictionary is a key-value pair.'''

#A simple dictionary 
alien = {'color': 'green', 'points': 5}

#Accessing value
print(f"The alien is {alien['color']} and is worth {alien['points']} points.")

#Adding a new key-value pair
alien['x_position'] = 0

#Looping through all key-value pairs
fav_numbers = {'Eric': 17, 'Tom': 4}
for name, number in fav_numbers.items():
    print(f"{name} loves {number}")

#Looping through all keys
fav_numbers = {'Eric': 17, 'Tom': 4}
for name in fav_numbers.keys():
    print(f"{name} loves number.")

#Looping through all the values
fav_numbers = {'Eric': 17, 'Tom':4}
for number in fav_numbers.values():
    print(f"{number} is a favorite.")

            ### User Input ###
'''Your programs can prompt the user for input. All input is 
stored as a string.'''

#Prompting for a value
name = input("What's your name? ")
print(f"Hello, {name}!")

#Prompting for numerical input
age = input("How old are you? ")
age = int(age)

pi = input("What's the value of pi? ")
pi = float(pi)
