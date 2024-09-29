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

# Criar um selectbox para escolher o tipo de veículo
vehicle_types = car_data['type'].unique()  # Obtém os tipos de veículos únicos
selected_vehicle_type = st.selectbox(
    'Selecione o tipo de veículo:', vehicle_types)

# Filtrar os dados com base no tipo de veículo selecionado
filtered_data = car_data[car_data['type'] == selected_vehicle_type]

# Criar o gráfico de barras usando Plotly Express
fig = px.bar(filtered_data, x='model',
             title=f"Veículos do tipo {selected_vehicle_type} por modelo",
             labels={'model': 'Modelo', 'count': 'Contagem'},
             text_auto=True)

# Exibir o gráfico interativo no Streamlit
st.plotly_chart(fig, use_container_width=True)
