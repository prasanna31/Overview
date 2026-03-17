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
    
        with st.expander("2.1.1 Scalars"):
            st.markdown("""
        A scalar is the simplest mathematical object—it is just a single number.

        Examples:
        3, -5, 0.7, π

        Scalars represent magnitude without direction. In machine learning, scalars are used to represent quantities such as loss values, weights (in simple models), and individual features.

        Mathematically:
        A scalar belongs to a field (typically ℝ for real numbers).

        Intuition:
        Think of a scalar as a point on a number line. It tells you “how much” but not “where” in space.

        In ML:
        - Learning rate → scalar
        - Loss value → scalar
        - Single feature value → scalar

        Key idea:
        Scalars are the building blocks; everything else (vectors, matrices) is made of scalars.
        """)

        with st.expander("2.1.2 Vectors"):
            st.markdown("""
        A vector is an ordered collection of numbers (scalars).

        Mathematically:
        x = [x₁, x₂, ..., xₙ] ∈ ℝⁿ

        Geometric intuition:
        A vector represents a point or direction in space.

        - In 2D → arrow in a plane
        - In 3D → arrow in space
        - In ML → high-dimensional point

        Example:
        x = [2, 3] → a point in 2D space

        Two interpretations:
        1. As a point → location in space
        2. As an arrow → direction + magnitude

        In Machine Learning:
        Each data point is a vector:
        x = [height, weight, age, income, ...]

        Key idea:
        A vector is a compact way to represent multiple features together.
        """)

        with st.expander("2.1.3 Vector Operations"):
            st.markdown("""
        Vector operations define how vectors interact.

        1. Addition:
        x + y = [x₁ + y₁, x₂ + y₂, ..., xₙ + yₙ]

        Intuition:
        Move along one vector, then the other.

        2. Scalar Multiplication:
        αx = [αx₁, αx₂, ..., αxₙ]

        Intuition:
        Stretch or shrink the vector.

        3. Dot Product:
        x · y = x₁y₁ + x₂y₂ + ... + xₙyₙ

        Geometric Interpretation:
        x · y = ||x|| ||y|| cosθ

        - Measures similarity between vectors
        - If large → similar direction
        - If zero → orthogonal (independent)

        In ML:
        - Used in linear models: y = w·x + b
        - Measures similarity (cosine similarity)

        Key idea:
        Dot product connects algebra with geometry.
        """)

        with st.expander("2.1.4 Vector Norms"):
            st.markdown("""
        A norm measures the length (magnitude) of a vector.

        1. L2 Norm (Euclidean):
        ||x||₂ = √(x₁² + x₂² + ... + xₙ²)

        Intuition:
        Distance from origin in space.

        2. L1 Norm:
        ||x||₁ = |x₁| + |x₂| + ... + |xₙ|

        Intuition:
        Manhattan distance (grid movement).

        3. General p-norm:
        ||x||ₚ = (Σ |xᵢ|ᵖ)^(1/p)

        Why norms matter:
        They quantify size, distance, and regularization.

        In ML:
        - L2 → smooth penalties (Ridge)
        - L1 → sparsity (Lasso)

        Key idea:
        Norm = “how big is this vector?”
        """)

        with st.expander("2.1.5 Matrices"):
            st.markdown("""
        A matrix is a 2D collection of numbers.

        Mathematically:
        A ∈ ℝ^(m×n)

        Example:
        A = [[1, 2],
            [3, 4]]

        Interpretation:
        A matrix represents a linear transformation.

        Geometric intuition:
        Applying a matrix to a vector transforms space:
        - Stretching
        - Rotating
        - Shearing

        In ML:
        - Dataset → matrix (rows = samples, columns = features)
        - Weights → matrices in neural networks

        Key idea:
        A matrix is not just numbers—it is a function acting on vectors.
        """)

        with st.expander("2.1.6 Matrix Operations"):
            st.markdown("""
        1. Matrix Addition:
        A + B → element-wise

        2. Scalar Multiplication:
        αA → scale all elements

        3. Matrix Multiplication:
        C = AB

        Definition:
        C[i][j] = Σ A[i][k] * B[k][j]

        Key condition:
        Columns of A = Rows of B

        Geometric intuition:
        Matrix multiplication = composition of transformations.

        If:
        y = Ax
        z = By

        Then:
        z = B(Ax) = (BA)x

        In ML:
        - Forward pass in neural networks
        - Feature transformations

        Important:
        Matrix multiplication is NOT commutative:
        AB ≠ BA

        Key idea:
        Matrix multiplication = chaining transformations.
        """)

        with st.expander("2.1.7 Special Matrices (Identity, Diagonal, Symmetric)"):
            st.markdown("""
        1. Identity Matrix (I):
        I x = x

        Example:
        I = [[1,0],
            [0,1]]

        Acts like “1” for matrices.

        2. Diagonal Matrix:
        Only diagonal elements are non-zero.

        D = [[d₁,0],
            [0,d₂]]

        Effect:
        Scales each dimension independently.

        3. Symmetric Matrix:
        A = Aᵀ

        Meaning:
        A[i][j] = A[j][i]

        Importance:
        - Real eigenvalues
        - Orthogonal eigenvectors

        In ML:
        - Covariance matrices are symmetric
        - Important in PCA

        Key idea:
        Special matrices simplify complex operations and reveal structure.
        """)
        with st.expander("2.1.8 Systems of Linear Equations"):
            st.markdown("""
        A system of linear equations is a collection of equations that we want to solve simultaneously.

        Example:
        x + y = 2  
        2x + y = 3  

        Goal:
        Find values of x and y that satisfy ALL equations at the same time.

        Matrix Form:
        Ax = b

        Where:
        A → coefficient matrix  
        x → variable vector  
        b → output vector  

        Example:
        [1 1] [x] = [2]  
        [2 1] [y]   [3]  

        Geometric Intuition:
        Each equation represents a geometric object:
        - In 2D → a line
        - In 3D → a plane

        Solution = intersection point of these objects.

        Three possible cases:
        1. Unique solution → lines intersect at one point
        2. Infinite solutions → lines overlap
        3. No solution → lines are parallel

        In Machine Learning:
        Most models try to solve Ax = b (or approximate it):
        - Linear regression
        - Least squares problems

        Key idea:
        Solving equations = finding where multiple constraints meet.
        """)

        with st.expander("2.1.9 Gaussian Elimination"):
            st.markdown("""
        Gaussian Elimination is a systematic method to solve Ax = b by transforming the matrix into a simpler form.

        Goal:
        Convert matrix into upper triangular form.

        Steps:
        1. Make zeros below the pivot (leading element)
        2. Repeat for each column
        3. Back substitute to find variables

        Example:
        x + y = 2  
        2x + y = 3  

        Step 1:
        Subtract 2 × (first row) from second row

        New system:
        x + y = 2  
        -y = -1  

        Step 2:
        Solve:
        y = 1  
        x = 1  

        Matrix View:
        We perform row operations:
        - Swap rows
        - Multiply row by scalar
        - Add/subtract rows

        Geometric Intuition:
        You are not changing the solution, just changing how the system is written.

        In ML:
        - Used in solving linear systems
        - Foundation of matrix factorization methods

        Key idea:
        Gaussian elimination simplifies the system without changing its solution.
        """)

        with st.expander("2.1.10 Vector Spaces"):
            st.markdown("""
        A vector space is a set of vectors where you can perform addition and scalar multiplication, and still remain inside the set.

        Formal Definition:
        A set V is a vector space if:
        - x + y ∈ V
        - αx ∈ V

        for all x, y ∈ V and scalar α.

        Examples:
        - ℝ² → all 2D vectors
        - ℝⁿ → all n-dimensional vectors

        Geometric Intuition:
        A vector space is a “space” where vectors live and behave nicely.

        Think of:
        - A plane
        - A 3D space
        - Even higher-dimensional spaces

        In ML:
        Data lives in high-dimensional vector spaces:
        x = [x₁, x₂, ..., xₙ]

        Key idea:
        Vector space = a universe where vectors can be combined freely.
        """)

        with st.expander("2.1.11 Subspaces"):
            st.markdown("""
        A subspace is a smaller vector space inside a larger vector space.

        Definition:
        A subset W ⊆ V is a subspace if:
        - Closed under addition
        - Closed under scalar multiplication

        Examples:
        - A line through the origin in ℝ²
        - A plane through the origin in ℝ³

        Important:
        Subspaces must pass through the origin.

        Why?
        Because 0 must be included (closure property).

        Geometric Intuition:
        A subspace is a “flat surface” inside a higher-dimensional space.

        In ML:
        - Column space
        - Null space
        - Feature spaces

        Key idea:
        Subspace = a valid smaller world inside a bigger vector space.
        """)

        with st.expander("2.1.12 Basis and Dimension"):
            st.markdown("""
        A basis is a set of vectors that can represent every vector in the space.

        Two conditions:
        1. Linearly independent
        2. Span the space

        Example in ℝ²:
        [1,0] and [0,1] form a basis

        Any vector:
        [x, y] = x[1,0] + y[0,1]

        Dimension:
        Number of vectors in the basis.

        ℝ² → dimension = 2  
        ℝ³ → dimension = 3  

        Geometric Intuition:
        Basis = coordinate system of the space

        Different bases → different ways of describing the same space.

        In ML:
        - Feature representation
        - PCA changes basis to better directions

        Key idea:
        Basis tells you how to build the entire space using minimal building blocks.
        """)

        with st.expander("2.1.13 Linear Independence and Dependence"):
            st.markdown("""
        Linear independence tells us whether vectors carry unique information or are redundant.

        Definition:
        Vectors v₁, v₂, ..., vₙ are linearly independent if:
        α₁v₁ + α₂v₂ + ... + αₙvₙ = 0  
        implies  
        α₁ = α₂ = ... = αₙ = 0

        If this is not true → vectors are linearly dependent.

        Intuition:
        - Independent → each vector adds a new direction
        - Dependent → at least one vector can be formed from others

        Example:
        [1,0] and [0,1] → independent  
        [1,2] and [2,4] → dependent (second is 2× first)

        Geometric View:
        - Independent vectors → span new dimensions
        - Dependent vectors → lie on same line/plane

        In ML:
        - Redundant features → dependence
        - Feature selection → remove dependent features

        Key idea:
        Independence = no redundancy.
        """)

        with st.expander("2.1.14 Rank of a Matrix"):
            st.markdown("""
        Rank of a matrix is the number of linearly independent rows or columns.

        Definition:
        rank(A) = number of independent rows = number of independent columns

        Important:
        Row rank = Column rank (always equal)

        Range:
        0 ≤ rank(A) ≤ min(m, n)

        Intuition:
        Rank tells how much “useful information” the matrix contains.

        Example:
        If columns are duplicates → rank decreases.

        Geometric View:
        Rank = dimension of space spanned by columns.

        In ML:
        - Full rank → no redundant features
        - Low rank → redundancy, compressibility
        - Used in PCA, dimensionality reduction

        Key idea:
        Rank = number of independent directions in data.
        """)

        with st.expander("2.1.15 Column Space and Row Space"):
            st.markdown("""
        Column Space:
        All possible linear combinations of columns of A.

        Col(A) = span of columns

        Row Space:
        All possible linear combinations of rows of A.

        Row(A) = span of rows

        Geometric Intuition:
        - Column space → where Ax can go
        - Row space → constraints imposed by A

        Dimension:
        dim(Col(A)) = dim(Row(A)) = rank(A)

        Important:
        Column space lies in ℝᵐ  
        Row space lies in ℝⁿ  

        In ML:
        - Column space → space of predictions
        - Row space → feature interactions

        Key idea:
        Column space = output space of the transformation.
        """)

        with st.expander("2.1.16 Null Space"):
            st.markdown("""
        Null space is the set of all vectors that get mapped to zero.

        Definition:
        Null(A) = {x | Ax = 0}

        Intuition:
        These are “invisible directions” of the transformation.

        Geometric View:
        - If Ax = 0 → vector x collapses to origin
        - Null space shows lost information

        Dimension:
        dim(Null(A)) = n - rank(A)

        This is the Rank-Nullity Theorem.

        In ML:
        - Null space → directions with no effect
        - Important in underdetermined systems

        Example:
        If two columns are identical → their difference lies in null space.

        Key idea:
        Null space = directions that vanish under transformation.
        """)

        with st.expander("2.1.17 Determinant"):
            st.markdown("""
        The determinant is a scalar value that describes how a matrix transforms space.

        For 2×2 matrix:
        A = [[a, b],
            [c, d]]

        det(A) = ad - bc

        Geometric Intuition:
        Determinant = scaling factor of area (or volume in higher dimensions).

        - det > 0 → orientation preserved
        - det < 0 → orientation flipped
        - det = 0 → collapsed (no inverse)

        If det(A) = 0:
        Matrix is singular → loses dimension

        In ML:
        - Used in probability (Gaussian distributions)
        - Indicates invertibility

        Key idea:
        Determinant tells how space is stretched or squashed.
        """)

        with st.expander("2.1.18 Inverse of a Matrix"):
            st.markdown("""
        The inverse of a matrix undoes its transformation.

        Definition:
        A⁻¹ exists if:
        AA⁻¹ = A⁻¹A = I

        Condition:
        det(A) ≠ 0

        Formula (2×2 case):
        A⁻¹ = (1/det(A)) * [[d, -b],
                            [-c, a]]

        Intuition:
        If A transforms space, A⁻¹ brings it back.

        Solving equations:
        Ax = b  
        x = A⁻¹b

        Geometric View:
        Inverse reverses scaling, rotation, etc.

        In ML:
        - Used in closed-form solutions (e.g., linear regression)
        - Often avoided in practice (numerical instability)

        Key idea:
        Inverse = undoing a transformation.
        """)

        with st.expander("2.1.19 Eigenvalues"):
            st.markdown("""
        Eigenvalues tell us how much a transformation stretches or compresses along special directions.

        Definition:
        For a matrix A, a scalar λ is an eigenvalue if:
        Ax = λx

        This means:
        Applying A to vector x only scales it, not change its direction.

        How to find:
        det(A - λI) = 0

        Solve this equation → eigenvalues.

        Intuition:
        Most vectors change direction when transformed.
        But some special directions only get stretched or shrunk.

        Those scaling factors = eigenvalues.

        Geometric View:
        - λ > 1 → stretching
        - 0 < λ < 1 → shrinking
        - λ = 0 → collapse to zero
        - λ < 0 → flip direction

        In ML:
        Eigenvalues tell importance of directions:
        - Large λ → important direction
        - Small λ → less important

        Key idea:
        Eigenvalues measure “how strong” a transformation is along special directions.
        """)

        with st.expander("2.1.20 Eigenvectors"):
            st.markdown("""
        Eigenvectors are the special directions that do not change direction under transformation.

        Definition:
        Ax = λx

        Here:
        x → eigenvector  
        λ → eigenvalue  

        Intuition:
        Most vectors rotate when transformed.
        Eigenvectors only scale, they don’t rotate.

        Geometric View:
        Imagine stretching a rubber sheet:
        Some directions stretch without turning — those are eigenvectors.

        Example:
        If A scales x-axis and y-axis differently:
        - x-axis → eigenvector
        - y-axis → eigenvector

        In ML:
        Eigenvectors represent meaningful directions in data:
        - PCA finds top eigenvectors
        - These capture maximum variance

        Key idea:
        Eigenvectors = directions that remain stable under transformation.
        """)

        with st.expander("2.1.21 Diagonalization"):
            st.markdown("""
        Diagonalization simplifies a matrix into its most basic form.

        Definition:
        A = PDP⁻¹

        Where:
        P → matrix of eigenvectors  
        D → diagonal matrix of eigenvalues  

        Meaning:
        We convert A into a form where it only scales axes.

        Intuition:
        Instead of working in a complicated coordinate system,
        we switch to a new basis where everything becomes simple scaling.

        Geometric View:
        - Original space → messy transformation
        - Eigenbasis → pure stretching along axes

        Why useful:
        P⁻¹ → change of basis  
        D → simple scaling  
        P → change back

        In ML:
        - PCA uses this idea
        - Simplifies computations
        - Helps understand structure of data

        Key idea:
        Diagonalization = expressing transformation in its simplest coordinate system.
        """)

        with st.expander("2.1.22 Singular Value Decomposition (SVD)"):
            st.markdown("""
        SVD is the most powerful matrix decomposition.

        Definition:
        A = UΣVᵀ

        Where:
        U → orthogonal matrix (left singular vectors)  
        Σ → diagonal matrix (singular values)  
        V → orthogonal matrix (right singular vectors)  

        Intuition:
        Any matrix transformation can be broken into 3 steps:
        1. Rotate (Vᵀ)
        2. Stretch (Σ)
        3. Rotate again (U)

        Geometric View:
        SVD decomposes transformation into:
        - rotation
        - scaling
        - rotation

        Important:
        Works for ANY matrix (even non-square).

        In ML:
        - PCA (via SVD)
        - Dimensionality reduction
        - Recommendation systems
        - Image compression

        Key idea:
        SVD = universal way to understand any matrix transformation.
        """)

        with st.expander("2.1.23 Orthogonality"):
            st.markdown("""
        Orthogonality means vectors are perpendicular.

        Definition:
        x · y = 0

        Intuition:
        Two vectors are orthogonal if they share no information.

        Geometric View:
        90° angle between vectors.

        Why important:
        Orthogonal vectors are independent and do not interfere.

        Orthogonal Matrix:
        QᵀQ = I

        Meaning:
        - Columns are orthogonal
        - Length preserved

        In ML:
        - PCA produces orthogonal components
        - Reduces redundancy
        - Improves numerical stability

        Key idea:
        Orthogonality = complete independence between directions.
        """)

        with st.expander("2.1.24 Projection"):
            st.markdown("""
        Projection is the process of mapping a vector onto another vector or subspace.

        Projection of x onto w:
        proj_w(x) = (x · w / w · w) w

        If w is unit vector:
        proj_w(x) = (x · w) w

        Intuition:
        Projection finds the “shadow” of a vector along a direction.

        Geometric View:
        Drop a perpendicular from x onto w.

        Why important:
        Projection extracts component of x in direction of w.

        In ML:
        - Linear regression → projection onto column space
        - PCA → projection onto principal components

        Key idea:
        Projection = extracting useful information along a direction.
        """)
with st.expander("2.2 Probability Theory"):

    with st.expander("2.2.1 Basic Terminology"):

        with st.expander("Experiment"):
            st.markdown("""
    An experiment is any process or action that produces an outcome, where the result is uncertain beforehand.

    Examples:
    - Tossing a coin
    - Rolling a dice
    - Predicting if an email is spam

    Key idea:
    An experiment defines the setting where randomness exists.

    Intuition:
    Think of an experiment as “asking a question whose answer is not known yet.”
    """)

        with st.expander("Sample Space"):
            st.markdown("""
    The sample space (Ω) is the set of all possible outcomes of an experiment.

    Examples:
    - Coin toss → Ω = {Heads, Tails}
    - Dice roll → Ω = {1,2,3,4,5,6}

    Properties:
    - Must include all possible outcomes
    - Outcomes are mutually exclusive

    Intuition:
    Sample space is the “universe” of all possibilities.

    Everything that can happen is inside Ω.
    """)

        with st.expander("Event"):
            st.markdown("""
    An event is a subset of the sample space.

    Examples:
    - Getting Heads → {Heads}
    - Getting an even number → {2,4,6}

    Types:
    - Simple event → single outcome
    - Compound event → multiple outcomes

    Operations:
    - Union (A ∪ B): A or B happens
    - Intersection (A ∩ B): both A and B happen
    - Complement (Aᶜ): A does not happen

    Intuition:
    Events are the specific outcomes we care about within the larger universe.
    """)

        with st.expander("Probability"):
            st.markdown("""
    Probability measures how likely an event is to occur.

    Definition:
    P(A) = number between 0 and 1

    - P(A) = 0 → impossible
    - P(A) = 1 → certain

    For equally likely outcomes:
    P(A) = (number of favorable outcomes) / (total outcomes)

    Example:
    P(even number on dice) = 3/6 = 1/2

    Intuition:
    Probability quantifies uncertainty.

    It answers:
    “How confident are we that this event will occur?”
    """)

        with st.expander("Axioms of Probability"):
            st.markdown("""
    Probability is built on three fundamental rules (Kolmogorov axioms):

    1. Non-negativity:
    P(A) ≥ 0

    2. Normalization:
    P(Ω) = 1

    3. Additivity:
    If A and B are disjoint:
    P(A ∪ B) = P(A) + P(B)

    Derived rule:
    P(Aᶜ) = 1 - P(A)

    General formula:
    P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

    Intuition:
    These axioms ensure probability behaves logically and consistently.

    They are the “laws” governing uncertainty.
    """)


    with st.expander("2.2.2 Types of Probability"):

        with st.expander("Classical Probability"):
            st.markdown("""
    Classical probability assumes all outcomes are equally likely.

    Formula:
    P(A) = (favorable outcomes) / (total outcomes)

    Example:
    Probability of getting a 3 on a dice:
    P(3) = 1/6

    When to use:
    - Games of chance
    - Symmetric situations

    Limitation:
    Does not work when outcomes are not equally likely.

    Intuition:
    Fair world → all outcomes treated equally.
    """)

        with st.expander("Frequentist Probability"):
            st.markdown("""
    Frequentist probability defines probability as long-run frequency.

    Formula:
    P(A) = (number of times A occurs) / (total trials)

    As trials → ∞, this stabilizes.

    Example:
    If it rains 300 out of 1000 days:
    P(rain) = 0.3

    Key idea:
    Probability is not a belief—it is an observed frequency.

    In ML:
    - Used in maximum likelihood estimation (MLE)
    - Data-driven approach

    Intuition:
    “What fraction of the time does this event happen?”
    """)

        with st.expander("Bayesian Probability"):
            st.markdown("""
    Bayesian probability treats probability as a degree of belief.

    Key Idea:
    We update our belief as we get new data.

    Bayes Theorem:
    P(A|B) = (P(B|A) * P(A)) / P(B)

    Where:
    P(A) → prior belief  
    P(B|A) → likelihood  
    P(A|B) → updated belief (posterior)

    Example:
    Medical test:
    - Prior → probability of disease
    - Likelihood → test accuracy
    - Posterior → probability after seeing result

    In ML:
    - Bayesian models
    - Uncertainty estimation

    Intuition:
    Start with a belief → update it with evidence.

    Key difference:
    Frequentist → based on data frequency  
    Bayesian → based on belief + evidence
    """)

    with st.expander("2.2.3 Conditional Probability"):

        with st.expander("Definition"):
            st.markdown("""
    Conditional probability answers:

    "What is the probability of A, given that B has already happened?"

    This fundamentally changes the space we are working in.

    Instead of considering all possible outcomes (Ω),
    we restrict ourselves ONLY to outcomes where B is true.

    So:
    Original space → Ω  
    New space → B  

    We now measure how much of B is occupied by A.

    This is why conditional probability is not just a formula—it is a change of perspective.
    """)

        with st.expander("Formula"):
            st.markdown("""
    P(A | B) = P(A ∩ B) / P(B)

    Derivation (very important):

    We restrict to region B.
    Inside B, the portion that also satisfies A is A ∩ B.

    So:
    Probability = (portion of B that is also A) / (total B)

    Example:
    Deck of 52 cards

    Let:
    A = card is King → P(A) = 4/52  
    B = card is Heart → P(B) = 13/52  

    A ∩ B = King of Hearts → 1/52  

    So:
    P(A | B) = (1/52) / (13/52) = 1/13  

    Interpretation:
    If you already know it's a Heart, probability of King becomes 1/13.

    Key transformation:
    Global probability → Local probability inside B.
    """)

        with st.expander("Intuition"):
            st.markdown("""
    The most important idea:

    Conditioning = shrinking the world.

    Imagine 100 people:
    - 40 are students (B)
    - 20 like coding (A)
    - 15 are both (A ∩ B)

    Without conditioning:
    P(A) = 20/100 = 0.2

    With conditioning:
    We ONLY look at students (40 people)

    Out of them, 15 like coding:
    P(A | B) = 15/40 = 0.375

    So probability increased because we changed the reference group.

    Key insight:
    Probabilities change because the denominator changes.

    This idea is used everywhere in ML:
    - filtering data
    - computing likelihoods
    - updating beliefs
    """)


    with st.expander("2.2.4 Independence"):

        with st.expander("Definition"):
            st.markdown("""
    Two events are independent if knowing one does not change the probability of the other.

    Formally:
    P(A | B) = P(A)

    Using conditional probability formula:
    P(A ∩ B) = P(A)P(B)

    This is the most important identity for independence.

    Interpretation:
    Information about B gives ZERO information about A.
    """)

        with st.expander("Independent Events"):
            st.markdown("""
    Independent events behave like completely separate systems.

    Example:
    Two coin tosses

    Let:
    A = first toss is Heads  
    B = second toss is Heads  

    P(A) = 1/2  
    P(B) = 1/2  

    Joint:
    P(A ∩ B) = 1/4 = (1/2)*(1/2)

    Why?
    Because outcome of first toss does not influence second.

    Geometric intuition:
    The probability of overlap = product of probabilities.

    In ML:
    Naive Bayes assumes features are conditionally independent:
    P(x₁, x₂, ..., xₙ | y) = Π P(xᵢ | y)

    Key idea:
    Independence simplifies joint probability into multiplication.
    """)

        with st.expander("Dependent Events"):
            st.markdown("""
    Events are dependent if one changes the probability of the other.

    Formally:
    P(A | B) ≠ P(A)

    Example:
    Drawing cards WITHOUT replacement

    Let:
    A = first card is Ace  
    B = second card is Ace  

    P(A) = 4/52  

    After drawing one Ace:
    Remaining Aces = 3  
    Remaining cards = 51  

    So:
    P(B | A) = 3/51 ≠ 4/52

    Thus dependent.

    General formula:
    P(A ∩ B) = P(A | B) * P(B)

    Key insight:
    Dependence means information flows between events.

    In ML:
    Most real-world features are dependent.
    Ignoring this (like in Naive Bayes) is a simplification.
    """)


    with st.expander("2.2.5 Bayes Theorem"):

        with st.expander("Formula"):
            st.markdown("""
    Bayes Theorem:

    P(A | B) = (P(B | A) * P(A)) / P(B)

    Derivation (important):

    From conditional probability:
    P(A | B) = P(A ∩ B) / P(B)  
    P(B | A) = P(A ∩ B) / P(A)

    So:
    P(A ∩ B) = P(B | A) * P(A)

    Substitute:
    P(A | B) = (P(B | A) * P(A)) / P(B)

    This is just algebra, but the interpretation is powerful.

    Extended form (multiple hypotheses):
    P(Aᵢ | B) = (P(B | Aᵢ)P(Aᵢ)) / Σ P(B | Aⱼ)P(Aⱼ)
    """)

        with st.expander("Prior, Likelihood, Posterior"):
            st.markdown("""
    Break Bayes into parts:

    1. Prior → P(A)
    Initial belief before seeing data

    2. Likelihood → P(B | A)
    How probable the evidence is if A is true

    3. Posterior → P(A | B)
    Updated belief after seeing evidence

    4. Evidence → P(B)
    Normalization (ensures probabilities sum to 1)

    Pipeline:
    Prior → incorporate data → Posterior

    Concrete Example:

    Disease test:

    P(Disease) = 0.01 (rare)  
    P(Positive | Disease) = 0.99  
    P(Positive | No Disease) = 0.05  

    We want:
    P(Disease | Positive)

    Compute:
    P(Positive) =
    0.99 * 0.01 + 0.05 * 0.99  
    = 0.0099 + 0.0495 = 0.0594  

    Now:
    P(Disease | Positive) =
    (0.99 * 0.01) / 0.0594 ≈ 0.166

    Even with a positive test,
    probability is only ~16.6%

    Why?
    Because prior was very small.

    This is extremely important intuition.
    """)

        with st.expander("Intuition"):
            st.markdown("""
    Bayes theorem reverses conditional probability.

    We often know:
    P(B | A) → how data behaves given a cause

    But we want:
    P(A | B) → probability of cause given data

    Bayes allows this reversal.

    Core insight:
    Posterior ∝ Likelihood × Prior

    Meaning:
    New belief = old belief × evidence strength

    Key intuition:

    - Strong prior → hard to change belief
    - Strong likelihood → strong evidence
    - Weak evidence → small update

    In ML:
    - Classification (Naive Bayes)
    - Bayesian inference
    - Updating models with new data

    Final takeaway:
    Learning = updating beliefs mathematically.
    """)
    with st.expander("2.2.6 Random Variables"):

        with st.expander("Definition"):
            st.markdown("""
    A random variable is a function that maps outcomes of a random experiment to real numbers.

    Formally:
    X : Ω → ℝ

    Meaning:
    Instead of working with raw outcomes (like "Heads", "Tail", "Red card"),
    we assign numbers to them so we can do mathematics.

    Example:
    Coin toss:
    Ω = {H, T}

    Define:
    X(H) = 1  
    X(T) = 0  

    Now instead of outcomes, we work with numbers.

    Key idea:
    Random variable = numerical representation of randomness

    Why important?
    Because ML models work with numbers, not abstract outcomes.
    """)

        with st.expander("Discrete Random Variables"):
            st.markdown("""
    A discrete random variable takes a finite or countable number of values.

    Examples:
    - Number of heads in 3 coin tosses → {0,1,2,3}
    - Number of customers arriving → {0,1,2,...}

    Key property:
    Values are countable

    We describe it using a PMF (Probability Mass Function)

    Example:
    X = number of heads in 2 tosses

    Values:
    0, 1, 2

    Probabilities:
    P(X=0) = 1/4  
    P(X=1) = 1/2  
    P(X=2) = 1/4  

    Key idea:
    Probability is assigned directly to each value.
    """)

        with st.expander("Continuous Random Variables"):
            st.markdown("""
    A continuous random variable takes infinitely many values in an interval.

    Examples:
    - Height
    - Weight
    - Time
    - Temperature

    Key property:
    Uncountably infinite values

    Important:
    P(X = exact value) = 0

    Instead, we work with intervals:
    P(a ≤ X ≤ b)

    We describe it using a PDF (Probability Density Function)

    Example:
    Height of people

    We cannot say:
    P(height = 170 cm)

    We say:
    P(165 ≤ height ≤ 175)

    Key idea:
    Probability is spread continuously, not at points.
    """)


    with st.expander("2.2.7 Probability Distributions"):

        with st.expander("PMF (Probability Mass Function)"):
            st.markdown("""
    Used for discrete random variables.

    Definition:
    PMF gives probability of each exact value.

    P(X = x)

    Properties:
    1. P(X = x) ≥ 0  
    2. Σ P(X = x) = 1  

    Example:
    Dice roll:

    P(X=1) = 1/6  
    P(X=2) = 1/6  
    ...  

    Interpretation:
    Each value has a specific probability mass.

    Key idea:
    Probability is concentrated at points.
    """)

        with st.expander("PDF (Probability Density Function)"):
            st.markdown("""
    Used for continuous random variables.

    Definition:
    PDF describes density of probability, not direct probability.

    f(x)

    Important:
    P(X = x) = 0

    Probability over interval:
    P(a ≤ X ≤ b) = ∫[a to b] f(x) dx

    Properties:
    1. f(x) ≥ 0  
    2. ∫ f(x) dx = 1  

    Example:
    Normal distribution (Gaussian)

    Key idea:
    PDF tells how dense probability is around a point,
    not the probability of that exact point.
    """)

        with st.expander("CDF (Cumulative Distribution Function)"):
            st.markdown("""
    CDF gives cumulative probability up to a value.

    Definition:
    F(x) = P(X ≤ x)

    For discrete:
    F(x) = Σ P(X ≤ x)

    For continuous:
    F(x) = ∫[-∞ to x] f(t) dt

    Properties:
    1. Monotonically increasing  
    2. Range: 0 to 1  

    Interpretation:
    CDF tells "how much probability has accumulated up to x"

    Key idea:
    CDF = accumulated probability curve.
    """)


    with st.expander("2.2.8 Expectation and Variance"):

        with st.expander("Expected Value"):
            st.markdown("""
    Expected value is the average or mean value of a random variable.

    It represents the "center of mass" of the distribution.

    Discrete:
    E[X] = Σ x P(X = x)

    Continuous:
    E[X] = ∫ x f(x) dx

    Example:
    Dice roll:

    E[X] = (1+2+3+4+5+6)/6 = 3.5

    Important:
    Expected value does not have to be a possible outcome.

    Interpretation:
    If you repeat experiment many times, average → E[X]

    In ML:
    - Loss functions are expectations
    - Models try to minimize expected error

    Key idea:
    Expectation = long-run average.
    """)

        with st.expander("Variance"):
            st.markdown("""
    Variance measures how spread out values are from the mean.

    Definition:
    Var(X) = E[(X - μ)²]

    Where:
    μ = E[X]

    Expanded form:
    Var(X) = E[X²] - (E[X])²

    Interpretation:
    - Small variance → values close to mean
    - Large variance → values widely spread

    Example:
    Two datasets:
    [4,5,6] vs [1,5,9]

    Same mean, different variance.

    Key idea:
    Variance = measure of uncertainty/spread.
    """)

        with st.expander("Standard Deviation"):
            st.markdown("""
    Standard deviation is the square root of variance.

    σ = √Var(X)

    Why needed?
    Variance is in squared units (hard to interpret),
    so we take square root to bring it back to original units.

    Example:
    If variance = 9,
    standard deviation = 3

    Interpretation:
    Average distance from the mean.

    In ML:
    - Used in normalization
    - Important in Gaussian distributions
    - Controls spread of data

    Key idea:
    Standard deviation = interpretable measure of spread.
    """)

    with st.expander("2.2.9 Common Distributions"):

        with st.expander("Bernoulli Distribution"):
            st.markdown("""
    This is the simplest distribution — a single binary outcome.

    Used when there are only TWO possible outcomes:
    Success (1) or Failure (0)

    Example:
    - Coin toss
    - Click / No Click
    - Spam / Not Spam

    Parameter:
    p = P(X = 1)

    PMF:
    P(X = x) = p^x * (1 - p)^(1 - x), where x ∈ {0,1}

    Mean:
    E[X] = p

    Variance:
    Var(X) = p(1 - p)

    Intuition:
    This models a single yes/no experiment.

    In ML:
    - Logistic regression outputs Bernoulli probability
    - Binary classification is Bernoulli modeling
    """)

        with st.expander("Binomial Distribution"):
            st.markdown("""
    Extension of Bernoulli to multiple independent trials.

    Question:
    "How many successes in n trials?"

    Example:
    - Number of heads in 10 tosses
    - Number of correct predictions

    Parameters:
    n = number of trials  
    p = probability of success

    PMF:
    P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)

    Mean:
    E[X] = np

    Variance:
    Var(X) = np(1 - p)

    Intuition:
    You repeat Bernoulli experiment n times and count successes.

    In ML:
    - Modeling counts
    - Used in likelihood functions
    """)


        with st.expander("Gaussian (Normal) Distribution"):
            st.markdown("""
    Most important distribution in ML.

    Shape:
    Bell curve (symmetric)

    Parameters:
    μ = mean (center)  
    σ² = variance (spread)

    PDF:
    f(x) = (1 / √(2πσ²)) * exp(-(x - μ)² / (2σ²))

    Properties:
    - Symmetric around mean
    - Mean = Median = Mode
    - Controlled by μ and σ

    68-95-99 rule:
    - 68% within 1σ
    - 95% within 2σ
    - 99% within 3σ

    Intuition:
    Many natural processes cluster around a mean with small deviations.

    Why everywhere?
    Central Limit Theorem:
    Sum of many random variables → Gaussian

    In ML:
    - Assumption in many models
    - Errors often assumed Gaussian
    - Used in linear regression
    """)


        with st.expander("Uniform Distribution"):
            st.markdown("""
    All values are equally likely.

    Discrete example:
    Dice → each value has probability 1/6

    Continuous example:
    X ~ Uniform(a, b)

    PDF:
    f(x) = 1 / (b - a), for a ≤ x ≤ b

    Mean:
    E[X] = (a + b) / 2

    Variance:
    Var(X) = (b - a)² / 12

    Intuition:
    No preference — completely flat probability.

    In ML:
    - Used for random initialization
    - Baseline assumption when no prior knowledge exists
    """)


    with st.expander("2.2.10 Joint and Marginal Probability"):

        with st.expander("Joint Distribution"):
            st.markdown("""
    Joint probability describes probability of multiple variables together.

    P(X, Y)

    Example:
    P(Weather = Rain, Traffic = Heavy)

    Discrete:
    P(X = x, Y = y)

    Continuous:
    f(x, y)

    Key idea:
    Captures relationship between variables.

    If independent:
    P(X, Y) = P(X)P(Y)

    If not:
    They influence each other.

    In ML:
    Joint distributions define full probabilistic models.
    """)

        with st.expander("Marginal Distribution"):
            st.markdown("""
    Marginal probability is obtained by summing or integrating out other variables.

    From joint:
    P(X) = Σ P(X, Y)   (discrete)
    P(X) = ∫ f(X, Y) dY   (continuous)

    Example:
    You know joint distribution of (Weather, Traffic),
    but want only Weather.

    So you "remove" Traffic.

    Intuition:
    Marginalization = ignoring other variables.

    Key idea:
    From joint → reduce to one variable.
    """)

        with st.expander("Conditional Distribution"):
            st.markdown("""
    Conditional distribution describes probability of one variable given another.

    P(X | Y)

    Formula:
    P(X | Y) = P(X, Y) / P(Y)

    Interpretation:
    Restrict joint distribution to Y.

    In ML:
    Most models compute:
    P(output | input)

    Example:
    P(Spam | Email features)

    Key idea:
    Conditional = focused view of joint distribution.
    """)


    with st.expander("2.2.11 Law of Total Probability"):

        with st.expander("Formula"):
            st.markdown("""
    If A₁, A₂, ..., Aₙ are mutually exclusive and exhaustive:

    P(B) = Σ P(B | Aᵢ) P(Aᵢ)

    Meaning:
    Break probability into cases.

    Example:
    P(Positive Test) =
    P(Positive | Disease)P(Disease)
    + P(Positive | No Disease)P(No Disease)
    """)

        with st.expander("Intuition"):
            st.markdown("""
    This is "divide and conquer" for probability.

    Instead of computing P(B) directly,
    we break it into simpler cases.

    Steps:
    1. Split world into cases (A₁, A₂, ...)
    2. Compute probability in each case
    3. Add them

    Geometric view:
    Partition the space → sum contributions.

    In ML:
    Used in:
    - Bayesian inference
    - Hidden variable models

    Key idea:
    Total probability = weighted sum over cases.
    """)


    with st.expander("2.2.12 Information Theory Basics"):

        with st.expander("Entropy"):
            st.markdown("""
    Entropy measures uncertainty in a random variable.

    Formula:
    H(X) = - Σ P(x) log P(x)

    Interpretation:
    - High entropy → high uncertainty
    - Low entropy → predictable

    Examples:
    Fair coin:
    H = 1 (maximum uncertainty)

    Biased coin:
    Lower entropy

    Extreme:
    If P=1 → H=0 (no uncertainty)

    In ML:
    - Used in decision trees (information gain)
    - Measures randomness in data

    Key idea:
    Entropy = amount of surprise.
    """)

        with st.expander("Cross Entropy"):
            st.markdown("""
    Measures how well one probability distribution approximates another.

    Formula:
    H(P, Q) = - Σ P(x) log Q(x)

    Where:
    P = true distribution  
    Q = predicted distribution  

    Interpretation:
    Penalty for predicting Q when true is P.

    In ML:
    This is the MOST important loss function.

    Example:
    Classification loss = Cross Entropy

    Key idea:
    Lower cross entropy = better predictions.
    """)

        with st.expander("KL Divergence"):
            st.markdown("""
    Measures difference between two distributions.

    Formula:
    KL(P || Q) = Σ P(x) log (P(x)/Q(x))

    Relation:
    KL = Cross Entropy - Entropy

    Properties:
    - KL ≥ 0
    - KL = 0 only if P = Q

    Interpretation:
    “How much extra information is needed if we use Q instead of P?”

    Important:
    KL is NOT symmetric.

    In ML:
    - Used in VAEs
    - Distribution matching
    - Regularization

    Key idea:
    KL divergence = distance between distributions.
    """)

        st.markdown("""
    Final Insight:

    Entropy → uncertainty  
    Cross Entropy → prediction error  
    KL Divergence → distribution difference  

    This trio forms the foundation of modern ML loss functions.
    """)
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