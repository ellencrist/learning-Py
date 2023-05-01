#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


df = pd.read_csv('C:/Users/Administrador/Downloads/Banco de Dados Empresa - Base.csv')


# In[12]:


df.head()


# In[13]:


df.shape


# In[14]:


df.info()


# In[15]:


df.describe()


# In[16]:


df['Idade'].describe()


# In[18]:


df['Idade'].mean()


# In[19]:


df['Idade'].median()


# In[21]:


df['Idade'].plot(kind='box', vert = False, figsize=(14,6))


# In[22]:


df['Idade'].plot(kind='density', figsize=(14,6))


# In[26]:


ax = df['Idade'].plot(kind='density', figsize=(14,6))
ax.axvline(df['Idade'].mean(), color = 'red')
ax.axvline(df['Idade'].median(), color = 'green')


# In[27]:


ax = df['Idade'].plot(kind='hist', figsize=(14,6))
ax.set_ylabel('Funcionários')
ax.set_xlabel('Idade')


# In[49]:


df.head()


# In[52]:


df['CampoEducacao'].value_counts()


# In[54]:


df['CampoEducacao'].value_counts().plot(kind='pie', figsize=(6,6))


# In[56]:


ax = df['CampoEducacao'].value_counts().plot(kind= 'bar', figsize=(14,6))
ax.set_ylabel('Campo de Educação')


# In[58]:


correlacao = df.corr()
correlacao


# In[69]:


fig = plt.figure(figsize = (8,8))
plt.matshow(correlacao, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(correlacao.columns)), correlacao.columns, rotation='vertical');
plt.yticks(range(len(correlacao.columns)), correlacao.columns)


# In[73]:


df.plot(kind='scatter', x = 'AnosMesmoGestor', y = 'AnosEmpresa', figsize=(14,6))


# In[77]:


ax = df[['NivelnoTrabalho', 'Renda Mensal']].boxplot(by='NivelnoTrabalho', figsize=(14,6))
ax.set_ylabel('Renda Mensal')


# In[78]:


boxplot_colunas = ['Idade', 'Diária', 'DistanciadeCasa']
df[boxplot_colunas].plot(kind='box', subplots=True, figsize=(14,8))

