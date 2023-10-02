from bs4 import BeautifulSoup
import requests

# requests web page

response = requests.get("https://santodigital.com.br/inteligencia-artificial-o-que-e-e-quais-seus-beneficios")


# obtém o código HTML da página "requisitada"

html = response.text


# faz um "parse" (conversão/ajuste) da página HTML

soup = BeautifulSoup(html, "html.parser")


# obtém apenas o texto do código do "body" da página 

texto = soup.body.get_text().strip()


# texto = texto[:4000]


# separa o texto em uma lista (vetor) de palavras

palavras = texto.replace("\n", " ").split(" ")


# stopwords (palavras comuns (preposições, artigos) que não vamos contar)

stopwords = ["A", "As", "O", "Os", "De", "Da", "Do", "Das", "Dos", 

             "E", "Que", "São", "Um", "É", "Com", "Nos", "Por"]


sumario = []

num = []


# percorre todas as palavras

for palavra in palavras:

  palavra = palavra.replace(",", "").replace(".", "")

  palavra = palavra.capitalize()

  if palavra in stopwords:

    continue

  if palavra in sumario:

    indice = sumario.index(palavra)

    num[indice] = num[indice] + 1

  else:

    sumario.append(palavra)

    num.append(1)


resumo = []


for (s, n) in zip(sumario, num):

  if n > 1:

    resumo.append({"sumario": s, "num": n})


# classifica a lista de dicionários

resumo2 = sorted(resumo, key=lambda res: res["num"], reverse=True)


# print(resumo2)

for i, linha in enumerate(resumo2):

  if i > 20:

    break

  print(f"{linha['sumario']}: {linha['num']} ocorrências")