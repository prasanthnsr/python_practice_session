#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dictionaries stores data in - key & value pairs (json format) which is an Mutable & defined within { }


# In[1]:


marks = {'sub_1':100, 'sub_2':90, 'sub_3':80}
marks


# In[8]:


type(marks)


# In[9]:


# Accessing specific item

print(marks['sub_1'])


# In[10]:


# Accessing specific item using get() - Alternativ approach to access specific items

marks.get('sub_1')


# In[6]:


# Dictionaries with fstring

new_sub = marks['sub_3']
print(f" You got {new_sub} marks !")


# In[30]:


# Building a Dick from scratch by adding elements to empty Dict

alien_0 = {}

alien_0['color'] = 'Green'
alien_0['points'] = 100

alien_0


# In[31]:


alien_0['x_position'] = 50
alien_0['y_position'] = 75

alien_0


# In[32]:


# Modify the values in Dick

alien_0['color'] = 'White'
alien_0['points'] = 1000
alien_0


# In[36]:


# Removing an item in the Dick using - del

del alien_0['color']
alien_0


# In[37]:


alien_0


# In[38]:


# Removing an item in the Dict using - pop() witn index - Item with matching index will be removed

alien_0.pop('points')
alien_0


# In[41]:


alien_0


# In[42]:


alien_0['color'] = 'Green'
alien_0['points'] = 100


# In[43]:


alien_0


# In[44]:


# Removing an item in the Dict using - popitem() - Removes last item (i.e., last key, value pair)

alien_0.popitem()


# In[45]:


alien_0


# In[46]:


# Delete the items in the Dict with - clear()

alien_0.clear()
print(alien_0)


# In[47]:


# Delete a Dict with - del

del alien_0
print(alien_0)


# In[11]:


# Loop through Dict to display (only) Keys

for x in marks:
    print(x)


# In[12]:


# Loop through Dict to display (only) Values

for x in marks:
    print(marks[x])


# In[13]:


# Loop through Dict to display (only) Values using values() - Alternative approach

for x in marks.values():
    print(x)


# In[14]:


# Loop through Dict to display both Keys & Values using items()

for x, y in marks.items():
    print(x, y)


# In[3]:


# Loop through Dict to display both Keys & Values using items() with fstrings

for x, y in marks.items():
    print(f"Student got {y} marks in {x}")


# In[18]:


marks_in_subjects = {'Maths':100, 'English':90, 'Hindi':80, 'Science':70, 'Social':60}
marks_in_subjects


# In[20]:


# Check if specific KEY exists or not using 'in'

if 'English' in marks_in_subjects:
    print("Key by the name 'English' exists")


# In[21]:


if 'German' in marks_in_subjects:
    print("Key by the name 'German' exists")
else:
    print("Key by the name 'German' NOT exists")


# In[23]:


# Check if specific KEY exists or not uning 'not in' - Alternative Approach

if 'German' not in marks_in_subjects:
    print("Key by the name 'German' NOT exists")


# In[27]:


# Finding the Leangth of the Dict

print(f"Length of the Dick by the name 'marks_in_subjects' is -: {len(marks_in_subjects)}")


# In[5]:


# Creating the Dick using - dict() constructor
# Note : keywords are not 'string literals'
# Note : for assignment we should use 'equals' rather than 'colon'

person = dict(name='Prasanth', location='Bangalore', state='Karnakata')
person


# In[6]:


# Create a replica of a Dict using - copy()

person


# In[7]:


person_prasanth


# In[8]:


person_prasanth = person.copy()
person_prasanth


# In[11]:


# Display only the keys of the Dict - keys()

person_keys = person.keys()
print(person_keys)


# In[12]:


type(person_keys)


# In[13]:


# Create a dictionary from a sequence of keys - fromkeys()

keys = {'a', 'e', 'i', 'o', 'u'}
vowels = dict.fromkeys(keys)
print(vowels)


# In[14]:


# Update the Dict with new Value based on Key - update()

person_prasanth


# In[15]:


person_prasanth_change = {'name': 'Prasanth_NSR'}
person_prasanth.update(person_prasanth_change)
person_prasanth


# In[ ]:




