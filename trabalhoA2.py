import requests
import streamlit as st
nome_do_filme = st.text_input('escreva um filme: ')
#é recomendado procurar filmes populares. Link fonte não possui um banco de dados extenso
link = 'https://www.omdbapi.com/?apikey=90c1591a&t=' + nome_do_filme
dvd = requests.get(link)
filme = dvd.json()

# utilizei a chave response para verificar se o filme estava na API
if filme['Response'] == 'True':
    actors = filme['Actors'].split(', ')
    first_actor = actors[0]
    print("Atores: ", filme['Actors'])
    print("Gênero: ", filme['Genre'])
    print("Classificação Indicativa: ", filme['Rated'])
    print("\n")
    
    link2 = 'https://www.omdbapi.com/?apikey=90c1591a&s=' + first_actor  # Search for movies by first actor's name
    dvd2 = requests.get(link2)
    search_results = dvd2.json()

    if search_results['Response'] == 'True' and search_results['totalResults'] != '0':
        movies = search_results['Search'][:3]  # Limit the number of movies to 3

        print("Primeiro ator: ", first_actor)
        print("Outros filmes dele:")
        for movie in movies:
            print(movie['Title'])
    else:
        print("Não foram encontrados outros filmes para este ator.")
