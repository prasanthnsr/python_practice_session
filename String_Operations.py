#!/usr/bin/env python
# coding: utf-8

# In[1]:


first_name = 'prasanth'
last_name = 'nsr'


# In[2]:


# Printing specific characters

print(first_name[4])


# In[3]:


print(first_name[4:7])


# In[3]:


# To concat multiple strings - fstring

full_name = f"{first_name} {last_name}" # String Concat
print(full_name)


# In[4]:


# String Init Cap - title()

print(full_name.title()) 


# In[5]:


print(f"Welcome to - {full_name.title()}")


# In[12]:


# adding white spaces - \t

print('Prasanth') # Normal Print
print('\t Prasanth') # Tab Delimeted


# In[13]:


# New Line Delimeted - \n

print('Prasanth\nNSR') 


# In[14]:


print('Langages : \n\t C \n\t C++ \n\t Java \n\t Python')


# In[6]:


# stripping of white spaces

name = '   Prasanth'
print(name)


# In[7]:


# Strip from both sides - strip()

full_name = '     prasanth_nsr     '
full_name.strip()


# In[8]:


# left stripping - lstrip()

full_name_left = '     prasanth_nsr'
full_name_left.lstrip()


# In[9]:


# Right stripping - rstrip()

full_name_right = 'prasanth_nsr     '
full_name_right.rstrip()


# In[3]:


name


# In[6]:


print(name[5])


# In[7]:


print(name[5:10])


# In[8]:


len(name)


# In[10]:


# Convert to Upper case - upper()

name_in_upper = name.upper()
name_in_upper


# In[11]:


# Convert to Lower case - lower()

name_in_lower = name.lower()
name_in_lower


# In[13]:


# Replace charecter with other characters - replace()

welcome = 'Hello, World'
print(welcome.replace('l','L'))


# In[14]:


# Split string substrings based on some character - split()

print(welcome.split(","))


# In[15]:


list_welcome = welcome.split(",")
print(list_welcome)


# In[7]:


# Counting the occurances on substrig in main string - count()

name = "prasanth_nsr"
substring_name = "s"

name_count = name.count(substring_name)
name_count


# In[ ]:





# In[1]:


# Zen of Python - Guidelines of Python

import this 


# In[ ]:


# Standards - pep8 - python enhancement praposal

1 proper indentation for redabality
2 line lengeth -  max 80 chars
3 blank line - spaces for redabality


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




