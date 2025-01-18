
import streamlit as st
import pandas as pd

# Configurar el título de la aplicación
st.title("📍 Validación de Direcciones y Cobertura")

# Subir archivo .xlsx
st.sidebar.header("Carga tu archivo")
uploaded_file = st.sidebar.file_uploader("Sube un archivo Excel (.xlsx)", type=["xlsx"])

# Procesar el archivo subido
if uploaded_file:
    # Leer el archivo con pandas
    data = pd.read_excel(uploaded_file)
    st.write("### Vista previa de los datos:")
    st.dataframe(data.head())
    
    # Validar si las columnas necesarias existen
    required_columns = {"Direccion", "Ciudad", "Cobertura", "Estrato"}
    if not required_columns.issubset(data.columns):
        st.error(f"El archivo debe contener las columnas: {', '.join(required_columns)}")
    else:
        # Formulario para buscar dirección y ciudad
        st.write("### Buscar dirección y ciudad:")
        direccion = st.text_input("Ingrese la dirección:")
        ciudad = st.text_input("Ingrese la ciudad:")
        
        if st.button("Buscar"):
            # Filtrar datos
            resultado = data[(data["Direccion"] == direccion) & (data["Ciudad"] == ciudad)]
            if not resultado.empty:
                cobertura = resultado["Cobertura"].iloc[0]
                estrato = resultado["Estrato"].iloc[0]
                st.success(f"✅ Cobertura: {cobertura}
🏠 Estrato: {estrato}")
            else:
                st.error("❌ No se encontraron datos para la dirección y ciudad ingresadas.")
else:
    st.warning("Por favor, sube un archivo para continuar.")
