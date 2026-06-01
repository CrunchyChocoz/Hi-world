import streamlit as st
import supabase as sb

SUPABASE = sb.create_client(st.secrets['sbURL'],st.secrets['sbPubAPI'])

st.set_page_config(layout='wide')
st.write(st.__version__,'  ',sb.__version__)
c1,c2,c3 = st.columns(3)
with c2:
  st.title('TIC TAC TOE')

c4,c5 = st.columns(2, vertical_alignment='top', border=True)
with c5:
  st.markdown('-*by CrunchyChocoz*')

c6,c7 = st.columns(2,border=True)
with c6:
  st.markdown('## LOGIN')
  
  with st.form('login',border=True):
    c6_00,c6_01 = st.columns([1,3], border=True)
    with c6_00:
      st.markdown('ALIAS:')
    with c6_01:
      login_user = st.text_input(label='luser', label_visibility='collapsed')
      
    c6_10,c6_11 = st.columns([1,3], border=True)
    with c6_10:
      st.markdown('PASSWORD:')
    with c6_11:
      login_pass = st.text_input(label='lpass', label_visibility='collapsed')  
    
    submit1 = st.form_submit_button('SUBMIT')
    if submit1:
      st.write('!!!')
with c7:
  st.markdown('## REGISTER')
  
  with st.form('register', border=True):
    c7_00,c7_01 = st.columns([1,3], border=True)
    with c7_00:
      st.markdown('ALIAS:')
    with c7_01:
      reg_user = st.text_input(label='ruser', label_visibility='collapsed')

    c7_10,c7_11 = st.columns([1,3], border=True)
    with c7_10:
      st.markdown('PASSWORD:')
    with c7_11:
      reg_pass = st.text_input(label='rpass', label_visibility='collapsed')      
    
    submit2 = st.form_submit_button('SUBMIT')
    if submit2:
      if not reg_user.strip() or not reg_pass.strip():
        st.stop()
      elif SUPABASE.table('LoginDB').select('normalized_alias').eq('normalized_alias',reg_user.lower().strip()).execute().data:
        st.error('Alias already taken')
        st.stop()
      elif len(reg_pass) <= 4:
        st.error('Password must have MORE than 4 characters')
        st.stop()
      else:
        SUPABASE.table('LoginDB').insert({'alias':reg_user, 'normalized_alias':reg_user.lower().strip(), 'password':reg_pass}).execute()
        st.success(f'Alias ({reg_user}) has been registered.')

st.sidebar.title('SidebaR')
