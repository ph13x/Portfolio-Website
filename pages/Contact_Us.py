import streamlit as st
from send_emails import send_email                              

st.header("Contact Me")

with st.form(key="emailer"):
    user_email = st.text_input("Your email address:", placeholder="user@example.com...")

    user_message = st.text_area("Your message:")
    button = st.form_submit_button("Submit")
    message = "Subject: Philip Joseph" + "\n" + user_email + "\n" + user_message
    if button:
       
        send_email(user_message=message)
       
        