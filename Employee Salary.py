#!/usr/bin/env python
# coding: utf-8

# # Employee Salary Analysis by KODI VENU

# In[15]:


import pandas as pd
import warnings
warnings.filterwarnings ('ignore')
import numpy as np
data = pd.read_csv('Salaries.csv')


# Displaying Top 10 Rows of the Dataset

# In[16]:


data.head(10)


# Displaying Last 10 Rows of the Dataset

# In[17]:


data.tail(10)


# Finding shape of the Dataset

# In[18]:


data.shape


# In[19]:


print("Number of rows", data.shape[0])
print("Number of columns", data.shape[1])


# Dataset Information

# In[20]:


data.info()


# Checking Null Values in the dataset

# In[24]:


data.isnull()


# In[25]:


data.isnull().sum()


# Drop ID, notes, agency and status columns

# In[23]:


data.columns


# In[27]:


data=data.drop(['Id','Notes','Status'],axis=1)


# In[29]:


data.head(1)


# Dataset Overall Statistics

# In[30]:


data.describe(include='all')


# Find occurrence of the employee names (Top 5) 

# In[31]:


data.columns


# In[32]:


data['EmployeeName'].value_counts()


# In[33]:


data['EmployeeName'].value_counts().head()


# find the number of unique job titles

# In[34]:


data.columns


# In[35]:


data['JobTitle'].nunique()


# total number of job titles contain captain

# In[36]:


data.columns


# In[39]:


data[data['JobTitle'].str.contains('CAPTAIN')]


# In[40]:


len(data[data['JobTitle'].str.contains('CAPTAIN')])


# In[41]:


data[data['JobTitle'].str.contains('CAPTAIN')].count()


# In[42]:


len(data[data['JobTitle'].str.contains('CAPTAIN',case=False)])


# In[44]:


data[data['JobTitle'].str.contains('CAPTAIN',case=False)].count()


# display all the employee names from fire department

# In[45]:


data.columns


# In[47]:


data['JobTitle'].str.contains('fire',case=False)


# In[48]:


data[data['JobTitle'].str.contains('fire',case=False)]


# In[49]:


data[data['JobTitle'].str.contains('fire',case=False)]['EmployeeName']


# find minimum, maximum and average BasePay

# In[50]:


data.columns


# In[52]:


data['BasePay'].describe(include='all')


# replace 'Not Provided' in employeename column to NaN

# In[54]:


data.columns


# In[55]:


data['EmployeeName']


# In[56]:


data['EmployeeName']=data['EmployeeName'].replace('Not provided',np.nan)


# In[57]:


data['EmployeeName']


# drop the rows having 5 missing vaues

# In[67]:


data.drop(data[data.isnull().sum(axis=1)==5].index,axis=0,inplace=True)


# In[69]:


data.isnull().sum(axis=1)


# find the job title of ALBERT PARDINI

# In[70]:


data.columns


# In[71]:


data[data['EmployeeName']=='ALBERT PARDINI']


# In[72]:


data[data['EmployeeName']=='ALBERT PARDINI'][ 'JobTitle']


# How much ALBERT PARDINI Make (Include Benefits)?

# In[73]:


data.columns


# In[74]:


data[data['EmployeeName']=='ALBERT PARDINI']


# In[76]:


data[data['EmployeeName']=='ALBERT PARDINI']['TotalPayBenefits']


# Display name of the person having the highest BasePay

# In[77]:


data.columns


# In[85]:


data[data['BasePay'].max()==data['BasePay']]


# In[86]:


data[data['BasePay'].max()==data['BasePay']]['EmployeeName']


# Find average BasePay of all employee per year

# In[87]:


data.columns


# In[88]:


data.groupby('Year').mean(['BasePay'])


# Find average BasePay of all employee per Job Title

# In[89]:


data.columns


# In[92]:


data.groupby('JobTitle').mean()


# In[93]:


data.groupby('JobTitle').mean()['BasePay']


# Find average BasePay of employee having Job Title ACCOUNTANT

# In[94]:


data.columns


# In[95]:


data['JobTitle']=='ACCOUNTANT'


# In[96]:


data[data['JobTitle']=='ACCOUNTANT']['BasePay']


# In[97]:


data[data['JobTitle']=='ACCOUNTANT']['BasePay'].mean()


# Find top 5 most common jobs

# In[98]:


data.columns


# In[99]:


data['JobTitle'].value_counts()


# In[100]:


data['JobTitle'].value_counts().head()


# In[ ]:




