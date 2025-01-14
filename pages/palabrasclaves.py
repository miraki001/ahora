import streamlit as st
import psycopg2
from sqlalchemy import text
from streamlit_extras.stylable_container import stylable_container


col41, mid, col42 = st.columns([1,1,20])
with col41:
    st.image('ic_launcher44.png', width=60)
with col42:
    st.title('Miraki')

st.subheader("Plataforma de Vigilancia Tecnólogica e Inteligencia Competitiva")


col1, col2, col3,col4 = st.columns(4)

tnuri = 0
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''



st.markdown("""
            <style>
            div.stButton {text-align:center}
            div.stButton > button:first-child {
                background-color: #b579c2;
                color:#000000;
                font-weight: bold;
            }
            div.stButton > button:hover {
                background-color: #79adc2;
                color:#ff0000;
                }
            </style>""", unsafe_allow_html=True)



if col1.button("Volver" ,  type='primary'):
    st.switch_page("streamlit_app.py")
if col2.button("Insertar"):
    st.switch_page("./pages/insertar_fuente.py")
if col3.button("Editar"):
    st.switch_page("./pages/editar_fuentes.py")
if col4.button("Borrar"):
    st.switch_page("./pages/borrarfuente.py")   



conn = st.connection("postgresql", type="sql")
qq = 'select palabra,peso from palabras_a_buscar  ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]



pfuente = st.text_input("ingrese el nombre de la palabra")


