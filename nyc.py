import streamlit as st
import pandas as pd
import numpy as np

st.title('Cicle Rides in NYC')
st.sidebar.image("credencial.jpeg")
st.sidebar.title('Brian Sanchez Robles')
st.sidebar.title('S19004873')
st.sidebar.title('zS19004873@estudiantes.uv.mx')
st.sidebar.markdown("##")


DATE_COLUMN = 'started_at'
DATA_URL = ('archivo.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

datos = st.text('Loading cicle nyc data...')
data = load_data(500)
datos.text("Done! (using st.cache)")



if st.sidebar.checkbox('Tabla'):
    st.subheader('Raw data')
    st.write(data)
    
    

if st.sidebar.checkbox('Recorrido por horas '):
    st.subheader('Numero de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)


horaFiltro = st.sidebar.slider('Hora', 0, 23, 1)
datosFiltrados = data[data[DATE_COLUMN].dt.hour == horaFiltro]


st.subheader('Mapa de recorrido a las %s:00 hrs' % horaFiltro)
st.map(datosFiltrados)



