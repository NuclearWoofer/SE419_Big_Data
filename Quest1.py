#!/usr/bin/env python
# coding: utf-8

# In[11]:


# taking user input
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))

# compare A, B, and C to find the largest number
if A > B and A > C:
    largest = A
    if B > C:
        middle = B
        smallest = C
    else:
        middle = C
        smallest = B
elif B > A and B > C:
    largest = B
    if A > C:
        middle = A
        smallest = C
    else:
        middle = C
        smallest = A
else:
    largest = C
    if A > B:
        middle = A
        smallest = B
    else:
        middle = B
        smallest = A

# print the result
print("The numbers in descending order are:", largest, middle, smallest)


# In[9]:


#results are as follow:
# A - B - C | OUTPUT | YOUR OUTPUTS
#-------------------------------------
# 1 - 2 - 3 | 3,2,1 | 3, 2, 1
# 1 - 3 - 2 | 3,2,1 | 3, 2, 1
# 2 - 1 - 3 | 3,2,1 | 3, 2, 1
# 2 - 3 - 1 | 3,2,1 | 3, 2, 1
# 3 - 1 - 2 | 3,2,1 | 3, 2, 1
# 3 - 2 - 1 | 3,2,1 | 3, 2, 1
#-------------------------------------


# In[10]:


print("Michael Lopez")


# In[ ]:




