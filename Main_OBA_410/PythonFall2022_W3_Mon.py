#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


# gives us the present working directory
get_ipython().run_line_magic('pwd', '')


# # Reading the Data

# In[3]:


#reading diabetes data -- from current working directory
# name of the file and format goes inside quotations
df = pd.read_csv("diabetes-1.csv")
df


# In[33]:


# reading datasets directly from their original location
df = pd.read_csv("/Users/ryanmaki/Documents/UO/OBA 410 /Class Datasets/diabetes-1.csv")
df


# # Exploring the Data

# ## Head and Tail

# In[24]:


# looking at the first n rows
# by default, it returns on first 5 rows if not otherwise specified
df.head()


# In[25]:


# getting the first 3 rows
df.head(3)


# In[26]:


# getting the last n rows -- tail()
df.tail()


# In[34]:


# get the last 7 rows of df
df.tail(7)


# ## Getting Info about Dataset

# In[35]:


# Getting the shape (dimension) of our data -- Shape attribute
df.shape


# In[36]:


# Getting the type of the columns in our data -- dtypes
df.dtypes


# In[37]:


# More comprehensive data on our data -- info()
df.info()


# In[38]:


df


# In[42]:


# changeing the display settings in Pandas
pd.options.display.max_rows=2000
pd.options.display.max_columns=100
df


# In[45]:


# resetting all display settings
pd.reset_option('^display')
df


# # Main Components of a DataFrame

# In[ ]:


df = 


# In[46]:


# columns
df.columns


# In[47]:


# index
df.index


# In[48]:


# values
df.values


# # Sorting DataFrames

# In[54]:


# Sorting df by prenganices
df.sort_values(by=['Pregnancies'])


# In[55]:


# Sorting df by Glucose Level
df.sort_values(by=['Glucose'])


# In[57]:


# Sorting df based on more than 1 column
# Glucose and BMI
df.sort_values(by=["Glucose", "BMI"])


# In[58]:


# Sorting values from largest to smallest -- 
# BloodPressure Descending
df.sort_values(by=["BloodPressure"], ascending=False)


# In[64]:


# Sorting df based on BloodPressure and Insulin, descending
df.sort_values(by=["BloodPressure", "Insulin"], ascending = False)


# In[72]:


# sort df based on BloodPressure, decending (large to small)
# and Insulin, ascending (small to large)
df.sort_values(by=["BloodPressure", "Insulin"],
               ascending = [False,True])


# In[75]:


# if we want to permanently sort, set in place to True
# BMI ascending
df.sort_values(by=['BMI'], inplace = True)


# In[76]:


df


# In[80]:


# sorting based on Index
df.sort_index(inplace=True)
df


# # Subsetting DataFrames

# ## Using Indexing Operator - Column Subsetting

# In[84]:


# Subset "BMI", "Age", "Outcome"
# More than 1 col, we pass col labels in a list
# a list to the indexing operator
df[["BMI", "Age", "Outcome"]]


# In[85]:


# Subset "Insulin" column from df
# Pass the single column name in a list to indexing operator
# output is a 1-col Data Frame
df[["Insulin"]]


# In[86]:


# Subset "Insulin" column from df
# pass the single col name directly to indexing operator
# Output is in Series Format
df["Insulin"]


# In[87]:


# for multiple cols we must pass them in a list
df["Age", "Outcome"]


# In[ ]:




