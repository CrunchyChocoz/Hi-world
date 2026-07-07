import streamlit as st
import random

c1,c2,c3 = st.columns([1,3,1])
with c2:
  st.title('CLASSIC TICTACTOE')
st.divider()

c4,c5,c6 = st.columns(3, border=True)
c7,c8,c9 = st.columns(3, border=True)
c10,c11,c12 = st.columns(3, border=True)
