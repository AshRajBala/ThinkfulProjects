# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:14:57 2015

@author: AshRajBala
"""

import scipy.stats as stats
import matplotlib as mpl
import matplotlib.pyplot as plt



x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

#Boxplot
plt.boxplot(x)

#REFERENCE FOR FIGURE CODE comes from: http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
# agg backend is used to create plot as a .png file
mpl.use('agg')

##########################################################################
import matplotlib.pyplot as plt #this is run after running mpl.use('agg')

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)
ax.set_title('Boxplot for x')
ax.set_xlabel('Distribution')
ax.set_ylabel('Values')

# Create the boxplot
bp = ax.boxplot(x)

## add patch_artist=True option to ax.boxplot() 
## to get fill color
bp = ax.boxplot(x, patch_artist=True)

# change outline color, fill color and linewidth of the boxes
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

# Save the figure
fig.savefig('boxplot.png', bbox_inches='tight')
plt.show()
##########################################################################


#Histogram
plt.hist(x, histtype='bar')
plt.figure()
# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))
# Create an axes instance
ax = fig.add_subplot(111)
ax.set_title('Histogram for x')
ax.set_xlabel('Values')
ax.set_ylabel('Frequency')
plt.show()

#QQ-plot
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.figure()



