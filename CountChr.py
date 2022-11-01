#!/usr/bin/env python
# coding: utf-8

# In[3]:


def CountChr():
    doc = open("C:\\Users\\ntobin\\Desktop\\GIS\\words.txt")
    for l in doc:
        words = l.strip()
        if len(words) > 19:
            print(words)


# In[4]:


CountChr()


# In[ ]:




