#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import stats
import pandas as pd
from scipy.stats import ttest_1samp
from statsmodels.stats.power import tt_ind_solve_power


# # T test

# In[ ]:


ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35]


# In[ ]:


ages_mean=np.mean(ages)
print(ages_mean)


# In[ ]:


sample_size=10
age_sample=np.random.choice(ages, sample_size)
age_sample


# In[ ]:


from scipy.stats import ttest_1samp


# In[ ]:


ttest, p_value=ttest_1samp(age_sample, 30)


# In[ ]:


print(p_value)


# In[ ]:


if p_value < 0.05:
    print('We are rejecting null hypothesis')
else:
    print('We are accepting null hypothesis')


# In[5]:


df=pd.read_excel('D:/MSC/FDS Practical/Data/Result.xlsx')
df


# In[6]:


df.describe()


# In[8]:


Ho='mu <= 113'
Ha='mu > 113'
# al -> alpha
al=0.05
# mu -> mean
mu=113
# tail type
tt = 1
# data
marks = df['Total'].values
print('Ho:', Ho)
print('Ha:', Ha)
print('al:', al)
print('mu:', mu)
print(marks)
print('')


# In[9]:


ts, pv = ttest_1samp(marks, mu)
print('t-stat', ts)
print('p-vals', pv)
t2pv = pv
t1pv = pv*2
print('1t tv', t1pv)
print('2t tv', t2pv)


# In[10]:


if tt == 1:
    if t1pv < al:
        print('Null Hypothesis: Rejected')
        print('Conclusion:', Ha)
    else:
        print('Null Hypothesis: Not Rejected')
        print('Conclusion:', Ho)
else:
    if t2pv < al/2:
        print('Null Hypothesis: Rejected')
        print('Conclusion:', Ha)
    else:
        print('Null Hypothesis: Not Rejected')
        print('Conclusion:', Ho)


# In[11]:


# null hyp
Ho = 'mu = 113'
# alt hyp
Ha = 'mu != 113'
# alpha
al = 0.05
# mu - mean
mu = 113


# In[13]:


# tail type
tt = 2
# data
marks = df['Total'].values
print('Ho:', Ho)
print('Ha:', Ha)
print('al:', al)
print('mu:', mu)
print(marks)
print('')


# In[14]:


ts, pv = ttest_1samp(marks, mu)
print('t-stat', ts)
print('p-vals', pv)
t2pv = pv
t1pv = pv*2
print('1t tv', t1pv)
print('2t tv', t2pv)


# In[15]:


if tt == 1:
    if t1pv < al:
        print('Null Hypothesis: Rejected')
        print('Conclusion:', Ha)
    else:
        print('Null Hypothesis: Not Rejected')
        print('Conclusion:', Ho)
else:
    if t2pv < al/2:
        print('Null Hypothesis: Rejected')
        print('Conclusion:', Ha)
    else:
        print('Null Hypothesis: Not Rejected')
        print('Conclusion:', Ho)


# # AB Testing

# In[18]:


sub1 = np.array([45,36,29,40,46,37,43,39,28,33])
sub2 = np.array([40,20,30,35,29,43,40,39,28,31])


# In[19]:


sns.distplot(sub1)


# In[20]:


sns.distplot(sub2)


# In[21]:


t_stat, p_val = stats.ttest_ind(sub1, sub2)
t_stat, p_val


# In[22]:


# perfome two sample t-test with equal variances
stats.ttest_ind(sub1, sub2, equal_var= True)


# In[ ]:





# In[ ]:




