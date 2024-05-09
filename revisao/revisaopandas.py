import pandas as pd
df = pd.read_html('https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Santa_Catarina')
lista = df[1]
print(lista)