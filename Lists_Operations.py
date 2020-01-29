#!/usr/bin/env python
# coding: utf-8

# In[21]:


cars = ['bmw','audi','toyato','benz']
cars


# In[2]:


type(cars)


# In[3]:


# Display list in an alphabital order - list.sort() - Sort changes the order parmenantly

cars.sort() 
cars


# In[4]:


# Display List in reverse order - reverse = True

cars.sort(reverse=True)
cars


# In[8]:


cars.reverse()
cars


# In[23]:


# Sorting a list Temperarly - sorted(list)

print(sorted(cars))


# In[11]:


# Length of list

len(cars)


# In[22]:


# Loops

students = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE']
students


# In[23]:


for student in students:
    print(student)


# In[20]:


for student in students:
    print(f"{student}, All the very best")


# In[24]:


print(f"{students[2]}, All the very best")


# In[5]:


marks = [60, 70, 80, 90, 100, 65, 75, 85, 95, 50]

if 105 in marks:
    print("Number present in the list")
else:
    print("Number not present in the list")


# In[6]:


# Add an element at the End

marks.append(1000)
marks


# In[7]:


# Add an element at any Index

marks.insert(3,99)
marks


# In[10]:


print(marks.pop())


# In[11]:


# Delete an element at the last index

marks.pop()
print(marks)


# In[15]:


print(marks)


# In[16]:


# Delete an element at the specific index - remove() - remove based on Value

marks.remove(100)
marks


# In[17]:


# Delete an element at the specific index - pop() - remove based on Index

marks.pop(3)
marks


# In[18]:


# Delete an element at the specific index - del

del marks[3]
print(marks)


# In[19]:


# Difference between del & pop - 'pop' will remove only 1 element in the list BUT 'del' will remove entire list if index not specified

del marks
print(marks)


# In[26]:


# Delete the elements in the list & retain the list

marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
marks


# In[27]:


# Difference between del & clear - 'del' will remove entire list if index not specified BUT 'clear' will delete the elements in the list but list is retained

marks.clear()
marks


# In[45]:


# Creating lilt in alternate way - List Constructor 

vovels = list(('a','e','i','o','u'))
vovels


# In[58]:


# Copying the elements of another list - copy()

english_vowels = vovels.copy()
english_vowels


# In[35]:


vovels.append('a')


# In[51]:


vovels.append('e')


# In[52]:


vovels.append('i')


# In[53]:


vovels.append('o')


# In[55]:


vovels.append('u')
vovels


# In[56]:


# Count of a specific element in the list - count(index)

count_i = vovels.count('i')
count_i


# In[57]:


count_u = vovels.count('u')
count_u


# In[14]:


# Difference between - append & extend - "append" will add an element at the END BUT "extend" will iterates through the iterable object one item at a time and appends each item to the list
# append - "append" will add an element at the END

list_append = [1, 2, 3, 4, 5]
list_append


# In[15]:


list_append.append(6)
list_append


# In[16]:


list_append.append([7, 8, 9])
list_append


# In[17]:


# extend - it iterates through the iterable object one item at a time and appends each item to the list

list_extend = [11, 22, 33, 44, 55]
list_extend


# In[19]:


list_extend.extend([66, 77, 88])
list_extend


# In[20]:


list_extend.extend([99])
list_extend


# In[ ]:





# In[ ]:




