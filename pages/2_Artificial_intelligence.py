import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components


st.title("Artificial Intelligence Overview")
with st.expander("AI graph"):
    st.title("Artificial Intelligence Ecosystem")

    # Create graph
    G = nx.Graph()

    edges = [

    ("Artificial Intelligence","Machine Learning"),
    ("Artificial Intelligence","Deep Learning"),
    ("Artificial Intelligence","Natural Language Processing"),
    ("Artificial Intelligence","Computer Vision"),
    ("Artificial Intelligence","Robotics"),
    ("Artificial Intelligence","Generative AI"),

    ("Machine Learning","Supervised Learning"),
    ("Machine Learning","Unsupervised Learning"),
    ("Machine Learning","Reinforcement Learning"),

    ("Deep Learning","Neural Networks"),
    ("Deep Learning","CNN"),
    ("Deep Learning","RNN"),
    ("Deep Learning","Transformers"),

    ("Natural Language Processing","Tokenization"),
    ("Natural Language Processing","Language Models"),
    ("Natural Language Processing","Text Classification"),
    ("Natural Language Processing","Machine Translation"),

    ("Generative AI","Large Language Models"),
    ("Generative AI","Diffusion Models"),
    ("Generative AI","GANs"),

    ("Large Language Models","GPT"),
    ("Large Language Models","BERT"),
    ("Large Language Models","LLaMA"),

    ("Generative AI","Retrieval Augmented Generation"),
    ("Retrieval Augmented Generation","Embeddings"),
    ("Retrieval Augmented Generation","Vector Databases"),

    ("Vector Databases","FAISS"),
    ("Vector Databases","Pinecone"),
    ("Vector Databases","Weaviate"),

    ("Artificial Intelligence","AI Infrastructure"),
    ("AI Infrastructure","GPU Computing"),
    ("AI Infrastructure","Model Training"),
    ("AI Infrastructure","Model Serving"),
    ("AI Infrastructure","Inference Engines"),

    ("Artificial Intelligence","AI Applications"),
    ("AI Applications","Chatbots"),
    ("AI Applications","Recommendation Systems"),
    ("AI Applications","Autonomous Vehicles"),
    ("AI Applications","Healthcare AI"),
    ("AI Applications","Fraud Detection")

    ]

    G.add_edges_from(edges)

    # Build interactive network
    net = Network(height="700px", width="100%", bgcolor="#111111", font_color="white")

    for node in G.nodes:
        net.add_node(node, label=node)

    for edge in G.edges:
        net.add_edge(edge[0], edge[1])

    net.repulsion()

    # Save and display


    net.save_graph("ai_graph.html")

    HtmlFile = open("ai_graph.html", "r", encoding="utf-8")
    components.html(HtmlFile.read(), height=700)

with st.expander("Clear AI overview"):
    import streamlit as st
    from graphviz import Digraph
    import streamlit.components.v1 as components

    st.title("AI Ecosystem Tree")

    dot = Digraph(comment="Artificial Intelligence")

    # Root
    dot.node("AI", "Artificial Intelligence")

    # Level 1
    dot.node("ML", "Machine Learning")
    dot.node("DL", "Deep Learning")
    dot.node("NLP", "Natural Language Processing")
    dot.node("CV", "Computer Vision")
    dot.node("GenAI", "Generative AI")
    dot.node("Infra", "AI Infrastructure")
    dot.node("Apps", "AI Applications")

    dot.edges([
        ("AI", "ML"),
        ("AI", "DL"),
        ("AI", "NLP"),
        ("AI", "CV"),
        ("AI", "GenAI"),
        ("AI", "Infra"),
        ("AI", "Apps"),
    ])

    # Level 2 - ML
    dot.node("Supervised", "Supervised Learning")
    dot.node("Unsupervised", "Unsupervised Learning")
    dot.node("RL", "Reinforcement Learning")
    dot.edges([
        ("ML", "Supervised"),
        ("ML", "Unsupervised"),
        ("ML", "RL"),
    ])

    # Level 2 - Deep Learning
    dot.node("CNN", "CNN")
    dot.node("RNN", "RNN")
    dot.node("Transformers", "Transformers")
    dot.edges([
        ("DL", "CNN"),
        ("DL", "RNN"),
        ("DL", "Transformers"),
    ])

    # Level 2 - Generative AI
    dot.node("LLM", "Large Language Models")
    dot.node("Diffusion", "Diffusion Models")
    dot.node("GANs", "GANs")
    dot.edges([
        ("GenAI", "LLM"),
        ("GenAI", "Diffusion"),
        ("GenAI", "GANs"),
    ])

    # Level 3 - LLM
    dot.node("GPT", "GPT")
    dot.node("BERT", "BERT")
    dot.node("LLaMA", "LLaMA")
    dot.edges([
        ("LLM", "GPT"),
        ("LLM", "BERT"),
        ("LLM", "LLaMA"),
    ])

    # Level 2 - RAG / Retrieval
    dot.node("RAG", "Retrieval-Augmented Generation")
    dot.node("VectorDB", "Vector Databases")
    dot.node("Embeddings", "Embeddings")
    dot.edges([
        ("GenAI", "RAG"),
        ("RAG", "VectorDB"),
        ("RAG", "Embeddings"),
    ])

    # Render the tree
    st.graphviz_chart(dot)


import streamlit as st

st.title("Artificial Intelligence Topics")

with st.expander("Definition of AI"):
    st.markdown("")

with st.expander("Why AI Exists"):
    st.markdown("")

with st.expander("Core Goals of AI"):
    st.markdown("")

with st.expander("Difference between AI, ML, and GenAI"):
    st.markdown("")

st.title("# 2️⃣ Machine Learning")
with st.expander("Supervised Learning"):
    st.markdown("")

with st.expander("Unsupervised Learning"):
    st.markdown("")

with st.expander("Reinforcement Learning"):
    st.markdown("")

st.title("# 3️⃣ Deep Learning")
with st.expander("Neural Networks"):
    st.markdown("")

with st.expander("CNN, RNN, Transformers"):
    st.markdown("")

st.title("# 4️⃣ Natural Language Processing")
with st.expander("Language Models"):
    st.markdown("")

with st.expander("Tokenization"):
    st.markdown("")

with st.expander("Text Classification"):
    st.markdown("")

with st.expander("Machine Translation"):
    st.markdown("")

st.title("# 5️⃣ Generative AI")
with st.expander("Large Language Models (GPT, BERT, LLaMA)"):
    st.markdown("")

with st.expander("Diffusion Models"):
    st.markdown("")

with st.expander("GANs"):
    st.markdown("")

with st.expander("Retrieval-Augmented Generation (RAG)"):
    st.markdown("")

st.title("# 6️⃣ AI Infrastructure")
with st.expander("GPUs & Hardware"):
    st.markdown("")

with st.expander("Model Training"):
    st.markdown("")

with st.expander("Model Serving & Inference"):
    st.markdown("")

st.title("# 7️⃣ AI Applications")
with st.expander("Chatbots"):
    st.markdown("")

with st.expander("Recommender Systems"):
    st.markdown("")

with st.expander("Autonomous Vehicles"):
    st.markdown("")

with st.expander("Healthcare AI"):
    st.markdown("")

with st.expander("Fraud Detection"):
    st.markdown("")

st.title("# 8️⃣ Data Preparation & Preprocessing (Non-Technical) ")
with st.expander("Data Collection"):
    st.markdown("")

with st.expander("Data Cleaning / Cleansing"):
    st.markdown("")

with st.expander("Data Labeling & Annotation"):
    st.markdown("")

with st.expander("Feature Engineering"):
    st.markdown("")

with st.expander("Data Augmentation"):
    st.markdown("")

st.title("# 9️⃣ Deployment & Production (Non-Technical / DevOps)")
with st.expander("Model Deployment"):
    st.markdown("")

with st.expander("Serving & API Creation"):
    st.markdown("")

with st.expander("Monitoring & Logging"):
    st.markdown("")

with st.expander("Scaling & Infrastructure Management"):
    st.markdown("")

with st.expander("CI/CD for AI Models"):
    st.markdown("")

with st.expander("Ethics, Fairness & Governance"):
    st.markdown("")