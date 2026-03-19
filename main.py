from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'message': 'Hello, World!'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurantes: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurantes is None:
            return {'Dados': dados_json}

        dados_restaurantes = {}
        for item in dados_json:
            if item['Company'] == restaurantes:
                 
                nome_do_restaurante = item['Company']
                dados_restaurantes[nome_do_restaurante].append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        else:
            print(f'O erro foi: {response.status_code}')
