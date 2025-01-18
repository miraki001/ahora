import streamlit as st
import psycopg2
from sqlalchemy import text

st.set_page_config(layout="wide")
conn = st.connection("postgresql", type="sql")
tnuri = st.session_state['vnuri']


with conn.session as session:
    actualiza = "insert into sectores (nuri,proyecto_nuri,sector,color)"
    actualiza = actualiza + " values (nextval('sectores_seq'),:proyecto_nuri,:sector,:color) ;"
    session.execute(text(actualiza), {"proyecto_nuri": vpro_nuri,"sector": vsector,"color": vcolor})
    session.commit()
