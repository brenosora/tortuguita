import requests
import json
import time
from unidecode import unidecode


def master():
    response = requests.get("https://covid19-brazil-api.now.sh/api/report/v1")
# Print the status code of the response.
    print(response.status_code)
# Se bem sucedido realiza a coleta de dados
    if response.status_code == 200:

    # Busca a ultima atualização de casos no Brasil
        brasil = requests.get('https://covid19-brazil-api.now.sh/api/report/v1')

    # r = requests.get('https://api.covid19api.com/summary')
    # r = requests.get('https://covid-api-brasil.herokuapp.com/casos')
        resultado = []
        packages_json = brasil.json()

        t1 = time.perf_counter()
        for n in range(len(packages_json['data'])):
            uid       = (packages_json['data'][n]['uid']     )
            uf        = (packages_json['data'][n]['uf']      )
            Estado    = (packages_json['data'][n]['state']   )
            Casos     = (packages_json['data'][n]['cases']   )
            Mortes    = (packages_json['data'][n]['deaths']  )
            Suspeitas = (packages_json['data'][n]['suspects'])
            Recusados = (packages_json['data'][n]['refuses'] )
            Datetime  = (packages_json['data'][n]['datetime'])
    

            dado = {
                'UID': uid,
                'UF': uf,
                'Estado': unidecode(Estado),
                'Casos': Casos,
                'Mortes': Mortes,
                'Suspeitas': Suspeitas,
                'Recusados': Recusados,
                'Data e Hora': Datetime
                    }
            resultado.append(dado)
        
            time.sleep(brasil.elapsed.total_seconds())
        
            print(f'O Estado {Estado} foi coletado em {brasil.elapsed.total_seconds()} segundos')
        
        t2 = time.perf_counter()
        print(f'Terminou em {t2-t1} segundos')
        with open('casos_atualizados_brasil.json', 'w') as f1:
            json.dump(resultado, f1, indent=2)

    
    # Busca por Pais
        pais = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/countries')

    # r = requests.get('https://api.covid19api.com/summary')
    # r = requests.get('https://covid-api-brasil.herokuapp.com/casos')
        resultado3 = []
        packages_json = pais.json()

        t5 = time.perf_counter()

        for n in range(len(packages_json['data'])):
            Pais       = (packages_json['data'][n]['country']     )
            Casos     = (packages_json['data'][n]['cases']   )
            Confirmandos =  (packages_json['data'][n]['confirmed']   )
            Mortes    = (packages_json['data'][n]['deaths']  )
            Recuperados = (packages_json['data'][n]['recovered'])
            Datetime  = (packages_json['data'][n]['updated_at'])
        
            dado3 = {
                'Pais': unidecode(Pais),
                'Casos': Casos,
                'Confirmandos': Confirmandos,
                'Mortes': Mortes,
                'Recuperados': Recuperados,
                'Data e Hora': Datetime
                    }
            resultado3.append(dado3)
        
            
        
            print(f'O Pais {Pais} foi coletado em {pais.elapsed.total_seconds()} segundos')
        
        t6 = time.perf_counter()
        print(f'Terminou em {t6-t5} segundos')
        with open('casos_atualizados_mundo.json', 'w') as f3:
            json.dump(resultado3, f3, indent=2)

