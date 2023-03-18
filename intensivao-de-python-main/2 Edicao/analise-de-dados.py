# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")
# deletar a coluna inútil

# axis = 0 - se for linha ; axis = 1 se for coluna
tabela = tabela.drop("Unnamed: 8", axis=1)

# Passo 2: Visualizar a base de dados
    # Entender as informações que você tem disponível
    # Procurar cagadas na base de dados
display(tabela)


# In[6]:


# Passo 3: Tratamento de Dados

# acertar informações que estão sendo reconhecidas de forma errada
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")


# corrigir informações vazias
# display(tabela[tabela["Profissão"].isna()])

tabela = tabela.dropna()
print(tabela.info())


# In[7]:


# Passo 4: Análise Inicial -> Entender as notas dos clientes
display(tabela.describe())


# In[12]:


# quanto maior o salário, maior a nota
# clientes de promoção são piores
import plotly.express as px

# cria o grafico

# Passo 5: Análise Completa -> entender como cada característica do cliente impacta na nota
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    # exibe o gráfico
    grafico.show()


# In[ ]:


# Perfil ideal de cliente
# Acima de 15 anos (não tem muita diferença entra as faixas etárias depois disso)
# Faixa salarial não parece fazer tanta diferença
# Áreas de trabalho: Entretenimento e Artista (evitar Construção)
# Tem entre 10 e 15 anos de experiência
# Com familías não tão grandes (até no máximo 7 pessoas)


# In[10]:


get_ipython().system('pip install plotly')

