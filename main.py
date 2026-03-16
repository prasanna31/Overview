import streamlit as st
import base64


st.markdown("""
<style>
.stApp {
    background-color: #D8E4C5;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<style>

/* Apply Comic Sans to everything */
html, body, [class*="css"]  {
    font-family: "Comic Sans MS", "Comic Sans", cursive;
    color: black;
}

# /* Rainbow gradient text */
# body, p, span, div, h1, h2, h3, h4, h5, h6 {
#     background: linear-gradient(
#         90deg,
#         red,
#         orange,
#         yellow,
#         green,
#         blue,
#         indigo,
#         violet
#     );
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

/* Ensure headings also black */
body, p, span, div, h1, h2, h3, h4, h5, h6 {
    color: black;
}

</style>
""",
unsafe_allow_html=True
)

st.set_page_config(
    page_title="Jayaprasanna R | AI Portfolio",
    page_icon="🤖",
    layout="wide"
)



# ---------- PROFILE IMAGE ----------
with open("./myphoto.jpeg", "rb") as file:
    img = base64.b64encode(file.read()).decode()

st.markdown(
    f"""
    <div class="profile-container">
        <img src="data:image/jpg;base64,{img}">
    </div>
    """,
    unsafe_allow_html=True
)


# ---------- PAGE CONTENT ----------
st.title("👋 Hello, I'm Jayaprasanna R")

st.subheader("AI Enthusiast | Backend Developer | ML Researcher")

st.markdown("""
I build **AI systems, machine learning models, and scalable backend applications**.

My passion is understanding the **mathematics behind intelligence** and turning those
ideas into real-world systems.
""")

st.markdown("---")


st.header("🚀 About Me")

st.markdown("""
- 🤖 Artificial Intelligence & Machine Learning  
- 🧠 Deep Learning and Neural Networks  
- 📊 Optimization Algorithms  
- ⚙️ Backend Engineering  
- 🎮 Machine Learning
""")


st.header("✨ Highlights")

c1, c2, c3 = st.columns(3)

c1.metric("ML Projects", "10+")
c2.metric("Research Areas", "Artificial Intelligence / Backend systems")
c3.metric("Focus", "Practical AI Systems")


st.markdown("---")

st.info("💡 This portfolio grows as I explore AI, optimization, and intelligent systems.")