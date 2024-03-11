import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")


st.write("<b>Feel free to contact me</b>", unsafe_allow_html=True)
st.markdown(
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kunal-dalvi-0b273b2b4)&nbsp;&nbsp;"
    "[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kunal9960)&nbsp;&nbsp;"
    "[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/bge3cXHuNC)&nbsp;&nbsp;"
)
