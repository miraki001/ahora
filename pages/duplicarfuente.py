import streamlit as st
import psycopg2
from sqlalchemy import text

st.set_page_config(layout="wide")
conn = st.connection("postgresql", type="sql")
tnuri = st.session_state['vnuri']
