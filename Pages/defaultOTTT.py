import streamlit as st
import random

st.markdown('<h1 style="text-align: center;">CLASSIC TICTACTOE</h1>', unsafe_allow_html=True)

st.divider()

board = st.container(border=True)
with board:
  st.html('''<style> div[data-testid="stLayoutWrapper"]:has(.classic-board)
               {border: 5px solid #2D2C35 !important;
                border-radius: 0px;
                padding: 20px;}
              </style>''')
  
  st.html('<div class="classic-board"></div>')
    
  c4,c5,c6 = st.columns(3,border=True)
  c7,c8,c9 = st.columns(3,border=True)
  c10,c11,c12 = st.columns(3,border=True)

  st.html('''<style> div[data-testid="stLayoutWrapper"]:has(.classic-board)
                     div[data-testid="stColumn"] > div
                     {height: 100px;
                      width: 100px;
                      background-color: #ffffff;
                      aspect-ratio: 1;}
             </style>''')
  
