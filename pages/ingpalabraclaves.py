import streamlit as st
import psycopg2
from sqlalchemy import text




col1, col2, = st.columns(2)
if col1.button("Grabar" ,  type='primary'):
    st.switch_page("./pages/palabrasclaves.py")
if col2.button("Cancelar"):
    st.switch_page("./pages/palabrasclaves.py")
