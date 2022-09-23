import requests
import json

requisicao = requests.get('https://api.hgbrasil.com/finance?key=2ebfe9dd')
valor = json.loads(requisicao.text)
'''print(valor) '''
dolar = valor['results']['currencies']['USD']['buy']
euro = valor['results']['currencies']['EUR']['buy']
real = float(input('Informe o valor desejado em reais: '))
dolarConvertido = real/dolar
euroConvertido = real/euro
print(f'Valor em dolar: {dolarConvertido}')
print(f'Valor em euro: {euroConvertido}')