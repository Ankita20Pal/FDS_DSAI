#!/usr/bin/env python
# coding: utf-8

# # Pract_6 : Discrete Distribution

# In[1]:


# for inline plots in jupyter
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image
import numpy as np


# In[2]:


import seaborn as sns
sns.set(color_codes = True)
sns.set(rc = {'figure.figsize' : (5,5)})


# # Uniform Distribution

# In[14]:


from scipy.stats import randint
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

low, high = 7, 31
mean, var, skew, kurt = randint.stats(low, high, moments='mvsk')

x = np.arange(randint.ppf(0.01, low, high), randint.ppf(0.99, low, high))
ax.plot(x, randint.pmf(x, low, high), 'bo', ms = 8, label = 'randint pmf')
ax.vlines(x, 0, randint.pmf(x, low, high), colors = 'b', lw = 5, alpha = 0.5) # alpha (change the color of line)


# In[ ]:


prob = randint.cdf(x, low, high)
prob


# # Bernoulli Distribution

# In[7]:


from scipy.stats import bernoulli
data_bern = bernoulli.rvs(size = 10000, p = 0.6)


# In[11]:


ax = sns.distplot(data_bern, 
                kde = False,
                color ='skyblue',
                hist_kws = {'linewidth': 15, 'alpha':1})
ax.set(xlabel = "Bernoulli Distribution", ylabel = 'Frequency')


# # Binomial Distribution

# In[15]:


from scipy.stats import binom
data_binom = binom.rvs(n = 10, p=0.8, size = 10000)


# In[17]:


ax = sns.distplot(data_binom, 
                kde = False,
                color ='skyblue',
                hist_kws = {'linewidth': 15, 'alpha':1})
ax.set(xlabel = "Binomial Distribution", ylabel = 'Frequency')


# # Poisson Distribution

# In[19]:


from scipy.stats import poisson
data_poisson = poisson.rvs(mu = 3, size = 10000)


# In[25]:


ax = sns.distplot(data_poisson,
                 bins =30,
                 kde = False,
                 color='skyblue',
                 hist_kws = {'linewidth':15, 'alpha':1})
ax.set(xlabel='Poisson Distribution', ylabel = 'Frequency')


# In[ ]:




