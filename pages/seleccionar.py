import streamlit as st


conn = st.connection("postgresql", type="sql")
actualizar = 'update novedades set select_web = ' + 'S' + ' ,nro_reporte = 0 where nuri = ' + vnuri + ';'
df1 = conn.query(actualizar, ttl="0"),
