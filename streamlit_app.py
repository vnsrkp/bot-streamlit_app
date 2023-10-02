import requests
import streamlit as st
import chek

st.title("LULLI STAR")
base_url ="https://api.telegram.org/bot6352616190:AAGtyBDCS41GRCFRLNc715E3zeS6ZqOn504"


def send_msg(text):
    
    parameters = {

        "chat_id" : "-4064434721",
        "text" : f"{text}",

    }
    response = requests.get(base_url + "/sendMessage", data = parameters)




a = st.text_input("Type Message Here")
# btn = st.button("Submit")
# if btn:
#     send_msg(a)
send_msg(a)

c = chek.read_msg()

st.write(c)