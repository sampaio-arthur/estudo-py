# exercício 1

num = int(input('digite um número inteiro maior que 0: '))
soma = 0
i = num - 1
while i > 0:
    soma += i
    i -= 1
print(f'a soma dos números menores que {num} é: {soma}')

# exercício 2

soma_idades = 0
for _ in range(5):
    idade = int(input('digite uma idade: '))
    soma_idades += idade
media = soma_idades / 5
print(f'a média das idades é: {media}')

#exercício 3

inicio = int(input('digite o primeiro número inteiro: '))
fim = int(input('digite o segundo número inteiro (maior que o primeiro): '))
print(f'números pares entre {inicio} e {fim}: ')
for i in range(inicio + 1, fim):
    if i % 2 == 0:
        print(i)

# exercício 4

inicio = int(input('digite o primeiro número inteiro: '))
fim = int(input('digite o segundo número inteiro (maior que o primeiro): '))
print(f'números ímpares entre {inicio} e {fim}: ')
for i in range(inicio + 1, fim):
    if i % 2 != 0:
        print(i)

# exercício 5

soma = 0
while True:
    numero = int(input('digite um número inteiro (negativo para parar): '))
    if numero < 0:
        break
    soma += numero
print(f'a soma dos números digitados é: {soma}')


# exercício 6

soma = 0
for _ in range(5):
    numero = int(input('digite um número inteiro: '))
    soma += numero
print(f'a soma dos números é: {soma}')
if soma % 2 == 0:
    print(f'a soma é um número par')
else:
    print(f'a soma é um número ímpar')


# exercício 7

numero = int(input('digite um número inteiro positivo: '))
if numero <= 1:
    print(f'o número não é primo')
else:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f'o número é primo')
    else:
        print(f'o número não é primo')


# exercício 8

numero = int(input('digite um número inteiro para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')


# exercício 9 

numero = int(input('digite um número inteiro maior que zero: '))
for i in range(numero):
    print(f'o dobro de {i} é: {2*i}')





