# for muito útil 

soma = 0
cont = 0
i = int(input('digite o número de início: '))
f = int(input('digite o número de fim: '))
p = int(input('digite as a sequência que você quer: '))
for i in range(i, f, p):
    if i % 3 == 0:
        print(i)    
        cont += 1
        soma += i       
print(f'a soma é: {soma} com um total de {cont} números')


# sleep serve muito bem para contagens 

from time import sleep
for i in range(10, 0, -1 ):
	print(i)
	sleep(1)
print(f'feliz ano novo!!!')




