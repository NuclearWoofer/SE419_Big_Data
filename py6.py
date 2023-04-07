#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dictionaries
d = {}
#d = {"George": 24, "Tom": 32}


# In[2]:


d["George"] = 24


# In[3]:


d["Tom"]=32
d["Jenny"]=16


# In[4]:


print(d["George"])


# In[5]:


print(d["Alice"])


# In[6]:


d["George"]=35
print(d["George"])


# In[7]:


d[10]=100
print(d[10])


# In[8]:


print(d)


# In[10]:


for key, value in d.items():
    print("key:",key)
    print("value:",value)
    print(" ")


# In[11]:


s={}


# In[12]:


s["AL"]="Alabama"
print(s["AL"])


# In[13]:


s["AL"]="Alabama"
s["AK"]="Alaska"
s["AZ"]="Arizona"
s["AR"]="Arkansas"
s["CA"]="California"
s["CO"]="Colorado"
s["CT"]="Connecticut"
s["DE"]="Deleware"
s["FL"]="Florida"
s["GA"]="Georgia"


# In[14]:


for key, value in s.items():
    print("Abbreviation: ",key)
    print("Full State Name: ",value)
    print(" ")


# In[15]:


print("Michael Lopez")


# In[ ]:




