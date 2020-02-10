#!/usr/bin/env python
# coding: utf-8

# In[108]:


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import Series   


# In[109]:


# Titanic Positive Case - Without any Mismatch Records

titanic_positive_source = "D:\\Projects\\Cadent\\Cadent_BigDataTesting_Automation\\Demo\\Script_without_UDF\\Data_Files\\Titanic\\Titanic_Input\\Titanic_PositiveCase_Source.xls"
titanic_positive_target = "D:\\Projects\\Cadent\\Cadent_BigDataTesting_Automation\\Demo\\Script_without_UDF\\Data_Files\\Titanic\\Titanic_Input\\Titanic_PositiveCase_Target.xls"
titanic_positive_mismatch = "D:\\Projects\\Cadent\\Cadent_BigDataTesting_Automation\\Demo\\Script_without_UDF\\Data_Files\\Titanic\\Titanic_Output\\Titanic_PositiveCase_Mismatch.xls"


# In[110]:


# Reading 'Source' data

source_p = pd.read_excel(titanic_positive_source, sheet_name = 'titanic')
print(source_p)


# In[111]:


# Reading 'Target' data

target_p = pd.read_excel(titanic_positive_target, sheet_name = 'titanic')
print(target_p)


# In[112]:


# Common Records accross Source & Target

source_target_common_p = source_p.merge(target_p, how = 'inner' ,indicator=False)
source_target_common_p


# In[113]:


# Writing Dataframe to a file

writer = ExcelWriter(titanic_positive_mismatch)
source_target_common_p.to_excel(writer, "Source_Target_Common")
writer.save()


# In[114]:


# Source minus Target - Rows Available at 'Source' Which Are Not Available at 'Target'

source_minus_target_p = source_p.merge(target_p, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only'] 
source_minus_target_p


# In[115]:


# Writing Dataframe to a file

source_minus_target_p.to_excel(writer, "Source_minus_Target")
writer.save()


# In[116]:


# Target minus Source - Rows Available at 'Target' Which Are Not Available at 'Source'

target_minus_source_p = source_p.merge(target_p, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='right_only']
target_minus_source_p


# In[117]:


# Writing Dataframe to a file

target_minus_source_p.to_excel(writer, "Target_minus_Source")
writer.save()


# In[118]:


# Rows which are not common between 'Source' & 'Target'

source_target_not_common_p = pd.concat([source_p,target_p]).drop_duplicates(keep=False)
source_target_not_common_p


# In[119]:


# Writing Dataframe to a file

source_target_not_common_p.to_excel(writer, "Source_Target_not_common")
writer.save()


# In[120]:


# Titanic Negative Case - With some Mismatch Records

titanic_negative_source = "D:\\Projects\\Cadent\\Cadent_BigDataTesting_Automation\\Demo\\Script_without_UDF\\Data_Files\\Titanic\\Titanic_Input\\Titanic_NegativeCase_Source.xls"
titanic_negative_target = "D:\\Projects\\Cadent\\Cadent_BigDataTesting_Automation\\Demo\\Script_without_UDF\\Data_Files\\Titanic\\Titanic_Input\\Titanic_NegativeCase_Target.xls"
titanic_negative_mismatch = "D:\\Projects\\Cadent\\Cadent_BigDataTesting_Automation\\Demo\\Script_without_UDF\\Data_Files\\Titanic\\Titanic_Output\\Titanic_NegativeCase_Mismatch.xls"


# In[121]:


# Reading 'Source' data

source_n = pd.read_excel(titanic_negative_source, sheet_name = 'titanic')
print(source_n)


# In[122]:


# Reading 'Target' data

target_n = pd.read_excel(titanic_negative_target, sheet_name = 'titanic')
print(target_n)


# In[123]:


# Common Records accross Source & Target

source_target_common_n = source_n.merge(target_n, how = 'inner' ,indicator=False)
source_target_common_n


# In[124]:


# Writing Dataframe to a file

writer = ExcelWriter(titanic_negative_mismatch)
source_target_common_n.to_excel(writer, "Source_Target_Common")
writer.save()


# In[125]:


# Source minus Target - Rows Available at 'Source' Which Are Not Available at 'Target'

source_minus_target_n = source_n.merge(target_n, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only'] 
source_minus_target_n


# In[126]:


# Writing Dataframe to a file

source_minus_target_n.to_excel(writer, "Source_minus_Target")
writer.save()


# In[127]:


# Target minus Source - Rows Available at 'Target' Which Are Not Available at 'Source'

target_minus_source_n = source_n.merge(target_n, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='right_only']
target_minus_source_n


# In[128]:


# Writing Dataframe to a file

target_minus_source_n.to_excel(writer, "Target_minus_Source")
writer.save()


# In[129]:


# Rows which are not common between 'Source' & 'Target'

source_target_not_common_n = pd.concat([source_n,target_n]).drop_duplicates(keep=False)
source_target_not_common_n


# In[130]:


# Writing Dataframe to a file

source_target_not_common_n.to_excel(writer, "Source_Target_not_common")
writer.save()


# In[9]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:





# In[ ]:





# In[ ]:





# In[102]:





# In[ ]:





# In[ ]:





# In[ ]:




