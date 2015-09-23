
# coding: utf-8

# # LOGISTIC REGRESSION 

# In[1]:

import pandas as pd
import numpy as np

#read data into dataframe
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#remove % symbol from interest rate and convert to float
loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]

#remove "month" at the end of loan length and convert to integer
loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]

#create a new column called Fico Score with lower limit value
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]


# In[2]:

df1=pd.DataFrame(loansData)


# In[3]:

df1.to_csv('loansData_clean.csv')


# In[4]:

loansData = pd.read_csv('loansData_clean2.csv')


# In[5]:

df2=pd.DataFrame(loansData)


# In[6]:

import statsmodels.api as sm


# In[7]:

ind_vars = loansData.columns[1:-13]


# In[8]:

print(ind_vars)


# In[9]:

X = np.asarray(df2[ind_vars])


# In[10]:

y = np.asarray(df2['Logit.Interest.Rate'])


# In[11]:

f = "y ~ X"


# In[12]:

import statsmodels.api as sm
import statsmodels.formula.api as smf


# In[13]:

logit_mod = sm.Logit(y,X)


# In[14]:

logit_res = logit_mod.fit()
print(logit_res.summary())


# In[15]:

logit_res.predict([1,10000])


# In[16]:

x=np.arange(100,50001,100)


# In[22]:

np.ones(len(x));


# In[18]:

proby= logit_res.predict(np.column_stack([np.ones(len(x)),x]))


# In[19]:

from matplotlib import pyplot as plot


# In[20]:

get_ipython().magic('matplotlib inline')


# In[21]:

plot.plot(x,1-proby)

