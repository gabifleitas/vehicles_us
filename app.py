import streamlit as st
import pandas as pd
import plotly_express as px

car_data_py = pd.read_csv(
    # leer los datos
    'vehicles_us.csv')

# primer encabezado, del histograma
st.header('Crear histograma')

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data_py, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


st.header('Crear grafico de dispersion')

# casilla de verificacion
disp_button = st.checkbox('Construir grafico de dispersion')

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.scatter(car_data_py, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
