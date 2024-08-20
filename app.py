from PIL import Image
import streamlit as st
from st_social_media_links import SocialMediaIcons
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Website", page_icon="💻", layout="wide")  

social_media_links = [
     "https://instagram.com/rayan_jpg",
     "https://github.com/Rayanlupo"
     "x.com/G_rayan21"
]
social_media_icons = SocialMediaIcons(social_media_links)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def local_css(file_name):
     with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")
     
lottie_coding = load_lottieurl("https://lottie.host/3d8eda2f-c9b8-47a2-803f-ab998db7faa4/TP1z0SoB4m.json")
img_arcade = Image.open("img_arcadeAPI.png")
img_files = Image.open("img_fileOrganizer.png")
with st.container():
    st.subheader("Hi, I'm Rayan")
    st.title("a Python Developer and Hardare Prototyper")
    

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My skills")

        st.subheader("Hardare Designing and Prototyping")
        st.write("- Fusion360") 
        st.write("- PCB design") 
        
        st.subheader("Python Development")
        st.write("- Data Management")
        st.write("- Task Automation")
        st.write("- Back-end Development")  
        
    with right_column:
        st.write("##")
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
with st.container():
    st.write("---")
    
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/contact@rayane.tech" method="POST">
        <input type="text" name="name"  placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email Address" required>
        <textarea name="message" placeholder ="Your Message Here" require></textarea>
        <input type="hidden" name="_captcha" value="false">
        <div class="button_container">
            <button type="submit">Send</button>
        </div>
    </form>

"""
left_column, right_column = st.columns(2)
with left_column:
    st.header("Let's get in touch")
    st.write("If you are working on a project and you need help with a part of it, or if you want to talk about a something just send me an message through my Instagram or this form, i'll answer you back in some hours, Maximum 2 days")
    social_media_icons.render()
with right_column:
       st.markdown(contact_form, unsafe_allow_html=True)



