#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = 3
b = 2
if a < b:
    print("a is less than b")
print("Not sure if a is less than b")


# In[2]:


a = 1
b = 2
if a < b:
    print("a is less than b")
    print("a is def less than b")
print("Not sure if a is less than b")


# In[5]:


c = 5
d = 4
if c < d:
    print("c is less than d")
else:
    print("c is NOT less than d")
    print("I don't think c is less than d")
print("Outside the if block.")


# In[8]:


g = 7
h = 9
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")


# In[11]:


name = "Larry"
height_m = 2
weight_kg = 110

bmi = weight_kg / (height_m ** 2)
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")


# In[14]:


print("You can print from the same line using a comma: ", (name), "is overweight")


# In[15]:


print("Michael Lopez")


# In[ ]:




