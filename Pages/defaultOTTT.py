import streamlit as st
import random
import supabase as sb

SUPABASE = sb.create_client(st.secrets['sbURL'],st.secrets['sbPubKey'])
room-id = random.randint(1000,999999)
st.query_params['game-id'] = room-id

st.markdown('<h1 style="text-align: center;">CLASSIC TICTACTOE</h1>', unsafe_allow_html=True)

st.divider()

board = st.container(border=True)
with board:
  st.html('''<style> div[data-testid="stLayoutWrapper"]:has(.classic-board)
  {border: 5px solid #2D2C35 !important;
   display: flex !important;
   justify-content: center !important;
   border-radius: 0px;
   padding: 20px;}
             </style>''')
    
  st.html('''<style> div[data-testid="stLayoutWrapper"]:has(.classic-board)
                     div[data-testid="stColumn"] > div
                     {max-width: 100px !important;
                      aspect-ratio: 1 !important;
                      display: flex !important;
                      justify-content: center !important;
                      border: 0px !important;
                      background-color: #ffffff;
                      }
             </style>''')

  st.html('<div class="classic-board"></div>')

def join_room(id):
  st.query_params('room-id') = id
  
c1,c2,c3 = st.columns(3)
with c1:
  with st.expander('ROOM-ID'):
    st.write(room-id)

with c3:
  st.write('JOIN ROOM')
  if st.button('ENTER ROOM-ID', on_click=join_room)

'''
def move(id):
  

for i in range(3):
  columns = st.columns(3)
  for j in range(3):
    n = i*3 + j
    with columns[j]:
      st.button('',key=f'tile{n}',on_click=move(), args=(n)):
'''      
    
