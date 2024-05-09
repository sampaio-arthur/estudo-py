num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2


if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Divisão por zero não é possível"

print(f'Soma:, {soma}')
print(f'Subtração:, {subtracao}')
print(f'Multiplicação :, {multiplicacao}')
print(f'Divisão :, {divisao}')


distancia = float(input("Digite a distância total percorrida pelo automóvel (em KM): "))
combustivel = float(input("Digite o total de combustível gasto (em litros): "))
consumo_medio = distancia / combustivel
print(f'Consumo médio do automóvel:, {consumo_medio}')


valor_vendas = float(input("Digite o total do valor (em reais) de vendas efetuadas pelo vendedor: "))
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
comissao = valor_vendas * 0.15
salario_total = salario_fixo + comissao
print(f'Salário total do vendedor:, {salario_total}')


a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
a, b = b, a
print(f'Valor de A após troca:, {a}')
print(f'Valor de B após troca:, {b}')


cotacao = float(input("Digite a cotação do dólar: "))
valor_dolar = float(input("Digite a quantidade de dólares disponíveis: "))
valor_real = valor_dolar * cotacao
print(f'Valor em reais:, {valor_real}')


valor_depositado = float(input("Digite o valor depositado: "))
rendimento = valor_depositado * 0.007  
valor_total = valor_depositado + rendimento
print(f'Valor com rendimento após um mês:, {valor_total}')


valor_compra = float(input("Digite o valor da compra: "))
valor_prestacao = valor_compra / 5
print(f'Valor das prestações:, {valor_prestacao}')

# Arthur Sampaio