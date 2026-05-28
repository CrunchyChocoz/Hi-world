import streamlit as st
st.title('TIC TAC TOE')
st.header('       -by CrunchyChocoz')
container = st.container()
with container:
  st.title('Container')
c1,c2,c3 = st.columns(3, border=True)
st.sidebar.title('SidebaR')
