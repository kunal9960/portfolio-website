import streamlit as st

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/image.png")

with col2:
    st.title("Kunal Dalvi")
    content = """
    Hi, I am Kunal! I am a Python programmer and a passionate data analysis enthusiast, 
    dedicated to unraveling insights from complex datasets through statistical methods and programming.
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")
