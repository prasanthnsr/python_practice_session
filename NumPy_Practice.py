#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy # ! - invoking operation from cmd (terminal)')


# In[13]:


get_ipython().system('pip install numpy --upgrade pip')


# In[2]:


get_ipython().system('pip install numpy --upgrade')


# In[1]:


# Numpy - Numerical computing library / package, Numpy suppors - Multi-Dimentioanl Arrays

import numpy as np # np is alias for numpy


# In[3]:


array_one = np.array([1,2,3,4,5])
array_one


# In[4]:


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


# In[3]:


# Indexing & Slicing of an array

a = np.arange(11)**2
a


# In[4]:


a[2]


# In[5]:


a[-2]


# In[6]:


# Slicing of an array

a[2:7] # Starting from 2nd element to 6th element as last index (7) is excluded


# In[7]:


# Slicing with step count

a[1:8:2]


# In[8]:


# Reversing an array

a[::-1]


# In[10]:


# Array with mix of Datatypes

students = np.array([['a','b','c','d'],
                    [10, 20, 30, 40],
                    [50, 60, 70, 80]])


# In[11]:


students


# In[ ]:


# < -> Little Indian
# > -> Big Indian
# u -> Unicode


# In[12]:


students[0]


# In[13]:


students[1]


# In[14]:


students[2]


# In[15]:


students[0:1]


# In[16]:


students[0:2, 2:4] # rows from 0 to 1 & cols from 2 to 3


# In[19]:


# Iterate over arrays

x = np.arange(11)**2
x


# In[20]:


# Printing square-root of an array

for i in x:
    print(i ** (1/2))


# In[21]:


student = np.array([['a','b','c','d'],
                    [10, 20, 30, 40],
                    [50, 60, 70, 80]])


# In[22]:


student


# In[23]:


for i in student:
    print('i = ', i)


# In[24]:


for element in student.flatten():  # flatten() - Row major Flatting
    print(element)


# In[26]:


for element in student.flatten(order = 'F'):  # flatten(order = 'F') - Column major Flatting
    print(element)


# In[27]:


for element in student.flatten(order = 'T'): 
    print(element)


# In[28]:


m = np.arange(12).reshape(3,4)
m


# In[30]:


for i in np.nditer(m): # Row major
    print(i)


# In[31]:


for i in np.nditer(m, order = 'F'): # Col major
    print(i)


# In[ ]:


# Difference between - Flatten & nditer

# Flatten - result an array - Values stores Permenent
# nditer - allows to iterate over array - Values stores Temperary 


# In[3]:


# Shallow Copy - master data will impact

fruits = np.array(['apple','mango','graps','banana'])


# In[4]:


basket_1 = fruits.view()
basket_2 = fruits.view()


# In[5]:


print(basket_1)


# In[6]:


print(basket_2)


# In[7]:


print("IDs for the arrays are different")
print(id(fruits))


# In[8]:


print("IDs for baskets")
print(id(basket_1))
print(id(basket_2))


# In[9]:


basket_1 is fruits


# In[11]:


basket_1.base is fruits


# In[12]:


# Changing elements in basket_1

basket_2[0] = 'kiwi' # Note : Changes effect original collection as well


# In[13]:


fruits


# In[14]:


basket_2


# In[15]:


basket_2 = np.array(['a', 'b', 'c'])


# In[16]:


# when we are creating an new array it will not effect the original (in this case - fruits)

basket_2


# In[17]:


fruits


# In[18]:


# Deep Copy - master data should not impact

basket = fruits.copy()


# In[20]:


basket is fruits


# In[21]:


# it dosn't share anything with the original (ie fruits)

basket.base is fruits


# In[22]:


basket[0] = 'lemon'


# In[23]:


basket


# In[25]:


# original (fruits) will not effect

fruits


# In[26]:


basket.shape = 2,2


# In[27]:


print(basket)


# In[8]:


# My NumPy Practice

np_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np_a)


# In[9]:


np_a


# In[12]:


type(np_a)


# In[13]:


np_a.shape


# In[14]:


# Difference between Arange & Linspace

# Arange

np_arrange = np.arange(12).reshape(3,4)
np_arrange


# In[17]:


# Linspace - Arranging 'z' numbers between 'x' & 'y'

ls_1 = np.linspace(5,10,6)
ls_1


# In[20]:


ls_2 = np.linspace(5,10,10)
ls_2


# In[21]:


ls_3 = np.linspace(5,10,5)
ls_3


# In[22]:


ls_4 = np.linspace(5,10,2)
ls_4


# In[23]:


ls_5 = np.linspace(5,10,3)
ls_5


# In[24]:


ls_6 = np.linspace(0,10,6)
ls_6


# In[26]:


ls_7 = np.linspace(0,10,6)
ls_7


# In[27]:


ls_8 = np.linspace(0,10,8)
ls_8


# In[28]:


# Initializing NumPy Array - Filling same number in an array of dimensions 'x' & 'y'

array_1 = np.full((2,2), 5)
array_1


# In[29]:


array_2 = np.full((2,4), 6)
array_2


# In[34]:


# Filling Random numbers in an array of dimensions 'x' & 'y'

array_3 = np.random.random((2,2))
array_3


# In[37]:


array_4 = np.random.random((5,5))
array_4


# In[39]:


# NumPy Array Inspection - shape - With 'shape' we can transpose the array

array_2


# In[40]:


array_2.shape


# In[58]:


array_2.size


# In[41]:


array_2.shape = (4, 2)


# In[42]:


array_2


# In[44]:


print(array_2.shape[0])


# In[48]:


print(array_2.shape[:, 1])   


# In[43]:


array_2.shape = (3,3)


# In[49]:


array_5 = np.arange(1,17).reshape(4,4)
array_5


# In[50]:


array_5.shape = (2, 8)
array_5


# In[51]:


array_5.shape = (8, 2)
array_5


# In[52]:


array_5.shape = (16, 1)
array_5


# In[53]:


array_5.shape = (3, 3)
array_5


# In[55]:


array_6 = np.arange(24)
array_6


# In[57]:


# Size of the array - size

array_6.size


# In[59]:


# Dimension of the array - ndim

array_7 = np.arange(24)
array_7


# In[61]:


array_7.ndim


# In[62]:


array_8 = array_7.reshape(2,4,3)
array_8


# In[63]:


array_8.ndim


# In[64]:


array_9 = np.arange(48).reshape(2,2,4,3)
array_9


# In[65]:


array_9.ndim


# In[66]:


# We can't change the dimensions of the array

array_9.ndim = 3


# In[68]:


array_10 = np.arange(24)
array_10


# In[69]:


array_10.size


# In[70]:


print(array_10.size)


# In[71]:


# Datatype of an array - dtype

array_10.dtype


# In[72]:


array_11 = array_10.reshape(3,4,2)
array_11


# In[73]:


array_11.dtype


# In[74]:


array_12 = np.linspace(5,7,11)
array_12


# In[75]:


array_12.dtype


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




