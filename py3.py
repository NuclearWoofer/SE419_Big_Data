#!/usr/bin/env python
# coding: utf-8

# In[1]:


def function():
    print("hi")
    print("hi 2")
print("This is outside the function")


# In[2]:


function()


# In[3]:


def function2(x):
    return 2 * x


# In[4]:


a = function2(3)
print(a)


# In[5]:


d = function2()


# In[6]:


def function3(x, y):
    return x + y


# In[7]:


e = function3(1,2)
print(e)


# In[8]:


def function4(some_argument):
    print(some_argument)
    print("weeee")


# In[9]:


function4("hello")
function4(55)


# In[10]:


#BMI Calculator Function
name1 = "Jean"
height_m1 = 2
weight_kg1 = 90

name2 = "Jean's Sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "Jean's Brother"
height_m3 = 2.5
weight_kg3 = 160


# In[11]:


def bmi_calc(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("BMI: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight."
    else:
        return name + "is overweight"


# In[12]:


result1 = bmi_calc(name1, height_m1, weight_kg1)


# In[13]:


print(result1)


# In[46]:


def conv_calc(miles):
    km = miles * 1.6
    return km
result = conv_calc(55)
print(55, "miles in kilometers is: ", result, "km")


# In[47]:


print("Michael Lopez")


# In[ ]:




