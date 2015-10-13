
# coding: utf-8

# In[7]:

from sklearn import datasets
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

get_ipython().magic('matplotlib inline')


# In[3]:

# load and select relevant data
iris = datasets.load_iris()


# In[5]:

X = iris.data[:, :2]  # we only take the first two features:length, and width
Y = iris.target


# In[8]:

# create scatterplot of sepal length vs. width by species
plt.scatter(X[:,0], X[:,1], c=Y)


# In[9]:

X


# In[30]:

# generate new random point
length = []
for sepalfeatures in enumerate(X): 
    #http://stackoverflow.com/questions/22171558/what-does-enumerate-mean
    #for each sepalfeatures in X, a tuple is produced with (counter, sepalfeatures)
    length.append(sepalfeatures[1][0])
    print(sepalfeatures)
    print((sepalfeatures)[0])
    print((sepalfeatures)[1]) # access index 1, which is array. To get length, we must do: sepalfeatures[1][0]
    print((sepalfeatures)[1][0])


# In[20]:

print(length)


# In[22]:

width = []
for sepalfeatures in enumerate(X):
    width.append(sepalfeatures[1][1])


# In[28]:

rand_point = []
rand_point.append(np.random.uniform(min(length), max(length)))
rand_point.append(np.random.uniform(min(width), max(width)))


# In[36]:

print(rand_point)
print(rand_point[0])
print(rand_point[1])


# In[37]:

sepalfeatures


# In[42]:

# Calculate the euclidean distance from new point to all existing points
# sqrt((p1-q1)**2 + (p2-q2)**2)
print(Y) #Y is in groups; to be classified based on sepal length and width

distances = []
count = 0
for sepalfeatures in enumerate(X):
    d = np.sqrt( (sepalfeatures[1][0]-rand_point[0])**2 + (sepalfeatures[1][1]-rand_point[1])**2 )
    distances.append([d, Y[count]])
    count = count + 1


# In[43]:

# Sort distances and take top 10 which will be closest 10 points
distances.sort()
top10 = distances[:10]


# In[44]:

top10


# In[45]:

# Determine the majority class of top 10

cls = []
for dist in top10:
	cls.append(dist[1])
Counter(cls)
# Majority class(es) is(are) 1 & 2.


# ## Using functions

# In[46]:

def prep_data():
    iris = datasets.load_iris()
    X = iris.data[:,:2]
    Y = iris.target

# userprovided_sepalfeatures = [random_sepal_length, random_sepal_width], k = # of neighbors
def knn(userprovided_sepalfeatures, k):
    prep_data()

    distances = []
    count = 0

    for preexisting_sepalfeatures in enumerate(X):
        d = np.sqrt( (preexisting_sepalfeatures[1][0]-userprovided_sepalfeatures[0])**2 + (preexisting_sepalfeatures[1][1]-userprovided_sepalfeatures[1])**2 )
        distances.append([d, Y[count]])
        count = count + 1

    distances.sort()
    top = distances[:k]	

    cls = []
    for el in top:
        cls.append(el[1])
    print(Counter(cls))
    print("0=serisota, 1=verisicolor, 2=virginica")
    print("Species: ", max(Counter(cls)))


# In[47]:

knn([3,2],3)

