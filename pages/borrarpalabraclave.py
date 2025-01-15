import streamlit as st
import psycopg2
from sqlalchemy import text

st.set_page_config(layout="wide")
conn = st.connection("postgresql", type="sql")

tpalabra = st.session_state['vpalabra']

with conn.session as session:
  actualiza = 'delete from palabras_a_buscar   where palabra = ' +  tpalabra
  session.execute(text(actualiza) )
  session.commit()
st.switch_page("./pages/palabrasclaves.py")
