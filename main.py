import streamlit

st.session_state.setdefault('login_attained',False)

page_login = st.page('Pages/yay.py', title='USER AUTHENTICATION', default=True)
page_game = st.page('Pages/Otictactoe.py', title='OTICTACTOE')

router_page = st.page_navigation([page_login]) if st.session_state == False else st.page_navigation([page_login,page_game])
router_page.run()
