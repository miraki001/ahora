import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)
