import streamlit as st
import send_mail

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject : New mail from {user_email}
From: {user_email}
{raw_message}

Regards:
{user_email}
"""
    button = st.form_submit_button()
    if button:
        send_mail.mail_sender(message)
        st.info("Your mail was sent successfully.")
