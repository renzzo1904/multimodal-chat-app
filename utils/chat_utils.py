import random
import time
import streamlit as st

def number_generator():
    for i in range(10):
        yield str(i)

def dummy_response_generator():
    """Function to generate a template answer. Debugging and codign purposes."""
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.1)

def get_initial_message():
    """ Get an initial message for the bot"""
    messages=[
            {"role": "assistant", "content": "Hello, how may i help you today 😄"}
        ]
    return messages

def update_chat(messages, role, content):
    """Helper function to update the chat history"""
    if content=="": pass
    else: messages.append({"role": role, "content": content})
    return messages

def print_chat(messages,last_response = None , for_stream=True):
    "helper function to print chat"

    if not for_stream:
        for message in messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
    else:
        try: 
            assert last_response!=None
        except AssertionError:
            st.write("No gnerator for streaming was passed")
            return 
        for message in messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        with st.spinner("generating ..."):
            time.sleep(1) # simulate thinking / delay
            with st.chat_message("assistant"):
                response_str = st.write_stream(last_response)
                return response_str


            

    