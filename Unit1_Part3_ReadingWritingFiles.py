# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:16:10 2015

@author: AshRajBala
"""

"""Testing Thinkful.com Data Science in Python."""

"""Unit 1 Exercise: Reading and Writing into Files section"""
print("Hello World")

#****************************************************************************#
"""
with open
"""
#****************************************************************************#

with open('path/to/filename', 'rU') as inputFile:

    #The rU tells Python we want to read from the file 
    #(the U stands for Universal Newlines, meaning it will properly handle 
    #newlines from any platform, Windows, Apple, or Linux

    # process the inputFile here
    # more processing

# after we stop indenting, the file is closed!


#****************************************************************************#
"""
pass
"""
#****************************************************************************#

with open('filename.csv','rU') as inputFile:
    pass

"""
Here the pass command is just a placeholder until we write the rest of our code. 
This doesn't actually import the whole file into Python, it just makes a connection 
to the file and puts a cursor at the head of the file. This is important when 
you're working with large files. You don't want to overload Python with too much 
data so it's good to get into a habit of only reading in the data you need when 
you need it.
"""

#****************************************************************************#
"""
Looking at data by iterating through lines
"""
#****************************************************************************#
with open('filename.csv','rU') as inputFile:
    for line in inputFile:
        print line

"""
At this point, the file cursor we created when we first opened the file is now 
at the end of the file. To get the file contents again, we'll need to repeat the 
open() command to reset the cursor.
"""

