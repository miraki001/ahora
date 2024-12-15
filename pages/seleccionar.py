import streamlit as st
import psycopg2

tnuri = st.session_state['vnuri']
st.write(tnuri)
conn = st.connection("postgresql", type="sql")

actualizar = 'update novedades set select_web = :estado,nro_reporte = 0 where nuri = ' + tnuri + ';'
nuri = tnuri
new = 'S'
st.write(actualizar)

with conn.session as session:
    session.execute(f"UPDATE novedades SET select_web = '{new}' WHERE nuri='{nuri}'")
    session.commit()
    st.success("Data sent")

try:
    conn.query(f"UPDATE novedades SET select_web = '{new}' WHERE nuri='{nuri}'")
    st.write('antes')
    conn.commit()
    com.close()
except Exception as e:
    st.write('antes eee   ')
    st.write(e)
    print(e)
finally:
    st.write("Yessss!!")

#cursor = conn.cursor()
#cursor.execute(actualizar, "S")


#df1 = conn.execute(actualizar, ttl="0",params={"estado": "S"} ),
