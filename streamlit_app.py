import streamlit as st
import pandas as pd
#import pages as pg
import os
import itables.options as it_op
from itables.streamlit import interactive_table
from streamlit_multipage import MultiPage
from streamlit_navigation_bar import st_navbar
import re


st.set_page_config(
    page_title="Miraki",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="disable",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""

<style>


 .css-1iyw2u1 {
        display: none;
    }

</style>

""", unsafe_allow_html=True)



vnuri =0
st.session_state.vnuri = 0
col41, mid, col42 = st.columns([1,1,20])
with col41:
    st.image('ic_launcher44.png', width=60)
with col42:
    st.title('Miraki')

st.subheader("Plataforma de Vigilancia Tecnólogica e Inteligencia Competitiva")

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


col1, col2, col3,col4,col5,col6,col7 = st.columns(7)

vnuri = 500
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''

#st.query_params.from_dict({"foo": "bar", "baz": [1, 2, 3]})
if col1.button("Home"):
    st.switch_page("streamlit_app.py")
if col2.button("Editar"):
    st.switch_page("./pages/editar.py")
if col3.button("Seleccionar"):
    st.write(st.session_state.vnuri)
    st.write("vnuri = ", server_state.vnuri)
    #st.switch_page("./pages/seleccionar.py")
if col4.button("Desmarcar"):
    st.switch_page("./pages/desmarcar.py")
if col5.button("Informes"):
    st.switch_page("./pages/nuevomenu.py")
if col6.button("Parametros"):
    st.switch_page("./pages/parametros.py")
if col7.button("Fuentes"):
    st.switch_page("./pages/fuentes.py")
 

#default=["copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
#default=["copyHtml5", "csvHtml5", "excelHtml5"],




#it_args = {}
#it_args["buttons"] = default
#it_args["select"] = True

  




conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,fecha,titulo,select_web as sel,detalle,imagen,link,titulo_es,detalle_es,eje_nuri from novedades order by nuri desc limit 50;', ttl="0"),
df = df1[0]
#st.write(df1[0])
#st.dataframe(df, hide_index=True, column_config={"titulo_es": None})
#st.dataframe(df, hide_index=True, column_config={"detalle_es": None})

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'nuri' : st.column_config.NumberColumn('nuri', required=True),
    'fuente' : st.column_config.TextColumn('fuente'),
#    'selec' : st.column_config.CheckboxColumn('selec'),
    'titulo' : st.column_config.TextColumn('titulo',  width='large'),
    'detalle' : st.column_config.TextColumn('detalle', width='large'),
    'imagen' : st.column_config.ImageColumn('imagen'),
    'link' : st.column_config.LinkColumn('link'),

    
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
                        'imagen' : st.column_config.ImageColumn('imagen'),
                        'link' : st.column_config.LinkColumn('link'),      
                        'titulo_es' : None,                        
                        'detalle_es' : None,    
                        'eje_nuri' : None,    
                        },
                        disabled=df.columns,
#                        num_rows="dynamic",
                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Selec]
                    return selected_rows.drop('Selec', axis=1)
                  
selection = dataframe_with_selections(df)

#st.dataframe(selection, use_container_width=False)
#selection.drop(selection.columns[-1],axis=1, inplace = True)
#st.write(selection)
#selection.drop(columns=[1], axis=1) 
ss = st.dataframe(selection, hide_index=True)
#st.write(ss)
#st.dataframe(selection.style.hide(axis="index"))
#st.write("Your selection:")
#st.write(ss[nuri])
#st.write(selection)
#st.write(f'selected row index: {selection.selected_row_index}')
#st.write(f'car name: {selection.df.at[selection.selected_row_index, "nuri"]}')
#st.write(selection[0])
st.write(selection['nuri'])
vnuri= selection.to_string(columns=['nuri'], header=False, index=False)
st.session_state.vnuri = vnuri
#with server_state_lock.count:
# server_state.count = vnuri
server_state.vnuri = vnuri
#st.write('vnuri valor')
#st.write(selection.nuri)
#st.write(selection.to_string(columns=['nuri'], header=False, index=False))
#st.write(selection.to_string(columns=['titulo'], header=False, index=False))
#st.write(selection.to_string(columns=['detalle'], header=False, index=False))

st.session_state['user_select_value'] = vnuri
st.session_state['vnuri'] = vnuri
st.session_state['vtitulo'] = selection.to_string(columns=['titulo'], header=False, index=False)
st.session_state['vdetalle'] = selection.to_string(columns=['detalle'], header=False, index=False)
st.session_state['vlink'] = selection.to_string(columns=['link'], header=False, index=False)
st.session_state['vimagen'] = selection.to_string(columns=['imagen'], header=False, index=False)
st.session_state['vtitulo_es'] = selection.to_string(columns=['titulo_es'], header=False, index=False)
st.session_state['vdetalle_es'] = selection.to_string(columns=['detalle_es'], header=False, index=False)



