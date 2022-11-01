#!/usr/bin/env python
# coding: utf-8

# In[8]:


def nested_sum(t):
    nested_sum = 0
    for n in t:
        nested_sum += sum(n)
    return nested_sum


# In[9]:


t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)


# In[ ]:




