import streamlit as st
from streamlit_navigation_bar import st_navbar


st_navbar(
    pages=["Home", "Library", "Tutorials", "Development", "Download"],
    options={"use_padding": False}
)
st.write(pages)
