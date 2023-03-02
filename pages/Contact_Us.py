import streamlit as st
from send_email import send_email

# st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    raw_subject = st.text_input("What topic do you want to discuss?")
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email} about {raw_subject}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")
