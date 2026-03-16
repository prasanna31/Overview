import streamlit as st
import base64

st.set_page_config(
    page_title="Jayaprasanna R | AI Portfolio",
    page_icon="🤖",
    layout="wide"
)

# ---------- FUNCTION TO SET BACKGROUND ----------
def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .glass {{
        background: rgba(0,0,0,0.6);
        padding: 40px;
        border-radius: 15px;
    }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)


# ---------- SET BACKGROUND ----------
set_background("/Users/jayaprasannar/Documents/GitHub/Overview/background.jpeg")


# ---------- TITLE SECTION ----------
col1, col2 = st.columns([1,2])

with col1:
    st.image("/Users/jayaprasannar/Documents/GitHub/Overview/profile.jpeg", width=250)

with col2:
    st.title("👋 Hello, I'm Jayaprasanna R")
    st.subheader("AI Enthusiast | Backend Developer | ML Researcher")

    st.markdown("""
    I build **AI systems, machine learning models, and scalable backend applications**.

    My passion is understanding the **mathematics behind intelligence** and turning those
    ideas into real-world systems.
    """)

st.markdown("---")


# ---------- ABOUT ----------
st.markdown("""
### 🚀 About Me

- 🤖 Artificial Intelligence & Machine Learning  
- 🧠 Deep Learning and Neural Networks  
- 📊 Optimization Algorithms  
- ⚙️ Backend Engineering  
- 🎮 Machine Learning for Games & Sports  

I enjoy **breaking down complex concepts** and documenting them clearly through
projects, experiments, and technical writing.
""")


# ---------- HIGHLIGHTS ----------
st.markdown("### ✨ Highlights")

col1, col2, col3 = st.columns(3)

col1.metric("ML Projects", "10+")
col2.metric("Research Areas", "AI / Optimization")
col3.metric("Focus", "Practical AI Systems")


st.markdown("---")

st.info(
    "💡 This portfolio evolves as I explore new ideas in AI, optimization, and intelligent systems."
)