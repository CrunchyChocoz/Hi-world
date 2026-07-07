import streamlit as st
import random

st.markdown('<h1 style="text-align: center;">CLASSIC TICTACTOE</h1>', unsafe_allow_html=True)
st.write(st.__version__)
st.divider()

table = st.container(border=True)
with table:
  st.html("""
  <style>
  div[data-testid="stLayoutWrapper"]:has(.classic-board) {
      border: 10px solid red !important;
      background: blue !important;
  }
  </style>
  """)

  st.html('<div class="classic-board"></div>')
  
  c4,c5,c6 = st.columns(3,border=True)
  c7,c8,c9 = st.columns(3,border=True)
  c10,c11,c12 = st.columns(3,border=True)
