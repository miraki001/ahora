import streamlit as st

tnuri = st.session_state['vnuri']
st.write(tnuri)
conn = st.connection("postgresql", type="sql")
actualizar = 'update novedades set select_web = ' + '"S"' + ',nro_reporte = 0 where nuri = ' + tnuri + ';'

st.write(actualizar)
df1 = conn.query(actualizar, ttl="0"),
