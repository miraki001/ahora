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
