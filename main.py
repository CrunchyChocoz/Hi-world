import streamlit as st

st.session_state.setdefault('login_attained',False)

page_login = st.Page('Pages/yay.py', title='USER AUTHENTICATION', default=True)
page_Home = st.Page('Pages/Home.py', title='OTIC TAC TOE')
page_DOTTT = st.Page('Pages/defaultOTTT.py', title='Default OTTT')
page_SOTTT = st.Page('Pages/superOTTT.py', title='Super OTTT')

if st.session_state.login_attained == False:
  router_page = st.navigation([page_login])  
else:
  router_page = st.navigation([page_Home,page_DOTTT,page_SOTTT])
router_page.run()
