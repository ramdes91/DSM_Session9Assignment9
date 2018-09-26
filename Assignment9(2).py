
# coding: utf-8

# #1 Read the dataset from the below link
# https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv
# Questions:
# 1. Delete unnamed columns
# 2. Show the distribution of male and female
# 3. Show the top 5 most preferred names
# 4. What is the median name occurence in the dataset
# 5. Distribution of male and female born count by states

# In[4]:


import pandas as pd
import numpy as np
import os
data = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv")
data.head()


# 1.Delete unnamed columns

# In[5]:


data.drop(['Unnamed: 0'], axis=1, inplace=True) 

data.head()


# 2.Show the distribution of male and female

# In[7]:


data['Gender'].value_counts()


# 3.Show the top 5 most preferred names

# In[14]:


data_names = data.groupby("Name").sum()
data_names.sort_values("Count", ascending = 0).head()


# 4.What is the median name occurence in the dataset

# In[15]:


data_names[data_names.Count == data_names.Count.median()]


# 5.Distribution of male and female born count by states

# In[16]:


data['State'].value_counts()

