#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy # ! - invoking operation from cmd (terminal)')


# In[13]:


get_ipython().system('pip install numpy --upgrade pip')


# In[2]:


get_ipython().system('pip install numpy --upgrade')


# In[3]:


# Numpy - Numerical computing library / package, Numpy suppors - Multi-Dimentioanl Arrays

import numpy as np # np is alias for numpy


# In[2]:


array_one = np.array[1,2,3,4,5]
array_one


# In[3]:


type(array_one)


# In[28]:


# Creating NumPy Array from Python List

a_1 = np.array([1, 2, 3])
print(a_1)


# In[29]:


# Creating NumPy Array from Python Set

a_2 = np.array((1, 2, 3))
print(a_2)


# In[31]:


# Edit NumPy array like in List

a_1[2] = 4
a_1


# In[ ]:


# Difference between - List & Array - which is optimized

# array is much more optimized way to operations

# reason - vectarization


# In[4]:


numbers = [1,2,3,4,5]
array_two = np.array(numbers)
array_two


# In[5]:


array_of_zeros = np.zeros((3,4)) # Datatype of array by default consider as Floats
array_of_zeros


# In[10]:


array_of_ones = np.ones((3,4))
array_of_ones


# In[11]:


# Converting float array to int - include int16 / int32

array_of_ones_int = np.ones((3,4), dtype=np.int16)
array_of_ones_int


# In[6]:


# Giving Range through arrange()

np.arange(1,11)


# In[9]:


# Print only even number betwen 1 & 30 from an array

np.arange(2,31,2)


# In[11]:


# To know the dimention of the array - shape

e = np.array([(1,2,3),(4,5,6)])
e


# In[12]:


e.shape


# In[33]:


x = np.array([(1,2,3),(4,5,6),(7,8,9)])
x


# In[45]:


# Displaying a specific row 

x[0,:]


# In[41]:


# Displaying a specific col 

x[:,1]


# In[39]:


# Displaying a col 

x[1:]


# In[14]:


x.shape


# In[17]:


a = np.arange(1,16)
a


# In[19]:


a.shape # 1 d array


# In[6]:


b = np.arange(1,9)
b


# In[22]:


b.shape # 1 d array


# In[24]:


# Reshaping array Note : reshape(4,2) should satsfy arange(1,9) i.,e reshape dimentions 4 x 2 = 8 should be equal to arrange 8

b = np.arange(1,9).reshape(4,2)
b


# In[25]:


b.shape


# In[26]:


# Reshaping array Note : reshape(5,6) didn't satsfy arange(1,9) i.,e reshape dimentions 5 x 6 = 30 is not equal to arrange 8

c = np.arange(1,9).reshape(5,6)
c


# In[11]:


# Universal operation in NupPy

# 1 Trinometric Functions

angles = np.array([0,30,40,60,90])


# In[12]:


# radians = angles * pi/180

angle_radians = np.radians(angles)
angle_radians


# In[13]:


print(np.sin(angle_radians))


# In[14]:


print(np.cos(angle_radians))


# In[15]:


# 1 Stasticas Functions

test_scores = np.array([1,3,5,7,9,11,13])

# Mean = Average

print(np.mean(test_scores))


# In[16]:


# Median = Mid number

print(np.median(test_scores)) 


# In[18]:


# Arthimatic Functions

a = np.array([10,10,10])
b = np.array([5,5,5])


# In[19]:


c = a + b
c


# In[20]:


d = a - b
d


# In[21]:


e = a * b
e


# In[22]:


a < 35


# In[23]:


a > 25


# In[24]:


# Squaring

a**2


# In[25]:


# un-array operators

ages = np.array([12,15,18,20])


# In[26]:


ages.sum()


# In[27]:


ages.min()


# In[28]:


ages.max()


# In[29]:


numbers = np.arange(12).reshape(3,4)
numbers


# In[30]:


# in a 2D array, axis_0 represents Cols & axis_1 represents Rows

sum_axis_0 = numbers.sum(axis = 0)
sum_axis_0


# In[31]:


sum_axis_1 = numbers.sum(axis = 1)
sum_axis_1


# In[32]:


array_a = np.arange(6)
array_a


# In[33]:


array_b = np.arange(4)
array_b


# In[35]:


# To perform mathematical operations (add, minus,...) on arrays - size of the array should be same

array_c = array_a + array_b
array_c


# In[48]:


# Reading data from file

salaries = np.genfromtxt('salary.csv',delimiter = ',')


# In[49]:


salaries


# In[13]:


salaries.shape


# In[22]:


mean_sal = np.mean(salaries)
print(f'Mean of Salary : {mean_sal}')


# In[23]:


median_sal = np.median(salaries)
print(f'Median of Salary : {median_sal}')


# In[24]:


standard_deviation_sal = np.std(salaries)
print(f'Standard Deviation of Salary : {standard_deviation_sal}')


# In[25]:


variance_sal = np.var(salaries)
print(f'Variance of Salary : {variance_sal}')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




