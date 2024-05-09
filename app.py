import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Kshitiz Bhargava", page_icon="👨‍💻", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/eb02d499-513b-4604-9f0a-f4bea7d13756/Mieu8YwRIZ.json")
img_self = Image.open("images/IMG_0479.jpeg")
img_flashchat = Image.open("images/flashchat.png")

with st.container():
    st_columns = st.columns([2, 0.1, 1])
    with st_columns[0]:
        st.title("Hi, I am Kshitiz Bhargava :wave:")
        st.subheader("Final Year Bachelor of Technology Student at VIT, Vellore")
        st.write("To know more about my projects and work, head over to my [GitHub](https://github.com/Kshitiz-b) profile.")
    with st_columns[2]:
        st.image(img_self, width=250, caption="Kshitiz Bhargava")

with st.container():
    st.write("---")
    st_columns = st.columns(2)
    with st_columns[0]:
        st.header("About Me")
        st.write("I am a Computer Science and Engineering major with a strong passion for software development, backed by a diverse skill set that includes expertise in HTML, CSS, C, C++, Java, and Python. Additionally, I have honed my skills in machine learning, specializing in this cutting-edge field to tackle complex problems and make data-driven decisions. Moreover, I've ventured into app development, harnessing the power of Flutter and Dart to create innovative and user-friendly mobile applications.")
    with st_columns[1]:
        st_lottie(lottie_coding, height=300)

with st.container():
    st.write("---")
    st.header("My Projects")
    st_columns = st.columns([1, 2])
    with st_columns[0]:
        st.image(img_flashchat, width=250)
    with st_columns[1]:
        st.subheader("FlashChat")
        st.write("A group chat app leveraging Firebase for backend services.")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    contact_form = """
    <form action="https://formsubmit.co/kshitizb168@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st_columns = st.columns(2)
    with st_columns[0]:
        st.markdown(contact_form, unsafe_allow_html=True)
    with st_columns[1]:
        st.empty()
