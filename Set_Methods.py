#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Elements in List[] - Ordered & Indexed & Changable (Mutable)
# Elements in Tuple() - Ordered & Indexzed & UnChangable (Immutable)

# Set is a collection type - elements in sets{} are - UnOrdered & UnIndexed 

vovels_set = {'e', 'a', 'i', 'u', 'o'}
vovels_set


# In[7]:


# Accessing items in the SET

for x in vovels_set:
    print(x)


# In[8]:


# Check if an element present in the SET or not

print("o" in vovels_set)


# In[9]:


print("x" in vovels_set)


# In[11]:


# Changing items in a SET - we can't change/modify an existing items in a SET as it's Immutable 

vovels_set{0} = 'x'


# In[12]:


# We can add an elemet(s) using add() - for single element / update() - for multiple elements

student_set = {'a', 'b', 'c', 'd', 'e'}
student_set


# In[13]:


# Ading single element to SET using - add()

student_set.add('f')
student_set


# In[14]:


# Ading multiple elements to SET using - update()

student_set.update(['x', 'y', 'z'])
student_set


# In[19]:


# Finding Length of the SET using - len()

print(f"Length of the student_set is -: {len(student_set)}")


# In[20]:


# Removing an element of the SET using - remove()

student_set


# In[21]:


# Remove an existing element using remove()

student_set.remove('z') 
student_set


# In[22]:


# Remove an un-existing element using remove() - Note : remove() will return error if trying to remove an un-existing element from the SET

student_set.remove('o')
student_set


# In[27]:


# Removing an element of the SET using - discard()

student_set


# In[28]:


# Remove an existing element using discard()

student_set.discard('e') 
student_set


# In[29]:


# Remove an un-existing element using discard() - discard() will not return any error if trying to remove an un-existing element from the SET

student_set.discard('x') 
student_set


# In[30]:


# Removing an element of the SET using - pop() - very last element of the SET will be Deleted

student_set


# In[31]:


# As SETs are un-ordered, so when using pop() we will not know which element will be deleted, very last element will be deleted

student_set.pop()
student_set


# In[33]:


# Deleting all items in SET - clear()
student_set.clear()
student_set


# In[34]:


# Deleting an entire  SET - del()

del student_set
student_set


# In[35]:


# Alternate approach to create a SET - using SET Constructor

set_xyz = set(('x', 'y', 'z'))
set_xyz


# In[36]:


# Copy the content of one set to another - copy()

copy_set_xyz = set_xyz.copy()
copy_set_xyz


# In[37]:


copy_set_xyz.update(['a', 'b', 'c'])
copy_set_xyz


# In[38]:


set_xyz


# In[39]:


# Identifying difference between sets using - difference()

set_xyx_minus_copy_set_xyz = set_xyz.difference(copy_set_xyz) # Equivalent to : A - B
set_xyx_minus_copy_set_xyz


# In[40]:


copy_set_xyx_minus_set_xyz = copy_set_xyz.difference(set_xyz)  # Equivalent to : B - A
copy_set_xyx_minus_set_xyz


# In[43]:


# Identifying difference between sets using - minus (-) operator - Alternative approach

set_xyx_minus_copy_set_xyz_alt = set_xyz - copy_set_xyz
set_xyx_minus_copy_set_xyz_alt


# In[44]:


copy_set_xyx_minus_set_xyz_alt = copy_set_xyz - set_xyz
copy_set_xyx_minus_set_xyz_alt


# In[45]:


set_xyz


# In[47]:


copy_set_xyz


# In[50]:


# Identifying difference between sets & update the differences to other set using - difference_update()

copy_set_xyz.difference_update(set_xyz)   # Equivalent to : A + append(A - B)
copy_set_xyz


# In[56]:


set_a = {1,2,3,4,5}
set_b = {5,6,7,8,9}

set_a.difference(set_b)


# In[57]:


set_a.difference_update(set_b)
set_a


# In[58]:


set_b.difference_update(set_a)
set_b


# In[60]:


# To check one set is a sub-set of other set, using - issubset()

set_x = {1,2,3,4,5}
set_y = {2,3,4}


# In[61]:


set_x.issubset(set_y)


# In[62]:


set_y.issubset(set_x)


# In[63]:


# Union of sets, using - union()

set_1 = {1,2,3,4,5}
set_2 = {5,6,7,8,9}

set_union = set_1.union(set_2)
set_union


# In[64]:


# Intersection of sets, using - intersection()

set_intersection = set_1.intersection(set_2)
set_intersection


# In[65]:


set_intersection_none = set_1.intersection()
set_intersection_none


# In[66]:


# To identify "symmetric_difference" of sets, using - symmetric_difference() 
# A symmetric_difference B = (A union B) - (A intersection B) (or) A symmetric_difference B = (A minus B) union (B minus A)

set_1 = {1,2,3,4,5}
set_2 = {5,6,7,8,9}


# In[67]:


set_1_symmetric_difference_set_2 = set_1.symmetric_difference(set_2)
set_1_symmetric_difference_set_2


# In[68]:


# To identify "symmetric_difference" of sets, using - the symbol - ^ - Alternative Approach

set_2_symmetric_difference_set_1 = set_2 ^ set_1
set_2_symmetric_difference_set_1


# In[ ]:




