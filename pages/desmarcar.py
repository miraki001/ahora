import streamlit as st
import psycopg2
from sqlalchemy import text

tnuri = st.session_state['vnuri']
st.write(tnuri)
conn = st.connection("postgresql", type="sql")

actualizar = 'update novedades set select_web = :estado,nro_reporte = 0 where nuri = ' + tnuri + ';'
nuri = tnuri
new = 'N'
st.write(actualizar)


with conn.session as session:
    #session.execute(f"UPDATE novedades SET select_web = '{new}' WHERE nuri='{nuri}'")
    session.execute(text("UPDATE novedades SET select_web = :val WHERE nuri= :nuri"), {"val": new,"nuri": nuri})
                        
    session.commit()
    st.success("Data sent")

