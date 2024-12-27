import streamlit as st
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
import pickle
from sklearn.preprocessing import LabelEncoder

st.title('Regresión')
df = pd.read_csv('data/datosEDA.csv')
df = df.drop("Unnamed: 0", axis = 1)
df.to_csv('data/datosEDA_modificado.csv', index=False)
df_registros = pd.read_csv('data/datosEDA_modificado.csv')


# este código transformará "Masculino" a 1 y "Femenino" a 0.
""" Género: Masculino 1, Femenino 0 \n"""
""" Desorden_sueño: Apnea 1, Insomnio 0 \n"""
""" IMC: Normal 0, Obeso 1, Sobrepeso 2 \n"""
label_encoder = LabelEncoder()
df_registros['Género'] = label_encoder.fit_transform(df_registros['Género'])
df_registros['Desorden_Sueño'] = label_encoder.fit_transform(df_registros['Desorden_Sueño'])
df_registros['IMC'] = label_encoder.fit_transform(df_registros['IMC'])

st.title("Tabla base de trabajo")
st.write(df_registros)

#-----------------------------------------------------------------------------------------------
#    Desorden_Sueño, ¿qué factores contribuyen a a existencia de trastornos del sueño?
#-----------------------------------------------------------------------------------------------
st.title("Predicción de Desórdenes del Sueño")
x_ds=df_registros[["Horas_sueño", "Edad", "Género", "Calidad_sueño", "IMC",
        "Minutos_ActFisica", "Nivel_Stress", "FrecCardiaca_reposo", "Pasos_Diarios"]]
y_ds=df_registros[["Desorden_Sueño"]]

"""Variables independientes (X): Horas_sueño, Edad, Género, Calidad_sueño, IMC, Minutos_ActFisica, Nivel_Stress, FrecCardiaca_reposo, Pasos_Diarios"""
"""Variable dependiente (Y): Desorden_Sueño"""

# Dividir datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x_ds, y_ds, test_size=0.2, random_state=30)

# Entrenar modelo
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Guardar el modelo con pickle
with open("modelo_desorden_sueño.pkl", "wb") as file:
       pickle.dump(model, file)

# Predicciones
y_pred = model.predict(x_test)
st.write("Predicciones del modelo:", y_pred)
st.write("Valores reales (de prueba):", y_test)

# Precisión
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Precisión del modelo: {accuracy:.2f}")    


#-----------------------------------------------------------------------------------------------
#    Calidad_sueño, ¿qué factores afectan la calidad del sueño?
#    Horas_sueño: ¿se quiere predecir la cantidad de horas que una persona duerme basada en 
#                 factores como la edad, nivel de estrés, otros? 
#-----------------------------------------------------------------------------------------------
st.title("Predicción de Calidad del Sueño")
x2_ds=df_registros[["Horas_sueño", "Edad", "Género", "Desorden_Sueño", "IMC",
        "Minutos_ActFisica", "Nivel_Stress", "FrecCardiaca_reposo", "Pasos_Diarios"]]
y2_ds=df_registros[["Calidad_sueño"]]

"""Variables independientes (X): Horas_sueño, Edad, Género, Desorden_Sueño, IMC, Minutos_ActFisica, Nivel_Stress, FrecCardiaca_reposo, Pasos_Diarios"""
"""Variable dependiente (Y): Calidad_sueño"""

# Dividir datos en entrenamiento y prueba
x2_train, x2_test, y2_train, y2_test = train_test_split(x2_ds, y2_ds, test_size=0.2, random_state=30)

# Entrenar modelo
model2 = RandomForestClassifier()
model2.fit(x2_train, y2_train)

# Guardar el modelo con pickle
with open("modelo_calidad_sueño.pkl", "wb") as file2:
       pickle.dump(model2, file2)

# Predicciones
y2_pred = model2.predict(x2_test)
st.write("Predicciones del modelo:", y2_pred)
st.write("Valores reales (de prueba):", y2_test)

# Precisión
accuracy = accuracy_score(y2_test, y2_pred)
st.write(f"Precisión del modelo: {accuracy:.2f}")
