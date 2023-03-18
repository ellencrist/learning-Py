#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas

#importar base de dados
tabela = pandas.read_csv("telecom_users.csv")

#visualizar base de dados
#entender as informações
#descobrir erros na base de dados

#axis-> = linha| axis -> 1 = coluna
tabela=tabela.drop("Unnamed: 0", axis=1) 
display(tabela)


# In[13]:


#tratamento de dados
#resolver os valores que estão sendo reconhecidos de forma errada
tabela["TotalGasto"] = pandas.to_numeric(tabela["TotalGasto"], errors="coerce")

#resolver valores vazios

#colunas em que todos os valores são vazios
tabela = tabela.dropna(how="all", axis=1)

#linhas que tem pelo menos 1 valor vazio
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())


# In[15]:


#analise inicial
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))


# In[23]:


#analise detalhada - descobrir as causas do cancelamento

#comparar cada coluna da base de dados com a columa Churn
import plotly.express as px

#cria o grafico

#para cada coluna da minha tabela, eu quero criar um gráfico.
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)

    #exibe o grafico
    grafico.show()


# In[5]:


get_ipython().system('pip install plotly')


# In[ ]:


conclusões

# Clientes que tem familias maiores tendem a cancelar menos
#    -promoções diferenciadas para mais pessoas da familia

# Os clientes nos primeiros meses tem uma tendência MUITO maior a cancelar
#   -pode ser algum marketing muito agressivo
#   -pode ser que a experiência nos primeiros meses seja ruim
#   -podemos fazer uma promoção de no primeiro ano é mais barato

# Tem algum problema no serviço de fibra

# Quanto mais serviços o cliente tem, menos ele cancela
#   -podemos oferecer mais serviços de graça ou com preço muito menor

#Quase todos os cancelamentos estão no contraro mensal
#   -oferecer desconto anual

# no boleto o cancelamento é  muito maior
#   -oferecer desconto no cartão, no débito automático.

