st.set_page_config(layout="wide")import streamlit as st
import pandas as pd
import itables.options as it_op
from itables.streamlit import interactive_table
import re
import hydralit_components as hc
import hydralit as hy
 
st.set_page_config(initial_sidebar_state="colapsed",
                  layaut="wide")



col1, col2, col3 = st.columns(3)

if col1.button("Home"):
    st.switch_page("streamlit_app.py")
if col2.button("Page 1"):
    st.switch_page("./pages/editar.py")
if col3.button("Page 2"):
    st.switch_page("./pages/seleccionar.py")

#default=["copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
#default=["copyHtml5", "csvHtml5", "excelHtml5"],




#it_args = {}
#it_args["buttons"] = default
#it_args["select"] = True

  




conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,select_web selec,fecha,titulo,detalle,imagen,link from novedades order by nuri desc limit 2000;', ttl="0"),
df = df1[0]
#st.write(df1[0])


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'nuri' : st.column_config.NumberColumn('nuri', required=True),
    'fuente' : st.column_config.TextColumn('fuente'),
    'selec' : st.column_config.CheckboxColumn('selec'),
    'titulo' : st.column_config.TextColumn('titulo',  width='large'),
    'detalle' : st.column_config.TextColumn('detalle', width='large'),
    'imagen' : st.column_config.ImageColumn('imagen'),
    'link' : st.column_config.LinkColumn('link'),
    
}
result = st.data_editor(df, column_config = config, num_rows='dynamic')
edited_df = st.data_editor(df) # 👈 An editable dataframe


