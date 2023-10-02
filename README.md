# Aula de 02/10 de Algoritmos e Estruturas de Dados I 

**Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc/**

O html usado: https://natosafe.com.br/beneficios-da-inteligencia-artificial/

1. ` pip install beautifulsoup4 `
2.
````
from bs4 import BeautifulSoup

import requests

# requests web page 
response = requests.get("https://natosafe.com.br/beneficios-da-inteligencia-artificial/")

# obtém o código HTML da página requisitada

html = response.text

# faz um "parse" (conversão/ajuste) da página html

soup = BeautifulSoup(html, "html.parse")

#mostra apenas o texto do código do body da página
print(soup.body.get_text().strip())
````
