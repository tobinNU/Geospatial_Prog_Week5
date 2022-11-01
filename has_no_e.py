#!/usr/bin/env python
# coding: utf-8

# In[21]:


def has_no_e():
    doc = open("C:\\Users\\ntobin\\Desktop\\GIS\\words.txt")
    for l in doc:
        words = l.strip()
        if words.find("e") == -1:
            print("Has no E:     ", words)


# In[22]:


has_no_e()


# In[23]:


def has_no_e_percent():
    doc = open("C:\\Users\\ntobin\\Desktop\\GIS\\words.txt")
    words_count = 0
    count = 0
    for l in doc:
        words_count = words_count + 1
        words = l.strip()
        if words.find("e") == -1:
            print("Has no E:      ", words)
            count = count + 1
    words_no_e_perc = (count/words_count) * 100
    print(words_no_e_perc, "% of words in file")


# In[24]:


has_no_e_percent()


# In[ ]:




