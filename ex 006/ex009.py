numcelsi = float(input('digite a temperatura em celcius : '))
convcelsipfaren = (9*numcelsi/5) + 32
print(f'sua temperatura de {round(numcelsi, 1)} graus celsius \n equivale a {round(convcelsipfaren, 1)} fahrenheit')
numfaren = float(input('digite a temperatura em fahrenheit : '))
convfarenpcelsi = (numfaren - 32) / 1.8
print(f'sua temperatura de {round(numfaren, 1)} fahrenheit \n equivale a {round(convfarenpcelsi, 1)} graus celsius')





