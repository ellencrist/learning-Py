#!/usr/bin/env python
# coding: utf-8

# In[77]:


import pyautogui
import pyperclip
import time
pyautogui.PAUSE = 1

#passo 1: Entrar no sistema da empresa (no link do drive)
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('Enter')

time.sleep(2)

#passo 2: Navegar até o local do relatório (entrar na pasta Exportar)
pyautogui.click(x=530, y=409, clicks=2)
time.sleep(1)

#passo 3: Exportar o relatório (fazer o download)
pyautogui.click(x=612, y=631)#selecionar arquivo
pyautogui.click(x=1602, y=238)#clicar nos três pontos
pyautogui.click(x=1352, y=839)#clicar em fazer download
time.sleep(2)


# In[78]:


#passo 4: Calcular os indicadores(faturamento e quantidade de produtos)
import pandas as pd

#é importante colocar um 'r' no começo de todo caminho 
tabela = pandas.read_excel(r"C:\Users\ielle\Downloads\Vendas - Dez.xlsx")
display(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela ["Quantidade"].sum()

print(faturamento)
print(quantidade)


# In[79]:


#passo 5: Enviar um e-mail para a diretoria

time.sleep(5)

#abrir aba e entrar no email
pyautogui.hotkey('ctrl', 't')
pyperclip.copy("https://mail.google.com/mail/u/3/#inbox")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('Enter')

time.sleep(4)
#clicar no botão escrever
pyautogui.click(x=120, y=239)
#preencher as informações do email
pyautogui.write('gamegam00012@gmail.com')#destinatário
pyautogui.press("tab")#selecionar o email

time.sleep(3)
pyautogui.press("tab")#ir para o campo assunto

pyperclip.copy("relatório de vendas")#assunto
pyautogui.hotkey('ctrl','v')
pyautogui.press("tab")#ir para o corpo do email

#corpo
texto = f'''Prezados bom dia,
O faturamento desse mês foi de R${faturamento:,.2f} , com a quantidade de {quantidade:,} itens vendidos!
 
 atenciosamente, ellencrist
 '''
pyperclip.copy(texto) 
pyautogui.hotkey('ctrl', 'v')

#enviar o email
pyautogui.hotkey('ctrl', 'enter')


# # use esse código para descobrir qual posição de um item que queira clicar

# In[80]:


import time

time.sleep(5)
pyautogui.position()


# In[81]:


pip install pyautogui

