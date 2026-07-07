import streamlit as st
import random

st.markdown('<h1 style="text-align: center;">CLASSIC TICTACTOE</h1>', unsafe_allow_html=True)
st.divider()

table = st.container(border=True)
with table:
  st.html('''<style> div[data-testid="stVerticalBlockBorderWrapper"]
              {background-color: #3b3f4b !important;
               border: 2px solid !important;
               border-radius: 100px
               padding: 20px}
             </style>''')
#  c4,c5,c6 = st.columns(3,border=True)
#  c7,c8,c9 = st.columns(3,border=True)
#  c10,c11,c12 = st.columns(3,border=True)
