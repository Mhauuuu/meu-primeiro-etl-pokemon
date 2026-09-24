import requests
import pandas as pd

url_api_pokemon = "https://pokeapi.co/api/v2/pokemon/pikachu"
resposta = requests.get(url_api_pokemon)
dados = resposta.json()

#print(dados)

nome = dados["name"]
peso = dados["weight"]
altura = dados["height"]

peso_kg = peso / 10
altura_m = altura/10

imc = peso_kg / (altura_m * altura_m)

#print(f" O pokemón {nome} tem o imc de {imc:.2f}")

dicionario_tabela = {
    "Nome": [nome], 
    "Peso": [peso_kg], 
    "Altura":[altura_m], 
    "IMC": [imc]
}


df = pd.DataFrame(dicionario_tabela)
df.to_csv("meu_pokemon.csv", index=False)


