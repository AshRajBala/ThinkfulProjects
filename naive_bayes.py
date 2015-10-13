
# coding: utf-8

# # NAIVE BAYES
# 
# ## INTRODUCTION

# The probabilistic model of Naive Bayes classifiers is based on Bayes’ Theorem, while the adjective “naive” comes from the assumption that the features in the data are mutually independent.

# More often than not, the features in the data aren't mutually independent, but Naive Bayes classifiers still perform well, and they perform especially well on small sample sizes, which is one of their main advantages. 

# Very simply, a Naive Bayes classifier will take an observation, compute the Bayesian probability of each possible hypothesis, and select the hypothesis with the highest probability (the Maximum A Posteriori (MAP) hypothesis) to classify the observation.

# In[3]:

# source of data: https://www.dropbox.com/s/hg0tqy6saqeoq0j/ideal_weight.csv?dl=0
# local source: /Users/AshRajBala/Repositories/ThinkfulProjects/ideal_weight.csv

import pandas as pd 
import matplotlib.pyplot as plt
import numpy
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import MultinomialNB
get_ipython().magic('matplotlib inline')

data = pd.read_csv("/Users/AshRajBala/Repositories/ThinkfulProjects/ideal_weight.csv", sep=',')

# Remove single quotes from column names
helper = []
for columnname in data.columns:
    helper.append(columnname[1:-1]) #extract string without quotes
    #See also http://stackoverflow.com/questions/14419206/what-does-1-mean-in-python
data.columns = helper


# In[4]:

# Remove single quotes from sex observation data
helper = []
for entriesinsexcol in data['sex']:
    helper.append(entriesinsexcol[1:-1])
data['sex'] = helper


# In[5]:

# Graph histogram for ideal weight and actual weight
plt.hist(data['actual'], bins=20, alpha=0.5, label='actual')
plt.hist(data['ideal'], bins=20, alpha=0.5, label='ideal')
plt.legend(loc='upper right')
plt.show()


# In[9]:

# Plot distribution of difference in weight
plt.hist(data['diff'], alpha=0.5, label='actual-ideal')


# In[10]:

# Plot distribution of difference in weight
plt.hist(data['diff'], alpha=0.5, label='actual-ideal')


# In[11]:

# Map 'sex' to a categorical variable. 0 = female, 1 = male
data['sex'] = pd.Categorical(data['sex']).codes #pd.Caregorical(data['sex']).labels has been deprecated. 

# Explore sex variable
data.groupby('sex').describe()


# There are more women than men in the dataset.

# We're going to use the sklearn.naive_bayes.GaussianNB to build our classifier of gender. A Gaussian Naive Bayes classifier assumes that the likelihood of the features is assumed to be Gaussian.

# In[12]:

from sklearn.naive_bayes import GaussianNB


# Now, we will:
# 
# 1. Fit a Naive Bayes classifier of sex to actual weight, ideal weight, and diff.
# 2. Determine how many points were mislabeled, and how many points were there in the dataset, total.
# 3. Predict the sex for an actual weight of 145, an ideal weight of 160, and a diff of -15.
# 4. Predict the sex for an actual weight of 160, an ideal weight of 145, and a diff of 15.

# In[13]:

# partition train and test data
train_cut = int(len(data) * 0.7)


# In[14]:

train_cut


# In[15]:

len(data)


# In[16]:

# partition train and test data
fortrain = data[:train_cut]
fortest = data[train_cut:]


# In[20]:

# declare training target and predictors and fit the model
train_target = fortrain['sex']
train_data = fortrain.ix[:,2:]# all rows, from second index column- i.e. from column named 'actual'
clf = GaussianNB()
clf.fit(train_data, train_target)


# In[21]:

# predict on test set
test_target = fortest['sex']
test_data = fortest.ix[:,2:]
pred = clf.predict(test_data)


# In[22]:

# see how close predictions are to actual value
testlist = list(test_target)
c = 0
for i in range(len(testlist)):
    if testlist[i] == pred[i]:
        c += 1
print("Correctly predicted " + str(c) + " of " + str(len(testlist)) + " values.")


# In[23]:

# predict sex for actual = 145, ideal = 160, diff = -15
# 0 = female, 1 = male
print(clf.predict([[145,160,-15]]))


# In[24]:

# predict sex for actual = 160, ideal = 145, diff = 15
# 0 = female, 1 = male
print(clf.predict([[160,145,15]]))

