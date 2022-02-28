import streamlit as st 
from bbquote.lib import get_quote


st.markdown("# Africa by toto!")

st.text(get_quote())