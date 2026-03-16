import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

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