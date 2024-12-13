import streamlit as st


st.set_page_config(layout="wide")

st.write("QueryParams: ", st.query_params)
st.write('session')
st.write(st.session_state)
#value  = int(st.query_params.get("nuri", vnuri))
st.write(vnuri)
