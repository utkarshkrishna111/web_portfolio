import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(".venv/images/photo.jpg",width = 300)

with col2:
    st.title("Utkarsh")
    content = """ Hi, I am Utkarsh. I am a python programmer and automation tester."""
    st.info(content)

content2 = """ Below you can find some of the applications I have built using Python. Feel free to contact me! """
st.write(content2)

