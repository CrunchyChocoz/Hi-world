import streamlit as st
import random

st.markdown('<h1 style="text-align: center;">CLASSIC TICTACTOE</h1>', unsafe_allow_html=True)

st.divider()

c1,c2,c3 = st.columns([2,1,2])
with c2:
  board = st.container(border=True)
  with board:
    st.html('''<style> div[data-testid="stLayoutWrapper"]:has(.classic-board)
                 {border: 5px solid #2D2C35 !important;
                  border-radius: 0px;
                  padding: 20px;}
                </style>''')
    
    st.html('<div class="classic-board"></div>')
      
    c4,c5,c6 = st.columns(3)
    c7,c8,c9 = st.columns(3)
    c10,c11,c12 = st.columns(3)
  
    st.html('''<style> div[data-testid="stLayoutWrapper"]:has(.classic-board)
                       div[data-testid="stColumn"] > div
                       {
                        background-color: #ffffff;
                        aspect-ratio: 1 !important;}
               </style>''')
    
