#!/usr/bin/env python
# coding: utf-8

# # Setup

# # Import

# In[2]:


import os
import glob
import pandas as pd
from datetime import date
import time


# In[3]:


today = date.today()
day = today.strftime("%d_%m_%Y")


# In[6]:


path = 'C:/Users/Admin/Desktop/Database_newspaper/'
dirs = os.listdir(path)


# # Set directory and Export

# In[12]:


os.chdir(path+"total")


# In[13]:


#os.listdir('./')


# In[14]:


# check extension and find all csv file
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


# In[15]:


#all_filenames


# In[17]:


# combine all the csv
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#export
combined_csv.to_csv(r'C:\Users\Admin\Desktop\Database_newspaper\total\total_concat.csv', index=False, encoding='utf-8-sig')


# In[19]:


print("Exported in date "+day)

