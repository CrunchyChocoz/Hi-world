import streamlit as st
st.set_page_config(layout='wide')

st.title('TIC TAC TOE')

c1,c2 = st.columns([1,3], vertical_alignment='top', border=True)
with c2:
  st.markdown('-*by CrunchyChocoz*')

c3,c4 = st.columns(2,border=True)
with c3:
  with st.form('login',border=True):
    c31,c32 = st.columns([1,4], border=True)
    with c31:
      st.markdown('ALIAS:')
      st.markdown('PASSWORD:')
    with c32:
      login_user = st.text_input(label='luser', label_visibility='collapsed')
      login_pass = st.text_input(label='lpass', label_visibility='collapsed')
    submit1 = st.form_submit_button('SUBMIT')
    if submit1:
      st.write('!!!')
with c4:
  with st.form('register', border=True):
    c41,c42 = st.columns([1,4], border=True)
    with c41:
      st.markdown('### Enter an :gray[ALIAS]')
      st.markdown('### Enter a Password:')
    with c42:
      reg_user = st.text_input(label='ruser', label_visibility='collapsed')
      reg_pass = st.text_input(label='rpass', label_visibility='collapsed')
    submit2 = st.form_submit_button('SUBMIT')
    if submit2:
      st.write('!!!!')
st.sidebar.title('SidebaR')
