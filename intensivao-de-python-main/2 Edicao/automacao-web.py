get_ipython().system('pip install selenium')

# firefox -> geckodriver
# chrome -> chromedriver
####Importante: baixar o webdriver
# Passo a Passo
# Passo 1: Abrir o navegador
from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")


# Passo 2: Importar a base de dados
import pandas as pd

tabela = pd.read_excel("commodities.xlsx")
display(tabela)

# import unicodedata
# produto = unicodedata.normalize("NFKD", produto).encode("ascii", "ignore")

for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    
    print(produto)
    produto = produto.replace("ó", "o").replace("ã", "a").replace("á", "a").replace(
    "ç", "c").replace("ú", "u").replace("é", "e")
    
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    print(link)
    navegador.get(link)

    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    preco = preco.replace(".", "").replace(",", ".")
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco)
    
    
print("Acabou")
display(tabela)
    
# .click() -> clicar
# .send_keys("texto") -> escrever
# .get_attribute() -> pegar um valor

# Passo 3: Para cada produto da base de dados
# Passo 4: Pesquisar o preço do produto
# Passo 5: Atualizar o preço na base de dados
# Passo 6: Decidir quais produtos comprar


# preencher a coluna de comprar
tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]
display(tabela)

# exportar a base para o excel
tabela.to_excel("commodities_atualizado.xlsx", index=False)

navegador.quit()

