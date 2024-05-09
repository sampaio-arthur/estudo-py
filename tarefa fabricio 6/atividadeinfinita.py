# exercício 1

numero = int(input('digite um número: '))

def verificar(numero):
    if numero >= 0 and numero <= 10:
        print(f"o número '{numero}' está entre 0 e 10")
    else:
        print(f"o número '{numero}' não está entre 0 e 10")

verificar(numero)

# exercício 2
x = 0
y = 0
num1 = int(input('digite um número: '))
num2 = int(input('digite um número: '))
num3 = int(input('digite um número: '))

def maior(x):
    if num1 > num2 and num1 > num3 :
        return num1
    elif num2 > num1 and num2 > num3 :
        return num2
    elif num3 > num1 and num3 > num2:
        return num3

def menor(y):
    if num1 < num2 and num1 < num3 :
        return num1
    elif num2 < num1 and num2 < num3 :
        return num2
    elif num3 < num1 and num3 < num2:
        return num3
print(f' o maior é {maior(x)} e o menor é {menor(y)}')

# exercício 3

def fatorial_loop(n):
    if n < 0:
        return "Erro: número negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial

def fatorial_recursivo(n):
    if n < 0:
        return "Erro: número negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

num = int(input("Digite um número não-negativo: "))
print("Fatorial (loop):", fatorial_loop(num))
print("Fatorial (recursivo):", fatorial_recursivo(num))


# exercício 4

n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))
prompt = str(input('digite a operação: (+, -, /, *): '))
z = 0
def menu(z):
    if prompt == '+':
       print(f'resultado da soma {n1 + n2}')
    elif prompt == '-':
        print(f'resultado da subtração {n1 - n2}')
    elif prompt == '/':
        print(f'resultado da divisão {n1 / n2}')
    elif prompt == '*':
        print(f'resultado da multiplicação {n1 * n2}')

menu(z)


        
    

