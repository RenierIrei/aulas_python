nome = "Pedro"  # str   → texto
altura = 1.78  # int   → número inteiro
idade = 25  # float → número decimal
adulto = True  # bool  → verdadeiro/falso
frutas = ["banana", "maçã", "ameixa", "manga"]  # list  → lista ordenada, permite duplicatas, mutável
posicoes_geograficas = ("latitude", "longitude")  # tuple → lista ordenada, permite duplicatas, imutável
capitais = {
    "Brasil": "Brasilia",
    "Argentina": "Buenos Aires",
    "Japão": "Tóquio",
}  # dict  → chave → valor
cartas_pokemon = {
    "Pikachu", "Kabigon", "Nyaoha", "Eevy", "Kabigon", "Kamonegi",
}  # set   → coleção sem ordem, sem duplicatas

# usando o print
print('Qual seu nome?', nome, 25, 1.78, True)  # se quiser printar algum string use entre aspas simples '', duplas "" ou triplas """"""
url = 'https://www.algumsite.com.br'
if url[0:6] == 'https':
    print('Esta em ordem')
else:
    print(url)
print(url[0:5])
print(frutas[0:2])

