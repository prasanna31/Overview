import streamlit as st

st.set_page_config(layout="wide")

st.title("Linear Algebra — Intuition for Machine Learning")

st.markdown("""
Linear algebra is the mathematics of **vectors and transformations**.

Almost every algorithm in machine learning can be written in the form:

Ax = b

Where

A → matrix (model / transformation)  
x → vector (data point)  
b → output vector  

Understanding linear algebra means understanding **how vectors behave and how matrices transform space**.
""")

# ------------------------------------------------
# VECTOR GEOMETRY
# ------------------------------------------------

st.header("Vector Geometry")

st.subheader("Vectors")

st.markdown("""
A **vector** is an ordered list of numbers representing magnitude and direction.

Example

v = (3,2)

Geometrically this is an arrow from the origin to the point (3,2).

Vectors represent

• directions  
• points in space  
• data samples  

In machine learning a data point like

[height, weight, age]

is a vector in 3-dimensional space.
""")

st.subheader("Dot Product")

st.markdown("""
The **dot product** measures similarity between two vectors.

Formula

u · v = Σ(uᵢ vᵢ)

Example

u = (1,2)  
v = (3,4)

dot product = 1×3 + 2×4 = 11

Geometric meaning

u · v = ||u|| ||v|| cos(θ)

If vectors point in the same direction → dot product large  
If perpendicular → dot product zero  

This idea becomes **cosine similarity** used in recommendation systems and NLP.
""")

st.subheader("Projection")

st.markdown("""
Projection means **dropping a vector onto another vector**.

Formula

proj_v(u) = (u·v / v·v) v

Geometrically it is the **shadow of vector u onto vector v**.

Projection is the key idea behind

• linear regression  
• least squares  
• PCA  
• signal decomposition
""")

st.subheader("Angles")

st.markdown("""
The angle between vectors measures **direction similarity**.

Formula

cos(θ) = (u·v)/(||u|| ||v||)

Important cases

θ = 0° → vectors point in same direction  
θ = 90° → vectors are independent  
θ = 180° → vectors opposite  

Many ML similarity measures are based on vector angles.
""")

st.subheader("Orthogonality")

st.markdown("""
Vectors are **orthogonal** if they are perpendicular.

Condition

u · v = 0

Orthogonal vectors represent **independent directions**.

This concept appears in

• orthogonal basis  
• Fourier transforms  
• PCA  
• QR decomposition
""")

# ------------------------------------------------
# MATRICES
# ------------------------------------------------

st.header("Matrices")

st.subheader("Matrix")

st.markdown("""
A **matrix** is a rectangular array of numbers.

Example

A =
[1 2  
 3 4]

Matrices represent **linear transformations**.

When a matrix multiplies a vector it **transforms the vector's position in space**.
""")

st.subheader("Matrix Multiplication")

st.markdown("""
Matrix multiplication composes transformations.

If

y = Ax  
z = By

Then

z = BAx

Meaning transformation B is applied after A.

In neural networks each layer is essentially **matrix multiplication**.
""")

st.subheader("Transpose")

st.markdown("""
The **transpose** flips rows and columns.

Aᵀ

Example

[1 2 3]ᵀ becomes

[1  
 2  
 3]

Transpose is used in

• covariance matrices  
• projections  
• least squares
""")

st.subheader("Determinant")

st.markdown("""
The **determinant** measures how much a matrix scales space.

det(A)

Interpretation

det(A) = 0 → transformation collapses space  
det(A) > 1 → space expands  
det(A) < 1 → space shrinks  

Geometrically determinant measures **area or volume scaling**.
""")

st.subheader("Inverse")

st.markdown("""
The **inverse matrix** reverses a transformation.

A⁻¹A = I

Meaning

Apply A then A⁻¹ → return to original vector.

Inverse is used to solve systems

Ax = b  
x = A⁻¹b
""")

# ------------------------------------------------
# LINEAR SYSTEMS
# ------------------------------------------------

st.header("Linear Systems")

st.subheader("Linear System")

st.markdown("""
A linear system is a collection of linear equations.

Example

2x + y = 5  
x − y = 1

In matrix form

Ax = b

Geometrically each equation represents a **plane or line**.

Solutions occur at **intersections of these planes**.
""")

st.subheader("Gaussian Elimination")

st.markdown("""
Gaussian elimination solves linear systems using **row operations**.

Steps

1 eliminate lower entries  
2 create triangular matrix  
3 solve using back substitution

This converts matrix into **row echelon form**.

Complexity roughly O(n³).
""")

st.subheader("Rank")

st.markdown("""
The **rank** of a matrix is the number of independent rows or columns.

rank(A)

Interpretation

rank = dimension of space spanned by columns.

Rank determines

• number of independent equations  
• existence of solutions  
• data dimensionality
""")

st.subheader("Null Space")

st.markdown("""
The **null space** contains vectors mapped to zero.

Ax = 0

Geometrically these are directions that the transformation **collapses to the origin**.

Dimension of null space = **nullity**.
""")

st.subheader("Column Space")

st.markdown("""
Column space is the set of all outputs Ax.

Col(A)

Geometrically this is the **space spanned by the columns of A**.

A system Ax=b has a solution **only if b lies in the column space**.
""")

# ------------------------------------------------
# EIGEN CONCEPTS
# ------------------------------------------------

st.header("Eigen Concepts")

st.subheader("Eigenvalues")

st.markdown("""
Eigenvalues describe how much a matrix stretches space.

Equation

Av = λv

λ is the scaling factor.

Large eigenvalues correspond to **directions of large transformation**.
""")

st.subheader("Eigenvectors")

st.markdown("""
Eigenvectors are directions that **do not rotate during transformation**.

Only their length changes.

Av = λv

These directions reveal the **intrinsic structure of the matrix**.
""")

st.subheader("Diagonalization")

st.markdown("""
If a matrix has enough eigenvectors it can be written as

A = P D P⁻¹

Where

D → diagonal matrix of eigenvalues

Diagonalization simplifies

• matrix powers  
• differential equations  
• many algorithms
""")

st.subheader("Spectral Decomposition")

st.markdown("""
For symmetric matrices

A = Q Λ Qᵀ

Where

Q → orthogonal eigenvectors  
Λ → eigenvalues

This decomposition is fundamental for

• PCA  
• spectral clustering  
• graph analysis
""")

# ------------------------------------------------
# MACHINE LEARNING CONNECTIONS
# ------------------------------------------------

st.header("Machine Learning Connections")

st.subheader("PCA")

st.markdown("""
Principal Component Analysis finds directions of **maximum variance**.

Steps

1 compute covariance matrix  
2 compute eigenvectors  
3 project data onto top eigenvectors

Result

High dimensional data becomes **lower dimensional while preserving information**.
""")

st.subheader("Covariance Matrix")

st.markdown("""
Covariance measures how variables change together.

Σ = E[(x − μ)(x − μ)ᵀ]

Diagonal values → variances  
Off-diagonal → correlations

Eigenvectors of covariance define **principal directions of data**.
""")

st.subheader("SVD")

st.markdown("""
Singular Value Decomposition factorizes any matrix as

A = U Σ Vᵀ

Interpretation

V rotates input space  
Σ scales axes  
U rotates output space

SVD is used for

• PCA  
• recommendation systems  
• image compression
""")

st.subheader("Embeddings")

st.markdown("""
Embeddings map objects to vectors in a latent space.

Examples

• word embeddings  
• graph embeddings  
• user-item embeddings

Similar objects appear **close together in vector space**.

Similarity is often measured using

cosine similarity or Euclidean distance.
""")

st.success("You now understand the core ideas of linear algebra used in machine learning.")