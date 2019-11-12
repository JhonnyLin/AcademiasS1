# declarando variavel
# input igual syso
# caixa baixa
# nome = input("digite o seu nome ").lower()
# idade = int(input("digite a sua idade"))

# if nome == 'pedro' and idade == 22 or nome == "dreak":
#     print("Salve Drake")
# elif nome == "murilo":
#     print("Salve henrique enrique")
# else:
#     print("não é ninja")

numero = 0
while numero < 5:
    print(numero)
    numero= numero +1

lista = ['cubo magico', 'pagode japones', 'skate', 'manga com leite']

for item in lista:
    print(item)

for i in range(0, len(lista), 1):
    print(i)

for j in range(len(lista)-1,0,-2):
    print(lista[j])

