#!/usr/bin/env python
# coding: utf-8

# <div style="border-radius: 20px; border: 3px solid #2E8B57; padding: 20px; background-color: #F0F8FF; font-size: 18px; text-align: center; box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.15);">
#       <h2 style="font-family: 'Verdana', sans-serif; color: #2E8B57; text-transform: capitalize; letter-spacing: 0.5px;">Analysis of Student Scores</h2>
# </div>
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[2]:


scores=pd.read_csv("Expanded_data_with_more_features.csv")


# In[3]:


scores.head()


# In[4]:


scores.shape


# In[5]:


scores.isnull().sum()


# In[6]:


scores.info()


# In[7]:


scores= scores.drop('Unnamed: 0', axis=1)


# In[8]:


scores.info()


# ## Gender Distribution

# In[9]:


plt.figure(figsize=(2,4))
ax= sns.countplot(data=scores, x= 'Gender')
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution between Students")
plt.show()


# ## From the above graph we can see that the number of female students is higher than the male students.

# In[10]:


scores['EthnicGroup'].value_counts()


# In[11]:


scores['LunchType'].value_counts()


# In[12]:


dx= scores.groupby('ParentEduc').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'})
dx


# In[13]:


sns.heatmap(dx, annot= True)
plt.title("Relationship between Parent's education and children's Score")
plt.show()


# ## From the above graph we can conclude that parent's education have a good impact on their children's education 

# In[14]:


mx= scores.groupby('ParentMaritalStatus').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'})
mx


# In[15]:


plt.figure(figsize=(5,4))
sns.heatmap(mx, annot= True)
plt.title("Relationship between Parent's Marital status and children's Score")

plt.show()


# ## From the above graph we can conclude that parent's Marital status have no impact or negligible impact on their children's education 

# In[51]:


scores[['MathScore','ReadingScore','WritingScore']].boxplot(figsize=(5,5))
plt.title("boxplot showing the outliers in 3 subjects")
plt.show()


# ## From the above boxplot we can see that all three subjects have some outliers which is describing that some students have the score out of range as well.
# ## Even one of the student in maths have zero marks. In reading and writing no student have zero marks. so, we can say that comparatively maths is the difficult subject for the students.

# In[17]:


groupA= scores.loc[(scores['EthnicGroup']=='group A')].count()
groupB= scores.loc[(scores['EthnicGroup']=='group B')].count()
groupC= scores.loc[(scores['EthnicGroup']=='group C')].count()
groupD= scores.loc[(scores['EthnicGroup']=='group D')].count()
groupE= scores.loc[(scores['EthnicGroup']=='group E')].count()

l=['groupA','groupB','groupC','groupD','groupE']
mlist=[groupA['EthnicGroup'],groupB['EthnicGroup'],groupC['EthnicGroup'],groupC['EthnicGroup'],groupD['EthnicGroup']]
plt.pie(mlist, labels= l, autopct= "%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()


# ## from the above pie chart we can conclude that Group 'C' and Group 'D' from the Ethnic group are the equally highest groups. 

# In[18]:


scores.info()


# In[52]:


sns.countplot(data=scores, x='NrSiblings')
plt.title("Number of siblings")
plt.show()


# ## From the above chart we can conclude that most of the students have one sibiling only, also there are few students who have 7 sibilings

# In[21]:


scores.info()


# In[29]:


x=pd.crosstab(index=scores['WklyStudyHours'],
              columns=scores['Gender'],
              values=scores['ReadingScore'],
              aggfunc='mean')
x 


# In[53]:


scores['WklyStudyHours'].value_counts().plot(kind='barh')
plt.title("Weekly study hours")
plt.show()


# ## This representing the weekly study hours of the student from which we can conclude that most students are studying 5-10 hours per week 

# In[33]:


gx= scores.groupby('Gender').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'}).reset_index()
gx


# In[49]:


plt.figure(figsize=(10,6))
gx_melted = gx.melt(id_vars="Gender", var_name="Subject", value_name="Average Score")
sns.barplot(x='Subject', y='Average Score', hue='Gender', data=gx_melted)

plt.title('Average Scores by Gender')
plt.ylabel('Average Score')
plt.xlabel('Subject')

plt.show()


# ## from the above graph we can conclude that female students are having highers marks than the male students in Reading and writing, whereas in Math male students have higher score than female students. 

# In[ ]:




