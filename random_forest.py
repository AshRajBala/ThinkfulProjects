
# coding: utf-8

# # INTRODUCTION:
# 
# In machine learning, decision trees are commonly used to help identify features, and specific values of those features, that are most likely to result in a target value. If the target value is categorical, the model is a classification tree; if the target value is continuous, the model is a regression tree.

# ## Random Forests:

# Imagine that an expert has a decision tree model in their head, and we assemble say 100 such experts. Loosely speaking, we have a decision forest. The idea behind Random Forests is to learn a bunch of decision tree classifiers (a forest of decision trees), and sort through the predictions of each decision tree to produce a result that is, in the aggregate, better than the prediction of any individual decision tree. Essentially, a random forest works as follows:
# 
# 1. Grow a large number of decision trees on your training data.
# 2. For each tree, use only a random subset of features and random subset of datapoints. This prevents overfitting by not letting all of the trees use the same features.
# 3. Make predictions by aggregating over each decision trees' individual predctions.
# 
# Random forests provide an extremely useful measure known as feature importances. 

# In Olympic gymnastic and diving competitions, a panel of judges scores a participant. The top and bottom scores are dropped and the rest are averaged. A Random Forest algorithm uses similar techniques to eliminate some of the trees' predictions. Each round, the Random Forest will randomly drop some number of trees and then average the result after, say, 100 rounds.

# # CODE:

# In[2]:

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as skm
import pylab as pl

# data source: https://archive.ics.uci.edu/ml/machine-learning-databases/00240/
# local file location for training: /Users/AshRajBala/Repositories/ThinkfulProjects/UCI HAR Dataset/train

subjects = pd.read_csv("/Users/AshRajBala/Repositories/ThinkfulProjects/UCI HAR Dataset/train/subject_train.txt", header=None, delim_whitespace=True, index_col=False)
subjects.columns = ['Subject']
subjects


# In[3]:

len(subjects.stack().value_counts()) # 21 participants


# In[4]:

feature_names = pd.read_csv("/Users/AshRajBala/Repositories/ThinkfulProjects/UCI HAR Dataset/features.txt", header=None, delim_whitespace=True, index_col=False)
len(feature_names) # 561 features
feature_names


# In[5]:

x_vars = pd.read_csv("/Users/AshRajBala/Repositories/ThinkfulProjects/UCI HAR Dataset/train/X_train.txt", header=None, delim_whitespace=True, index_col=False)


# In[6]:

x_vars


# In[7]:

helper = []; helper2 = []; helper3 = []; helper4 = []; helper5 = []; helper6 = []
for el in list(feature_names[1]):
	helper.append(re.sub('[()-]', '', el))
for el in helper:
	helper2.append(re.sub('[,]', '_', el))
for el in helper2:
	helper3.append(el.replace('Body', ''))
for el in helper3:
	helper4.append(el.replace('Mag', ''))
for el in helper4:
	helper5.append(el.replace('mean', 'Mean'))
for el in helper5:
	helper6.append(el.replace('std', 'STD'))
x_vars.columns = helper6
# 7352 observations, 561 columns
y_var = pd.read_csv("/Users/AshRajBala/Repositories/ThinkfulProjects/UCI HAR Dataset/train/y_train.txt", header=None, delim_whitespace=True, index_col=False)
y_var.columns = ['Activity']


# In[8]:

data = pd.merge(y_var, x_vars, left_index=True, right_index=True)
data = pd.merge(data, subjects, left_index=True, right_index=True)
# 7352 obs, 562 columns

# change activity to categorical variable
data['Activity'] = pd.Categorical(data['Activity']).codes

# partition data into training, test, and validation sets
fortrain = data.query('Subject >= 27')
fortest = data.query('Subject <= 6')
forval = data.query("(Subject >= 21) & (Subject < 27)")


# In[9]:

# fit random forest model
train_target = fortrain['Activity']
train_data = fortrain.ix[:,1:-2]
rfc = RandomForestClassifier(n_estimators=500, oob_score=True)
rfc.fit(train_data, train_target)


# In[10]:

train_target = fortrain['Activity']
train_data = fortrain.ix[:,1:-2]


# In[11]:

# determine oob to show accuracy of model
rfc.oob_score_

# determine most important features
importances = rfc.feature_importances_
indices = np.argsort(importances)[::-1]
for i in range(10):
    print("%d. feature %d (%f)" % (i + 1, indices[i], importances[indices[i]]))


# In[13]:

# define validation set and make predictions
val_target = forval['Activity']
val_data = forval.ix[:1,-2]
val_pred = rfc.predict(val_data)


# In[ ]:

# define test set and make predictions
test_target = fortest['Activity']
test_data = fortest.ix[:,1:-2]
test_pred = rfc.predict(test_data)


# In[ ]:

# calc and print accuracy scores
print("mean accuracy score for validation set = %f" %(rfc.score(val_data, val_target)))
print("mean accuracy score for test set = %f" %(rfc.score(test_data, test_target)))


# In[ ]:

# visualize confusion matrix
# How?

