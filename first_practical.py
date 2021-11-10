#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_dict={"Name":["a","b","c","d","e","f"],
        "age":[20,25,21,38,30,31],
        "Desgnation":["VP","CEO","CEO","MD","HR","MD"]}
import pandas as pd
import numpy as nm
df=pd.DataFrame(my_dict)
df


# In[2]:


df.to_csv('Csv example')
df


# In[3]:


df.to_csv('CSV Ex', index=False)
df_csv=pd.read_csv('CSV Ex')
df_csv


# In[73]:


import pandas as pd
Location="D:/MSC/FDS_Practical/student-mat.csv.csv"
df=pd.read_csv(Location,header=None)
df.head()


# In[ ]:


import pandas as pd
Location="D:/MSC/FDS_Practical/student-mat.csv.csv"
df=pd.read_csv(Location, header=None)
df.head()


# In[20]:


import pandas as pd
Name=["Ankita","soni","suchi","anjali","roshni"]
Grade=[85,80,86,90,89]
bsdegree=[1,0,1,0,1]
msdegree=[1,1,1,0,0]
phddegree=[0,0,0,1,0]
marks=zip(Name,Grade,bsdegree,msdegree,phddegree)
col=['Name','Grade','Bsc','Msc','PhD']
df=pd.DataFrame(data=marks, columns=col)
df


# In[14]:


import pandas as pd
Location="D:/MSC/FDS_Practical/gradedata.xlsx"
df=pd.read_excel(Location)
df.head()


# In[12]:


import pandas as pd
names=['Anu','soni','suchi','ram','shyam']
grades=[85,80,86,84,90]
Gradelist=zip(names,grades)
df=pd.DataFrame(data=Gradelist, columns=['Names','Grades'])

writer=pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# In[3]:


import sqlite3
con=sqlite3.connect('D:/MSC/FDS_Practical/portal_mammals.sqlite')
cur=con.cursor()
for row in cur.execute('select * from species;'):
    print(row)
con.close()


# In[6]:


import sqlite3
con=sqlite3.connect('D:/MSC/FDS_Practical/portal_mammals.sqlite')
cur=con.cursor()
cur.execute('select plot_id from plots where plot_type="Control"')
print(cur.fetchall())
cur.execute('select species from species where taxa="Bird"')
print(cur.fetchone())
con.close()


# In[7]:


import pandas as pd
import sqlite3
con=sqlite3.connect('D:/MSC/FDS_Practical/portal_mammals.sqlite')
df=pd.read_sql_query('select * from surveys',con)
print(df.head())
con.close()


# In[11]:


from pandas import DataFrame
st={'Name':['Ankita','Suchi','Soni','Pushpa','Roshni'],
   'marks':[80,89,88,90,76]}
df=DataFrame(st,columns=['Name','marks'])
print(df)


# In[12]:


import sqlite3
conn=sqlite3.connect('TestDB1.db')
c=conn.cursor()


# In[26]:


c.execute('create table st1(Full Name , Marks)')
conn.commit()


# In[27]:


df.to_sql('st1',conn,if_exists='replace',index=False)
df


# In[30]:


print(c.execute('select Name,max(marks) from std'))


# In[29]:


df=DataFrame(c.fetchall(),columns=['Name','marks'])


# In[21]:


df


# In[74]:


import pandas as pd
import sqlite3 as sql
import os
st_id=['rj01','rj02','rj03','rj04','rj05','rj06']
F_Name=['Ankita','Suchi','Soni','Pushpa','Roshni','Anjali']
L_Name=['Pal','Mishra','Gupta','Pal','Yadav','Sharma']
Dept=['MscIT','BscIT','Mcom','Bsc','MscIT','MscDSAI']
Email=['ankita@gmail.com','suchi@gmail.com','soni@gmail.com','pushpa@gmail.com','roshni@gmail.com','anjali@gmail.com']


# In[75]:


studata=zip(st_id,F_Name,L_Name,Dept,Email)


# In[77]:


df=pd.DataFrame(data=studata,columns=['st_id','F_Name','L_Name','Dept','Email'])
print(df)


# In[47]:


from sqlalchemy import create_engine
df1=df.to_csv('studentdata.csv',index=False,header=True)
df1


# In[48]:


df2=df.to_excel('studentdata2.xlsx',index=False,header=True)
df2


# In[52]:


db_filename=r'studentdata.db'
con=sql.connect(db_filename)
df.to_sql('student',
         con,
         schema=None,
         if_exists='replace',
         index=True,
         index_label=None,
         dtype=None)
con.close()

db_file=r'studentdata.db'
engine=create_


# In[6]:


import numpy as np
import pandas as pd
state=pd.read_csv('D:/MSC/FDS_Practical/US_violent_crime.csv')
state.head()


# In[7]:


def some_fun(x):
    return x*2
state.apply(some_fun)
state.apply(lambda n: n*2)


# In[8]:


state.transform(func=lambda x : x*10 )


# In[10]:


mean_per=state.groupby('State')["Murder"].mean().rename("User_mean").reset_index()
print(mean_per)


# In[11]:


mer=state.merge(mean_per)
mer


# In[12]:


#checking for missing values
print(state.isnull().sum())


# # random

# In[2]:


import pandas as pd 
import numpy as np
rows=['r1','r2','r3','r4','r5']
cols=['c1','c2','c3','c4','c5']
data=np.random.randint(0,100, size=(5,5))
df=pd.DataFrame(data, columns=cols, index=rows)
df


# In[3]:


df.iloc[4,2]


# In[4]:


#Deling with 0 and Nan Value

df.iloc[3,3]=0
df.iloc[1,2]=np.nan
df.iloc[4,0]=np.nan
df['c6']=0
df['c7']=np.nan


# In[5]:


df


# In[14]:


df.iloc[3,4]


# In[15]:


# print row and column which dont have a zero value

df.loc[:, df.all()]


# In[16]:


# select those column which have atleast one non-zero number(1-9)----> using df.any() 
    
df.loc[:, df.any()]


# In[18]:


# print those col which have atleast one NaN value ----> using isnull().any()

df.loc[:,df.isnull().any()]


# In[19]:


df.loc[:, df.isnull().all()]


# In[20]:


# print those col which dont have NaN(null) value ------> using notnull().all()

df.loc[:, df.notnull().all()]


# In[21]:


df.loc[:,df.notnull().any()]


# In[25]:


# delet all col which have all NaN(null) value -----> using dropna()

df.dropna(how='all', axis=1)


# In[27]:


# delet all col which have atleast one NaN(null) value

df.dropna(how='any', axis=1)


# In[28]:


# rename the NaN value with average value of that rows in particular col

df.fillna(df.mean())


# In[29]:


# rename the nan value with maximum value of those rows

df.fillna(df.max())


# In[30]:


df.fillna(df.sum())


# In[32]:


def fun(x):
    return x*2
df.apply(fun)

#df.apply(lambda x: x*2)


# In[33]:


def fun(x):
    return x+2
df.apply(fun)

#df.apply(lambda x: x+2)


# In[36]:


# create a new col, with multiplication of col4

df['new_col']=df['c4'].apply(lambda x: x*2)
df


# In[48]:


# example

import pandas as pd
import numpy as np
ex=pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]), columns=['a', 'b','c'])
ex


# In[53]:


ex.apply(lambda x: x* 10)


# In[55]:


import pandas as pd
import numpy as np
import random
data=pd.DataFrame({'C':[random.choice(('a', 'b', 'c')) for i in range(100)],
                  'B':[random.randint(1,10) for i in range(100)],
                  'A':[random.randint(1,10) for i in range(100)]
                  })
data


# In[57]:


g=data.groupby('C')['A'].mean()
g


# In[62]:


GrpBy=data.groupby('C')['A'].mean().rename('D').reset_index()
GrpBy


# In[63]:


data.merge(GrpBy)


# In[64]:


# example

import pandas as pd
import numpy as np
airline=pd.read_csv('D:/MSC/FDS_Practical/airline_stats.csv.csv')
airline.head()


# In[65]:


airline.isnull().sum() #print total number of missing value or null value 


# In[67]:


airline.fillna(airline.mean(),inplace=True) #replace null value with mean 


# In[68]:


airline.isnull().sum()


# In[69]:


GP=airline.groupby('pct_atc_delay')['pct_weather_delay'].mean().rename('user').reset_index()
GP


# In[70]:


airline.merge(GP)


# In[71]:


airline.apply(lambda x:x*2)


# In[ ]:




