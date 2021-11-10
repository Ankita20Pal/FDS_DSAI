#!/usr/bin/env python
# coding: utf-8

# # Practical 7 : Continuous Distribution

# In[2]:


# for inline plots in jupyter
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image
import numpy as np


# In[3]:


import seaborn as sns
sns.set(color_codes = True)
sns.set(rc = {'figure.figsize' : (5,5)})


# # Uniform Distribution

# In[5]:


from scipy.stats import uniform


# In[6]:


n = 100000
start = 10
width =20
data_uniform = uniform.rvs(size = n, loc = start, scale = width)


# In[8]:


ax = sns.distplot(data_uniform,
                 bins = 100, # 100 , 100 value k liye bin hona chahiye
                 kde = True,
                 color = 'skyblue',
                 hist_kws = {'linewidth': 15, 'alpha': 1})
ax.set(xlabel = 'Unifrom Distribution', ylabel = 'Frequency')


# # Normal Distribution

# In[13]:


from scipy.stats import norm
# generate random number from N(0,1)
data_normal = norm.rvs(size=10000, loc=0, scale=1) # scale 100


# In[14]:


ax = sns.distplot(data_normal,
                 bins = 100, # 100 , 100 value k liye bin hona chahiye
                 kde = True,
                 color = 'skyblue',
                 hist_kws = {'linewidth': 15, 'alpha': 1})
ax.set(xlabel = 'Unifrom Distribution', ylabel = 'Frequency')


# # Exponential Distribution 

# In[15]:


from scipy.stats import expon

data_expon = expon.rvs(size=1000, loc=0, scale=1) # scale 100


# In[16]:


ax = sns.distplot(data_expon,
                 bins = 100, # 100 , 100 value k liye bin hona chahiye
                 kde = True,
                 color = 'skyblue',
                 hist_kws = {'linewidth': 15, 'alpha': 1})
ax.set(xlabel = 'Exponential Distribution', ylabel = 'Frequency')


# # Chi Square Distribution

# In[18]:


from numpy import random

x = random.chisquare(df=2, size=(2,3))

print(x)


# In[20]:


sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()


# # Weibull Distribution

# In[22]:


a = 5 # shape

s = np.random.weibull(a, 1000)


# In[23]:


import matplotlib.pyplot as plt

x = np.arange(1, 100)/50

def weib(x, n, a):
    return (a/n) * (x/n)**(a-1)*np.exp(-(x/n)**a)


# In[24]:


count, bins, ignored = plt.hist(np.random.weibull(5., 1000))

x = np.arange(1, 100.)/50

scale = count.max()/weib(x, 1., 5.).max()

plt.plot(x, weib(x, 1., 5.)*scale)

plt.show()


# In[ ]:




