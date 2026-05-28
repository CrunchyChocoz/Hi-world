import streamlit as st
st.title('TIC TAC TOE')
c1,c2 = st.columns([1,3], vertical_alignment='top', border=True)
with c2:
  st.header('-by CrunchyChocoz')
with st.form('alias_form', border=True):
  username = st.text_input('Enter an Alias')
  submit_alias = st.form_submit_button('SUBMIT')
  if submit_alias:
    st.write('!!!!')
st.sidebar.title('SidebaR')
