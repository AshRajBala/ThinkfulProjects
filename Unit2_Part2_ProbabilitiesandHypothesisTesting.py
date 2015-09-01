# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 06:46:37 2015

@author: AshRajBala
"""

"""
Overview of Probability
"""

"""
INTRO:
 An event is the outcome of an experiment. 
 An experiment, in probability, is a test to see what the outcome will be if 
 you do something (i.e., what event will occur).
"""

"""
RANDOMNESS:
A random variable is a function that associates a real number, x, with the 
outcome of an experiment, and it's usually denoted by X. So let's say you flip 
a coin twice. The space of possible events S is given by S = {HH, HT, TH, TT}. 
To find the probability of one of those outcomes, we ask P(X = x), or, what is 
the probability that the random variable X is equal to some real number x? The 
expected value of a random variable is a probability-weighted average of 
possible outcomes for that variable.
"""

"""
PROBABILITY DISTRIBUTIONS:
A probability distribution maps all the possible values of a random variable to
their corresponding probabilities. Probability distributions can be "discrete" 
or "continuous." If your random variables are discrete (there are a finite set 
of possible outcomes, e.g. flipping a coin heads or tails) or continuous 
(an infinite number of possible outcomes, e.g. scores on a test). 
"""

"""
Plotting Probability Distributions in Python
"""


"""
When running import matplotlib.pyplot as plt (first line below), ran into 
this error:
ImportError: dlopen(//anaconda/lib/python3.4/site-packages/matplotlib/_png.so, 
2): Library not loaded: @loader_path/../../../libpng15.15.dylib
  Referenced from: //anaconda/lib/python3.4/site-packages/matplotlib/_png.so
  Reason: image not found

Following steps from this link: 
http://stackoverflow.com/questions/28848270/import-matplotlib-pyplot-gives-importerror-dlopen-library-not-loaded-libpng1  
helped resolve the issue.
Specifically, at the terminal, the following lines were typed:
conda remove matplotlib
pip uninstall matplotlib
conda install matplotlib
"""
  
  
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

mean = 0
variance = 1
sigma = np.sqrt(variance) # this is the standard deviation
x = np.linspace(-3,3,100)
plt.plot(x, mlab.normpdf(x,mean,sigma))

plt.show()

"""
HYPOTHESIS TESTING:
You test the null hypothesis in the following way:
1. Determine the null hypothesis and the alternative hypothesis.
2. Collect the appropriate sample.
3. Use measurements from the sample to determine the likelihood of the null hypothesis.

Depending on the hypothesis, and especially on the sample, different statistical 
tests will be appropriate. For example, the Chi Square test is appropriate for 
categorical variables, while the Wilcoxon Rank-Sum test is better for continuous 
variables.
"""

"""
STATISTICAL SIGNIFICANCE:
In statistics, a result is considered statistically significant if it's 
unlikely to have occurred by chance. 

The probability that the result occurred by chance is referred to as the p-value, 
and the threshold is usually indicated by alpha.

A statistically significant result is one whose p-value < alpha.

A p-value less than 0.05 indicates we can reject the null hypothesis. 
"""

"""
A word on the null hypothesis:
From:https://medium.com/@maradydd/the-null-hypothesis-loves-you-and-wants-you-to-be-happy-3189413d8cd0

Apophenia is the technical term for those imaginary relationships. 
It’s what happens when you look up at the full moon and see a rabbit or a 
person’s face, or when you believe there’s a secret message beyond 
“the ratio between a circle’s circumference and diameter is constant” 
encoded in the digits of π. Conspiracy theories thrive on apophenia. 
It was first named in order to describe the onset of schizophrenia: 
apophany in contrast to epiphany. It is the unavoidable consequence of being a 
member of a species whose super-strength is its self-adapting, pattern-matching 
brain. Apophenia is our super-weakness. The null hypothesis shields us against 
it with its own body.
"""


