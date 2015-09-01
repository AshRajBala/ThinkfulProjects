# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:54:27 2015

@author: AshRajBala
"""

import pandas as pd

import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt 

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#STEP 1: Clean the dataset:remove rows with null values for better visualization of dataset
loansData.dropna(inplace=True)

data_to_plot=[loansData['Amount.Funded.By.Investors'], loansData['Amount.Requested']]
# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)

## add patch_artist=True option to ax.boxplot() 
## to get fill color
bp = ax.boxplot(data_to_plot, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)
    
## Custom x-axis labels
ax.set_xticklabels(['Amount Funded', 'Amount Requested'])
## Remove top axes and right axes ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
# Save the figure
fig.savefig('boxplot.png', bbox_inches='tight')

"""
INTERPRETATION OF RESULTS:
The medians for both Amount Funded and Requested are approximately the same, although
both do not seem to follow a normal distribution (with some positive skew).

The range of amount requested is also greater than the amount that is funded.
"""
#import numpy

import matplotlib.pyplot as pypl

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

loansData.hist(column='Amount.Requested')
plt.show()

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()

"""
Anaconda crashed! Unable to view plots for some reason. Will try again
"""

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()
