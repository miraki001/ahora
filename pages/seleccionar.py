import streamlit as st

tnuri = st.session_state['vnuri']
st.write(tnuri)
conn = st.connection("postgresql", type="sql")
actualizar = 'update novedades set select_web = :estado,nro_reporte = 0 where nuri = ' + tnuri + ';'

st.write(actualizar)

cursor = conn.cursor()
cursor.execute(actualizar)


#df1 = conn.execute(actualizar, ttl="0",params={"estado": "S"} ),
