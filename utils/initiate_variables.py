import streamlit as st
from .chat_utils import get_initial_message 

def init_state_vars():
    "Initialize session state variables"
    if 'generated_messages' not in st.session_state: st.session_state['generated_messages'] = get_initial_message()
    if 'past_query' not in st.session_state: st.session_state['past_query'] = ["."]
    if 'input' not in st.session_state: st.session_state['input'] = ""
    if 'messages' not in st.session_state: st.session_state['messages'] = get_initial_message()
    if 'lock_input' not in st.session_state: st.session_state["lock_input"] = False
    if 'query' not in st.session_state: st.session_state['query'] = ""
    if 'send_button_clicked' not in st.session_state: st.session_state['send_button_clicked'] = False
    if 'last_clicked' not in st.session_state:st.session_state['last_clicked'] = 0

# Function to load CSS file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)