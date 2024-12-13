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
 

#default=["copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
#default=["copyHtml5", "csvHtml5", "excelHtml5"],




#it_args = {}
#it_args["buttons"] = default
#it_args["select"] = True

  




conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,fecha,titulo,detalle,imagen,link from novedades order by nuri desc limit 2000;', ttl="0"),
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
st.write("Your selection:")
st.write(selection)
st.write(selection['nuri'] )
MultiPage.save({"nuri": selection['nuri'] , "titulo": selection['titulo'] }, namespaces=["Input Page"])




