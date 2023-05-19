
import streamlit as st
from twilio.rest import Client

def send_message(body, to):
    account_sid = "AC5f879e1950492316bd67150703f0aee2"
    auth_token = "cf9c9ff370163af0f27303af4302c851" 
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_="+13204139325",
        to=to
    )
    return message.sid

st.title("Send Alert Message")

body = ("(🚨🚨🚨I am in Trouble🚨🚨🚨 //// 🚨🚨🚨I NEED HELP🚨🚨🚨)")
to = ("+919944393616")

if st.columns(3)[1].button("SOS Button"):
    message_sid = send_message(body, to)
    st.success(f"Message sent! SID: {message_sid}")
