import streamlit as st
from streamlit_autorefresh import st_autorefresh
import random
import time
import supabase as sb

SUPABASE = sb.create_client(st.secrets['sbURL'],st.secrets['sbPubAPI'])

st_autorefresh(interval=10000)

if 'status' not in st.session_state:
  st.session_state.status = 'waiting'
  
if 'room_id' not in st.session_state:
  room_id = random.randint(1000,999999)
  st.query_params['room_id'] = room_id
  st.session_state.room_id = room_id

if 'table_initiated' not in st.session_state:
  st.session_state.table_initiated = True
  st.session_state.Player_1 = st.session_state.alias
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
      if id_str == None or id_str == '':
        room_code = 0
      else:
        room_code = int(id_str)
      room = SUPABASE.table('ActivePlayersDB').select('*').eq('room-id',room_code).execute().data
      if room:
        if room_code == room[0]['room-id']:
          st.session_state.room_id = room_code
          st.query_params['room_id'] = room_code
          SUPABASE.table('ActivePlayersDB').update({'Player_2':st.session_state.alias, 'status':'connected'}).eq('room-id',room_code).execute()
          st.success(f"Room ({st.session_state.Player_1}) joined successfully")         
          st.rerun()
        else:
          st.error('NO ROOM FOUND')
      else:
        st.error('???')

status = SUPABASE.table('ActivePlayersDB').select('status').eq('room-id',st.session_state.room_id).execute().data[0]['status']
st.session_state.status = status

if st.session_state.status == 'connected' and 'Player_2' not in st.session_state:
  Players = SUPABASE.table('ActivePlayersDB').select('Player_1,Player_2').eq('room-id',st.session_state.room_id).execute().data[0]
  st.session_state.Player_1, st.session_state.Player_2 = Players['Player_1'], Players['Player_2']

with c2:
  st.markdown(f"<h5 style='text-align: center;'>{st.session_state.Player_1}'s ROOM</h5>", unsafe_allow_html=True)
  if st.session_state.status == 'connected':
    st.write('')
    st.divider()
    with st.form('P1',):
      st.write('READY?')
      if st.form_submit_button('ready?'):
        if st.session_state.alias == st.session_state.Player_1:
          SUPABASE.table('ActivePlayersDB').update({'readyP1':True}).eq('room-id',st.session_state.room_id).execute()
          st.success('READY!')
      
with c3:
  if st.session_state.status == 'connected':
    st.markdown(f"<h5 style='text-align: center;'>{st.session_state.Player_2} connected</h5>", unsafe_allow_html=True)
    st.write('')
    st.divider()
    with st.form('P2'):
      st.write('READY?')
      if st.form_submit_button('ready?'):
        if st.session_state.alias == st.session_state.Player_2:
          SUPABASE.table('ActivePlayersDB').update({'readyP2':True}).eq('room-id',st.session_state.room_id).execute()
          st.success('READY!')

if 'game_start' not in st.session_state:
  ready_status = SUPABASE.table('ActivePlayersDB').select('readyP1,readyP2').eq('room-id',st.session_state.room_id).execute().data[0]
  st.session_state.game_start = True if (ready_status['readyP1'] and ready_status['readyP2']) else False
#------------------------------------------------------------------------------------------------------------------------------------------------------------

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
  board_data = SUPABASE.table('defaultOTTTDB').select('*').eq('id',st.session_state.game_id).execute().data
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
    for i in range(0,3):
      columns = st.columns(3)
      for j in range(0,3):
        index = int(f'{i}{j}')
        with columns[j]:
          state = bool(board_data[0][f'Tile{index}'])
          if state:
            st.write(board_data[0][f'Tile{index}'])
          else:
            st.button('',key=f'tile{index}' ,on_click=move, args=(index))

def get_game_id():
    query = SUPABASE.table('defaultOTTTDB').insert({})
    response = query.execute()
    st.session_state.game_id = response.data[0]['id']

if st.session_state.status == 'connected':
  if st.session_state.game_start:
    if 'game_id' not in st.session_state:
      get_game_id()
      
    st.divider()
    create_board()
