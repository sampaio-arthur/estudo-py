# def soma(num1, num2):
#     return print(f'a soma é {num1 + num2}')
  
# soma(int(input('primeiro número: ')), int(input('segundo número: ')))

def somarial(num):
    soma = 0
    while num > 0:
        num += -1
        soma += num
    return print(f'a soma é: {soma}')
somarial(int(input('digite um número: ')))




  
    
