import streamlit as st
import psycopg2
from sqlalchemy import text

st.set_page_config(layout="wide")
conn = st.connection("postgresql", type="sql")

#vtitulo = st.session_state['vtitulo']
vtitulo1 = "eeeeee"

fuente = st.session_state['vdescrip'] 
pais = st.session_state['vpais'] 
activa = st.session_state['vactiva'] 

tnuri = st.session_state['vnuri']
url = st.session_state['vfuente']

st.markdown("""
<style>
    .stTextInput input[aria-label="**Titulo**"] {
        background-color: #0066cc;
        color: #33ff33;
    }
    .stTextInput input[aria-label="test color2"] {
        background-color: #cc0066;
        color: #ffff33;
    }
</style>
""", unsafe_allow_html=True)




#st.write("QueryParams: ", st.query_params)
#st.write('session')
#st.write(st.session_state)
#value  = int(st.query_params.get("nuri", vnuri))
#st.write(st.session_state['vnuri'])
#st.write(st.session_state['vtitulo'])
#title = st.text_input("Movie title", "Life of Brian")
st.header(":blue[fuente]")

vtitle = st.text_input("fuente", fuente)
vurl = st.text_input("url ", url)

pais =  st.text_input("pais", st.session_state['vpais'])
activa = st.text_input("Activa", st.session_state['vactiva'])
separador = st.text_input("Separado", st.session_state['vsepa'])
xpath_tit = st.text_input("xpath titulo", st.session_state['vtit'])
xpath_det = st.text_input("xpath detalle", st.session_state['vdet'])
xpath_link = st.text_input("xpath link", st.session_state['vlink'])


col10, col20 = st.columns(2)
if col10.button(":red[**Grabar**]"):
    with conn.session as session:
        #session.execute(f"UPDATE novedades SET select_web = '{new}' WHERE nuri='{nuri}'")
        session.execute(text("UPDATE fuentes_py SET fuente = :url, activa = :activa, xpath_titulo = :tit  WHERE nuri= :nuri"), {"url": vurl,"activa": activa,"tit": xpath_tit,"nuri": tnuri})
                        
        session.commit()
        st.success("Data sent")

    st.switch_page("./pages/fuentes.py")
if col20.button(":red[**Cancelar**]"):
    st.switch_page("streamlit_app.py")
