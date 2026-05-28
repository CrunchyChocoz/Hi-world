import streamlit as st
st.title('TIC TAC TOE')
c1,c2 = st.columns([1,2], vertical_alignment='top', border=True)
with c2:
  st.header('-by CrunchyChocoz')
form_name = st.form('Enter a Username: ') 
c1,c2 = st.columns(2, border=True)
st.sidebar.title('SidebaR')
