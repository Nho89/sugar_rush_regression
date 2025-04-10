import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib  # Importar joblib para cargar el modelo

st.title("Proyecto Sugar Rush")
st.subheader("Análisis de consumo de azúcar")

st.info("Dataset: [Global Sugar Consumption Trends (1960–2023)](https://www.kaggle.com/datasets/ak0212/global-sugar-consumption-trends-19602023)")
st.markdown("Este conjunto de datos ofrece una exploración exhaustiva de los patrones globales de consumo de azúcar a lo largo de seis décadas, sintetizando datos económicos, agrícolas y de salud pública para descubrir los factores que impulsan y las consecuencias del aumento de la ingesta de azúcar. Abarca el período 1960-2023, con entradas por país y año para más de 200 países.")

#cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv(".data/sugar_consumption.csv")
    return df

df = load_data()
st.dataframe(df.head())