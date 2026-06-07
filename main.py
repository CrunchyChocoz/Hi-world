import streamlit as st

st.session_state.setdefault('login_attained',False)

page_login = st.Page('Pages/yay.py', title='USER AUTHENTICATION', default=True)
page_game = st.Page('Pages/Otictactoe.py', title='OTICTACTOE')

router_page = st.navigation([page_login]) if st.session_state == False else st.navigation([page_login,page_game])
router_page.run()
