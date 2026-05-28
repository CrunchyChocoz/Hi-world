import streamlit as st
st.title('TIC TAC TOE')
c1,c2 = st.columns([1,2], vertical_allignment='top')
with c2:
  st.header('-by CrunchyChocoz')
c1,c2,c3 = st.columns(3, border=True)
st.sidebar.title('SidebaR')
