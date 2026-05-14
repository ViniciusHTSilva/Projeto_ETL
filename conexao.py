import requests

# injestao de dados por uma api

def buscar_dados():

    url = 'https://api.openbrewerydb.org/v1/breweries'

    params = {
        "page": 1,
        "per_page": 200,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

    else:
        print('Erro de conexão')
        return []


print(len(buscar_dados()))
