# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:44:43 2015

@author: AshRajBala
"""

"""Testing Thinkful.com Data Science in Python."""

"""Unit 1 Exercise: Datatype section"""
print("Hello World")

#****************************************************************************#
"""Booleans"""
#****************************************************************************#

"""
You can use bool() to convert a value to a Boolean.
Anything that represents "nothing", such as None, 0, and empty strings/lists, will evaluate to False;
anything that represents "something" is True:
"""
t = True
type(t) #Ans: <class 'bool'>
bool(42) #Ans: True
bool("Happy go lucky") #Ans: True
bool(0) #Ans: False
bool("") #Ans: False

"""You can assign return values to a variable:"""
answer = 1 >= 2
answer #Ans: False


#****************************************************************************#
"""Strings"""
#****************************************************************************#

"""You can substitute values into strings with the format() method:"""
"{0} don't think it {1} like it is, but it {2}".format("They", "be", "do")

"""
You can treat strings like a list of characters, if you want.
This selects the first character in the sentence.
IMPORTANT: Strings are 0-indexed:
"""

"Yar matey!"[0] #Ans: 'Y'


#****************************************************************************#
"""Lists"""
#****************************************************************************#
"""
A list is just a sequence of stuff, usually numbers.Lists are important because they are so flexible.
IMPORTANT 1: Like strings, lists are zero-indexed.
IMPORTANT 2: Lists retain order. They don't automatically order their elements.
The order in which you add stuff to your list is the order that the list will retain.
"""

li = [] # An empty list!
other_li = [1, 2, 3] # A prefilled list!
li.append(1)
li.append(5)
li.append(3)
li #Ans: [1 5 3]
li.pop()
li #Ans: [1 5]
li[0] #Ans: 1


li = [1, 2, 4, 3, 5] # Select a range between index 1 and 3 (closed/open range, in math terms)
li[1:3] #Ans: [2, 4]
li[2:] #Begin at index loc. 2(?);  Ans: [4, 3, 5]
li[:3] #End before index loc. 3(?);  Ans: [1, 2, 4]
li[::2] # Select every second entry (i.e. step by 2) [SYNTAX: li[start:end:step]];  Ans: [1, 4, 5]
li[::-1] # Reverse the list [SYNTAX: li[start:end:step]]; Ans:[5, 3, 4, 2, 1]
del li[2]# Delete the 3rd item
li #Ans:[1, 2, 3, 5]
1 in li # Check if 1 is in list li; Ans:True
len(li) #What's the length of the list li?; Ans: 4


#****************************************************************************#
"""Tuples"""
#****************************************************************************#
"""
The mug analogy: in the case of lists, if you break the handle off of your coffee mug,
there is no going back to the old mug, unless you explicitly glue it back together.
Similarly, in lists, when you provide a function such as append (see above), you have
changed the li object; there is no going back to the old li


Creating layers in photography analogy:Tuples are immutable lists;
they do the same operations as lists, but you don't actually modify a tuple.
When you add something to a tuple, a new tuple is created with the added value.
You can't even append() on a tuple. You can add two tuples, but that gives you a new tuple:
Tuples maintain structure. Can be thought of as "coordinates" 
"""

tup = (1, 2, 3)
tup.append(4) #You cannot append to a tuple; error message displayed
tup + (4, 5, 6) #but you can add tuples together; Ans: (1, 2, 3, 4, 5, 6)
#Interesting note: The answer *does* return a tuple, but it *doesn't* save the tuple as tup. 
tup #Ans: (1, 2, 3)
new_tup = tup + (4, 5, 6)
new_tup #Ans: (1, 2, 3, 4, 5, 6)

bookmark = (42, 5) # page number, line number
"""bookmark can now act as key to look up a reference"""


bookmark1 = (35, 5)
bookmark2 = (86, 15)
bookmark3 = (106, 11)
notes = [bookmark1, bookmark2, bookmark3]
"""Each bookmark refers to a singular location, and notes is a list of these locations."""

 
#****************************************************************************#
"""Sets"""
#****************************************************************************#
"""
Unlike lists and tuples, sets do NOT retain order; like lists, they only allow unique entries
Sets are created with either set() or {}. Because they work in the same way as mathematical sets,
intersection, union, and difference operations work as you would expect:
"""

my_set = {1, 2, 2, 3, 4, 5, 6, 7}
my_set #Ans: {1, 2, 3, 4, 5, 6, 7}
your_set = {6, 7, 8, 9, 10}
your_set #Ans: {8, 9, 10, 6, 7}

# Set intersection - finds the common elements
my_set & your_set #Ans: {6, 7}

# Set union - combines the two sets into one
my_set | your_set #Ans: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Set difference - finds the elements in one set but not in the other
my_set - your_set #Ans: {1, 2, 3, 4, 5}

# Existence within a set
1 in my_set #Ans: True


#****************************************************************************#
"""Dictionaries"""
#****************************************************************************#
"""
The dictionary data structure simply associates one value with another,
so that k : v, where k is a key and v is the value associated with that key.
The definitions are stored inside the dictionary, and you can only access them
by calling on the dictionary itself first.
"""

stooges = {"Larry": "balding, with frazzled hair",
               "Curly": "short buzz-cut",
               "Moe"  : "bowl cut"}
stooges
{'Larry': 'balding, with frazzled hair', 'Moe': 'bowl cut', 'Curly': 'short buzz-cut'} 

#To acces one element of the dictionary, call the dictionary with the key
stooges['Larry'] #Ans: 'balding, with frazzled hair'

stooges.keys() #Ans: ['Larry', 'Moe', 'Curly']
stooges.values() #Ans: ['balding, with frazzled hair', 'bowl cut', 'short buzz-cut']
"Larry" in stooges #Ans: True
#If you lookup a non-existing key, then you get a KeyError. You can avoid this by using the get() method:
stooges["Shemp"] #Error:Traceback (most recent call last):...Keyerror...
stooges.get("Shemp")
# Returns None, which is suppressed from display, but we can explicitly print it:
print(stooges.get("Shemp")) #Ans: None

