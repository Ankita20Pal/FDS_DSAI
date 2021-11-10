#!/usr/bin/env python
# coding: utf-8

# # Practical 2 :-  Data Visualization

# In[3]:


import matplotlib.pyplot as plt

fig,ax=plt.subplots()

x=[2,4,6,6,9,2,7,2,6,1,8,4,5,9,1,2,3,7]
y=[7,8,2,4,6,4,9,5,9,3,6,7,2,4,6,7,1,9]

ax.scatter(x,y)


# In[24]:


import pandas as pd

iris=pd.read_csv('D:/MSC/FDS_Practical/Data/iris.csv',index_col=0)

print(iris.head())


# In[30]:


import matplotlib.pyplot as plt
fig, ax=plt.subplots()

ax.scatter(iris['SepalLengthCm'],iris['SepalWidthCm'])

ax.set_title('Iris Dataset')

ax.set_xlabel('SepalLengthCm')
ax.set_ylabel('SepalWidthCm')


# # Line chart

# In[8]:


import pandas as pd
import numpy as np

x=range(1,6)
y=np.random.randint(1,20,5)
plt.plot(x,y)                      # plot() --> plot a graph of line chart

plt.xticks(x)   # print the value of x in x axis 
plt.yticks(y)   # print the value of y in y axis


# In[13]:


import matplotlib.pyplot as plt

fig,ax=plt.subplots()

x=[2,4,6,6,9,2,7,2,6,1,8,4,5,9,1,2,3,7]
y=[7,8,2,4,6,4,9,5,9,3,6,7,2,4,6,7,1,9]

ax.plot(x,y)


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

fig,ax=plt.subplots()


df=pd.DataFrame({
    'name':['an','ak','ap','aj','pr','pl','dp'],
    'age':[20,19,22,19,18,20,21],
    'gender':['m','f','m','m','f','m','m'],
    'state':['sp','sa','sj','sd','so','se','sr'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
    
})
# gca stands for 'get current axis'
ax=plt.gca() 
df.plot(kind='line', x='name', y='num_children', ax=ax)
df.plot(kind='line', x='name', y='num_pets', color='red', ax=ax)


# In[ ]:


import pandas as pd
iris=pd.read_csv('D:/MSC/FDS_Practical/Data/iris.csv', index_col=0)
print(iris.head())


# In[32]:


columns = iris.columns.drop(['Species'])
x_data = range(0, iris.shape[0])
fig, ax = plt.subplots()
for column in  columns:
    ax.plot(x_data, iris[column], label=column)

ax.set_title('Iris Dataset')
ax.legend()


# # Histogram

# In[33]:


import matplotlib.pyplot as plt
fig, ax=plt.subplots()
ax.hist(iris['SepalLengthCm'])
ax.set_title('Iris')
ax.set_xlabel('SepalLengthCm')
ax.set_ylabel('Frequency')


# In[ ]:





# # Bar chart

# In[34]:


wine_reviews=pd.read_csv('D:/MSC/FDS_Practical/Data/winemag-data-130k-v2.csv',index_col=0)
print(wine_reviews.head())


# In[36]:


fig , ax=plt.subplots()
data=wine_reviews['points'].value_counts()
pt=data.index
frequency=data.values
ax.bar(pt, frequency)
ax.set_title('Wine review scores')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')


# In[39]:


wine_reviews['points'].value_counts().sort_index().plot.bar()


# In[40]:


wine_reviews.groupby('country').price.mean().sort_values(ascending=False)[:6].plot.bar()


# In[17]:


import numpy as np
import matplotlib.pyplot as plt

objects=('Python','C++','Java','Pearl','Scala','Lisp')

y_pos=np.arange(len(objects))

performance=[10,8,6,4,2,1]

plt.bar(y_pos, performance , width=0.5, align='edge' ,alpha=0.7 , color=['r','r','g','g','b','b']) 

plt.xticks(y_pos, objects)

plt.ylabel('Usage')
plt.xlabel('Programming Language')

plt.title('Programming Language Usage')


# In[49]:


import matplotlib.pyplot as plt
plt.figure(figsize= (12,7))
countries=['USA','Brazil','Spain','UK','India']
totalDeapth=[112596, 37312,5971,27136.40597,7449]


plt.bar(countries,  totalDeapth, width=0.9, align='center', color='cyan',edgecolor='red' )
i=1.0
j=2000
for i in range(len(countries)):
    plt.annotate(totalDeapth[i], (-0.1+i , totalDeapth[i]+j))
plt.legend(labels=['Total Deapth'])
plt.title('Bar plot representing the total deaths by the top 6 countries due to coronavirus')
plt.xlabel('Countries')
plt.ylabel('Deapth')
plt.savefig('1BarPlot.png')
plt.show() # dsiplaying the bar 

21 sep, 2021 - Tuesday
# In[5]:


# using barh 

import matplotlib.pyplot as plt

plt.figure(figsize=[14,10])

plt.barh(['as','ac','ad','af','ar'], [202649,710887,476658,288797,287399], label="Danger Zone" ,color='r')
plt.barh(['in','it','pa','ge','ir'], [265928,235278,199696,186205,173832], label="Not safe zone" ,color='g')
         
plt.legend()
         
plt.xlabel('Total Cases')
plt.ylabel('Countries')
         
plt.title('Top ten countries most affected by coronavirus')

plt.savefig('2BarPlot.png')
plt.show()


# In[8]:


# using groupby with unstack, stacked

import pandas as pd
df=pd.DataFrame({
    'name':['ankita','ar','ap','al','ae','am','an'],
    'age':[23,28,22,19,24,25,20],
    'gender':['f','m','f','m','m','f','m'],
    'state':['cal','dc','cal','dc','cal','tex','tex'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
    

})

df.groupby(['state','gender']).size().unstack().plot(kind='bar',stacked=True)


# In[9]:


df.groupby(['gender','state']).size().unstack().plot(kind='bar',stacked=True)


# In[13]:


# using plot

import matplotlib.pyplot as plt
import pandas as pd

data={'country':['USA','Can','Ger','UK','France'],
     'GDP-Per_Capita':[45000,42000,52000,49000,47000],
     'Income_per_capita':[4000,5000,7000,55000,60000]}

df=pd.DataFrame(data)
df.plot(x='country',y=['GDP-Per_Capita','Income_per_capita'], kind='bar')


# In[57]:


import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=[15,10])

totalDeath=[113055,37312,5971,7473,33694]
totalRecovery=[773480,347973,230688,129095,166584]
activecase=[1139958,347973,239999,129360,34730]
country=['in','cal','bra','it','ru']
X=np.arange(len(totalDeath))

plt.bar(X, totalDeath, color='black', width=0.25)
plt.bar(X+0.25, totalRecovery, color='g', width=0.25)
plt.bar(X+0.5, activecase, color='black', width=0.25)

plt.legend(['Total Deaths','Total Recovery','Active cases'])

plt.xticks([i +0.25 for i in range(5)] , country)

plt.xlabel('Countries')
plt.ylabel('cases')
         
plt.title('Bar plot representing the total deaths, total recovery, and active cases country wise')

plt.savefig('2BarPlot.png')
plt.show()


# # Pie Chart

# In[26]:


# using plot.pie

import matplotlib.pyplot as plt
import pandas as pd

data={'task':[300,500,700],
     "task type":['task pending','tasks ongoing','tasks completed']}
df=pd.DataFrame(data)
df.set_index('task type', inplace=True)

df.plot.pie(y='task', figsize=(5,5) , autopct='%1.1f%%', startangle=90)


# In[34]:


# using explode in pie

import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

labels=['civil','electrical','mechanical','chemical']
sizes=[15,30,45,10]

explode=(0.1, 0.1, 0.1, 0.4)  # see the fig-----red part 

fig,ax=plt.subplots()
ax.pie(sizes, 
      explode=explode,
      labels=labels,
      autopct='%1.1f%%',
       shadow=True,
       startangle=90)

ax.axis('equal')
ax.set_title('Engineering Diciplines')


# # subplots

# In[31]:


plt.figure(figsize=(20,10))  # in 1 figure , display the 4 different types of graph

plt.subplot(2,2,1)
plt.bar(range(1,6), np.random.randint(1,20,5))
plt.title('2,2,1')

plt.subplot(2,2,2)
plt.bar(range(1,6), np.random.randint(1,20,5))
plt.title('2,2,2')

plt.subplot(2,2,3)
plt.scatter(range(1,6), np.random.randint(1,20,5), s=100,color='r')
plt.title('2,2,3')

plt.subplot(2,2,4)
plt.plot(range(1,6), np.random.randint(1,20,5), marker='o', color='g',linestyle='--')
plt.title('2,2,4')


# In[32]:


# display  bar, scatter and plot in a single graph 

plt.bar(range(1,6), np.random.randint(1,20,5),width=0.5)
plt.scatter(range(1,6), np.random.randint(1,20,5), s=100,color='r')
plt.plot(range(1,6), np.random.randint(1,20,5), marker='o', color='g',linestyle='--')

