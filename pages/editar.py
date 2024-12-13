import streamlit as st


st.set_page_config(layout="wide")
value  = int(st.query_params.get("nuri", vnuri))
st.write(value)
