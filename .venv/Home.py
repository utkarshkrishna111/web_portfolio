import streamlit as st
import pandas

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

col3, empty_col ,col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv(".venv/data.csv", sep= ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(".venv/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(".venv/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")