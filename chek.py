import requests
import streamlit as st

base_url ="https://api.telegram.org/bot6352616190:AAGtyBDCS41GRCFRLNc715E3zeS6ZqOn504"


def read_msg():

    response = requests.get(base_url + "/getUpdates")

    data = response.json()
    
    # return data["result"][-1]["message"]["text"]


    if data["result"]:
        return data["result"][-1]["update_id"] + 1 and  data["result"][-1]["message"]["text"]

    



read_msg()

# print(read_msg(offset))
# st.write(read_msg(offset))