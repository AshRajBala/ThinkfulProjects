# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:01:01 2015

@author: AshRajBala
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import collections


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()
chi2, p = scipy.stats.chisquare([freq.values()])
msg = "Test Statistic: {}\np-value: {}"
print(msg.format( chi2, p))

"""
Previously, i had set 'agg' as backend that screwed up the GUI plot.
If that happens, do this at the terminal:
$ spyder --reset
$ spyder
"""

