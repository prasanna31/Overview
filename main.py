import streamlit as st

st.set_page_config(
    page_title="Jayaprasanna R | AI Portfolio",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("👋 Hello, I'm Jayaprasanna R")

# Subtitle
st.subheader("AI Enthusiast | Backend Developer | Machine Learning Researcher")

st.markdown("---")

# Introduction
st.markdown("""
Welcome! I'm **Jayaprasanna**, a developer and researcher passionate about building intelligent systems.

My work lies at the intersection of **Artificial Intelligence, Machine Learning, and Scalable Backend Systems**.  
I enjoy understanding the **mathematics behind algorithms** and turning those ideas into practical applications.

Currently, my interests include:

- 🤖 Artificial Intelligence & Machine Learning  
- 🧠 Deep Learning and Neural Networks  
- 📊 Optimization Algorithms  
- ⚙️ Backend Engineering and System Design  
- 🎮 Machine Learning for Games and Sports  

I also enjoy **breaking down complex concepts** and documenting them clearly — whether it's through **projects, research, or writing technical books**.

This app serves as a space where I showcase:

- 📚 Projects  
- 🧪 Experiments  
- 📈 Machine Learning Models  
- 📝 Research Notes  
- 🚀 Interactive Demos
""")

st.markdown("---")

# Highlights
st.header("✨ Highlights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="ML Projects", value="10+")

with col2:
    st.metric(label="Research Areas", value="AI / Optimization")

with col3:
    st.metric(label="Focus", value="Practical AI Systems")

st.markdown("---")

# Closing
st.info(
    "💡 This portfolio is continuously evolving as I explore new ideas in AI, machine learning, and system design."
)