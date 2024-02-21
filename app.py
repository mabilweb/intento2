import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Mi primera aplicación', divider='rainbow')

car_data = pd.read_csv(open("vehicles_us.csv")) # leer los datos


hist_button = st.button('Construir histograma') # crear un botón
hist_button2 = st.button('Construir dispersión') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 

        
if hist_button2: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer",y='price')
    st.plotly_chart(fig, use_container_width=True) 


build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")