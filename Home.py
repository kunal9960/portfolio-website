import streamlit as st
import pandas as pd

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

col1, col2 = st.columns(2)
with col1:
    st.image("images/image.gif")

with col2:
    st.title("Kunal Dalvi")
    content = """
    Hi! I'm Kunal. A Python enthusiast with a keen interest in data analysis. 
    I'm driven by curiosity and love taking on new challenges. 
    I'm dedicated to unravel insights from complex datasets through statistical methods and programming.
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python.")

df = pd.read_csv("data.csv", sep=";")

max_rows = max(len(df[:10]), len(df[10:]))

for i in range(max_rows):
    col3, col4 = st.columns(2)

    with col3:
        if i < len(df[:10]):
            row = df.iloc[i]
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            if row["title"] == "PDF Templates":
                st.write(f"[Source Code]({row['url']})")
            else:
                st.write(f"[Link]({row['link']}) &nbsp;&nbsp;&nbsp; [Source Code]({row['url']})")
        else:
            st.empty()

    with col4:
        if i < len(df[10:]):
            row = df.iloc[i + 10]
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Link]({row['link']}) &nbsp;&nbsp;&nbsp; [Source Code]({row['url']})")
        else:
            st.empty()
