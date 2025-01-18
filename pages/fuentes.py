import streamlit as st
import psycopg2
from sqlalchemy import text
from streamlit_extras.stylable_container import stylable_container



col41, mid, col42 = st.columns([1,1,20])
with col41:
    st.image('ic_launcher44.png', width=60)
with col42:
    st.title('Miraki')

st.subheader("Plataforma de Vigilancia Tecnólogica e Inteligencia Competitiva")


col1, col2, col3,col4,col5,col6,col7 = st.columns(7)

tnuri = 0
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''



st.markdown("""
            <style>
            div.stButton {text-align:center}
            div.stButton > button:first-child {
                background-color: #b579c2;
                color:#000000;
                font-weight: bold;
            }
            div.stButton > button:hover {
                background-color: #79adc2;
                color:#ff0000;
                }
            </style>""", unsafe_allow_html=True)


st.session_state["Editar"] = False

if col1.button("Home" ,  type='primary'):
    st.switch_page("streamlit_app.py")
if col2.button("Insertar"):
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/editar_fuentes.py")
if col3.button("Editar", disabled=not st.session_state["Editar"] ):
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/editar_fuentes.py")
if col4.button("Borrar", ):
    st.switch_page("./pages/borrarfuente.py")   
if col5.button("Verificar"):
    st.switch_page("./pages/verifpagbs.py")
if col6.button("Ejecutar"):
    st.switch_page("./pages/scraptodo.py")
if col7.button("Duplicar"):
    st.switch_page("./pages/duplicarfuente.py")



conn = st.connection("postgresql", type="sql")
qq = 'select nuri,fuente as url,activa,fecha_act,descrip as fuente,pais,fuente_org,urllink,tipo_busq,posjson from fuentes_py where proyecto_nuri = 1  ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]

agree = st.checkbox("Solo Activas")

pfuente = st.text_input("ingrese el nombre de la fuente")


if pfuente:
    mask = df.applymap(lambda x: pfuente in str(x).lower()).any(axis=1)
    df = df[mask]

#st.write(df1[0])
#st.dataframe(df, hide_index=True, column_config={"titulo_es": None})
#st.dataframe(df, hide_index=True, column_config={"detalle_es": None})

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'nuri' : st.column_config.NumberColumn('nuri', required=True),
    'url' : st.column_config.LinkColumn('url'),
#    'selec' : st.column_config.CheckboxColumn('selec'),
    'fuente' : st.column_config.TextColumn('fuente',),
    'fecha_act' : st.column_config.TextColumn('fecha_act',),
    'activa' : st.column_config.TextColumn('activa'),
    'pais' : st.column_config.TextColumn('pais',  width='large'),

    
}
#result = st.data_editor(df, column_config = config, num_rows='dynamic')
def dataframe_with_selections(df):
                    df_with_selections = df.copy()
                    df_with_selections.insert(0, "Selec", False)
                    # Get dataframe row-selections from user with st.data_editor
                    edited_df = st.data_editor(
                        df_with_selections,
                        hide_index=True,
                        column_config=
                        {"Select": st.column_config.CheckboxColumn(required=True),
                        'url' : st.column_config.LinkColumn('url'),      
                        },
                        disabled=df.columns,
#                        num_rows="dynamic",
                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Selec]
                    return selected_rows.drop('Selec', axis=1)
                  
selection = dataframe_with_selections(df)

cnt = len(selection)
if cnt>0:

    st.session_state["Editar"] = False
    
    vnuri = selection.to_string(columns=['nuri'], header=False, index=False)
    st.write(vnuri)
    tnuri = vnuri
    vquery = 'select * from fuentes_py where nuri = ' + vnuri + ';'
    df2 = conn.query(vquery, ttl="0"),
    df3 = df2[0]
    st.write(df3)
    st.session_state['vsepa'] = df3.to_string(columns=['separador'], header=False, index=False)
    st.session_state['vtit'] = df3.to_string(columns=['xpath_titulo'], header=False, index=False)
    st.session_state['vdet'] = df3.to_string(columns=['xpath_detalle'], header=False, index=False)
    st.session_state['vlink'] = df3.to_string(columns=['xpath_link'], header=False, index=False)
    st.write(df3.to_string(columns=['separador'], header=False, index=False))
    st.session_state['vtipo'] = df3.to_string(columns=['tipo'], header=False, index=False)
    st.session_state['vbus'] = df3.to_string(columns=['busqueda_pers'], header=False, index=False)
    st.session_state['vidioma'] = df3.to_string(columns=['idioma'], header=False, index=False)
    st.session_state['vcod'] = df3.to_string(columns=['cod_pais'], header=False, index=False)
    st.session_state['vobserva'] = df3.to_string(columns=['observa'], header=False, index=False)
    st.session_state['vimagen'] = df3.to_string(columns=['xpath_image'], header=False, index=False)
    st.session_state['vdet'] = df3.to_string(columns=['xpath_detalle'], header=False, index=False)
    st.session_state['vatributo1'] = df3.to_string(columns=['atributo1'], header=False, index=False)
    st.session_state['vatributo2'] = df3.to_string(columns=['atributo2'], header=False, index=False)
    st.session_state['vtipobus'] = df3.to_string(columns=['tipo_busq'], header=False, index=False)
    st.session_state['vfuenteorg'] = df3.to_string(columns=['fuente_org'], header=False, index=False)
    st.session_state['vurllink'] = df3.to_string(columns=['urllink'], header=False, index=False)
    st.session_state['vposjson'] = df3.to_string(columns=['posjson'], header=False, index=False)


    st.session_state['vfuente'] = selection.to_string(columns=['url'], header=False, index=False)
    st.session_state['vdescrip'] = selection.to_string(columns=['fuente'], header=False, index=False)
    st.session_state['vnuri'] = selection.to_string(columns=['nuri'], header=False, index=False)
    st.session_state['vpais'] = selection.to_string(columns=['pais'], header=False, index=False)
    st.session_state['vactiva'] = selection.to_string(columns=['activa'], header=False, index=False)

    tnuri = st.session_state['vnuri']
    st.write(tnuri)





