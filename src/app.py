import streamlit as st
import pandas as pd
from utils.data_processing import load_data
from utils.visualization import plot_distribution, plot_correlation

st.title('Análisis Descriptivo de los Países Más Felices del Mundo 2024')
st.write('Esta aplicación realiza un análisis descriptivo del dataset de los países más felices del mundo en 2024.')

# Ruta del archivo CSV relativa a la carpeta raíz del proyecto
file_path = 'happiest-countries-in-the-world-2024.csv'
df = load_data(file_path)
st.write(df.describe())

st.write('### Visualizaciones')
plot_distribution(df, 'happiness_score')
st.image('distribution_happiness_score.png')

plot_correlation(df)
st.image('correlation_matrix.png')

country = st.text_input('Ingrese el nombre de un país:')
if st.button('Filtrar'):
    filtered_df = df[df['country'] == country]
    st.write(filtered_df.describe())
    plot_distribution(filtered_df, 'happiness_score')
    st.image('distribution_happiness_score.png')

