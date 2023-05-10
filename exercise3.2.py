#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = "hello there"
a.find("there")


# In[2]:


a.find("HELLO")


# In[16]:


file = open("yesno.txt", "r")


# In[17]:


lines = file.readlines()


# In[18]:


file.close()


# In[19]:


print(lines)


# In[20]:


countYes=0
countNo=0


# In[21]:


for line in lines:
    line = line.strip()
    #count
    if line.find("YES") != -1 and len(line)==3:
        countYes+=1
    if line.find("NO") !=1 and len(line)==2:
        countNo+=1
        
        
print("Yes: ",countYes)
print("No: ",countNo)


# In[22]:


print("Michael Lopez")


# In[ ]:




