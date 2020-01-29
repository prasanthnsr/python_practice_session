#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Tuple - is a immutable collection

# Tuple should be defined within - ()

dimentions = (200,20)
print(dimentions)


# In[4]:


type(dimentions)


# In[5]:


# Modifying tuple not possible as tuple is immutable

dimentions[0] = 100


# In[28]:


# Adding / deleting delment form a tuple not possible as tuple is immutable

student_tuple = ('a', 'b', 'c', 'd', 'e')
student_tuple[0] = 'xyz'


# In[7]:


print(dimentions[0])


# In[29]:


# Clear Tuple not possible as tuple is immutable

student_tuple = ('a', 'b', 'c', 'd', 'e')
student_tuple.clear()
student_tuple


# In[1]:


student_tuple = ('a', 'b', 'c', 'd', 'e')
print(student_tuple)


# In[2]:


student_tuple


# In[5]:


print(student_tuple[2])


# In[9]:


# Loops with Tuple

student_tuple = ('a', 'b', 'c', 'd', 'e')
for x in student_tuple:
    print(x)


# In[11]:


student_tuple = ('a', 'b', 'c', 'd', 'e')
for x in student_tuple:
    print(f"Student Name - {x}")


# In[18]:


# Check if specific item present in the tuple

student_tuple = ('a', 'b', 'c', 'd', 'e')
if "x" in student_tuple:
    print("x - is a student")
else:
    print("x - is not a student")


# In[20]:


student_tuple = ('a', 'b', 'c', 'd', 'e')
if "e" in student_tuple:
    print("e - is a student")
else:
    print("e - is not a student")


# In[27]:


# Length of the tuple

student_tuple = ('a', 'b', 'c', 'd', 'e')
print(f"Length of the student_tuple is -: {len(student_tuple)}")


# In[34]:


# Delete a touple

student_tuple = ('a', 'b', 'c', 'd', 'e')
del(student_tuple)
student_tuple


# In[35]:


# Tuble creation using - Tuble Constructor

employee_tuple = tuple(('X','Y','Z'))
employee_tuple


# In[37]:


# Count of occarance of a specific element in tuple - count()

dept_tuple = tuple((10, 20, 30, 40, 50, 40, 30, 20, 10))
count_of_dept_10 = dept_tuple.count(10)
count_of_dept_10


# In[43]:


count_of_dept_50 = dept_tuple.count(50)
print(f"50 occared {count_of_dept_50} times")


# In[46]:


count_of_dept_100 = dept_tuple.count(100)
print(f"100 occared {count_of_dept_100} times")


# In[47]:


# Index of occarance of a specific element in tuple - index()

index_of_50 = dept_tuple.index(50)
index_of_50


# In[48]:


index_of_50 = dept_tuple.index(50)
print(f"Index of 50 is - {index_of_50}")


# In[56]:


index_of_50 = dept_tuple.index(50)
print(f"50 is at {index_of_50}th index in tuple dept_tuple")


# In[53]:


index_of_100 = dept_tuple.index(100)
print(f"10 is at {index_of_100}th place in tuple dept_tuple")


# In[54]:


index_of_100 = dept_tuple.index(100)
if(index_of_100):
    print("100 present at the Tuple - dept_tuple")
else:
    print("100 NOT present at the Tuple - dept_tuple")


# In[ ]:





# In[ ]:




