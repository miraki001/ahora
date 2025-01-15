import streamlit as st
import psycopg2
from sqlalchemy import text
from streamlit_extras.stylable_container import stylable_container



st.set_page_config(page_title='First app', page_icon="📊", initial_sidebar_state="expanded", layout='wide')
from streamlit.components.v1 import html
#st.sidebar.image("https://picsum.photos/200")
st.image('ic_launcher44.png', width=60)
with st.container():
    st.text("This is paragraph :)") 
    html("""
    <script>
        // Locate elements
        var decoration = window.parent.document.querySelectorAll('[data-testid="stDecoration"]')[0];
        var sidebar = window.parent.document.querySelectorAll('[data-testid="stSidebar"]')[0];
        // Observe sidebar size
        function outputsize() {
            decoration.style.left = `${sidebar.offsetWidth}px`;
        }
        new ResizeObserver(outputsize).observe(sidebar);
        // Adjust sizes
        outputsize();
        decoration.style.height = "3.0rem";
        decoration.style.right = "45px";
        // Adjust text decorations
        decoration.innerText = "Mirake - Plataforma de Vigilancia Tecnologica e Inteligencia Competitiva"; // Replace with your desired text
        decoration.style.fontWeight = "bold";
        decoration.style.display = "flex";
        decoration.style.justifyContent = "center";
        decoration.style.alignItems = "center";
        //decoration.style.fontWeight = "bold";
        //decoration.style.backgroundImage = "none"; // Remove background image
        //decoration.style.backgroundSize = "unset"; // Remove background size
    </script>
""", width=0, height=0)



col41, mid, col42 = st.columns([1,1,20])
with col41:
    st.image('ic_launcher44.png', width=60)
with col42:
    st.title('Miraki')

st.subheader("Plataforma de Vigilancia Tecnólogica e Inteligencia Competitiva")


col1, col2, col3,col4 = st.columns(4)

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



if col1.button("Volver" ,  type='primary'):
    st.switch_page("./pages/parametros.py")
if col2.button("Insertar"):
    st.switch_page("./pages/insertar_fuente.py")
if col3.button("Editar"):
    st.switch_page("./pages/editar_fuentes.py")
if col4.button("Borrar"):
    st.switch_page("./pages/borrarpalabraclave.py")   



conn = st.connection("postgresql", type="sql")
qq = 'select palabra,peso from palabras_a_buscar  ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]



ppalabra = st.text_input("ingrese el nombre de la palabra")

if ppalabra:
    mask = df.applymap(lambda x: ppalabra in str(x).lower()).any(axis=1)
    df = df[mask]



colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'palabra' : st.column_config.TextColumn('palabra', required=True),
    'peso' : st.column_config.NumberColumn('peso',),


    
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
                        'url' : st.column_config.LinkColumn('palabra'),      
                        },
                        disabled=df.columns,
#                        num_rows="dynamic",
                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Selec]
                    return selected_rows.drop('Selec', axis=1)
                  
selection = dataframe_with_selections(df)

cnt = len(selection)
#st.write(f'selected row index: {selection.selected_row_index}')

vpalabra = selection.to_string(columns=['palabra'], header=False, index=False)
st.write(vpalabra)
st.session_state['vpalabra'] = vpalabra

