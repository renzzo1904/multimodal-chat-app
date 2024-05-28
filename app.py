import streamlit as st
import io 
import time
from PIL import Image
from audiorecorder import audiorecorder
from utils.chat_utils import dummy_response_generator,update_chat,print_chat
from utils.initiate_variables import init_state_vars,load_css
from utils.callbacks import *

############################################################

st.set_page_config(layout="wide")

init_state_vars()                                                # Initiate all the state variables needed.
load_css("custom-styles-component/custom_send_buton.css")        # Inject CSS

############################################################

with st.sidebar:

    st.title("Multimodal Chat")

    st.selectbox("Select the model enhancing the answers.", ["Model1","Model2"])

############################################################
# - - - -  - - - - - - - - LAYOUT - - - - - - - - - - - - - - 

chat_col, aux_col = st.columns([4,1]) # Create aone column to hold the chat and the other to hold other components

with chat_col:


    chat_space = st.empty()         # create a space for the chat
    inputs_space = st.empty()     # create a space for text_input, audio_input and file_input 

    with chat_space.container(height=400):

            message_space = st.empty() 

    with inputs_space.container():

        input_cols = st.columns([8,1,1])

        input_cols[1].button("",key="send_button",on_click=click_button_send)

        input_cols[0].text_input(".",key="text_input",
                                 label_visibility="collapsed",
                                 placeholder="Send your message",
                                 on_change=send_and_clear_text) # Text Input 

        with input_cols[2]:
            audiorecorder("","")

############################################################
#  - - - - - - - - - UPDATE LAYOUT ELEMENTS - - - - - - - - -  

if st.session_state.messages:
    with message_space.container(): 
        print_chat(st.session_state.messages,for_stream=False) 

if st.session_state.query: # and st.session_state.query != st.session_state.past_query[-1]:

    messages = st.session_state['messages']
    messages = update_chat(messages, "user", st.session_state.query)
    response = dummy_response_generator()    
    st.write(st.session_state.query)
        # Update Layout Elements 
    if st.session_state.messages:
        with message_space.container(): 
            response_str = print_chat(st.session_state.messages,
                       response,
                       for_stream=True) 
    #st.write(st.session_state.send_button_clicked)
    messages = update_chat(messages,"assistant",response_str)

    st.session_state.past_query.append(st.session_state.query)
    st.session_state.generated_messages.append({"role":"assistant","content":response_str})
    st.session_state['send_button_clicked'] = False

    