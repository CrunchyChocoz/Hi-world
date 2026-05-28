import streamlit as st
st.title('TIC TAC TOE')
c1,c2 = st.columns([1,3], vertical_alignment='top', border=True)
with c2:
  st.markdown('### -*by CrunchyChocoz*')
with st.form('alias_form', border=True):
  st.markdown('## Enter an :gray[ALIAS]')
  username = st.text_input(label='', label_visibility='collapsed')
  submit_alias = st.form_submit_button('SUBMIT')
  if submit_alias:
    st.write('!!!!')
st.sidebar.title('SidebaR')
