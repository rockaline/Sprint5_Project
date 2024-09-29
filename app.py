import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Aplicativo do Projeto da Sprint 5')

# lendo os dados
car_data = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar histograma')  # criar um botão para histograma
# criar um botão para dispersão
disp_button = st.button('Criar gráfico de dispersão')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig_1 = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_1, use_container_width=True)

if disp_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar uma dispersão
    fig_2 = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_2, use_container_width=True)
