# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 08:04:32 2015

@author: AshRajBala
"""

"""
DISTRIBUTIONS AS FREQUENCIES:
One way to think about a distribution is in terms of the frequency that you 
see a given number.
"""

import collections

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

print(c)

# calculate the number of instances in the list
count_sum = sum(c.values())


#In the Thinkful course, the syntax for the following line is given as:
#for k,v in c.iteritems(). However, in Python 3, we just say items. :
#Ref: http://stackoverflow.com/questions/7888786/python-word-count-and-rank

for k,v in c.items():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

"""
BOX PLOT REPRESENTATION OF DISTRIBUTION:
A box plot draws horizontal lines at the median, the first quartile 
(the 25th percentile of the data) and the third quartile (the 75th percentile). 
These three lines form the top and bottoms of two boxes. A (vertical) line is 
then drawn from the middle of the quartile lines to the ends of the data range, 
barring any outliers. What defines an outlier (which are typically drawn with 
asterisks) depends on the package. 

BOXPLOTS also provide info on variability of data, specifically:
1. Range
2. Interquartile Range (IQR = Q3-Q1)
3. Skewness or shape of dataset
"""

"""
GENERATING A BOXPLOT:
Note: The show() function below will open a second window with the plot. 
The code will pause until you close the plot. 
You can save the plot using the savefig() function in pyplot instead of show().
You call it on the plt object and pass in the filename you wish to use. 
For example, to save the file as "boxplot.png", you'd type plt.savefig("boxplot.png"). 
This will save the current plt object with the filename you specified.
"""

import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.show()

"""
GENERATING A HISTOGRAM:
While exact location statistics may not be clear, the most and least frequent 
values are readily apparent.
"""

plt.hist(x, histtype='bar')
plt.show()

"""
QQ PLOTS:
So far, we have only discussed discrete data (remember, this means data that 
can be counted like heads/tails of a coin toss or rolling dice). But we can 
apply the basic concepts from above to continuous data (e.g. any value within a
range; scores on a test or height and weight). Certainly, continuous data will 
have quartile measures and a median, so a box plot of continuous data is really 
no different than a discrete data set. However, on a continuous scale, the 
probability associated with any given number is 0. For example, if a dart is 
thrown at a random point along a line, the chance that it lands at 4.1 cm from 
the origin is 0, as is the probability it lands at 2.32323232 cm from the 
origin (allowing for infinite precision in measurement of the point of contact). 
It makes sense, though, to discuss the chance of this dart landing within a 
range of values.
"""
"""
For this reason we are more concerned with the marginal distribution or 
probability density of a value, which when summed over a range of values 
yield a probability mass. This probability mass is the relative likelihood of 
the range of values compared to the entire distribution.
"""

"""
Certain distributions are found over and over again in all kinds of data sets. 
The most important distribution by far is the "normal distribution," which is 
shaped like a bell, indicating that data closer to the mean is more likely than 
observations far from the mean. 

Another important distribution is the "uniform 
distribution," which is simply a flat line, reflecting that all numbers over the 
given range are equally likely.
"""

"""
Once we start to understand distributions, we can start to do some more rigorous 
testing of data. Often, we ask whether or not a data observation is likely given 
the underlying distribution. For discrete cases, this is a relatively easy when 
one knows the shape of the distribution--it is just the relative frequency 
discussed above. In a discrete case, it is also easy to ask how likely it is to 
get a result less than or equal to the current observation-just add the relative 
frequencies of the all the possible outcomes below or equal to the observation.

For continuous variables, the mathematics involved in getting a range of values 
is a little tricky (again, single values have 0 likelihood) and can involve 
calculus. With normally-distributed variables, there are reference tables that 
make calculations easy. So to calculate how likely it is to get a value less 
than the current observation, we 1) scale the observation (subtract the mean 
and divide by the standard deviation) and compare that to 2) the cumulative 
distribution table of a Normal variable.
"""

"""
Given a set of data, it is often useful to test whether or not it belongs to a 
certain distribution. Testing for normality (whether or not the data is normally 
distributed) is a popular initial step when inspecting data. To visually test 
data, you can create a QQ Plot, which plots a given set of data against the 
theoretical quantiles of normally-distributed data with the same mean and 
standard deviation of the data set in question. When plotted out, the data 
should form a straight line.

E.g.:
"""

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.figure()
test_data2 = np.random.uniform(size=1000)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph


