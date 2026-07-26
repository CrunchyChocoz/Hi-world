import streamlit as st
from streamlit_autorefresh import st_autorefresh
import random
import time
import supabase as sb

SUPABASE = sb.create_client(st.secrets['sbURL'],st.secrets['sbPubAPI'])

st_autorefresh(interval=2000)

if 'refresh' not in st.session_state:
  st.session_state.refresh = False
  st.session_state.refresh_counter = 0
  
if 'room_id' not in st.session_state:
  room_id = random.randint(1000,999999)
  st.query_params['room_id'] = room_id
  st.session_state.room_id = room_id
  
if 'status' not in st.session_state:
  st.session_state.status = 'waiting'

SUPABASE.table('ActivePlayersDB').insert({'room-id':st.session_state.room_id, 'Player_1':st.session_state.alias}).execute()

st.markdown('<h1 style="text-align: center;">CLASSIC TICTACTOE</h1>', unsafe_allow_html=True)
st.divider()
  
c1,c2,c3 = st.columns(3)
with c1:
  with st.expander('ROOM-ID'):
    st.write(st.session_state.room_id)
  st.divider()

  st.write('JOIN ROOM')
  with st.form('join_match',clear_on_submit=True):
    id_str = st.text_input('Enter Room Code')
    if st.form_submit_button('SUBMIT'):
      if id_str == None:
        room_code = 0
      else:
        room_code = int(id_str)
      room = SUPABASE.table('ActivePlayersDB').select('*').eq('room-id',room_code).execute().data
      if room:
        if room_code == room[0]['room-id']:
          st.session_state.room_id = room_code
          st.query_params['room_id'] = room_code
          st.success(f"Room ({SUPABASE.table('ActivePlayersDB').select('Player_1').eq('room-id',room_code).execute().data[0]['Player_1']}) joined successfully")
          SUPABASE.table('ActivePlayersDB').update({'Player_2':st.session_state.alias}).eq('room-id',room_code).execute()
          st.session_state.Player_1 = SUPABASE.table('ActivePlayersDB').select('Player_1').eq('room-id',st.session_state.room_id).execute().data[0]['Player_1']
          st.session_state.Player_2 = SUPABASE.table('ActivePlayersDB').select('Player_2').eq('room-id',st.session_state.room_id).execute().data[0]['Player_2']
          st.session_state.readyP1 = False
          st.session_state.readyP2 = False
          st.session_state.status = 'connected'
          st.session_state.refresh = True
          st.rerun()

        else:
          st.error('NO ROOM FOUND')
      else:
        st.error('???')

with c2:
  st.markdown(f"<h5 style='text-align: center;'>{SUPABASE.table('ActivePlayersDB').select('Player_1').eq('room-id',st.session_state.room_id).execute().data[0]['Player_1']}'s ROOM</h5>", unsafe_allow_html=True)
  if st.session_state.status == 'connected':
    st.write('')
    st.divider()
    with st.form('P1',):
      st.write('READY?')
      if st.form_submit_button('ready?'):
        if st.session_state.alias == st.session_state.Player_1:
          st.session_state.readyP1 = True
          st.success('READY!')
      
with c3:
  Player_2 = SUPABASE.table('ActivePlayersDB').select('Player_2').eq('room-id',st.session_state.room_id).execute().data[0]['Player_2']
  if st.session_state.status == 'connected':
    st.markdown(f"<h5 style='text-align: center;'>{Player_2} connected</h5>", unsafe_allow_html=True)
    st.write('')
    st.divider()
    with st.form('P2'):
      st.write('READY?')
      if st.form_submit_button('ready?'):
        if st.session_state.alias == st.session_state.Player_2:
          st.session_state.readyP2 = True
          st.success('READY!')
          
  

if 'turn' not in st.session_state:
  if random.randint(0,1) == 0:
    st.session_state.turn = 'Player_1'
  else:
    st.session_state.turn = 'Player_2'

def move(index):
  if 'counter' not in st.session_state:
    st.session_state.counter = 1
    SUPABASE.table('defaultOTTTDB').insert({f'Tile{index}':'X'}).execute()
  else:
    st.session_state.counter += 1

  if st.session_state.counter % 2 == 1:
    SUPABASE.table('defaultOTTTDB').update({f'Tile{index}':'X'}).eq('id',st.session_state.game_id).execute()
  else:
    SUPABASE.table('defaultOTTTDB').update({f'Tile{index}':'O'}).eq('id',st.session_state.game_id).execute()
    st.rerun()

def create_board():
  board_data = SUPABASE.table('defaultOTTTDB').select('*').eq('id',game_id).execute().data
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
    for i in range(1,4):
      columns = st.columns(3)
      for j in range(1,4):
        index = int(f'{i}{j}')
        with columns[j]:
          state = bool(board_data[0][f'Tile{index}'])
          if state:
            st.write(board_data[0][f'Tile{index}'])
          else:
            st.button('',key=f'tile{index}' ,on_click=move(), args=(index))

def get_game_id():
    query = SUPABASE.table('defaultOTTTDB').insert({})
    response = query.execute()
    st.session_state.game_id = response.data[0]['id']

if st.session_state.status == 'connected':
  if st.session_state.readyP1 and st.session_state.readyP2:
    if 'game_id' not in st.session_state:
      get_game_id()
      
    st.divider()
    create_board()
