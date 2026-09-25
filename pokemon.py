import requests
import pandas as pd

lista_de_pokemon = ["pikachu", "charmander", "squirtle", "mewtwo"]
dados_finais = []

for pokemon in lista_de_pokemon:
    url_api_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    
    resposta = requests.get(url_api_pokemon)
    dados = resposta.json()

    nome = dados["name"]
    peso = dados["weight"]
    altura = dados["height"]

    peso_kg = peso / 10
    altura_m = altura/10

    imc = peso_kg / (altura_m * altura_m)

    linha = {
        "Nome": nome,
        "Peso": peso_kg,
        "Altura": altura_m,
        "IMC": imc
    }

    dados_finais.append(linha)

df = pd.DataFrame(dados_finais)
df.to_csv("meu_pokemon.csv", index=False)


