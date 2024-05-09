# exercicio 1

n1 = float(input('digite a sua primeira nota : '))
n2 = float(input('digite a sua segunda nota : '))
n3 = float(input('digite a sua terceira nota : '))
media = (n1 + n2 + n3) / 3
if media >= 7 :
    print('voce foi aprovado')
elif media < 7 and media > 5 :
    print('voce pegou recuperacao')
elif media <= 5 :
    print('voce foi reprovado')


# exercicio 2
    
v1 = int(input('digite o primeiro valor : '))
v2 = int(input('digite o segundo valor : '))
if v1 > v2 :
    print(f'{v1} eh maior que {v2}')
elif v1 == v2 :
    print(f'{v2} sao iguais {v1}')
elif v2 > v1 :
    print(f'{v2} eh maior que {v1}')


# exercicio 3 
    
sexo = str(input('informe seu sexo : '))
if sexo.upper() == 'M' or sexo.upper() == 'F' :
    print('sexo valido')
else :
    print('sexo invalido')


# exercicio 4
    
num1 = int(input(' digite o primeiro numero : '))
num2 = int(input(' digite o segundo numero : '))
if num1 > num2 :
    print(num1 - num2)
elif num1 == num2 : 
    print('0')
elif num2 > num1 :
    print(num2 - num1)



# exercicio 5 / 6

nota1 = float(input('digite a primeira nota (de 0 a 10): '))
nota2 = float(input('digite a segunda nota (de 0 a 10): '))
nota3 = float(input('digite a terceira nota (de 0 a 10): '))
nota4 = float(input('digite a quarta nota (de 0 a 10): '))
sexo = input('digite o sexo do aluno (M ou F): ')
media = (nota1 + nota2 + nota3 + nota4) / 4
if sexo.upper() == 'M' and media >= 6 :
    print('caro aluno, voce foi aprovado')
elif sexo.upper() == 'M' and media < 6 :
    print('caro aluno, voce foi reprovado')
elif sexo.upper() == 'F' and media >= 6 :
    print('cara aluna, voce foi aprovada')
elif sexo.upper() == 'F' and media < 6 :
    print('cara aluna, voce foi reprovada')


#exercicio 7

nint = int(input('digite seu numero inteiro : '))
if nint >= 0 :
    print('numero positivo')
elif nint < 0 :
    print('numero negativo')


# exercicio extra 

x = float(input('digite o comprimento do lado X: '))
y = float(input('digite o comprimento do lado Y: '))
z = float(input('digite o comprimento do lado Z: '))
if x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print('triangulo equilatero')
    elif x == y or x == z or y == z:
        print('triangulo isosceles')
    elif x != y and x != z and y != z :
        print('triangulo escaleno')
else:
    print('os valores nao podem formar um triangulo')

# sampaio, arthur
