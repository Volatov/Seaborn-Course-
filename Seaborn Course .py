#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


sns.get_dataset_names()


# In[3]:


mpg = sns.load_dataset('mpg')


# In[4]:


mpg


# In[ ]:





# In[ ]:





# In[ ]:


sns.set_theme()


# In[ ]:


sns.set_style('ticks')   #white, darkgrid, whitegrid, dark, ticks


# In[ ]:


sns.set_context('paper', font_scale=1.2)    #paper, talk, poster 


# In[ ]:





# In[10]:


mpg.corr(numeric_only=True)


# In[11]:


sns.heatmap(mpg.corr(numeric_only=True))


# In[16]:


plt.figure(figsize=(10,5))
sns.scatterplot(data=mpg, x='weight', y='mpg', hue="origin", palette="mako")
sns.despine(left=True)


# In[17]:


sns.lineplot(data=mpg, x="model_year", y="mpg")


# In[18]:


sns.pointplot(data=mpg, x="model_year", y="mpg")


# In[19]:


sns.kdeplot(data=mpg, x='weight', y='mpg')


# In[20]:


sns.kdeplot(data=mpg, x='weight', y='mpg', fill=True)


# In[22]:


sns.histplot(data=mpg, x='weight', y='mpg', fill=True)


# In[23]:


sns.histplot(data=mpg,x='mpg')


# In[25]:


sns.histplot(data=mpg,x='mpg', kde=True, bins=5)


# In[26]:


sns.kdeplot(data=mpg,x='mpg')


# In[27]:


sns.ecdfplot(data=mpg,x='mpg')


# In[28]:


sns.rugplot(data=mpg,x='mpg')


# In[29]:


sns.countplot(data=mpg, x='origin')


# In[30]:


sns.barplot(data=mpg, x='origin', y='mpg')


# In[32]:


sns.boxplot(data=mpg, x='origin', y='mpg')


# In[33]:


sns.violinplot(data=mpg, x='origin', y='mpg')


# In[34]:


sns.stripplot(data=mpg, x='origin', y='mpg')


# In[35]:


sns.jointplot(data=mpg,x='weight', y='mpg')


# In[36]:


sns.jointplot(data=mpg,x='weight', y='mpg', kind='reg')


# In[37]:


sns.jointplot(data=mpg,x='weight', y='mpg', kind='hex')


# In[38]:


sns.jointplot(data=mpg,x='weight', y='mpg', kind='kde')


# In[40]:


sns.jointplot(data=mpg,x='weight', y='mpg', kind='kde', fill=True)


# In[41]:


sns.pairplot(data=mpg)


# In[42]:


sns.pairplot(data=mpg, hue='origin')


# In[43]:


tips = sns.load_dataset('tips')


# In[44]:


tips


# In[45]:


sns.relplot(data=tips, x='total_bill', y='tip', col='sex')


# In[46]:


sns.relplot(data=tips, x='total_bill', y='tip', col='time')


# In[47]:


fg = sns.FacetGrid(tips, col='day', row='sex')


# In[50]:


FG = sns.FacetGrid(tips, col='day', row='sex')
FG.map_dataframe(sns.histplot, x="tip")


# In[51]:


FG = sns.FacetGrid(tips, col='day', row='sex')
FG.map_dataframe(sns.scatterplot, x="tip", y='total_bill')


# In[ ]:




