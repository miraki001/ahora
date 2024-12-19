st.set_page_config(layout="wide")

vtitulo = st.session_state['vtitulo']
vtitulo1 = "eeeeee"


tnuri = st.session_state['vnuri']
ttitulo = st.session_state['vtitulo']

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
#st.text_input("test color")
st.text_input("test color2")



#st.write("QueryParams: ", st.query_params)
#st.write('session')
#st.write(st.session_state)
#value  = int(st.query_params.get("nuri", vnuri))
#st.write(st.session_state['vnuri'])
#st.write(st.session_state['vtitulo'])
#title = st.text_input("Movie title", "Life of Brian")
st.header(":blue[titulo]")

vtitle = st.text_input("**Titulo**", ttitulo)
vtitle_es = st.text_input("**Titulo en Castellano** ", st.session_state['vtitulo_es'])

vdet= st.text_input("**Destalle**", st.session_state['vdetalle'])
vdet_es = st.text_input(":red[Detalle en Castellano] ", st.session_state['vdetalle_es'])

