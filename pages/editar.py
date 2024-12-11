import streamlit as st
from streamlit_navigation_bar import st_navbar
from streamlit_theme import st_theme


page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)
