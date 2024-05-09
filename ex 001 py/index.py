qtde_coca = 150
qtde_pepsi = 130
preco_coca = 1.50
preco_pepsi = 1.50
custo_loja = 2500
faturamento = (qtde_coca * preco_coca) + (qtde_pepsi * preco_pepsi)
lucro = faturamento - custo_loja
margem = lucro / faturamento
print(margem)
