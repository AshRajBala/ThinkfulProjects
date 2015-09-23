
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

ind_vars = loansData.columns[1:-11]


# In[8]:

print(ind_vars)


# In[9]:

X = np.asarray(df2[ind_vars])


# In[10]:

X


# In[11]:

y = np.asarray(df2['Logit.Interest.Rate'])


# In[12]:

f = "y ~ X"


# In[13]:

import statsmodels.api as sm
import statsmodels.formula.api as smf


# In[14]:

logit_mod = sm.Logit(y,X)


# In[15]:

logit_res = logit_mod.fit()
print(logit_res.summary())


# In[16]:

logit_res.predict([1,10000,720])


# In[18]:

from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')


# In[19]:

x=np.arange(100,20001,100)


# In[20]:

np.ones(len(x))


# In[21]:

proby= logit_res.predict(np.column_stack([np.ones(len(x)),x,x]))


# In[24]:

plt.plot(x,proby)


# In[ ]:



