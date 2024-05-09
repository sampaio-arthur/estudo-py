# exercício 1

nome = 'Volta o cão arrependido. Com suas orelhas tão fartas Com seu osso roído. E com o rabo entre as patas'
contador = 0
for i in range(44):
    nome 
    contador += 1
    print(nome, contador)

# exercercío 2

for i in range(10):
    print(f'tabuada do {i}: ')
    for j in range(10):
        resultado = i * j
        print(f'o resultado de {i} x {j} é {resultado}')
        
# exercício 3

lista = [1, 5, 2, 30, 10, 50, 12, 8, 9, 60]
maior = max(lista)
menor = min(lista)
print(f'o maior valor é {maior} e o menor valor é {menor}')

# exercício 4

lista = [2,12,20,0,1,3,40,7,5,10]
lista.sort()
print(lista)


# exercício 5

file = 'sc.txt'
with open(file, 'r', encoding='utf-8') as teste:
    for indice, linha in enumerate(teste):
        print(indice, linha)

# ou

"""
import pandas as pd
nome_do_arquivo = 'Lista-municipio-populacao.xlsx'
dados = pd.read_excel(nome_do_arquivo)

"""



        
        