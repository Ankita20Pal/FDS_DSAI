#!/usr/bin/env python
# coding: utf-8

# # Seaborn

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[2]:


os.chdir('D:/MSC/FDS_Practical/Data')
cars_data=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
cars_data.size


# In[3]:


cars_data.dropna(axis=0, inplace=True)  # drop null value by row wise, inplace true-->change in original data 
cars_data.size


# In[4]:


cars_data=pd.read_csv('Toyota.csv', index_col=0)
cars_data.head()


# In[5]:


# scatter plot and line plot using regplot

sns.set(style='darkgrid')
sns.regplot(x=cars_data['Age'],y=cars_data['Price'])


# In[6]:


# using regplot with fit_reg

# when we dont want regression line then we use fit_reg=False

sns.regplot(x=cars_data['Age'],y=cars_data['Price'], fit_reg=False)


# In[7]:


# using regplot with marker function --> change the shape 

sns.regplot(x=cars_data['Age'],y=cars_data['Price'], marker='*' ,fit_reg=False)  # instead of o shape , * print


# In[8]:


# using lmplot funtion
#                            ...............                ...........                  ..............
sns.lmplot(x='Age',y='Price',data=cars_data, fit_reg=False, hue='FuelType', legend=True, palette='Set2') #palette --> set of color ,, if we use set2 -> color wll change


# In[9]:


# using displot -- (histogram)

sns.displot(cars_data['Age'])


# In[10]:


# displot using kde

sns.displot(cars_data['Age'] , kde=False)


# In[11]:


# bin function

sns.displot(cars_data['Age'] , kde=False, bins=5)


# In[12]:


# using countplot 

sns.countplot(x='FuelType' ,data=cars_data)


# In[13]:


# using countplot with hue 

sns.countplot(x='FuelType' ,data=cars_data, hue='Automatic')

# ans
# # see the result -->the automatic car only in the petrol type , not in diesel and CNG


# In[14]:


# using crosstab

pd.crosstab(index=cars_data['Automatic'], columns=cars_data['FuelType'], dropna=True)


# In[15]:


sns.boxplot(x=cars_data['FuelType'], y= cars_data['Price'])


# In[16]:


sns.boxplot(x=cars_data['FuelType'], y= cars_data['Price'], hue='Automatic' , data=cars_data)


# In[17]:


f ,(ax_box, ax_hist)=plt.subplots(2,gridspec_kw={'height_ratios':(.15 , .85)})


# In[18]:


f ,(ax_box, ax_hist)=plt.subplots(2,gridspec_kw={'height_ratios':(.15 , .85)})
sns.boxplot(cars_data['Price'], ax=ax_box)
sns.distplot(cars_data['Price'], ax=ax_hist, kde=False)


# # Pairwise Plot

# In[19]:


sns.pairplot(cars_data, kind='scatter' , hue='FuelType', diag_kws={'bw':0.1})
plt.show()


# # Heatmap

# In[20]:


data=np.random.randint(1, 100, size=(10, 10))
print('The data to be plotted: \n')
print(data)


# In[21]:


# using heatmap

hm = sns.heatmap(data=data)
plt.show()


# In[22]:


hm = sns.heatmap(data= data,
                 vmin='30',
                vmax='70')
plt.show()


# In[23]:


# setting the parameter value
cmap='tab20'
center=0

annot= True

hm=sns.heatmap(data=data,  cmap=cmap, annot=annot)

plt.show()

