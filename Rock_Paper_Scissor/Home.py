import streamlit as st
import time
st.set_page_config(page_title='Game Ai', page_icon='📈', layout="wide", initial_sidebar_state="collapsed")
# st.logo('../images/logo.png', icon_image='../images/neww.png')
st.sidebar.title("Hi There!")

welcome_message = """
**Welcome to the Ultimate Rock-Paper-Scissors Showdown! ✊✋✌️**

Step into the arena and challenge yourself in this timeless game of strategy and quick thinking. Whether you're here to relive a classic or test your skills against our AI, get ready for an exciting match! Make your move, and let’s see if you’ve got what it takes to outwit the machine. May the best hand win!
"""

def stream_data():
    time.sleep(2)
    for word in welcome_message.split(" "):
        yield word + " "
        time.sleep(0.02)
    st.image("images/rock.png", caption="Sunrise Of AI",use_column_width ='always')

st.write_stream(stream_data)
