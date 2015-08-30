# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:04:58 2015

@author: AshRajBala
"""

import pandas as pd
from scipy import stats

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

data = data.splitlines()
data = [i.split(', ') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


#Anaconda crashes, if trying to pass values as tuples the following (example shown for mean, but holds true for all others):
# print("The mean weekly houshold spending (in pounds) on alcohol is: %f and for tobacco it is %f" % (df['Alcohol'].mean(),df['Tobacco'].mean()))  


#Hence, print statements were separately written out as below:
print("The mean weekly houshold spending (in pounds) on alcohol is: %f" % df['Alcohol'].mean())  
print("The median weekly houshold spending (in pounds) on alcohol is: %f" % df['Alcohol'].median()) 
print("Most households spend %f pounds on alcohol every week" % stats.mode(df['Alcohol'])[0][0]) 
print("The range of alcohol spending per week is" % (max(df['Alcohol']) - min(df['Alcohol'])))
print("The standard deviation for alcohol spending is %f" % df['Alcohol'].std())
print("The variability of alcohol spending as measured by variance is %f" % df['Alcohol'].var())


print("The mean weekly houshold spending (in pounds) on alcohol is: %f" % df['Tobacco'].mean())  
print("The median weekly houshold spending (in pounds) on alcohol is: %f" % df['Tobacco'].median()) 
print("Most households spend %f pounds on alcohol every week" % stats.mode(df['Tobacco'])[0][0]) 
print("The range of alcohol spending per week is" % (max(df['Tobacco']) - min(df['Tobacco'])))
print("The standard deviation for alcohol spending is %f" % df['Tobacco'].std())
print("The variability of alcohol spending as measured by variance is %f" % df['Tobacco'].var())
