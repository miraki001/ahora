import streamlit as st

tnuri = st.session_state['vnuri']
st.write(tnuri)
conn = st.connection("postgresql", type="sql")
actualizar = 'update novedades set select_web = :estado,nro_reporte = 0 where nuri = ' + tnuri + ';'

st.write(actualizar)
with conn.cursor() as cur:
        cur.execute(actualizar, params={"estado": "S"} )
        


#df1 = conn.execute(actualizar, ttl="0",params={"estado": "S"} ),
