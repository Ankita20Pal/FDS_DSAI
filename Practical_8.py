#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.read_csv('D:/MSC/FDS Practical/Data/stats.csv')


# In[7]:


df


# In[16]:


# mean
m=df['Salary'].mean()
m


# In[17]:


# sum of salaries
sum1=df['Salary'].sum()
sum1


# In[18]:


#maximum
max1=df['Salary'].max()
max1


# In[31]:


#minimum
min1=df['Salary'].min()
min1


# In[32]:


#Total Count
cnt=df['Salary'].count()
cnt


# In[14]:


# median 
median=df['Salary'].median()
median


# In[15]:


# mode
mode1=df['Salary'].mode()
mode1


# In[ ]:


countrywise_sum=df.groupby(['Country'])['Salary'].sum()
countrywise_sum


# In[8]:


countrywise_count=df.groupby(['Country']).count()
countrywise_count


# Measure of variability

# In[11]:


# variance of salaries
var1=df['Salary'].var()
var1


# In[10]:


# standard deviation
std1=df['Salary'].std()
std1


# Measure of Symmetry

# In[12]:


skew1=df.skew(axis=0, skipna=True)
skew1


# In[19]:


# The skewness is positive so x will have right side tail.


# # Covariance and Correlation

# In[20]:


bw=pd.read_csv('D:/MSC/FDS Practical/Data/BirthWeight.csv')
bw


# In[22]:


bw.set_index('Infant ID', inplace=True)
bw.head()


# In[23]:


bw.cov() 


# In[24]:


bw.corr()


# In[30]:


print(bw.corr(method='pearson'))

print('\nExplanation of result : ')
print('\n# Covariance indicates that there is correlation exists between two')
print('# Correlation coefficiant of 0.818 indicates the relation between two is positive')


# In[ ]:




