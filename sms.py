# import os
# from twilio.rest import Client

# account_sid = "AC5f879e1950492316bd67150703f0aee2"
# auth_token = "84385c74b21d11aa856f9ee64e74d1c9"
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#   body="(🚨🚨🚨I am in Trouble🚨🚨🚨)",
#   from_="+13204139325",
#   to="+919360214003"
# )
# print(message.sid)

import streamlit as st
from twilio.rest import Client

def send_message(body, to):
    account_sid = "AC5f879e1950492316bd67150703f0aee2"
    auth_token = "" 
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_="+13204139325",
        to=to
    )
    return message.sid

st.title("Send Alert Message")

body = ("(🚨🚨🚨I am in Trouble🚨🚨🚨 //// 🚨🚨🚨I NEED HELP🚨🚨🚨)")
to = ("")

if st.columns(3)[1].button("SOS Button"):
    message_sid = send_message(body, to)
    st.success(f"Message sent! SID: {message_sid}")
