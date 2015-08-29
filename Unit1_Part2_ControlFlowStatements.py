# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:45:50 2015

@author: AshRajBala
"""

"""Testing Thinkful.com Data Science in Python."""

"""Unit 1 Exercise: Control Flow Statements section"""
print("Hello World")

#****************************************************************************#
"""if"""
#****************************************************************************#

if 5 > 3:
    print("Yep, math works today.")

 
#****************************************************************************#
"""if-else"""
#****************************************************************************#   
if 5 < 3:
    print("Things might be a little off...")
else:
    print("Yep, math works today.")    
    
#****************************************************************************#
"""if-elif-else"""
#****************************************************************************#   

if 5 < 3:
    print("Things might be a little off...")
elif 5 == 3:
    print("Maybe we should stay inside.")
else:
    print("Yep, math works today.")
    

#****************************************************************************#
"""for"""
#****************************************************************************#   

beatles = ("John", "Paul", "George", "Ringo")
for beatle in beatles:
    print(beatle)

#In the example below, the else statement at the end will only print if the for 
#loop finishes without encountering a break statement.
for n in range(1,100):
    if n % 3 == 0:
        print(n)
else:
    print("The loop is over")  
 
   
#****************************************************************************#
"""while"""
#****************************************************************************#   

#This program will print Still running! ten times, one for each mile, 
#and then print Whew! I'm tired. 
#The += operator simply increases miles_run by one.  
miles_run = 0
running   = True

while running:
    if miles_run <= 10:
        print("Still running! On mile {}".format(miles_run))
        miles_run += 1
    else:
        running = False
else:
    print("Whew! I'm tired")
    
#****************************************************************************#
"""try"""
#****************************************************************************#   

#Handles errors cleanly
1/0
#Error: Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
  #ZeroDivisionError: integer division or modulo by zero

#How to handle this error cleanly with 'try'
a = 1
b = 0
try:
    a / b
except ZeroDivisionError:
    print("Cannot divide by zero.")
    

#****************************************************************************#
"""Functions"""
#****************************************************************************#   

#IN-BUILT FUNCTIONS AND THIER MANIPULATIONS
#range()
#Staring number for range is by default 0, but we can set it to 1, as shown below:
for i in range(1,10):
     print(i)

"""     
Ans:
1
2
3
4
5
6
7
8
9
"""



"""
Sometimes the built in types aren't enough. We've used a dictionary before. 
The Python built-in dictionary is great, but there's another dictionary that is 
better for a lot of the operations we're going to be doing. It's called a defaultdict, 
and you get it by importing it like you would any other package:

The defaultdict allows us to add values to a dictionary in a loop.
This allows us the ability to keep running tallies of things as we process the data. 
For instance:
"""

import collections
#Step1: Create a list of values (number_list)
number_list = [1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,5,6,7,8,8,8,8,9,9,9,9] 

#Step2: Create a new defaultdict. Specify that the defaultdict should contain 
#integer values by giving the argument int
count_dict = collections.defaultdict(int) 

#Step3: Iterate through number_list with the for loop. 
#When we do this, each value in number_list gets assigned to i. 
#We then use i as the key and add 1 to the value for that number using the += operator.
for i in number_list:
    count_dict[i] += 1

count_dict #Ans: defaultdict(<class 'int'>, {1: 2, 2: 4, 3: 2, 4: 2, 5: 6, 6: 1, 7: 1, 8: 4, 9: 4})


"""IMPORTANT NOTE"""
"""    
In version 2.7, Python introduced a Counter that could also be used here. 
For example: instead of using the for loop to populate the count_dict, you could 
simply use the code count = collections.Counter(number_list) and Python will 
automatically tally the counts when it reads in the list.   
""" 

#USER-DEFINED FUNCTIONS:
def addition(a, b):
    """Adds two numbers and prints the result"""
    x = a + b
    print(x) #prints output to stdout, aka console
    return x #returns the output out of the function
addition(2,2)
#If we had passed two strings, the result would have been a concatenation of the strings

#Illustrating the power of the return function
from datetime import datetime
import logging

def log_handler(msg):
    """Sends msg to the logging platform"""
    date = str(datetime.now())
    msg = date + " - " + msg
    return logging.info(msg)

def log(msg):
    """A convenience function. Adds msg to the logs with log_handler"""
    msg = str(msg)
    print("Message logged: " + msg)
    return log_handler(msg)

def addition(a, b):
    """Adds two numbers and logs the result"""
    x = a + b
    log("Adding {0} and {1} = {2}.".format(a, b, x))
    return x

addition(1, 2)
addition(2, 3)
addition(5, addition(3, 5))

"""
The above script will return:
Message logged: Adding 1 and 2 = 3
Message logged: Adding 2 and 3 = 5
Message logged: Adding 3 and 5 = 8
Message logged: Adding 5 and 8 = 13
"""




"""
Writing an algorithm is a lot like writing a recipe. 
You have a list of ingredients, like a list of variables and a dataset; 
you have a list of instructions, like a list of functions and commands to run in a script. 
Take the following recipe for brownies:

Ingredients:
1/2 cup butter
1 cup sugar
2 eggs
1 tsp vanilla extract
1/2 cup cocoa
1/2 cup flour

Directions:
1. If butter is not soft, then melt butter.
2. Blend melted butter and sugar until mixture has creamy consistency, about 3 minutes
3. Add eggs and vanilla; stir
4. Add cocoa and flour; mix until well blended, about 4 minutes
5. Pour into greased round glass cake pan
6. Bake in oven 350 degrees for 30 minutes

Now you can convert the instructions into code. 
First, you'll represent each ingredient as a variable. 
You'll need to add the ingredients to a bowl to mix them, 
so you'll use an empty list as a container. 
For actions such as "melt" or "bake", you'll just print out the action that 
we would be doing. In an actual algorithm these functions would be 
transformations on the data such as removing empty entries in a dataset, 
or converting all the numbers from percentages to decimals, or 
training a logistic model, etc.
"""

# Ingredients are stored as a dictionary of tuples. Each tuple contains the name
# of the ingredients and the amount in milliliters (unless otherwise specified)
# Why a dictionary of tuples? Because it is kinda convenient, and shows off how to
# combine multiple data structures.
ingredients = {
    "butter"  : ("butter", 118.3),
    "sugar"   : ("sugar", 236.6),
    "vanilla" : ("vanilla", 4.929),
    "eggs"    : ("eggs", 2), # whole eggs
    "cocoa"   : ("cocoa", 118.3),
    "flour"   : ("flour", 118.3)
}
# The butter was refrigerated, so it's not soft yet.
butter_soft = False
bowl = []
# To make the cake, we'll need the following functions
def melt(this):
    print("Melting {0}.".format(this))

def bake(this, temp):
    print("Baking {0} at {1}.".format(this, temp))

def mix(this):
    print("Mixing {0}.".format(this))

def add_to_bowl(ingredient):
    print("Adding {0} to the bowl.".format(ingredient))
    return bowl.append(ingredient)

##### Start the algorithm! #####

if butter_soft != True:
    melt(ingredients["butter"][0])
    butter_soft = True
  
add_to_bowl(ingredients["butter"][0])
add_to_bowl(ingredients["sugar"][0])

mixing_time = 0
mixture_creamy = False

# Mix until creamy
while mixture_creamy == False:
    mix(bowl)
    mixing_time += 1
    if mixing_time == 3:
        # After 3 minutes, the mixture will be creamy,
        # and our while loop will stop
        mixture_creamy = True

add_to_bowl(ingredients["eggs"][0])
add_to_bowl(ingredients["vanilla"][0])

mix(bowl)

add_to_bowl(ingredients["cocoa"][0])
add_to_bowl(ingredients["flour"][0])

mixing_time = 0
well_blended = False

# Mix until well-blended
while well_blended == False:
    mix(bowl)
    mixing_time += 1
    if mixing_time == 4:
        well_blended = True   
        
# In cooking terms: pour contents of the bowl into a cake pan
# In Python terms: redefine the bowl variable as cake_pan
       
cake_pan = bowl

cooking_temp = 350
cooking_time = 30

for minute in range(0, cooking_time):
    bake(cake_pan, cooking_temp)

print("Cake is done!")






  
