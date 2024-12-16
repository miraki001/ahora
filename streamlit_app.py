import streamlit as st
import pandas as pd
import itables.options as it_op
from itables.streamlit import interactive_table
from streamlit_multipage import MultiPage
import re


 
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
    st.switch_page("./pages/seleccionar.py")
if col4.button("Desmarcar"):
    st.switch_page("./pages/desmarcar.py")
if col5.button("Informes"):
    st.switch_page("./pages/informes.py")
 

#default=["copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
#default=["copyHtml5", "csvHtml5", "excelHtml5"],




#it_args = {}
#it_args["buttons"] = default
#it_args["select"] = True

  




conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,fecha,titulo,detalle,imagen,link from novedades order by nuri desc limit 50;', ttl="0"),
df = df1[0]
#st.write(df1[0])


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
st.write(selection)
#selection.drop(columns=[1], axis=1) 
#ss = st.dataframe(selection, hide_index=True)
#st.write(ss)
#st.dataframe(selection.style.hide(axis="index"))
st.write("Your selection:")
#st.write(ss[nuri])
st.write(selection)
#st.write(f'selected row index: {selection.selected_row_index}')
#st.write(f'car name: {selection.df.at[selection.selected_row_index, "nuri"]}')
#st.write(selection[0])
st.write(selection['nuri'])
vnuri= selection.to_string(columns=['nuri'], header=False, index=False)
st.write('vnuri valor')
st.write(selection.nuri)
st.write(selection.to_string(columns=['nuri'], header=False, index=False))
st.write(selection.to_string(columns=['titulo'], header=False, index=False))
st.write(vnuri[0])
st.session_state['user_select_value'] = vnuri
st.session_state['vnuri'] = vnuri
st.session_state['vtitulo'] = selection.to_string(columns=['titulo'], header=False, index=False)
st.session_state['vdetalle'] = selection.to_string(columns=['detalle'], header=False, index=False)
st.session_state['vlin'] = selection.to_string(columns=['link'], header=False, index=False)
st.session_state['vimagen'] = selection.to_string(columns=['imagen'], header=False, index=False)

"""
if 'user_select_value' not in st.session_state:
    st.session_state['user_select_value'] = 5000 #or whatever default
user_select_value = st.session_state['user_select_value']

if st.button('Save Filters'):
        st.session_state['user_select_value'] = vnuri
        st.session_state['vnuri'] = vnuri
        st.session_state['vtitulo'] = selection['titulo']

if st.button('Clear page Filters'):
        st.session_state['user_select_value'] = 0 # or default value
st.write(user_select_value)
"""
#def input_page(st, **state):
#  MultiPage.save({"nuri": selection['nuri'] , "titulo": selection['titulo'] }, namespaces=["Input Page"])





