import streamlit as st
import pandas as pd
import itables.options as it_op
from itables.streamlit import interactive_table
import re
import hydralit_components as hc
 

st.set_page_config(initial_sidebar_state="expanded")





# define what option labels and icons to display
option_data = [
   {'label':"editar"},
   {'label':"seleccionar"},
   {'label':"informes"},
]

# override the theme, else it will use the Streamlit applied theme
over_theme = {'txc_inactive': 'white','menu_background':'purple','txc_active':'yellow','option_active':'blue'}
font_fmt = {'font-class':'h2','font-size':'150%'}

# display a horizontal version of the option bar
op = hc.option_bar(option_definition=option_data,title='Miraki',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

# display a version version of the option bar
#op2 = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=False)




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


