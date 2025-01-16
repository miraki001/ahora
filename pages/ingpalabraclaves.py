import streamlit as st
import psycopg2
from sqlalchemy import text


tipo = st.session_state['vTipo'] 
if tipo == 'Editar':
    tpalabra = st.session_state['vpalabra'] 
    tpeso = st.session_state['vpeso'] 

if tipo == 'Ingresar':
    tpalabra = ''
    tpeso = 0


vpalabra = st.text_input("Palabra", tpalabra)

col1, col2, = st.columns(2)
if col1.button("Grabar" ,  type='primary'):
    st.switch_page("./pages/palabrasclaves.py")
if col2.button("Cancelar"):
    st.switch_page("./pages/palabrasclaves.py")
