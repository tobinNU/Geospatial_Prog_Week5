#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cumsum(t):
    cum_sum = 0
    hold = []
    for n in t:
        cum_sum += n
        hold.append(cum_sum)
    return hold


# In[2]:


t = [1, 2, 3]
cumsum(t)

