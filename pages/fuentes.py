import streamlit as st
import psycopg2
from sqlalchemy import text

st.set_page_config(
    page_title="Miraki",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

col1, col2, col3,col4,col5 = st.columns(5)

tnuri = 0
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
    st.switch_page("./pages/desmarcar.py")
if col5.button("Scrap"):
    st.switch_page("./pages/fuente_scrap.py")



conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente as url,activa,fecha_act,descrip as fuente,pais from fuentes_py where proyecto_nuri = 1  ;', ttl="0"),
df = df1[0]

agree = st.checkbox("Solo Activas")

if agree:
    df['activa'] = 'S'


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

st.write(f'selected row index: {selection.selected_row_index}')

vnuri = selection.to_string(columns=['nuri'], header=False, index=False)
st.write(vnuri)
tnuri = vnuri
if  selection['nuri'] is not empty:
    vquery = 'select * from fuentes_py where nuri = ' + vnuri + ';'
    df2 = conn.query(vquery, ttl="0"),
    df3 = df2[0]
    st.write(df3)

st.session_state['vfuente'] = selection.to_string(columns=['url'], header=False, index=False)
st.session_state['vdescrip'] = selection.to_string(columns=['fuente'], header=False, index=False)
st.session_state['vnuri'] = selection.to_string(columns=['nuri'], header=False, index=False)
st.session_state['vpais'] = selection.to_string(columns=['pais'], header=False, index=False)
st.session_state['vactiva'] = selection.to_string(columns=['activa'], header=False, index=False)





