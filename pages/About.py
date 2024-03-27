import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 100px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
