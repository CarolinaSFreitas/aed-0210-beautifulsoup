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