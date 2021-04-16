#!/usr/bin/env python
# coding: utf-8

# #                      Data Analysis on Superstore Dataset
#  
#  
#  ###                                                                                                            -  By Bhaavik Bogam
# 

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[23]:


data=pd.read_csv('SampleSuperstore.csv')


# In[24]:


data


# In[25]:


data.isnull()


# In[26]:


data.isnull().any()


# sb.catplot(x="Category",y="Sales", data=data)

# In[27]:


data.keys()


# In[28]:


per=(data['Category'].value_counts()/len(data['Category']))*100
per[0]


# In[29]:


labels =data['Category'].unique()
sizes= [per[0],per[1],per[2]]
fig, ax= plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
ax.axis('equal')


# In[30]:


plt.figure(figsize=(9,6))
sb.barplot(x=data['Segment'].value_counts().head(20).keys(),
            y=data['Segment'].value_counts().head(20).values
           )

plt.tight_layout()
plt.xticks(rotation=90)
plt.tick_params(axis='x',
                which='major',
                labelsize=8
                )
plt.grid(axis = 'y')
plt.tight_layout()


# In[31]:


plt.figure(figsize=(12,8),)
sb.barplot(x=data['City'].value_counts().head(20).keys(),
            y=data['City'].value_counts().head(20).values,
           palette=("Blues_d")
           )


plt.tight_layout()
plt.xticks(rotation=90)
plt.tick_params(axis='x',
                which='major',
                labelsize=8
                )
plt.grid(axis = 'y')
plt.tight_layout()


# In[32]:


plt.figure(figsize=(9,6)) 
plt.bar(x=data['Region'], 
        height=data['Sales'], 
        color='lightblue')
plt.grid(axis = 'y')
plt.xticks(rotation=45)


# In[33]:


data['Sub-Category'].value_counts()


# In[34]:


sb.set(font_scale=1.4)
data['Sub-Category'].value_counts().plot(kind='bar', figsize=(12, 8), rot=0)
plt.xlabel("Category", labelpad=14)
plt.xticks(rotation=90)
plt.ylabel("Count ", labelpad=14)


# In[36]:


plt.figure(figsize=(12,8),)
sb.barplot(x=data['State'].value_counts().head(20).keys(),
            y=data['State'].value_counts().head(20).values,
           palette=("Blues_d")
           )


plt.tight_layout()
plt.xticks(rotation=90)
plt.tick_params(axis='x',
                which='major',
                labelsize=8
                )
plt.grid(axis = 'y')
plt.tight_layout()


# ## Conclusion:
# 1: After doing Analysis of Category and Segment we have figure out that we made more profit in Furniture 60.3 % followed by Office Supplies 21.2% and Technology 18.5% ,Product sold the most to Consumer followed by corporate and home office.
# 
# 2:The top 5 profitable city was New York City, Los Angeles, Philadelphia, San Francisco and Seattle.
# 
# 3:The top 5 profitable city was California, New York, Texas,Pennsylvania and Washington.
# 
# 4:Weak areas where we can work to make more proﬁt is in the Segment of Home office and Corporate products.Along with that we can focus on the Sub-Category product like Machines, Supplies, Bookcases, Envelopes and Labels emphasize more on this product to make profit.

# In[ ]:




