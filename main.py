import streamlit as st

st.session_state.setdefault('login_attained',False)

page_login = st.Page('Pages/yay.py', title='USER AUTHENTICATION', default=True)
page_Home = st.Page('Pages/Home.py', title='OTIC TAC TOE')

if st.session_state.login_attained == False:
  router_page = st.navigation([page_login])  
else:
  router_page = st.navigation([page_Home])
router_page.run()
