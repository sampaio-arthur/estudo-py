idade = int(input('qual a sua idade? '))
print(f'sua idade é {idade} anos ')
nome = str(input('qual o seu nome? '))
print(f'o seu nome é {nome}')
altura = float(input('qual a sua altura? '))
print(f'sua altura é {altura}')
solteiro = input('Você está solteiro? (Responda com sim ou não): ')
if solteiro == "sim":
    solteiro = True
    print('Você está feliz!')
else:
    solteiro = False
    print('Que merda, irmão!')

print(f'Solteiro: {solteiro}')


