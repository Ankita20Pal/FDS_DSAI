#!/usr/bin/env python
# coding: utf-8

# In[4]:


def bayes_law(p_a, p_b_given_a, p_b_given_not_a):
    not_a = 1 - p_a
    p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
    p_a_given_b = (p_b_given_a * p_a) / p_b
    
    return p_a_given_b

p_a = 0.0002
p_b_given_a = 0.85
p_b_given_not_a = 0.05
result = bayes_law(p_a, p_b_given_a, p_b_given_not_a)
print("P(A/B)=%.3f%%" % (result*100))


# In[3]:


# Calculating P(A/B) given P(A) = 30% , P(not A) = 70% , P(B/A) = 75% , P(congratulation/not spam) = 35%

def bayes_laaw(p_a, p_b_given_a, p_b_given_not_a ):
    # calculating P(B)
    not_a = 1 - p_a
    p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
    
    # calculating P(A/B)
    p_a_given_b = (p_b_given_a * p_a) / p_b
    
    return p_a_given_b

p_a = 0.3
p_b_given_a = 0.75
p_b_given_not_a = 0.35
p_not_a = 0.7

result = bayes_laaw(p_a, p_b_given_a, p_b_given_not_a)
print('P(A/B) = %.3f%%' % (result*100))


# In[ ]:





# In[ ]:




