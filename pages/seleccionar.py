import streamlit as st
import psycopg2

tnuri = st.session_state['vnuri']
st.write(tnuri)
conn = st.connection("postgresql", type="sql")

actualizar = 'update novedades set select_web = :estado,nro_reporte = 0 where nuri = ' + tnuri + ';'
nuri = tnuri
new = 'S'
st.write(actualizar)

try:
    conn.query(f"UPDATE novedades SET select_web = '{new}' WHERE nuri='{nuri}'")

    conn.commit()
except Exception as e:
    print(e)
finally:
    st.write("Yessss!!")

#cursor = conn.cursor()
#cursor.execute(actualizar, "S")


#df1 = conn.execute(actualizar, ttl="0",params={"estado": "S"} ),
