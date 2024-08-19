import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Website", page_icon=":tada:", layout="wide")  
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://lottie.host/3d8eda2f-c9b8-47a2-803f-ab998db7faa4/TP1z0SoB4m.json")
with st.container():
    st.subheader("Hi, I'm Rayan")
    st.title("a Python Developer and Hardare Prototyper")
    st.write("I use my python skills to work on data management, automations and Back-end development")
    st.write("i use my CAD designing and Electronic circuits skills to protype products as my business card holder or my powerpoint remote")
    st.write("[Instagram](instagram.com/rayan_jpg)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My skills")
        st.write("##")
        st.subheader("Hardare Designing and Prototyping")
        st.write("""
        -Fusion360. 
        -PCB design.
        """)
        st.subheader("Python Development")
        st.write("""
        -Data Managent.
        -Automations.
        -Back-end Development.  
        """)
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")