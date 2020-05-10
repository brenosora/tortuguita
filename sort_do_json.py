import json


#Sort dos Casos Atualizado no Brasil pela UF
def sort_uf(package):
    return package['UF']

with open('casos_atualizados_brasil.json', 'r') as f1:
    brasil = json.load(f1)
    
brasil.sort(key=sort_uf)
brasil_sort = json.dumps(brasil, indent=2)
print(brasil_sort)

#Sort dos Casos em data especifica no Brasil pela UF
def sort_uf(package):
    return package['UF']

with open('casos_atualizados_brasil_data_especifica.json', 'r') as f2:
    data = json.load(f2)
    
data.sort(key=sort_uf)
data_sort = json.dumps(data, indent=2)
print(data_sort)

#Sort dos Casos no Mundo pelo Pais
def sort_uf(package):
    return package['Pais']

with open('casos_atualizados_Mundo.json', 'r') as f3:
    mundo = json.load(f3)
    
mundo.sort(key=sort_uf)
mundo_sort = json.dumps(mundo, indent=2)
print(mundo_sort)