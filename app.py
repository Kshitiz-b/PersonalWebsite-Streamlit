import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Emoji bank https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Kshitiz Bhargava", page_icon="👨‍💻", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# loading assets
lottie_coding = load_lottieurl("https://lottie.host/eb02d499-513b-4604-9f0a-f4bea7d13756/Mieu8YwRIZ.json")
img_self = Image.open("images/IMG_0479.jpeg")
img_flashchat = Image.open("images/flashchat.png")

# Header
with st.container():
    left_column, middle_column ,right_column = st.columns([2, 0.11, 1])
    with left_column:
        st.title("Hi, I am Kshitiz Bhargava :wave:")
        st.subheader("Final Year Bachelor of Technology Student at VIT, Vellore")
        #   st.write("I am passionate about Machine Learning, AWS, Flutter and many more...")
        st.write("To know more about my projects and work head over to my [GitHub](https://github.com/Kshitiz-b) profile")
    with middle_column:
        st.empty()
    with right_column:
        st.image(img_self, width=250)# Load an image from the web
        st.markdown("""
            <style>
            [data-testid="stImage"] img {
                border-radius: 50%;  # This makes the image round
            }
            </style>
            """, unsafe_allow_html=True)
    
# About
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write("""I am a Computer Science and Engineering major with a strong passion for software development, backed by a diverse skill set that includes expertise in HTML, CSS, C, C++, Java, and Python. Additionally, I have honed my skills in machine learning, specializing in this cutting-edge field to tackle complex problems and make data-driven decisions. Moreover, I've ventured into app development, harnessing the power of Flutter and Dart to create innovative and user-friendly mobile applications.""")
                 
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,4))
    with image_column:
        st.image(img_flashchat, width=250)
    with text_column:
        st.subheader("FlashChat")
        st.write("A Group Chat App that uses Firebase as the backend for authentication and database.")

# Contact
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/kshitizb168@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()