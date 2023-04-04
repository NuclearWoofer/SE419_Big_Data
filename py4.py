#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [3,10,-1]
print(a)


# In[2]:


a.append(1)


# In[3]:


print(a)


# In[4]:


a.append("Hello")
print(a)


# In[5]:


a.append([1,2])
print(a)


# In[6]:


a.pop()


# In[7]:


print(a)


# In[9]:


a[0]


# In[10]:


print(a[0])


# In[11]:


a[0] = 100
print(a)


# In[12]:


b = ["banana","apple","microsoft"]


# In[13]:


temp = b[0]
b[0] = b[1]
b[1] = temp
print(b)


# In[16]:


fruitlist = ["green", "blue", "yellow"]
i, j = 0, 2
# Swap index i=0 with index j=2
fruitlist[i], fruitlist[j] = fruitlist[j], fruitlist[i]
print(fruitlist)


# In[17]:


print(a[-1])


# In[18]:


a[1:3]


# In[19]:


a[:3]


# In[20]:


a[2:]


# In[23]:


a[0:2] = ["lisa",1.74]
a


# In[24]:


a + ["me",1.79]


# In[25]:


del(a[0])


# In[26]:


a


# In[30]:


x = ["a", "b", "c"]
y = list(x)


# In[31]:


print("Michael Lopez")


# In[ ]:




