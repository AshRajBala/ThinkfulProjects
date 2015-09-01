# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:52:04 2015

@author: AshRajBala
"""

import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#STEP 1: Clean the dataset:remove rows with null values for better visualization of dataset
loansData.dropna(inplace=True)

#STEP 2:Boxplot
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

#STEP 3:Histogram
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

#STEP 4:QQ-Plot
import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()
