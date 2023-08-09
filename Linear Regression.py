#!/usr/bin/env python
# coding: utf-8

# # Linear Regression

# In[6]:


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# ## Housing Data

# In[8]:


# reading the data
house1ft = pd.read_csv('House_1feature-1.csv')
house1ft.head(3)


# In[10]:


# creating features and target sets
x_house1, y_house1 = house1ft[['Square_feet']], house1ft['Price']
display(x_house1.head(2))
display(y_house1.head(2))


# In[31]:


# split to train and test
x_train, x_test, y_train, y_test = train_test_split(x_house1, y_house1, random_state=32)


# In[16]:


# check our work
print('initial features set size:', x_house1.shape)
print("x_train shape:", x_train.shape)
print("x_train shape:", x_test.shape)

print("y_train shape:", y_train.shape)
print("y_train shape:", y_test.shape)


# In[18]:


# define the model
lr = LinearRegression()
# fit the model
lr.fit(x_train, y_train)


# In[19]:


# intercept value
lr.intercept_


# In[20]:


# coefficient value
lr.coef_


# In[21]:


# regression equation
# price = 107137.66 + 71.92(square_feet)


# In[22]:


# prediction
h1 = [1000]
h2 = [3000]
lr.predict([h1,h2])


# In[23]:


# use the equation to predict h1 price
107137.656 + 71.922*1000


# In[25]:


print('LR acc on train: {:.3f}'.format(lr.score(x_train, y_train)))
print('LR acc on test: {:.3f}'.format(lr.score(x_test, y_test)))


# ## Boston Housing Data

# In[28]:


# reading the data
boston = pd.read_csv("boston_housing_data-1.csv", index_col=0)
boston.head(5)


# In[29]:


# creating features and target sets
# target_medv is target, everything else is a feature
x_boston, y_boston = boston.iloc[:,:-1], boston['target_medv']
display(x_boston.head(3))
display(y_boston.head(3))


# In[32]:


# split to train and test
x_train1, x_test1, y_train1, y_test1 = train_test_split(x_boston, y_boston, random_state=0)


# In[33]:


# check our work
print('initial features set size:', x_boston.shape)
print("x_train shape:", x_train1.shape)
print("x_train shape:", x_test1.shape)

print("y_train shape:", y_train1.shape)
print("y_train shape:", y_test1.shape)


# In[34]:


# define the model
lr1 = LinearRegression()
# fit the model
lr1.fit(x_train1, y_train1)


# In[35]:


# intercept value
lr1.intercept_


# In[36]:


# coefficient value
lr1.coef_


# In[ ]:


# prediction
b1 = [1000]
b2 = [3000]
lr.predict([h1,h2])


# In[38]:


print('LR acc on train: {:.3f}'.format(lr1.score(x_train1, y_train1)))
print('LR acc on test: {:.3f}'.format(lr1.score(x_test1, y_test1)))


# In[ ]:




