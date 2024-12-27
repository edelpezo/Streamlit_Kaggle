import streamlit as st
import pandas as pd

st.title('Carga de Dato desde Kaggle')

# botón de carga de archivos CSV
st.write("Archivos fuentes CSV:")
uploaded_file = st.file_uploader("Seleccione el archivo", type="csv", accept_multiple_files=False)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.title("Datos originales")   
    st.write(df)

    # renombro columnas para conocer la medida que representa
    #    axis = 0 horizontal/filas y axis = 1 vertical/columnas, acepta "rows" o "columns"
    #    inplace = True actualiza el dataset y False crea una copia
    
    st.title("Renombrar columnas: identificar la medida que representa")
    """ No hay filas vacías o con datos erróneos """
    df.rename({"Sleep Duration":"Horas_sueño", "Occupation":"Ocupación",
        "Age":"Edad", "Gender": "Género", "Person ID":"ID_Persona",
        "Quality of Sleep": "Calidad_sueño",
        "Physical Activity Level": "Minutos_ActFisica", 
        "Stress Level": "Nivel_Stress", "BMI Category": "IMC",
        "Blood Pressure": "Presión_Arterial", "Heart Rate":"FrecCardiaca_reposo", 
        "Daily Steps": "Pasos_Diarios", "Sleep Disorder": "Desorden_Sueño"  },
        axis="columns", inplace=True)
    st.write(df)

    """ Nuevo archivo CSV con EDA: ver carpeta data """
    df = df.copy(deep=True)  # This is a deep copy (copia profunda)
    df.to_csv('data/datosEDA.csv') 
    st.write(df)
  


