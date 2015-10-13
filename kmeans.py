
# coding: utf-8

# Previously, we've looked at data where we did know what belonged to what. Our data was labeled, and we could learn off of those labels. For those data we could use supervised learning techniques. Often, data won't be neatly and nicely labeled.
# 
# There can be many attributes or features, but no label to indicate which rows belong to which label or group. Without the labels, we'd be hard-pressed to build a classification model. We wouldn't even know what values we're classifying things as!
# 
# One approach to this situation is to try to find some "natural" groupings in the data. Clustering is one such approach that looks at each of the different attributes in the data and tries to group the data based on rows that have similar values for the attributes.

# In[15]:

# Source: https://drive.google.com/file/d/0B7Vwt0JZZE6qSzIyckNiU0x3U3c/view
# Local source: /Users/AshRajBala/Repositories/ThinkfulProjects/undata.csv

import pandas as pd

# Load un data
un = pd.read_csv("/Users/AshRajBala/Repositories/ThinkfulProjects/un.csv")


# In[21]:

len(un)


# In[23]:

# Get num of rows, Get num of ******non-null****** values present in each column
un.count()

# Highest number of missing values (lowest values in output):
# educationMale              76
# educationFemale            76


# Based on the number of non-null values, we can cluster on tfr, lifeMale, lifeFemale, infantMortality, GDP/cap

# In[19]:

# Determine datatype of each column
un.dtypes


# In[20]:

# How many countries are present in data? 207
len(un['country'])


# We're going to see how lifeMale, lifeFemale and infantMortality cluster according to GDPperCapita, keeping in mind that we don't know in advance how many clusters there will be.

# In[24]:

# Because indexes start from 0, we need columns 6,7,8, and 9
data = un.ix[:,:10]
data = data.dropna()


# In[ ]:



