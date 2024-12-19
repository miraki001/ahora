col1, col2, col3,col4,col5,col6,col7 = st.columns(7)

vnuri = 500
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''

#st.query_params.from_dict({"foo": "bar", "baz": [1, 2, 3]})
if col1.button("Home"):
    st.switch_page("streamlit_app.py")
if col2.button("Insertar"):
    st.switch_page("./pages/insertar_fuente.py")
if col3.button("Editar"):
    st.switch_page("./pages/editar_fuente.py")
if col4.button("Borrar"):
    #st.switch_page("./pages/desmarcar.py")
if col5.button("Probar Scrap"):
    st.switch_page("./pages/fuente_scrap.py")
