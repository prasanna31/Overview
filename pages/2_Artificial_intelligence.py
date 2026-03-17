import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

st.markdown("""
<style>
.stApp {
    background-color: #D8E4C5;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* H1 Styling (#) */
h1 {
    background-color: #eef2ff;
    padding: 14px;
    border-left: 10px solid #4f46e5;
    border-radius: 8px;
    font-size: 36px;
}

/* H2 Styling (##) */
h2 {
    background-color: #f5f7ff;
    padding: 10px;
    border-left: 7px solid #6366f1;
    border-radius: 6px;
}

/* H3 Styling (###) */
h3 {
    background-color: #f8f9ff;
    padding: 6px;
    border-left: 4px solid #818cf8;
    border-radius: 4px;
}

/* Optional: nicer paragraph spacing */
p {
    font-size: 17px;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)

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

with st.expander("Artificial Intelligence Topics"):

    with st.expander("Definition of AI"):
        st.markdown("""**Artificial Intelligence (AI)** is the branch of computer science that focuses on creating machines and software capable of performing tasks that normally require human intelligence.  
    These tasks include:

    - Learning from data and experience  
    - Reasoning and problem-solving  
    - Understanding natural language and speech  
    - Making predictions and decisions  

    In short, AI enables computers to **think, learn, and act intelligently**, simulating human cognitive abilities in various domains.
    """)

    with st.expander("Why AI Exists"):
        st.markdown("""
    AI exists because humans alone **cannot efficiently process the massive amounts of data** generated every day.  
    The goals of AI include:

    - **Automating repetitive and complex tasks** that would take humans too long to perform  
    - **Extracting insights from large datasets** to make better decisions  
    - **Enhancing productivity and innovation** across industries  
    - **Solving problems that require intelligence**, such as medical diagnosis, language translation, or autonomous driving  

    In short, AI exists to **augment human intelligence**, allowing machines to assist or perform tasks that are difficult, dangerous, or time-consuming for humans.
    """)

    with st.expander("Core Goals of AI"):
        st.markdown("""
    The **core goals of Artificial Intelligence** are focused on making machines capable of performing intelligent tasks like humans. Key goals include:

    1. **Mimic Human Cognitive Abilities** – AI aims to replicate human-like reasoning, perception, and decision-making.  
    2. **Learn from Experience** – Systems should improve over time by analyzing data and past outcomes.  
    3. **Adapt to New Situations** – AI should generalize knowledge and adjust to unforeseen scenarios.  
    4. **Automate Intelligent Tasks** – Performing tasks efficiently that normally require human intelligence, such as diagnosis, prediction, and planning.  
    5. **Enhance Human Capabilities** – AI is designed to assist humans, augmenting productivity and reducing errors.  

    These goals collectively drive AI development across industries, from healthcare and finance to autonomous systems and creative applications.
    """)

    with st.expander("Difference between AI, ML, and GenAI"):
        st.markdown("""
    Here’s how **Artificial Intelligence (AI)**, **Machine Learning (ML)**, and **Generative AI (GenAI)** differ:

    - **Artificial Intelligence (AI):**  
    The broad field of creating machines that can perform tasks requiring human intelligence.  
    Examples: problem-solving, decision-making, language understanding.

    - **Machine Learning (ML):**  
    A subset of AI where systems **learn patterns from data** and improve over time without explicit programming.  
    Examples: predicting house prices, classifying emails as spam, recommendation systems.

    - **Generative AI (GenAI):**  
    A subset of AI (and often ML) focused on **creating new content** such as text, images, or code.  
    Examples: GPT generating text, DALL·E generating images, GANs creating synthetic data.

    **Summary:**  
    AI is the big umbrella, ML is the learning engine under it, and GenAI is the creative subset producing novel outputs.
    """)

with st.expander("Machine Learning"):
    import streamlit as st

    # 1. Introduction to Machine Learning
    with st.expander("1. Introduction to Machine Learning"):

        with st.expander("1.1 What is Machine Learning"):
            st.markdown("""
        Machine Learning is a branch of Artificial Intelligence that focuses on building systems capable of learning from data rather than being explicitly programmed with rules. Instead of telling a computer exactly how to solve a problem step by step, we provide it with examples and allow it to discover patterns on its own.

        At its core, machine learning is about learning a mapping between inputs and outputs. Given data, the model tries to approximate a function that can generalize well to unseen examples. This ability to generalize is what makes machine learning powerful—it doesn’t just memorize; it learns underlying structure.

        For example, instead of writing thousands of rules to detect spam emails, we train a model on past emails labeled as “spam” or “not spam,” and it learns the patterns that distinguish them. This paradigm shift—from rule-based systems to data-driven learning—is what defines machine learning.
        """)

        with st.expander("1.2 History of Machine Learning"):
            st.markdown("""
        The journey of machine learning began with a simple but profound question: can machines think? In the 1950s, pioneers like Alan Turing laid the conceptual foundation, while early models like the perceptron attempted to mimic how neurons work.

        However, progress was not linear. After initial excitement, limitations in computational power and data led to periods known as “AI winters,” where interest declined. The field regained momentum in the 1980s and 1990s with the rise of statistical learning methods such as decision trees, support vector machines, and Bayesian approaches.

        The real transformation began in the 2000s and accelerated in the 2010s, driven by three key factors: massive datasets, powerful GPUs, and improved algorithms. This era gave birth to deep learning, where neural networks with many layers began outperforming traditional methods in tasks like image recognition, speech processing, and natural language understanding.

        Today, machine learning has evolved from a theoretical idea into a foundational technology that powers much of the modern digital world.
        """)

        with st.expander("1.3 Why Machine Learning Exists"):
            st.markdown("""
        Machine learning exists because many real-world problems are simply too complex to solve using explicit programming. In traditional software development, we define rules and logic manually. But what happens when the problem does not have clear rules?

        Consider recognizing faces in images. Lighting conditions, angles, expressions, and backgrounds vary infinitely. Writing rules to handle all such variations is practically impossible. This is where machine learning becomes essential—it learns directly from data instead of relying on handcrafted logic.

        Another reason is the explosion of data. Every second, enormous amounts of data are generated from sensors, websites, and user interactions. Hidden within this data are patterns that can drive decisions, predictions, and automation. Machine learning provides the tools to extract these patterns efficiently.

        In essence, machine learning exists to bridge the gap between complexity and automation. It allows systems to adapt, improve over time, and make intelligent decisions in environments where traditional programming fails.
        """)

        with st.expander("1.4 Types of Machine Learning"):
            st.markdown("""
        Machine learning can be broadly categorized based on how the model learns from data and the kind of feedback it receives.

        In supervised learning, the model is trained on labeled data, meaning each input comes with a known output. The goal is to learn a mapping from inputs to outputs so that it can make accurate predictions on new data. Common tasks include regression, where outputs are continuous, and classification, where outputs belong to discrete categories.

        Unsupervised learning, on the other hand, deals with unlabeled data. Here, the model tries to uncover hidden patterns or structures within the data. Clustering and dimensionality reduction are typical examples, where the system groups similar data points or compresses information into lower dimensions.

        Semi-supervised learning lies between these two extremes, using a small amount of labeled data along with a large amount of unlabeled data. This is particularly useful when labeling data is expensive or time-consuming.

        Reinforcement learning takes a completely different approach. Instead of learning from a static dataset, an agent interacts with an environment and learns through trial and error. It receives rewards or penalties based on its actions and gradually improves its strategy to maximize long-term rewards.

        Each of these paradigms addresses different kinds of problems, and choosing the right one depends on the nature of the data and the task at hand.
        """)

        with st.expander("1.5 Real-World Applications of Machine Learning"):
            st.markdown("""
        Machine learning is not just a theoretical concept—it is deeply embedded in the technologies we use every day. Its applications span across industries, transforming how systems operate and decisions are made.

        In computer vision, machine learning enables systems to interpret and understand visual data. This powers applications such as facial recognition, medical image analysis, and autonomous driving.

        In natural language processing, it allows machines to understand and generate human language. From chatbots and translation systems to sentiment analysis, machine learning makes human-computer interaction more natural and intuitive.

        Recommendation systems are another powerful application. Platforms like Netflix, Amazon, and Spotify use machine learning to analyze user behavior and suggest content tailored to individual preferences.

        In healthcare, machine learning assists in diagnosing diseases, predicting patient outcomes, and analyzing medical images with remarkable accuracy. In finance, it is used for fraud detection, risk assessment, and algorithmic trading.

        Even everyday tools like voice assistants rely on machine learning for speech recognition and response generation.

        The common thread across all these applications is the ability of machine learning to identify patterns in data and use them to make intelligent decisions, often at a scale and speed that humans cannot match.
        """)



# 2. Mathematical Foundations
with st.expander("2. Mathematical Foundations"):
    with st.expander("2.1 Linear Algebra for ML"):
        st.markdown("")
    with st.expander("2.2 Probability Theory"):
        st.markdown("")
    with st.expander("2.3 Statistics for Machine Learning"):
        st.markdown("")
    with st.expander("2.4 Optimization Theory"):
        st.markdown("")
    with st.expander("2.5 Information Theory"):
        st.markdown("")

# 3. Data and Feature Engineering
with st.expander("3. Data and Feature Engineering"):
    with st.expander("3.1 Types of Data"):
        st.markdown("")
    with st.expander("3.2 Data Collection"):
        st.markdown("")
    with st.expander("3.3 Data Cleaning"):
        st.markdown("")
    with st.expander("3.4 Handling Missing Data"):
        st.markdown("")
    with st.expander("3.5 Feature Engineering"):
        st.markdown("")
    with st.expander("3.6 Feature Scaling"):
        st.markdown("")
    with st.expander("3.7 Feature Selection"):
        st.markdown("")
    with st.expander("3.8 Dimensionality Reduction"):
        st.markdown("")

# 4. Supervised Learning
with st.expander("4. Supervised Learning"):
    with st.expander("4.1 Regression"):
        st.markdown("")
    with st.expander("4.2 Classification"):
        st.markdown("")
    with st.expander("4.3 Bias-Variance Tradeoff"):
        st.markdown("")
    with st.expander("4.4 Model Evaluation Metrics"):
        st.markdown("")
    with st.expander("4.5 Regularization Techniques"):
        st.markdown("")

# 5. Regression Algorithms
with st.expander("5. Regression Algorithms"):
    with st.expander("5.1 Linear Regression"):
        st.markdown("")
    with st.expander("5.2 Polynomial Regression"):
        st.markdown("")
    with st.expander("5.3 Ridge Regression"):
        st.markdown("")
    with st.expander("5.4 Lasso Regression"):
        st.markdown("")
    with st.expander("5.5 Elastic Net"):
        st.markdown("")

# 6. Classification Algorithms
with st.expander("6. Classification Algorithms"):
    with st.expander("6.1 Logistic Regression"):
        st.markdown("")
    with st.expander("6.2 Decision Trees"):
        st.markdown("")
    with st.expander("6.3 Random Forest"):
        st.markdown("")
    with st.expander("6.4 Support Vector Machines"):
        st.markdown("")
    with st.expander("6.5 Naive Bayes"):
        st.markdown("")
    with st.expander("6.6 K-Nearest Neighbors"):
        st.markdown("")
    with st.expander("6.7 Gradient Boosting"):
        st.markdown("")
    with st.expander("6.8 XGBoost / LightGBM / CatBoost"):
        st.markdown("")

# 7. Unsupervised Learning
with st.expander("7. Unsupervised Learning"):
    with st.expander("7.1 Clustering"):
        st.markdown("")
    with st.expander("7.2 Dimensionality Reduction"):
        st.markdown("")
    with st.expander("7.3 Density Estimation"):
        st.markdown("")
    with st.expander("7.4 Association Rule Learning"):
        st.markdown("")

# 8. Clustering Algorithms
with st.expander("8. Clustering Algorithms"):
    with st.expander("8.1 K-Means Clustering"):
        st.markdown("")
    with st.expander("8.2 Hierarchical Clustering"):
        st.markdown("")
    with st.expander("8.3 DBSCAN"):
        st.markdown("")
    with st.expander("8.4 Mean Shift"):
        st.markdown("")
    with st.expander("8.5 Gaussian Mixture Models"):
        st.markdown("")

# 9. Dimensionality Reduction
with st.expander("9. Dimensionality Reduction"):
    with st.expander("9.1 Principal Component Analysis (PCA)"):
        st.markdown("")
    with st.expander("9.2 Linear Discriminant Analysis (LDA)"):
        st.markdown("")
    with st.expander("9.3 t-SNE"):
        st.markdown("")
    with st.expander("9.4 UMAP"):
        st.markdown("")
    with st.expander("9.5 Autoencoders"):
        st.markdown("")

# 10. Semi-Supervised Learning
with st.expander("10. Semi-Supervised Learning"):
    with st.expander("10.1 Self-Training"):
        st.markdown("")
    with st.expander("10.2 Co-Training"):
        st.markdown("")
    with st.expander("10.3 Label Propagation"):
        st.markdown("")
    with st.expander("10.4 Pseudo-Labeling"):
        st.markdown("")

# 11. Reinforcement Learning
with st.expander("11. Reinforcement Learning"):
    with st.expander("11.1 Markov Decision Processes"):
        st.markdown("")
    with st.expander("11.2 Policy vs Value Functions"):
        st.markdown("")
    with st.expander("11.3 Q-Learning"):
        st.markdown("")
    with st.expander("11.4 Deep Q Networks"):
        st.markdown("")
    with st.expander("11.5 Policy Gradient Methods"):
        st.markdown("")
    with st.expander("11.6 Actor-Critic Methods"):
        st.markdown("")

# 12. Ensemble Learning
with st.expander("12. Ensemble Learning"):
    with st.expander("12.1 Bagging"):
        st.markdown("")
    with st.expander("12.2 Boosting"):
        st.markdown("")
    with st.expander("12.3 Stacking"):
        st.markdown("")
    with st.expander("12.4 Voting Classifiers"):
        st.markdown("")

# 13. Neural Networks
with st.expander("13. Neural Networks"):
    with st.expander("13.1 Perceptron"):
        st.markdown("")
    with st.expander("13.2 Multi-Layer Perceptron"):
        st.markdown("")
    with st.expander("13.3 Activation Functions"):
        st.markdown("")
    with st.expander("13.4 Backpropagation"):
        st.markdown("")
    with st.expander("13.5 Loss Functions"):
        st.markdown("")
    with st.expander("13.6 Optimization Algorithms"):
        st.markdown("")

# 14. Deep Learning Architectures
with st.expander("14. Deep Learning Architectures"):
    with st.expander("14.1 Convolutional Neural Networks"):
        st.markdown("")
    with st.expander("14.2 Recurrent Neural Networks"):
        st.markdown("")
    with st.expander("14.3 LSTM and GRU"):
        st.markdown("")
    with st.expander("14.4 Transformers"):
        st.markdown("")
    with st.expander("14.5 Attention Mechanisms"):
        st.markdown("")

# 15. Model Training and Optimization
with st.expander("15. Model Training and Optimization"):
    with st.expander("15.1 Gradient Descent"):
        st.markdown("")
    with st.expander("15.2 Stochastic Gradient Descent"):
        st.markdown("")
    with st.expander("15.3 Mini-Batch Gradient Descent"):
        st.markdown("")
    with st.expander("15.4 Adam Optimizer"):
        st.markdown("")
    with st.expander("15.5 Learning Rate Scheduling"):
        st.markdown("")

# 16. Model Evaluation
with st.expander("16. Model Evaluation"):
    with st.expander("16.1 Train / Validation / Test Split"):
        st.markdown("")
    with st.expander("16.2 Cross Validation"):
        st.markdown("")
    with st.expander("16.3 Confusion Matrix"):
        st.markdown("")
    with st.expander("16.4 Precision Recall"):
        st.markdown("")
    with st.expander("16.5 ROC Curve and AUC"):
        st.markdown("")

# 17. Model Deployment
with st.expander("17. Model Deployment"):
    with st.expander("17.1 Model Serialization"):
        st.markdown("")
    with st.expander("17.2 APIs for ML Models"):
        st.markdown("")
    with st.expander("17.3 Real-Time vs Batch Inference"):
        st.markdown("")
    with st.expander("17.4 Monitoring ML Models"):
        st.markdown("")

# 18. Responsible Machine Learning
with st.expander("18. Responsible Machine Learning"):
    with st.expander("18.1 Bias in Machine Learning"):
        st.markdown("")
    with st.expander("18.2 Fairness"):
        st.markdown("")
    with st.expander("18.3 Explainable AI"):
        st.markdown("")
    with st.expander("18.4 Model Interpretability"):
        st.markdown("")
    with st.expander("18.5 Ethical AI"):
        st.markdown("")
st.title("Deep Learning")
with st.expander("Neural Networks"):
    st.markdown("")

with st.expander("CNN, RNN, Transformers"):
    st.markdown("")

st.title("Natural Language Processing")
with st.expander("Language Models"):
    st.markdown("")

with st.expander("Tokenization"):
    st.markdown("")

with st.expander("Text Classification"):
    st.markdown("")

with st.expander("Machine Translation"):
    st.markdown("")

st.title("Generative AI")
with st.expander("Large Language Models (GPT, BERT, LLaMA)"):
    st.markdown("")

with st.expander("Diffusion Models"):
    st.markdown("")

with st.expander("GANs"):
    st.markdown("")

with st.expander("Retrieval-Augmented Generation (RAG)"):
    st.markdown("")

st.title("AI Infrastructure")
with st.expander("GPUs & Hardware"):
    st.markdown("")

with st.expander("Model Training"):
    st.markdown("")

with st.expander("Model Serving & Inference"):
    st.markdown("")

st.title("AI Applications")
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

st.title("Computer Vision")
with st.expander("Image Classification"):
    st.markdown("")

with st.expander("Object Detection"):
    st.markdown("")

with st.expander("Segmentation"):
    st.markdown("")

with st.expander("Face / Gesture Recognition"):
    st.markdown("")

st.title("Data Preparation & Preprocessing (Non-Technical) ")
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

st.title("Deployment & Production (Non-Technical / DevOps)")
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