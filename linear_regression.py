# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:40:19 2015

@author: AshRajBala
"""

import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData['Interest.Rate'][0:5] # first 5 rows of Interest.Rate
loansData['Loan.Length'][0:5] # first 5 rows of Loan.Length
loansData['FICO.Range'][0:5] # first 5 rows of FICO.Range

"""
The interest rate column has '%' symbols in it, and the loan length column has 
the string 'months' in it. The FICO range is a categorical variable; to use it 
in our calculations, we need it to be numeric.
We also need to:
Remove the '%' symbols from the Interest.Rate column.
Remove the word 'months' from the Loan.Length column.
"""

"""
We can use a lambda function.. A lambda function is a so-called anonymous 
function, meaning that it's not bound to a name.

Lambda functions are often used in conjunction with concepts like filter(), 
map(), and reduce(). map() will map the lambda function to each element of 
what's passed to it. 
"""
# Need to remove the % symbol
# Let's grab one of the values to experiment with

x = loansData['Interest.Rate'][0:5].values[1]
x #Ans: '12.12%'
x = x.rstrip('%') # Removes the % from the end 
x #Ans: '12.12'

x = float(x) # Convert x to a number
type(x)
x = x / 100 # because this is a percentage
x #Ans: 0.12119999999999999
x = round(x, 4) # We don't need that much precision, round to 4 digits
# Now we know what we have to do. Combine the above into a single lambda function
y = lambda x: round(float(x.rstrip('%')) / 100, 4)
y(x) #Ans: 0.1212

# So the lambda function is working, now we need to map this lambda function
# over all of the values in loansData['Interest.Rate']. For this, Python has
# a method called .map()
help(map) # If you use the help() function, press q to exit the help screen.

"""
Help on built-in function map in module __builtin__:

map(...)
    map(function, sequence[, sequence, ...]) -> list
    
    Return a list of the results of applying the function to the items of
    the argument sequence(s).  If more than one sequence is given, the
    function is called with an argument list consisting of the corresponding
    item of each sequence, substituting None for missing values when not all
    sequences have the same length.  If the function is None, return a list of
    the items of the sequence (or a list of tuples if more than one sequence). 
"""

# Store the result in a variable so we don't overwrite our data right away,
# in case something goes wrong

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

type(cleanInterestRate) #Ans: <class 'pandas.core.series.Series'>

# Looks good so far! Let's check the values
cleanInterestRate[0:5]

# It worked! Our column is full of properly-formatted floats.
# Now we just need to replace the column in the dataframe

loansData['Interest.Rate'] = cleanInterestRate
loansData['Interest.Rate'][0:5]

loansData['Loan.Length'][0:5]
# We need to remove ' months' and convert to an integer
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
cleanLoanLength[0:5]
 # In the answer, notice this ^dtype: int64^ means the data type is an integer. 
# This is what we want.

# Now for the FICO.Range
loansData['FICO.Range'][0:5]

# For this one, we'll split the numbers and replace it with a list of
# two numbers in the form of [start, end]. Unfortunately, we'll need to
# use multiple passes - we can't just do it all in one .map(lambda...)
# First we'll use the .split() method.

cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange[0:5]

cleanFICORange[0:5].values[0] #Ans: ['735', '739']
type(cleanFICORange[0:5].values[0]) #Ans: <type 'list'>
cleanFICORange[0:5].values[0][0] #Ans: '735'
type(cleanFICORange[0:5].values[0][0]) #Ans: <type 'str'>

# This is a start. As you can see, we have only a list of strings. Now, 
# for each string inside of each list, we need to convert it to an integer.
# But, we'll have to get inside each list. To do that, we can use a list
# comphrehension. The list comp starts here...|  ([ below) and ends here...
#| (] below)

cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
type(cleanFICORange[0:5].values[0][0]) #Ans: <type 'int'>

# We have successfully converted the strings inside the list to integers
# If you don't understand list comprehensions, take a peek at this blog post:
# http://carlgroner.me/Python/2011/11/09/An-Introduction-to-List-Comprehensions-in-Python.html
# # Now we can replace the column in our data frame with the cleaned data

loansData['FICO.Range'] = cleanFICORange
loansData['FICO.Range'][0:5]
loansData['FICO.Range'][0:5].values[0][0] #Ans: 735
type(loansData['FICO.Range'][0:5].values[0][0]) #Ans: <type 'int'>
#Success!


#Alternative method using list comprehensions as suggested online; specifically here:
#https://gist.github.com/bsima/22baa3cb5d511e173a55


import pandas as pd
#read data into dataframe
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#remove % symbol from interest rate and convert to float
loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]

#remove "month" at the end of loan length and convert to integer
loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]

#create a new column called Fico Score with lower limit value
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]


import matplotlib.pyplot as plt

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

"""
SCATTERPLOT MATRIX:
A scatterplot matrix is a grid of plots of multiple variables that shows the 
relationship of each variable to each of the others.
Create a scatterplot matrix.
"""

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

"""
NOTE:
From: http://stackoverflow.com/questions/26360759/understanding-the-diagonal-in-pandas-scatter-matrix-plot
As you can tell, the scatter matrix is plotting each of the columns specified 
against each other column.

However, in this format, when you got to a diagonal, you would see a plot of a 
column against itself. Since this would always be a straight line, Pandas decides 
it can give you more useful information, and plots the density plot of just that 
column of data.

See http://pandas.pydata.org/pandas-docs/stable/visualization.html#density-plot.

If you would rather have a histogram, you could change your plotting code to:

axs = scatter_matrix(df, alpha=0.2, diagonal='hist')

Also see this: http://machinelearningmastery.com/quick-and-dirty-data-analysis-with-pandas/
"""

#Our linear model is going to look something like this:
#InterestRate = b + a1(FICOScore) + a2(LoanAmount)

#We're going to use statsmodels to find the model coefficients b 
#(which is the y-intercept), a1, and a2.

import numpy as np
import pandas as pd
import statsmodels.api as sm

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']


#When we extract a column from a DataFrame, it's returned as a Series datatype. 
#You want to reshape the data like this:

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

#Now you want to put the two columns together to create an input matrix 
#(with one column for each independent variable):
x = np.column_stack([x1,x2])

#Now we create a linear model:
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary()

"""
Since we are estimating, it would be nice to know how reliable our estimate is. 
We learned earlier that smaller p-values indicate that we can reject the null 
hypothesis; there is a very small chance our results are due to chance. 
Conventionally, a p-value should be 0.05 or less.
"""

