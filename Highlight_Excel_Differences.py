#!/usr/bin/env python
# coding: utf-8

# In[47]:


# Highlight Excel Differences

# Reference Script : https://matthewkudija.com/blog/2018/07/21/excel-diff/


# In[ ]:


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile 


# In[48]:


# Titanic Negative Case - With some Mismatch Records

titanic_negative_source = "D:\\Projects\\Cadent\\Cadent_BigDataTesting_Automation\\Demo\\Script_without_UDF\\Data_Files\\Titanic\\Titanic_Highlight_Differences\\HD_Input\\Titanic_Source.xls"
titanic_negative_target = "D:\\Projects\\Cadent\\Cadent_BigDataTesting_Automation\\Demo\\Script_without_UDF\\Data_Files\\Titanic\\Titanic_Highlight_Differences\\HD_Input\\Titanic_Target.xls"
titanic_negative_mismatch = "D:\\Projects\\Cadent\\Cadent_BigDataTesting_Automation\\Demo\\Script_without_UDF\\Data_Files\\Titanic\\Titanic_Highlight_Differences\\HD_Output\\Titanic_Highlight_Difference.xls"


# In[49]:


# Reading 'Source' data

source_n = pd.read_excel(titanic_negative_source, sheet_name = 'titanic_source').fillna(0)
print(source_n)


# In[50]:


# Reading 'Target' data

target_n = pd.read_excel(titanic_negative_target, sheet_name = 'titanic_target').fillna(0)
print(target_n)


# In[51]:


# Verify both Source & Target were Equal or not

source_n.equals(target_n)


# In[52]:


# Source minus Target & Highlight Difference

source_minus_target = source_n.copy()
for row in range(source_minus_target.shape[0]):
    for col in range(source_minus_target.shape[1]):
        value_OLD = source_n.iloc[row,col]
        try:
            value_NEW = target_n.iloc[row,col]
            if value_OLD==value_NEW:
                source_minus_target.iloc[row,col] = target_n.iloc[row,col]
            else:
                source_minus_target.iloc[row,col] = ('{} => {}').format(value_OLD,value_NEW)
        except:
            source_minus_target.iloc[row,col] = ('{} => {}').format(value_OLD, 'NaN')


# In[32]:


# Writing Dataframe to a file

writer = ExcelWriter(titanic_negative_mismatch)
source_minus_target.to_excel(writer, "Source_minus_Target")
writer.save()


# In[ ]:


# Till this point, code is working fine. Issues with the below code


# In[53]:


# writer = pd.ExcelWriter(fname, engine='xlsxwriter')

writer = ExcelWriter(titanic_negative_mismatch)
source_minus_target.to_excel(writer, sheet_name="Source_minus_Target", index=False)
# target_n.to_excel(writer, sheet_name = titanic_negative_source.stem, index=False)
# source_n.to_excel(writer, sheet_name = titanic_negative_target.stem, index=False)
writer.save()


# In[8]:


# Applying Formates & Colors

Workbook  = writer.book
Worksheet = writer.sheets['Source_minus_Target']
Worksheet.hide_gridlines(2)

# Define format for - unCHANGED cells

grey_fmt = workbook.add_format({'font_color': '#E0E0E0'}) 

# Define format for - CHANGED cells

highlight_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color':'#B1B3B3'})


# In[ ]:


#  Highlight CHANGED cells

worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
                                        'criteria': 'containing',
                                        'value':'→',
                                        'format': highlight_fmt})
# Highlight unCHANGED cells

worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
                                        'criteria': 'not containing',
                                        'value':'→',
                                        'format': grey_fmt})
writer.save()


# In[ ]:





# In[ ]:





# In[26]:





# In[ ]:





# In[ ]:





# In[102]:





# In[ ]:





# In[ ]:





# In[ ]:




