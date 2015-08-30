# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:08:27 2015

@author: AshRajBala
"""
"""
UNIT 2: OVERVIEW OF STATISTICS
Data originally from: http://lib.stat.cmu.edu/DASL/Datafiles/AlcoholandTobacco.html
"""

import pandas as pd

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''


# First, split the string on the (hidden characters that indicate) newlines.
data = data.splitlines() #This would also work: data.split('\n')

#Then split each item in this list on the commas:
data = [i.split(', ') for i in data]

# The bracketed expression is a list comprehension. 
# A list comprehension is a way of iterating through the values of a list. 
# You can use a list comprehension to print values or transform the values. 
# In this case, the string first gets split into a list of strings (each row is a string). 
# We then use a list comprehension to take each string and split that into a list so that 
# we end up with a list of lists. 

#Now convert, to create a pandas dataframe:
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


#****************************************************************************#
"""
MEASURES OF CENTRAL TENDENCY
"""
#****************************************************************************#

df['Alcohol'].mean() #Ans: 5.4436363636363634
df['Alcohol'].median() #Ans: 5.63

#While pandas has built-in types for mean and median, we'll need to import the mode() 
#function from scipy.stats 

from scipy import stats

#If all numbers occur equally often, stats.mode() will return the smallest number
stats.mode(df['Alcohol']) #Ans:(array([ 4.02]), array([ 1.]))



#****************************************************************************#
"""
MEASURES OF VARIABILITY
"""
#****************************************************************************#

"""
Once we've got the center (or measures of central tendency), 
the next piece of information about data is how far the values go 
on either side of the center, which is known as the variability of the data.

1. Range; 
2. Variance (the measure of distribution about the mean. 
How close or far are values in a set from the mean?)
3. Relative variability: the standard deviation divided by the mean. 
The relative variability is useful for comparing variation between samples.
"""

max(df['Alcohol']) - min(df['Alcohol']) # Ans: 2.4500000000000002
df['Alcohol'].std() #Ans:  0.79776278087252406
df['Alcohol'].var() #Ans: 0.63642545454546284

max(df['Tobacco']) - min(df['Tobacco']) #Ans: 1.8499999999999996
df['Tobacco'].std() #Ans: 0.59070835751355388
df['Tobacco'].var() #Ans: 0.3489363636363606



#****************************************************************************#
"""
MEASURES BASED ON RANING DISTRIBUTION
"""
#****************************************************************************#

"""
Simple ranking: when the data are ordered in some way, the rank of a data point 
is simply its position in that order.
Percentile ranking: the percent of data points that are below a data point.
z-score: the number of standard deviations that a data point is from the mean. 
The z-score of a data point is equal to the value x minus the mean, 
divided by the standard deviation.
"""

