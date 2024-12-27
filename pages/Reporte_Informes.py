import streamlit as st
st.title('Reporte del Análisis de datos')
st.image("img/Reporte.png", width=80)

# Archivo PDF existente
file_path = 'reporte.pdf'

# Leer el contenido del archivo PDF en formato binario
with open(file_path, "rb") as file:
    pdf_data = file.read()

# Crear el botón de descarga
st.download_button(
    label="Descargar PDF",
    data=pdf_data,
    file_name="reporte.pdf",
    mime="application/pdf"
)
