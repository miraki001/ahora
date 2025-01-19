import streamlit as st
import psycopg2
from sqlalchemy import text

st.set_page_config(layout="wide")
conn = st.connection("postgresql", type="sql")

tnuri = st.session_state['vnuri']

with conn.session as session:
  actualiza = 'delete from proyectos   where nuri = ' +  tnuri
  session.execute(text(actualiza) )
  session.commit()
st.switch_page("./pages/proyectos.py")
