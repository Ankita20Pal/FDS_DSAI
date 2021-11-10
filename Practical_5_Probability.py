#!/usr/bin/env python
# coding: utf-8

# # Practical_5 : Probability

# In[34]:


# probability of getting 3 when a die is rolled

ns = 6 # n(s)={1,2,3,4,5,6}
na = 1 # n(A)={3}
pa = na/ns # P(A)
print('Probability of getting 3 is',pa)


# Q) Pobability of atleast getting one head when a coin is tossed thrice 

# In[35]:


ns = 8 # n(s) = {HHH, HHT, HTH, TTH, THT, HTT, TTT}
na =7  #n(A) = {HHH, HHT, HTH, TTH, THT, HTT}
pa = na/ns #P(A)
print('Probability of getting atleast 1 head',pa)


# In[36]:


# A glass jar contains 5 red, 3 blue, and 3 green jelly beans. if a jelly bean is chosen at random from the jar ,
# what is the probability that it is not blue?

ns = 10 # n(s) = {5 red, 3 blue, 3 green}
na =7  #n(A) = {5 red, 3 green}
pa = na/ns #P(A)
print('Probability of getting not blue jelly beans is :',pa)


# In[37]:


# if the probability that person A will be alive in 20 years is 0.7 and the probabilty that person B will be alive in 
# 20 years is 0.5, what is the probabilty that they will both be alive in 20 years?

P = 0.7 * 0.5
print('Probability that they will be alive after 20 years is :',P)


# In[38]:


def event_probability(n, s):
    return n/s


# In[39]:


# A fair die is tossed twice. Find the probability of getting a 4 or 5 on the first toss and a 1,2 or 3 in the second toss.

pa = event_probability(2, 6) # probability of getting a 4 or 5
pb = event_probability(3, 6) # probability of getting 1, 2 or 3

P = pa*pb

print('Probability of getting a 4 or 5 on the first toss and a 1, 2 or 3 in the secon toss is :',P)


# In[40]:


# A bag contains 5 white marbles, 3 black marbles and 2 green marbles. In each draw, a marble is drawn from the bag 
# and not replaced. In three draws, find the probability of obtaining white, black and green in that order.

pw = event_probability(5, 10) 
pb = event_probability(3, 9) 
pg = event_probability(2, 8) 

print('Probability of obtaining white, black and green in that order is :', (pw*pb*pg))


# In[41]:


# sample space
cards = 52

# calculate the probability of drawing a heart or a club

hearts = 13
clubs = 13
heart_or_club = event_probability(hearts, cards) + event_probability(clubs, cards)

print(heart_or_club)


# In[42]:


# calculate the probability of drawing an ace, king or a green

aces = 4
kings = 4
queens = 4
ace_king_or_queen = event_probability(aces, cards) + event_probability(queens, cards) + event_probability(kings, cards)

print(ace_king_or_queen)


# In[43]:


# calculate the probability of drawing a heart or an ace (Union)

hearts = 13
aces = 4
ace_of_hearts = 1
heart_or_ace = event_probability(hearts, cards) + event_probability(aces, cards) - event_probability(ace_of_hearts, cards)

print(round(heart_or_ace, 1))


# In[44]:


# calculate the probability of drawing red cards or a face cards

red =26
face = 12
red_face_card = 6
red_or_face = event_probability(red, cards) + event_probability(face, cards) - event_probability(red_face_card, cards)

print(round(red_or_face, 1))


# In[45]:


# Probability of not getting 5 when a fair die is rolled

ns = 6 # n(s)={1,2,3,4,5,6}
na = 1 # n(A)={5}
pa = na/ns

print('Probability of not getting 5 is :',1-pa)


# In[46]:


import pandas as pd
import numpy as np

df = pd.read_csv('D:/MSC/FDS Practical/Data/student-mat.csv.csv')
df.head(3)


# In[47]:


len(df)


# In[48]:


df['grade_A'] = np.where(df['G3']*5 >= 80, 1, 0)


# In[49]:


df['high_absenses'] = np.where(df['absences'] >= 10, 1, 0)


# In[50]:


df.head(3)


# In[51]:


df['count'] = 1


# In[52]:


df.head()


# In[53]:


df = df[['grade_A','high_absenses','count']]
df.head()


# In[54]:


final = pd.pivot_table(df, 
                       values ='count', 
                       index = ['grade_A'], 
                       columns =['high_absenses'],
                       aggfunc = np.size, 
                       fill_value = 0
                      )


# In[55]:


print(final)
print(type(final))


# In[56]:


# calcualte the probability the student will get grade A given that missing 10 or more classess

#P(A) = (35+5)/(277+78+35+5) = 0.1012658  # P(A) grade of 80%
#P(B) = (78+5)/(277+78+35+5) = 0.210      # P(B) missing 10 or more classes
#P(A or B) = 5/(277+78+35+5) = 0.0126

#P(A|B) = P(A or B) / P(B) = 0.060
#p(A|B)

total = final.iloc[0,0] + final.iloc[0,1] + final.iloc[1,0] + final.iloc[1,1] 

a = final.iloc[1].sum()
Pa = event_probability(a, total)
print('Probability of student getting grade A is :',Pa)

b = final[1].sum()
Pb = event_probability(b, total)
print('Probability of student will get high absenses is :',Pb)

a_or_b = final.iloc[1,1] 
Pa_or_Pb = event_probability(a_or_b, total)
print(Pa_or_Pb)

Pa_Pb = event_probability(Pa_or_Pb, Pb)
print('Probability of student getting grade A with high absenses is :',Pa_Pb)


# # Combinatorics : Permutation , Variation &  Combination

# In[31]:


import itertools
from itertools import product
box = ['g','b']
perm = []
for p in itertools.product(box, repeat = 2):
    perm.append(p)
perm


# In[ ]:


import itertools
from itertools import product
box1 = ['g','b','y']
perm = []
for p in itertools.product(box1, repeat = 3):
    perm.append(p)
perm


# In[ ]:


import itertools
box = ['g','b']
perm = itertools.permutations(box)

for i in list(perm):
    print(i)


# In[ ]:


import itertools
box = ['g','b','y']
perm = itertools.permutations(box)

for i in list(perm):
    print(i)


# # variation 

# In[ ]:


box = ['g','b','y']
perm = []
for p in itertools.product(box, repeat = 2):
    perm.append(p)

perm


# In[ ]:


box = ['g','b','y']
perm = itertools.permutations(box, 2)

for i in list(perm):
    print(i)


# # Combination

# Combination with repetitions : C(n, k) = (n+k-1)! / k!(n-1)!

# In[ ]:


from itertools import combinations_with_replacement

box = ['g','b']
comb = combinations_with_replacement(box, 2)

for i in list(comb):
    print(i)


# In[ ]:


from itertools import combinations_with_replacement

box = ['g','b','y','w']
comb = combinations_with_replacement(box, 2)

for i in list(comb):
    print(i)


# without repetitions : 
#     
#     C(n, k) = n! / k!(n-k)!

# In[ ]:


from itertools import combinations

box = ['g','b','y']
comb = combinations(box, 2)

for i in list(comb):
    print(i)


# In[ ]:




