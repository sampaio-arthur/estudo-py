preco_unidade = float(input('digite o preço por unidade: '))
quantidade = int(input('digite a quantidade : '))
valor_pago = float(input('digite o valor pago pelo cliente: '))
custo_total = quantidade * preco_unidade
troco = valor_pago - custo_total
print(f' foram comprados {quantidade} itens \n custo total de {custo_total} \n o cliente pagou {valor_pago}  \n pague o troco de {troco} reais')
