
# coding: utf-8

# # REGRESSION AND CLASSIFICATION

# ## Regression: 
# Measure of relationship between mean value of one variable with corresponding value(s) of (an) other variable(s). Unlike classification (discussed below), regression models continuous/ordered values.
# In regression, we evaluate our model based on how close the predicted value is to the actual value of an observation. 
# 
# ## Classification:
# Process of determining the category or class that an observation belongs to.
# Can be binary (spam or no spam) or multiclass (which one of "n" classes, does an observation belong to?).
# Classification is a supervised learning technique: we need to have a dataset with correct class labels for training. When correct class labels are not available, the corresponding unsupervised learning technique we can use is clustering.

# ## Supervised Learning - Steps:

# #### STEP 1:  Process and generate the initial data set for modeling. 
# It will contain both the predictor variables (x1...xn) and the target variable y (Y is called the target variable because the supervised learning's "goal" is to is predict the missing variable y).

# #### STEP 2: Split the data into training and testing sets for evaluation of our prediction model. 
# 
# Q: Why split? Why can't we evaluate our model on the training data itself? 
# A: Because then, we'd have a very optimistic view of our models performance, since it was optimized directly on the training data.
# 
# The split needs to be performed in such a way that both sets contain the same patterns of data. For example, if the initial data set has 100 observations, with the predictor value being 60 "Y" and 40 "N" in these observations, the individual training and testing sets should also have the Y and N in the same ratio of 3:2. 
# 
# Splitting is usually done through random selection.
# 
# Typically, the training set has 70% of the records in the initial data set.

# #### STEP 3: Build a model on the training data set.
# 
# Building a model (also called training or fitting) boils down to optimizing a set of parameters on the training set. For instance, in the case of linear regression, we assume a linear relationship between our features and our response variable, and learn the coefficients of the model from our training set. This occurs through minimizing our squared error loss function:
# 
# Loss(*beta*) = **1/n** x (summation over i) (**y_i** - [**X_i** x *beta*])^2, with respect to each*beta* parameter (i.e., taking the partial derivatives and setting them to zero).  
# 
# Avoid overfitting models (learning the training data too closely; otherwise, this would cause the prediction of new data to perform more poorly). 

# #### STEP 4: Test the model using the test data set. 
# We use the model to predict the value of Y in each of the test records. Then compare the predicted value of Y with the actual value of Y. This gives an indication of the accuracy of the prediction model built. 

# #### STEP 5: Fine tune the model using cross-validation. 
# Try different algorithms/parameters, until the accuracy reaches an acceptable level.

# #### STEP 6: Predict unknown data.
# Use the model built on new data (where Y is NOT known) to predict Y.

# ### Demonstration of Overfitting:

# In[14]:

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# Set seed for reproducible results
np.random.seed(414)

# Gen toy data
X = np.linspace(0, 15, 1000)
print(X)


# In[15]:

y = 3 * np.sin(X) + np.random.normal(1 + X, .2, 1000)
print(y)


# In[16]:

train_X, train_y = X[:700], y[:700]
print(train_X)


# In[17]:

print(train_y)


# In[18]:

test_X, test_y = X[700:], y[700:]
print(test_X)


# In[19]:

print(test_y)


# In[20]:

train_df = pd.DataFrame({'X': train_X, 'y': train_y})
print(train_df)


# In[21]:

test_df = pd.DataFrame({'X': test_X, 'y': test_y})
print(test_df)


# In[22]:

# Linear Fit
poly_1 = smf.ols(formula='y ~ 1 + X', data=train_df).fit()
poly_1.summary()


# In[23]:

# Quadratic Fit
poly_2 = smf.ols(formula='y ~ 1 + X + I(X**2)', data=train_df).fit()
poly_2.summary()


# In[ ]:



