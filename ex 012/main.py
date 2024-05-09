# exercício 4
lista = [2,12,20,0,1,3,40,7,5,10]


# exercício 5

file = 'cidade.txt'

teste = open(file, 'r', encoding='utf-8')  
for indice, linha in enumerate(teste):
    print(indice, linha)
teste.close()
