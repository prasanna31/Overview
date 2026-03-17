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

st.title("Machine Learning")
with st.expander("Supervised Learning"):
    st.markdown("""
## Supervised Learning

Supervised Learning is a machine learning paradigm where a model learns a mapping from **inputs (features)** to **outputs (labels)** using a labeled dataset.

Each training example is represented as:

xᵢ → input vector  
yᵢ → corresponding label

The training dataset is:

D = {(x₁,y₁), (x₂,y₂), (x₃,y₃) ... (xₙ,yₙ)}

The goal of the learning algorithm is to find a function:

f(x) ≈ y

that minimizes prediction error on unseen data.

Formally, the model tries to minimize a **loss function**:

L(y, f(x))

and learns parameters θ such that:

θ* = argmin Σ L(yᵢ , f(xᵢ))

---

## Types of Supervised Learning

### 1. Regression

Regression predicts **continuous values**.

Example:

Predict house price from features

x = (size, location, rooms)

y = price

The output variable is a **real number**.

---

### 2. Classification

Classification predicts **categorical labels**.

Examples:

Spam / Not Spam  
Fraud / Not Fraud  
Cat / Dog / Car

The output variable belongs to a **finite set of classes**.

---

# Major Supervised Learning Algorithms

---

REGRESSION (IN-DEPTH EXPLANATION)

1. What is Regression

Regression is a machine learning and statistical technique used to model the
relationship between variables and predict a continuous numerical output.

Unlike classification, which predicts categories (spam/not spam),
regression predicts real numbers.

Examples
- Predicting house prices
- Predicting temperature
- Predicting stock prices
- Predicting revenue
- Predicting electricity demand


------------------------------------------------------------

2. Basic Idea

Regression tries to learn a function that maps inputs to outputs.

Input variables → Features
Output variable → Target

Example

House Size → House Price

The model tries to learn:

Price = f(Size)


------------------------------------------------------------

3. Linear Regression

The simplest regression model assumes the relationship is linear.

Equation

y = β0 + β1x

Where

y  = predicted value
x  = input variable
β0 = intercept (value when x = 0)
β1 = slope (rate of change)

Example

Price = 50000 + 150 × Size

Meaning
Every extra square foot increases price by $150.


------------------------------------------------------------

4. Multiple Linear Regression

Sometimes we have multiple input variables.

Example house dataset

Size
Bedrooms
Location
Age

The model becomes

y = β0 + β1x1 + β2x2 + β3x3 + ... + βnxn

Example

Price =
50000
+ 120 × Size
+ 20000 × Bedrooms
+ 30000 × LocationScore


------------------------------------------------------------

5. Goal of Regression

Regression tries to find parameters that minimize prediction error.

The difference between prediction and true value is called a residual.

Residual

Residual = Actual Value − Predicted Value


------------------------------------------------------------

6. Loss Function

To train regression models we use a loss function.

The most common one is Mean Squared Error (MSE).

MSE = average of (Actual − Predicted)^2

Why squared?

• penalizes large errors more
• keeps values positive
• easier to optimize mathematically


------------------------------------------------------------

7. Optimization

To minimize loss, algorithms adjust model parameters.

The most common algorithm is Gradient Descent.

Gradient Descent repeatedly updates parameters in the direction that
reduces prediction error.

Update rule

New Parameter = Old Parameter − LearningRate × Gradient


------------------------------------------------------------

8. Polynomial Regression

Linear regression cannot model curves.

Polynomial regression solves this by adding higher order terms.

Example

y = β0 + β1x + β2x² + β3x³

This allows the model to capture nonlinear patterns.


------------------------------------------------------------

9. Regularization in Regression

When models become too complex they overfit the training data.

Regularization adds penalties to keep coefficients small.

Two major types exist.


Ridge Regression (L2)

Adds penalty on squared coefficients.

Loss = MSE + λ(β1² + β2² + ... + βn²)

Effect
• reduces large coefficients
• stabilizes the model


Lasso Regression (L1)

Adds penalty on absolute coefficients.

Loss = MSE + λ(|β1| + |β2| + ... + |βn|)

Effect
• forces some coefficients to become zero
• performs feature selection


Elastic Net

Combines L1 and L2 penalties.


------------------------------------------------------------

10. Overfitting

Overfitting happens when the model memorizes training data instead of
learning general patterns.

Signs

• very low training error
• high test error

Causes

• too many features
• complex model
• small dataset


------------------------------------------------------------

11. Underfitting

Underfitting happens when the model is too simple to capture patterns.

Example

Using a straight line to fit a curved dataset.

Signs

• high training error
• high test error


------------------------------------------------------------

12. Evaluation Metrics

R² Score (Coefficient of Determination)

Measures how much variance in the target variable is explained by the model.

R² = 1 − (Residual Sum of Squares / Total Sum of Squares)

Interpretation

R² = 1  → perfect model
R² = 0  → model explains nothing


Other metrics

MAE  (Mean Absolute Error)
RMSE (Root Mean Squared Error)


------------------------------------------------------------

13. Types of Regression Models

Linear Regression
Models linear relationships.

Polynomial Regression
Captures nonlinear curves.

Ridge Regression
Controls large coefficients.

Lasso Regression
Performs feature selection.

Elastic Net
Combines ridge and lasso penalties.

Support Vector Regression (SVR)
Uses margin-based optimization.

Bayesian Regression
Treats parameters as probability distributions.

Quantile Regression
Predicts different percentiles of the target variable.


------------------------------------------------------------

14. Real World Applications

Economics
Predict GDP growth.

Healthcare
Predict disease risk.

Finance
Predict stock returns.

Retail
Predict product demand.

Energy
Predict electricity consumption.

Weather
Predict temperature and rainfall.


------------------------------------------------------------

15. Intuition

Regression is essentially about fitting the best curve through data.

The model tries to answer:

"What function best explains how inputs influence outputs?"

# Evaluation Metrics

### Regression

Mean Squared Error

MSE = (1/n) Σ (y − ŷ)²

Root Mean Squared Error

RMSE = √MSE

R² Score

Measures variance explained.

---

### Classification

Accuracy

Precision

Recall

F1 Score

ROC-AUC

---

Supervised learning forms the backbone of modern AI systems such as recommendation engines, fraud detection systems, medical diagnosis tools, and natural language classifiers.
""")

with st.expander("Unsupervised Learning"):
    st.markdown("")

with st.expander("Reinforcement Learning"):
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