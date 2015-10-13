
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

# In[27]:

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# Set seed for reproducible results
np.random.seed(414)

# Gen toy data
X = np.linspace(0, 15, 1000)


# In[24]:

y = 3 * np.sin(X) + np.random.normal(1 + X, .2, 1000)


# In[25]:

train_X, train_y = X[:700], y[:700]


# In[26]:

test_X, test_y = X[700:], y[700:]


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


# ### Metrics and Cross-Validation:

# ### Metrics:
# 
# When building a supervised model, it's important to have a clear idea of how you will evaluate its performance. As we've discussed, one crucial part of evaluation is to separate your training and testing set to avoid overfitting. Once we have done this, it's time to decide exactly what metric we will use to evaluate our model. Metrics differ between regression and classification models:

# #### Regression:

# 1. Mean Squared Error: Mean square error between our predicted outcomes, and the true response in our test set.
# 
# 2. Mean Absolute Error: Mean absolute error between our predicted outcomes, and the true response in our test set.
# 
# 3. R-Squared: Coefficient of determination from regression score function.

# #### Classification:

# 4. Accuracy: The percentage of data points labeled correctly by the model.
# 
# 5. Precision: The ratio of (true positives / (true_positives + true_negatives)). The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.
# 
# 6. Recall: The ratio of (true_positives / (true_positives + false_negatives)). The recall is intuitively the ability of the classifier to find all the positive samples.
# 
# A typical work flow while building a model is to split your data, build your model, and then choose a metric to evaluate it.For instance, suppose we wanted to build a classifier to predict whether or not an individual had cancer. In this scenario, the harm of incorrectly predicting that some one does not have cancer who actually does is far worse than predicting that a healthy person has cancer. Thus, we want to minimize our false negatives, and might choose recall as our metric.

# ### Cross-validation:

# It is often desirable to use cross validation to get a further estimate of your models performance. In cross validation, we take our training set, and iterative split it into folds of subtraining and sub_testing data (I've added the sub prefix to avoid confusion between the original train/test split we performed). We train our model on the sub_train folds, and evaluate it on the sub_test fold. The basic approach is this:
# 
# The training set is split into k smaller sets (the value of k will give the name of the cross validation approach; for example, if k=10, we are implementing 10-fold cross validation).
# The model is trained on k - 1 of these smaller sets.
# The resulting model is validated on the remaining set.

# In[28]:

from sklearn.cross_validation import KFold


# In[29]:

kf = KFold(4, n_folds=2)


# In[30]:

for train_df, test_df in kf:
    print("%s %s" % (train_df, test_df))

