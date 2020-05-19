import json
from collections import defaultdict

def json_br():
	f = open('casos_atualizados_brasil.json',)

	data = json.load(f)
	#print(data)
	f.close()
	return data
	

def json_za_warudo():
	f = open('casos_atualizados_mundo.json',)

	data = json.load(f)
	#print(data)
	f.close()
	return data

def mortes():
	data = json_br()
	c = defaultdict(int)
	for d in data:


	    c[d['Data e Hora']] += d['Mortes']

	data = [{'Data e Hora': dta , 'Mortes': mortes} for dta, mortes in c.items()]
	#print('mortes: ',data[0]['Mortes'])
	return data[0]['Mortes']

def casos():
	data = json_br()
	c = defaultdict(int)
	for d in data:


	    c[d['Data e Hora']] += d['Casos']

	data = [{'Data e Hora': dta , 'Casos': casos} for dta, casos in c.items()]
	#print('casos: ',data[0]['Casos'])
	return data[0]['Casos']

def suspeitas():
	data = json_br()
	c = defaultdict(int)
	for d in data:


	    c[d['Data e Hora']] += d['Suspeitas']

	data = [{'Data e Hora': dta , 'Suspeitas': suspeitas} for dta, suspeitas in c.items()]
	#print('suspeitas: ',data[0]['Suspeitas'])
	return data[0]['Suspeitas']

def recusados():
	data = json_br()
	c = defaultdict(int)
	for d in data:


	    c[d['Data e Hora']] += d['Recusados']

	data = [{'Data e Hora': dta , 'Recusados': recusados} for dta, recusados in c.items()]
	#print('recusados: ',data[0]['Recusados'])
	return data[0]['Recusados']

'''
def sort_big():
	list_big = []
	data = json_za_warudo()
	for x in data:
		list_big.append(x['Pais'])
		list_big.append(x['Mortes'])
	print(list_big)
'''
#sort_big()



'''
a idéia é pegar os 10 dicionarios com o maior numero de mortes e usar isso 
pra dar o display no index.html

rodar a lista, pegar todos os keys e values mortes e colocar em uma lista

'''