idade = int(input('Digite sua idade: '))
print(idade)
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')


frutas = ["banana", "maçã", "ameixa", "manga"]
print(frutas)
if len(frutas) >= 4:
    frutas.append("abacaxi")
else:
    frutas.remove("manga")
print(frutas)