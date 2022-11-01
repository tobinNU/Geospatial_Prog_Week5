#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

df = pd.read_csv('C:\\GIS\\national_register_listed_20220106_MAONLY.csv')

print(df.to_string()) 


# In[31]:


df.head(n=10)


# In[30]:


ax = df['County'].value_counts().plot.bar()


# In[ ]:




