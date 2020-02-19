#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# NumPy Mathematical Functions

array_sum = np.sum([10, 20])
array_sum


# In[3]:


a, b, c = 10,20,30


# In[4]:


a


# In[5]:


b


# In[6]:


c


# In[7]:


# Sum without axis - sum of all elements

abc = np.sum([a,b,c])
abc


# In[10]:


np.sum([[10, 20],[50, 60]])


# In[11]:


# Sum with axis=0 - sum of corresponding elements / Col wise sum

np.sum([[10, 20],[50, 60]], axis=0)


# In[12]:


# Sum with axis=1 - adding elements within array / sum of emements group by array / Row wise sum

np.sum([[0, 2],[0, 6]], axis=1)


# In[ ]:


np_a = [1, 2, 3]
np_b = [4, 5, 6]


# In[18]:


# Sum of Arrays without axis - sum of all elements

a_plus_b = np.sum([np_a, np_b])
a_plus_b


# In[17]:


# Sum of Arrays with axis=0 - sum of corresponding elements / Col wise sum

a_plus_b_axis_0 = np.sum([np_a, np_b], axis=0)
a_plus_b_axis_0 


# In[19]:


# Sum of Arrays with axis=1  - adding elements within array / sum of emements group by array / Row wise sum

a_plus_b_axis_1 = np.sum([np_a, np_b], axis=1)
a_plus_b_axis_1 


# In[23]:


# Substraction of Arrays - Col wise minus

b_minus_a = np.subtract(np_b, np_a)
b_minus_a


# In[27]:


# Subtract doesn't support - axis paramete

b_minus_a = np.subtract(np_b, np_a, axis=0)
b_minus_a


# In[25]:


# Multiplication of Arrays - Col wise multiplication

a_multiplys_b = np.multiply(np_a, np_b)
a_multiplys_b


# In[28]:


# Multiplication doesn't support - axis paramete

a_multiplys_b_axis_0 = np.multiply(np_a, np_b, axis=0)
a_multiplys_b_axis_0


# In[30]:


# Division of Arrays - Col wise division

b_divide_a = np.divide(np_b, np_a)
b_divide_a


# In[31]:


# Division doesn't support - axis paramete

b_divide_a_axis_0 = np.divide(np_b, np_a, axis=0)
b_divide_a_axis_0


# In[38]:


angles = [0, 30, 45, 60, 90]


# In[39]:


print(np.sin(angles))


# In[40]:


print(np.cos(angles))


# In[41]:


print(np.tan(angles))


# In[43]:


# Array Comparision - Element wise

aa = np.array([1,2,3])
bb = np.array([1,2,3])
cc = np.array([1,2,9])


# In[44]:


np.equal(aa,bb)


# In[45]:


np.equal(aa,cc)


# In[46]:


# Array Comparision - Array wise

np.array_equal(aa,bb)


# In[47]:


np.array_equal(aa,cc)


# In[49]:


# Aggregrate Functions - works on single array

aaa = np.array([1,2,4])


# In[50]:


print(np.sum(aaa))


# In[51]:


print(np.min(aaa))


# In[52]:


print(np.max(aaa))


# In[53]:


print(np.mean(aaa))


# In[54]:


print(np.median(aaa))


# In[55]:


# Correlation Coefficient

print(np.corrcoef(aaa))  


# In[56]:


# Standard Deviation

print(np.std(aaa))


# In[58]:


array_a = np.array([[1,2,3],[4,5,6]])
array_b = np.array([[3,4,5],[5,6,7]])


# In[59]:


print(array_a)


# In[60]:


print(array_b)


# In[63]:


# Aggregrate Function - Sum - without axis

print(np.sum([array_a, array_b]))


# In[64]:


# Aggregrate Function - Sum - with axis=0
 
print(np.sum([array_a, array_b], axis=0))


# In[65]:


# Aggregrate Function - Sum - with axis=1
 
print(np.sum([array_a, array_b], axis=1))


# In[ ]:


# Arrays with concept of Broadcasting


# In[ ]:




