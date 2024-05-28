import streamlit as st
import time 

def click_button_send():
    current_time = time.time()
    if current_time - st.session_state['last_clicked'] > .5:  # 1 second debounce
        st.session_state['send_button_clicked'] = True
        st.session_state['last_clicked'] = current_time

        st.session_state.query = st.session_state.text_input
        st.session_state.text_input = ""
    else: pass

def reset_button():
    """Callback to block / unblock input."""
    st.session_state.send_button = not st.session_state.send_button

def send_and_clear_text():
    """Function to clear the text input text"""
    st.session_state.query = st.session_state.text_input
    st.session_state.text_input = ""
    st.write("hooray")
    #click_button_send() # manage the button part 

def send_test():
    """Callback to send whatever is on the text_space"""
    if st.text_input:
        pass



    
