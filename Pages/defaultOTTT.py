import streamlit as st
import random
import supabase as sb

SUPABASE = sb.create_client(st.secrets['sbURL'],st.secrets['sbPubAPI'])
#if 'room-id' not in st.session_state:

#@st.cache_data
def id_gen():
  num = random.randint(1000,999999)
  return num

room_id = id_gen()
st.query_params['room_id'] = room_id
SUPABASE.table('ActivePlayersDB').insert({'room-id':room_id, 'Player_1':st.session_state.alias}).execute()

st.markdown('<h1 style="text-align: center;">CLASSIC TICTACTOE</h1>', unsafe_allow_html=True)
st.divider()
  
c1,c2,c3 = st.columns(3)
with c1:
  with st.expander('ROOM-ID'):
    st.write(room_id)
  st.divider()
  
  st.write('JOIN ROOM')
  with st.form('join_match',clear_on_submit=True):
    id_str = st.text_input('Enter Room Code')
    if st.form_submit_button('SUBMIT'):
      if id_str == None:
        id = 0
      else:
        id = int(id_str)
      room = SUPABASE.table('ActivePlayersDB').select('*').eq('room-id',id).execute().data
      if room:
        if id == room[0]['room-id']:
          
          res = SUPABASE.table('ActivePlayersDB').update({'Player_2':st.session_state.alias}).eq('room-id',id).select().execute()
          st.write(res.data)
          st.query_params['room_id'] = id
          st.success(f"Room ({SUPABASE.table('ActivePlayersDB').select('Player_1').eq('room-id',id).execute().data[0]['Player_1']}) joined successfully")
      else:
        st.error('NO ROOM FOUND')

with c2:
  st.write(f"{SUPABASE.table('ActivePlayersDB').select('Player_1').eq('room-id',id).execute().data[0]['Player_1']}'s ROOM")
  Player_2 = SUPABASE.table('ActivePlayersDB').select('Player_2').eq('room-id',id).execute().data[0]['Player_2']
  if Player_2 != None and Player_2 != 'NULL':
    st.write(f'{Player_2} connected')

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
  
'''
def move(id):
  

for i in range(3):
  columns = st.columns(3)
  for j in range(3):
    n = i*3 + j
    with columns[j]:
      st.button('',key=f'tile{n}',on_click=move(), args=(n)):
'''      
    
