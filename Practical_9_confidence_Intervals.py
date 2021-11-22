#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
import seaborn as sns
import numpy as np
import statsmodels.api as sm
from scipy.stats import stats
import pandas as pd

import os


# In[2]:


df = pd.read_csv('D:/MSC/FDS Practical/Data/loans_income.csv')
df.head()


# # The Bootstrap

# In[3]:


loan_income = np.array(pd.read_csv('D:/MSC/FDS Practical/Data/loans_income.csv'))
loan_income[:5]


# In[4]:


# making a flat list from list of list
loan_income = np.array([item for sublist in loan_income for item in sublist])


# In[8]:


def bootstrap(l, R):
    n = len(loan_income)
    means_of_boot_samples = []
    for reps in range(R):
        boot_sample = np.random.choice(loan_income, size=n)
        means_of_boot_samples.append(round(np.mean(boot_sample), 3))
    return means_of_boot_samples

bootstrap(loan_income, 7)                                     


# In[9]:


np.std(bootstrap(loan_income, 100))


# produce a histogram or boxplot

# In[10]:


plt.figure(dpi = 200)

plt.subplot(221)
plt.title('R = 10000')
plt.hist(bootstrap(loan_income, 10000), edgecolor= 'k')

plt.subplot(222)
plt.title('R = 1000')
plt.hist(bootstrap(loan_income, 1000), edgecolor= 'k')

plt.subplot(223)
plt.title('R = 100')
plt.hist(bootstrap(loan_income, 100), edgecolor= 'k')

plt.subplot(224)
plt.title('R = 10')
plt.hist(bootstrap(loan_income, 10), edgecolor= 'k')

plt.tight_layout()


# Find Confidence intervals

# In[11]:


data = bootstrap(loan_income, 1000)
lower_lim,upper_lim = np.percentile(data, 2.5), np.percentile(data, 95)
print('Lower limit: ', lower_lim)
print('Upper limit: ', upper_lim)


# In[13]:


plt.figure(dpi = 100)

plt.title(' 95% Confidence intervals of loan applicants based on sample of 10000 means')

sns.distplot(bootstrap(loan_income, 1000), hist=True, kde = True ,
            color = 'darkblue', bins = 50,
            hist_kws = {'edgecolor':'black'},
            kde_kws = {'linewidth':2})

plt.axvline(x = lower_lim, color = 'red')
plt.axvline(x = upper_lim, color = 'red')


# In[ ]:





# In[ ]:




