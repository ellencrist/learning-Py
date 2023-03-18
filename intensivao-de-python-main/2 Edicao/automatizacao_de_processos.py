#!/usr/bin/env python
# coding: utf-8

# In[63]:


get_ipython().system('pip install pyautogui')


# In[17]:


import pyautogui
import time

#pyautogui.click -> clique com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar uma tecla
#pyautogui.hotkey -> apertar uma combinação de textos(ex: Ctrl + D)

pyautogui.PAUSE = 0.5

#entrar no sistema da empresa
pyautogui.hotkey("ctrl","t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
#pode ser que o navegador tenha que carregar
time.sleep(4)

#fazer login
#clicar no espaço de login
pyautogui.click(x=930, y=514)
#digitar o login
pyautogui.write("meu_login")

#clicar no espaço de senha
pyautogui.click(x=888, y=620)
#digitar a senha
pyautogui.write("minhasenha")
#clicar em acessar
pyautogui.click(x=848, y=742)
time.sleep(3)

#exportar base de dados
pyautogui.click(x=559, y=397) #seleciona o arquivo
pyautogui.click(x=1055, y=251) #clica na lista de opcoes
pyautogui.click(x=1149, y=869) #faz o download
time.sleep(3)


# In[67]:


#calcular os indicadores

import pandas as pd

tabela = pd.read_csv(r"Compras.csv")
display(tabela)

total_gasto = tabela["Valorfinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)


# In[74]:


import pyperclip

#enviar um email

#entrar no email
pyautogui.hotkey("ctrl","t")
pyautogui.write("https://mail.google.com/mail/u/3/#inbox")
pyautogui.press("enter")
time.sleep(4)

#clicar no botão inscrever
pyautogui.click(x=160, y=232)

#preencher as informações do email
pyautogui.write("seuemail@gmail.com")
pyautogui.press("tab")

#avançar para o campo assunto
pyautogui.press("tab")
pyperclip.copy("Relatório de vendas")
pyautogui.hotkey("ctrl", "v")

#corpo do email
pyautogui.press("tab")


texto = f"""
Prezados, 
segue o relatório de vendas com:
o total gasto: R${total_gasto:,.2f}
a quantidade de produtos: R${quantidade:,.2f}
e seu preço médio: R${preco_medio:,.2f}

Dúvidas? estou a disposição.
At.te

"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

#enviar
pyautogui.hotkey("ctrl","enter")


# In[73]:


time.sleep(5)
print(pyautogui.position())


# In[ ]:




