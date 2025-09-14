import streamlit as st
                                

st.header("Contact Me")

with st.form(key="emailer"):
    user_email = st.text_input("Your email address:", placeholder="user@example.com...")

    user_message = st.text_area("Your message:")
    button = st.form_submit_button("Submit")
    if button:
       message = f"""Subject: Philip Joseph
       This was sent from {'[{user_email}]({user_email})'}
            '{user_message}'
        """
       