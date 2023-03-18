numeros = [1,2,3,4,5]

print(type(numeros)) 

# função "type" retorna o que é "números" 

print(numeros[-1])

numeros[0] = 100

print(numeros)

# funcao "append" adiciona valores na lista

lista_vazia = []
lista_vazia.append("Teste")
lista_vazia.append(1)
lista_vazia.append(True)
lista_vazia.append(2.5)
print(lista_vazia)

index = 0

while index < len(lista_vazia):
    print(lista_vazia[index])
    index = index + 1


for x in lista_vazia:
    print(x)

del lista_vazia[0]
print(lista_vazia)

lista_vazia.pop()
print(lista_vazia)