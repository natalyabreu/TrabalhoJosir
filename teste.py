import requests
import streamlit as st
import pandas as pd

# Coletar a entrada do usuário
nome_do_filme = st.text_input('Digite o nome de um filme: ')

if st.button('Consultar Filmes'):
    # Verificar se o filme existe na API do OMDb
    link = 'https://www.omdbapi.com/?apikey=90c1591a&t=' + nome_do_filme
    dvd = requests.get(link)
    filme = dvd.json()

    if filme['Response'] == 'True':
        atores = filme['Actors'].split(', ')
        primeiro_ator = atores[0]
        st.write("Atores: ", filme['Actors'])
        st.write("Gênero: ", filme['Genre'])
        st.write("Classificação Indicativa: ", filme['Rated'])
        st.write("\n")

        # Pesquisar por filmes pelo nome do primeiro ator
        link2 = 'https://www.omdbapi.com/?apikey=90c1591a&s=' + primeiro_ator
        dvd2 = requests.get(link2)
        resultados_pesquisa = dvd2.json()

        lista = []
        dados = {
            'Atores': filme['Actors'],
            'Gênero': filme['Genre'],
            'Classificação Indicativa': filme['Rated'],
            'Primeiro Ator': primeiro_ator
        }
        lista.append(dados)

        if resultados_pesquisa['Response'] == 'True' and resultados_pesquisa['totalResults'] != '0':
            filmes = resultados_pesquisa['Search'][:3]  # Limitar o número de filmes a 3
            df = pd.DataFrame(lista)
            st.write(df)
            st.write("Primeiro Ator: ", primeiro_ator)
            st.write("Outros filmes dele:")
            for filme in filmes:
                st.write(filme['Title'])
        else:
            st.write("Não foram encontrados outros filmes para este ator.")
