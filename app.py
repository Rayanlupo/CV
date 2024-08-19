from PIL import Image
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
img_arcade = Image.open("img_arcadeAPI.png")
img_files = Image.open("img_fileOrganizer.png")
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
        -Fusion360 # 
        -PCB design #
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
    st.header("My Projects")
    st.write("##")

    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_arcade)
    with text_column:
        st.subheader("Arcade Sessions API")
        st.write(
            """
            Arcade is a HackClub's program that gives student the chance to get rewards based on how many hours they work on their projects, to register an hour you have to start a session, and each session is equal to an hour or less where you were working on your project, i made this API to organize all my sessions and have an overview on them. 
            """
                )
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_files)
    with text_column:
        st.subheader("File Organizer")
        st.write(
            """
            i created a file organizer using python to manage my downloads folder            
 """
                )
#Contact
with st.container:
    st.write("---")
    st.header("Let's get in touch")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/contact@rayane.tech" method="POST">
        <input type="text" name="name"  placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email Address" required>
        <input textarea name="message" placeholder ="Your Message Here" require>
        <input name="hidden" name="_captcha" value="false">
        <button type="submit">Send</button>
    </form>

"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()



