import streamlit as st


st.set_page_config(layout="wide")
vnuri  = int(st.query_params.get("nuri", value))
st.write(vnuri)
