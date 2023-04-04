#!/usr/bin/env python
# coding: utf-8

# In[1]:


#loops
a = ["banana","apple","microsoft"]


# In[2]:


print(a[0])
print(a[1])
print(a[2])


# In[3]:


for element in a:
    print(element)
    


# In[4]:


for element in a:
    print(element)
    print(element)


# In[5]:


b = [20,10,5]
for e in b:
    print(e)


# In[6]:


b = [20,10,5]
total = 0
for e in b:
    total = total + e
print(total)


# In[7]:


range(1,5)


# In[30]:


#calculate the sum of 1 to 100 but excluding he number 100
#the sum would normally be 5050, since the range is not 1, 101 to incude 100, this is what i came up with.
sum = 0 
for i in range(1,100):
    sum += i
print(sum)


# In[31]:


list(range(1,5))


# In[32]:


c = list(range(1,5))
print(c)


# In[33]:


for i in range(1,5):
    print(i)


# In[34]:


print(list(range(1,8)))


# In[35]:


total3 = 0
for i in range(1,8):
    if i % 3 == 0:
        total3 += i
print(total3)


# In[39]:


total4 = 0
for i in range(1, 100):
    if(i % 3 == 0 and i % 5 == 0):
        total4 += i
print(total4)


# In[40]:


print("Michael Lopez")


# In[ ]:




