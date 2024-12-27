import streamlit as st
import pandas as pd
# import matplotlib as plt
# import seaborn as sns
import numpy as np

st.title("Leyendo CSV obtenido de la data original")
""" Nombres de columnas cambiados a español """
df = pd.read_csv('data/datosEDA.csv')

rows, cols = df.shape
st.write(f"Registros actuales: {rows} filas y {cols} columnas")
st.write(df)

# Elimina columna duplicada de índices
df = df.drop("Unnamed: 0", axis = 1)
# Elimina personas sin desorden del sueño (celda con None)
df.dropna(subset=['Desorden_Sueño'], axis=0, inplace=True)
# Reemplaza la etiqueta Normal Weight por Normal
df['IMC'] = df['IMC'].replace('Normal Weight', 'Normal', regex=True)


rows, cols = df.shape
st.write(f'Elimina los valores "Normal Weight" por "Normal"')
st.write(f'Elimina los valores vacíos de "Desorden del sueño"')
st.write(f"Elimina columna duplicada de índices: {rows} filas y {cols} columnas")

# reemplaza los valores vacíos de Desorden del sueño
#df[['Desorden_Sueño']] = df[['Desorden_Sueño']].fillna('No registrado')

st.title("Archivo CSV actualizado con EDA: Versión Final")
df = df.copy(deep=True)  # This is a deep copy (copia profunda)
df.to_csv('data/datosEDA_Final.csv') 
st.write(df)

st.title("Subconjunto numérico")
""" Horas de sueño, actividad física, frecuencia cardiaca y pasos diarios """
df_num=df[["Horas_sueño", "Minutos_ActFisica", "Nivel_Stress", "Calidad_sueño" ]]
st.write(df_num.head())
""" ESTADÍSTICA DESCRIPTIVA: todos los registros """
st.write(df_num.describe())

# Gráfico Barras # 1
st.title("Gráfico de barras # 1")
""" HORAS DE SUEÑO PROMEDIO POR DESORDEN DE SUEÑO Y GÉNERO DE LA PERSONA """
# Totales personas por género 
st.write(df["Género"].value_counts())
# Totales personas por desorden de sueño
st.write(df["Desorden_Sueño"].value_counts())

df_barras=df[["Desorden_Sueño", "Horas_sueño", "Género"]]
agg_barra = df_barras.groupby(by=["Género", "Desorden_Sueño"], as_index=False)["Horas_sueño"].mean()
agg_barra.rename({"mean": "Prom_Horas_sueño"}, axis="columns", inplace=True)
st.write(agg_barra.head())
source = agg_barra
st.bar_chart(source, x="Desorden_Sueño", y="Horas_sueño", color="Género", stack=False, horizontal=True, use_container_width=True)
cn1_g1=""
""""""


# Gráfico Barras # 2
st.title("Gráfico de barras # 2")
""" PERSONAS CON TRASTORNOS DE SUEÑO POR OCUPACIÓN Y GÉNERO """

df_barras2=df[["Desorden_Sueño", "Ocupación", "Género", "Horas_sueño"]]
agg_barra2 = df_barras2.groupby(by=["Género", "Desorden_Sueño", "Ocupación"], as_index=False)["Horas_sueño"].count()
agg_barra2.rename({"count": "CantPersonas"}, axis="columns", inplace=True)
st.write(agg_barra2.head())
source = agg_barra2
st.bar_chart(source, x="Ocupación", y="Desorden_Sueño", color="Género", horizontal=True)

# Gráfico Dispersión # 3
st.title("Gráfico de Dispersión")
""" RELACIÓN NIVEL DE ESTRÉS vs HORAS DE SUEÑO Y CALIDAD DE SUEÑO """
st.write(df_num.head())
chart_data = df_num
st.scatter_chart(
    chart_data,
    x="Nivel_Stress",
    y=["Horas_sueño", "Calidad_sueño"],
    color=["#FF0000", "#0000FF"],
)

# Gráfico Áreas # 4
st.title("Gráfico de Áreas")
""" RELACIÓN NIVEL DE ESTRÉS vs HORAS DE SUEÑO Y MINUTOS ACTIVIDAD FÍSICA """
chart_data = df_num
st.area_chart(
    chart_data,
    x="Nivel_Stress", 
    y=["Horas_sueño", "Minutos_ActFisica"],
    color=["#ff5733", "#F08080"],
)