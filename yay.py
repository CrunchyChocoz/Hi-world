import streamlit as st
st.set_page_config(layout='wide')

c1,c2,c3 = st.columns(3)
with c2:
  st.title('TIC TAC TOE')

c4,c5 = st.columns([1,2], vertical_alignment='top', border=True)
with c5:
  st.markdown('-*by CrunchyChocoz*')

c6,c7 = st.columns(2,border=True)
with c6:
  with st.form('login',border=True):
    c61,c62 = st.columns([1,4], border=True)
    with c61:
      st.markdown('ALIAS:')
      st.markdown('PASSWORD:')
    with c62:
      login_user = st.text_input(label='luser', label_visibility='collapsed')
      login_pass = st.text_input(label='lpass', label_visibility='collapsed')
    submit1 = st.form_submit_button('SUBMIT')
    if submit1:
      st.write('!!!')
with c7:
  with st.form('register', border=True):
    c71,c72 = st.columns([1,4], border=True)
    with c71:
      st.markdown('### Enter an :gray[ALIAS]')
      st.markdown('### Enter a Password:')
    with c72:
      reg_user = st.text_input(label='ruser', label_visibility='collapsed')
      reg_pass = st.text_input(label='rpass', label_visibility='collapsed')
    submit2 = st.form_submit_button('SUBMIT')
    if submit2:
      st.write('!!!!')
st.sidebar.title('SidebaR')
