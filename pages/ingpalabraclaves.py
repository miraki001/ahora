import streamlit as st
import psycopg2
from sqlalchemy import text


def actualizar:
    with conn.session as session:
        actualiza = "UPDATE fuentes_py SET fuente = :url, activa = :activa,"
        actualiza = actualiza + "xpath_titulo = :tit, "
        actualiza = actualiza + "descrip = :desc, "
        actualiza = actualiza + "pais = :pais, "
        actualiza = actualiza + "separador = :separador, "
        actualiza = actualiza + "xpath_detalle = :det, "
        actualiza = actualiza + "xpath_link = :link, "
        actualiza = actualiza + "xpath_image = :image, "
        actualiza = actualiza + "tipo = :tipo, "
        actualiza = actualiza + "busqueda_pers = :busq, "
        actualiza = actualiza + "idioma = :idioma, "
        actualiza = actualiza + "cod_pais = :cod "
        actualiza = actualiza + " WHERE nuri= :nuri"
        #"desc": vtitle, "fuente": vurl, "pais": pais,"activa": activa, "separador": separador, "det": xpath_det, "link": xpath_link,"image": xpath_image, "tipo": tipo,"busq": busqueda, "idioma": idioma,"cod": codigo
        session.execute(text(actualiza), {"url": vurl,"activa": activa,"tit": xpath_tit,"desc": vtitle, "pais": pais,"separador": separador, "det": xpath_det, "link": xpath_link,"image": xpath_image, "tipo": tipo,"busq": busqueda, "idioma": idioma,"cod": codigo, "nuri": tnuri})
        #session.execute(text("UPDATE fuentes_py SET fuente = :url, activa = :activa, xpath_titulo = :tit    WHERE nuri= :nuri"), {"url": vurl,"activa": activa,"tit": xpath_tit, "desc": vtitle, "fuente": vurl, "pais": pais,"activa": activa, "separador": separador, "det": xpath_det, "link": xpath_link, "tipo": tipo,"busq": busqueda, "idioma": idioma,"cod": codigo,"nuri": tnuri})
                        
        session.commit()

tipo = st.session_state['vTipo'] 
if tipo == 'Editar':
    tpalabra = st.session_state['vpalabra'] 
    tpeso = st.session_state['vpeso'] 

if tipo == 'Ingresar':
    tpalabra = ''
    tpeso = 0


vpalabra = st.text_input("Palabra", tpalabra)

vpeso = st.number_input("Peso", tpeso)



col1, col2, = st.columns(2)
if col1.button("Grabar" ,  type='primary'):
    st.switch_page("./pages/palabrasclaves.py")
if col2.button("Cancelar"):
    st.switch_page("./pages/palabrasclaves.py")
