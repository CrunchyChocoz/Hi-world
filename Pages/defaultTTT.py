import streamlit as st
st.set_page_config(layout='wide')

c1,c2,c3 = st.columns(3)
with c2:
  st.title('TIC TAC TOE')

c4,c5 = st.columns(2, vertical_alignment='top')
with c5:
  st.markdown('-*by CrunchyChocoz*')

st.divider()

