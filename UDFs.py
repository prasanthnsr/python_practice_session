#!/usr/bin/env python
# coding: utf-8

# In[4]:


# UDF Defination

def greet_user():
    """ Display Greetings """ # doc string - commenting inside a UDF
    print('Welcome !')


# In[5]:


# UDF call

greet_user() 


# In[6]:


# Passing parameters to UDF & Arguments Decleration

# Whoever log-in to the site, greet that user

def greet_a_user(username):
    """ Greeting a specific user who logedin """
    print(f'Hello - {username.title()}')


# In[8]:


# Passing paramaters / arguments run-time

greet_a_user(pRaSaNtH) # arguments should be in quotes


# In[9]:


# Passing paramaters / arguments run-time

greet_a_user('pRaSaNtH') # arguments should be in quotes


# In[ ]:


# Different types of Arguments - Positional Arguments, Keyword Arguments, Default Arguments


# In[4]:


# Positional Arguments example

def discribe_pet(animal_type, pet_name):
    print(f"\n I have an animal type - {animal_type}")
    print(f"{animal_type}'s name is - {pet_name.title()}")


# In[5]:


discribe_pet('cat', 'pixcy')


# In[7]:


def kids(kid_name='name', kid_gender='gender'):
    print(f"\n I have a {kid_gender} kid by the name {kid_name.title()}")


# In[10]:


kids(kid_gender = 'Female', kid_name = 'Madhu')


# In[11]:


kids(kid_gender = 'Male', kid_name = 'Abhi')


# In[36]:


# Default arguments should be difined at the end of paramaters

def describe_pet(pet_name, animal_type='dog'):
    print(f"\n I have a {animal_type}")
    print(f" my {animal_type}'s name is - {pet_name.title()}")


# In[37]:


describe_pet('rocky') # Making use of default arguments


# In[38]:


describe_pet('rocky', 'Dogie')


# In[39]:


# UDF with Return values

def get_name_formatted(first_name, last_name):
    """ Returns a full name well formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# In[20]:


get_name_formatted('prasanth','nsr')


# In[12]:


# UDFs with Lists as Argument

def congrats_user(names):
    for name in names:
        print(f"{name}, Congrats ! Well Done !")


# In[15]:


user_names = ['AAA','BBB','CCC']
congrats_user(user_names)


# In[18]:


# UDFs with Tuples as Argument

def english_vovels(vovels):
    for vovel in vovels:
        print(f"{vovel} - is a Vovel")


# In[19]:


vovels = ('a','e','c','d','e')
english_vovels(vovels)


# In[20]:


# UDFs with Dictionaries as Argument

def student_marks(dict):
    for subject, marks in dict:
        print(f"Scored {marks} marks in {subject}")


# In[21]:


marks = {'sub_1':100, 'sub_2':90, 'sub_3':80}
student_marks(marks)


# In[ ]:




