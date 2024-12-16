import streamlit as st

st.set_page_config(layout="wide")

vtitulo = st.session_state['vtitulo']
vtitulo1 = "eeeeee"
col1, col2, col3,col4,col5 = st.columns(5)

tnuri = st.session_state['vnuri']
ttitulo = st.session_state['titulo']

if col1.button("Home"):
    st.switch_page("streamlit_app.py")
if col2.button("Editar"):
    st.switch_page("./pages/editar.py")
if col3.button("Seleccionar"):
    st.switch_page("./pages/seleccionar.py")
if col4.button("Desmarcar"):
    st.switch_page("./pages/seleccionar.py")
if col5.button("Informes"):
    st.switch_page("./pages/informes.py")

#st.write("QueryParams: ", st.query_params)
#st.write('session')
#st.write(st.session_state)
#value  = int(st.query_params.get("nuri", vnuri))
#st.write(st.session_state['vnuri'])
#st.write(st.session_state['vtitulo'])
#title = st.text_input("Movie title", "Life of Brian")
vtitle = st.text_input("Titulo", ttitulo)
