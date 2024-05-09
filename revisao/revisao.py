#  Descreva brevemente o que é um algoritmo e por que é importante na programação: algoritmo é uma sequência de passo que realiza uma determinada tarefa, ele é importante pois, é a base para a resolução de problemas utlizando linguagem de programção.

# Dê um exemplo simples de um algoritmo para encontrar o maior número em uma lista.
lista = [1, 20, 10, 8 , 15]
print(max(lista))

#Explique a diferença entre eficiência de tempo e eficiência de espaço em algoritmos: eficiência de tempo é o quão rápido o seu algoritmo pode ser executado e eficiência de espaço é o quanto de memória é necessário para rodar o algoritmo.

#Liste pelo menos três linguagens de programação e suas principais áreas de aplicação: python - análise de dados, php - web, JavaScript - web.

# O que são variáveis em programação? Por que são importantes? 
# variáveis como já diz o nome são variantes que podem possuir qualquer valor e são extremamente importantes para a criação de algoritmos.

# Explique o conceito de "palavras reservadas" em Python. Dê exemplos: sao palavras que ja possuem uma funcao propria, ao declarar uma variavel com uma palavra reservada, ela atomaticamente perde aquela funcao. exemplo: and, or.

#Liste e explique brevemente os operadores aritméticos em Python: "+"" -> soma. "-" -> subtração. "/" -> divisão. "%" -> resto da divisão. "*" -> multiplicação. "**" -> potenciação.

#Quais são os operadores de atribuição em Python?
#Operador de atribuição com adição (+=): adiciona o valor à variável e atualiza o valor da variável. Operador de atribuição com subtração (-=): subtrai o valor da variável e atualiza o valor da variável. Operador de atribuição com multiplicação (*=): multiplica o valor da variável e atualiza o valor da variável

#Explique a diferença entre operadores relacionais e operadores lógicos: operadores relacionais são utilizados para comparar dois valores, já os operadores logicos sao utilizados apra comparar dois ou mais valores.

#Escreva um algoritmo em Python que determine se um número é par ou ímpar

num = int(input('digite um numero: '))
if num % 2 == 0:
    print('o numero é par!')
else:
    print('o numero é ímpar!')
    
# Escreva um programa que peça a idade do usuário e, em seguida, determine se ele é maior de idade (idade >= 18) ou não

idade = int(input('coloque a sua idade: '))
if idade >= 18:
    print('você é de maior!')
else:
    print('você é de menor!')

# Explique a diferença entre if, elif e else em Python: if é uma condição que se for verdadeira executa o bloco de código, else é uma condição que só executa quando if for falso e elif é a mistura de else com if.

#Escreva um programa que imprima os números de 1 a 10 usando um loop while
num = 0
while num < 10:
    num +=1
    print(num)

 #Escreva um programa que calcule a soma dos números de 1 a 100 usando um loop for
 
soma = 0
for i in range(0,100):
    i+=1
    soma += i
    print(i)
print(soma)

#  Explique a diferença entre os loops while e for: for é iterado um número determinado de vezes já o while só para de executar quando satisfazer uma condição.