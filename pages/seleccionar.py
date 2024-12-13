import streamlit as st

tnuri = st.session_state['vnuri']
conn = st.connection("postgresql", type="sql")
actualizar = 'update novedades set select_web = ' + 'S' + ' ,nro_reporte = 0 where nuri = ' + tnuri + ';'
df1 = conn.query(actualizar, ttl="0"),
