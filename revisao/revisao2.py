"""
num = input('informe um numero: ')
print(f'o numero informado foi: {num}')


num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
print(f'a soma foi {num1 + num2}')

nota1 = float(input('digite a nota: '))  
nota2 = float(input('digite a nota: '))  
nota3 = float(input('digite a nota: '))  
nota4 = float(input('digite a nota: '))  
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'sua media foi {media}')


metros = float(input('digite a quantidade em metros: '))
cent = metros * 100
print(f'a conversao de {metros} metros em centimetros eh {cent} centimetros')



raio = float(input('informe o raio: '))
pi = 3.14
area = (raio * raio) * pi
print(f'a area do circulo eh {area}')


lado = float(input('informe o tamanho do lado: '))
area = lado * lado
print(f'a area do quadrado eh {area} e o dobro da area eh {area * 2}')

valorhora = float(input('quanto voce ganha por hora: '))
dias = int(input('quantas dias voce trabalha no mes? '))
horas = dias * 8
salario = valorhora * horas
print(f'voce ganha {salario} p/mes')

f = float(input('informe a temperatura em F: '))
c = 5 *((f - 32) / 9)
print(f'a temperatura de {f} F eh {c} em C')

c = float(input('digite a temperatura em celsius: '))
f = c/5 * 9 + 32
print(f'a temperatura {c} em C eh {f} em F')
"""