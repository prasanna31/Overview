import streamlit as st

st.title("Data Structures and Algorithms Patterns Guide")

st.markdown("""
<style>
.stApp {
    background-color: #D8E4C5;
}
</style>
""", unsafe_allow_html=True)

import streamlit as st

st.markdown("""
<style>

/* Style for all subheaders */
h3 {
    background-color: #111111;
    padding: 12px 16px;
    border-left: 6px solid #00FFD1;
    border-radius: 8px;
    color: white;
}

/* Optional spacing improvement */
h3 {
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)
# ARRAYS
st.header("Arrays")

st.subheader("Introduction")
st.markdown("""
Arrays store elements in **contiguous memory locations** and allow **constant time random access** using indices.
They are one of the most fundamental data structures and are widely used in problems involving
searching, sorting, and numerical computations.
""")

st.subheader("Array Patterns")
st.markdown("""
1. Two Pointer Pattern  
2. Sliding Window Pattern  
3. Prefix Sum Pattern  
4. Difference Array Pattern  
5. Kadane’s Algorithm Pattern  
6. Cyclic Sort Pattern  
7. Partition Pattern  
8. Dutch National Flag Pattern  
9. Binary Search Pattern  
10. Rotated Array Search Pattern  
11. Subarray Sum Pattern  
12. Product Except Self Pattern  
13. Merge Sorted Arrays Pattern  
14. Frequency Counting Pattern  
15. Greedy Rearrangement Pattern  
16. Matrix Traversal Pattern  
17. Spiral Traversal Pattern  
18. Diagonal Traversal Pattern  
19. Range Query Pattern  
20. Array Simulation Pattern
""")


# STRINGS
st.header("Strings")

st.subheader("Introduction")
st.markdown("""
Strings represent sequences of characters and are used to model textual data.
Efficient string algorithms are important for **search engines, compilers, bioinformatics, and NLP systems**.
""")

st.subheader("String Patterns")
st.markdown("""
1. Two Pointer String Pattern  
2. Sliding Window String Pattern  
3. Frequency Counter Pattern  
4. Anagram Detection Pattern  
5. Palindrome Check Pattern  
6. Expand Around Center Pattern  
7. String Hashing Pattern  
8. Rabin Karp Pattern  
9. KMP Pattern  
10. Z Algorithm Pattern  
11. Longest Substring Pattern  
12. Subsequence Matching Pattern  
13. Pattern Matching Pattern  
14. Trie Based String Search Pattern  
15. Suffix Structure Pattern  
16. Compression Pattern  
17. Encoding Decoding Pattern  
18. Edit Distance Pattern  
19. Lexicographic Ordering Pattern  
20. String Greedy Construction Pattern
""")


# LINKED LIST
st.header("Linked Lists")

st.subheader("Introduction")
st.markdown("""
Linked lists store elements as nodes connected using pointers.
Unlike arrays, they allow **efficient insertion and deletion without shifting elements**.
""")

st.subheader("Linked Lists Patterns")
st.markdown("""
1. Fast Slow Pointer Pattern  
2. Reverse Linked List Pattern  
3. Reverse Sublist Pattern  
4. Merge Two Lists Pattern  
5. Detect Cycle Pattern  
6. Find Cycle Start Pattern  
7. Middle Node Pattern  
8. Remove Nth Node Pattern  
9. Partition List Pattern  
10. Rotate List Pattern  
11. Intersection Detection Pattern  
12. Add Numbers Pattern  
13. Clone Random Pointer Pattern  
14. Flatten Linked List Pattern  
15. Reorder List Pattern  
16. Pairwise Swap Pattern  
17. Split List Pattern  
18. Merge K Lists Pattern  
19. Two Pointer Distance Pattern  
20. Dummy Node Pattern
""")


# STACK
st.header("Stack")

st.subheader("Introduction")
st.markdown("""
A stack follows the **Last In First Out (LIFO)** principle.
Stacks are heavily used in **expression evaluation, recursion, parsing, and undo systems**.
""")

st.subheader("Stack Patterns")
st.markdown("""
1. Monotonic Stack Pattern  
2. Next Greater Element Pattern  
3. Previous Smaller Element Pattern  
4. Balanced Parentheses Pattern  
5. Expression Evaluation Pattern  
6. Infix to Postfix Pattern  
7. Postfix Evaluation Pattern  
8. Histogram Area Pattern  
9. Stock Span Pattern  
10. Daily Temperatures Pattern  
11. Stack Simulation Pattern  
12. Minimum Stack Pattern  
13. Path Simplification Pattern  
14. Recursion Simulation Pattern  
15. Stack Based DFS Pattern  
16. Parenthesis Depth Pattern  
17. Stack Compression Pattern  
18. Undo Redo Pattern  
19. Browser History Pattern  
20. Stack Parsing Pattern
""")


# QUEUE
st.header("Queue")

st.subheader("Introduction")
st.markdown("""
Queues follow the **First In First Out (FIFO)** principle.
They are widely used in **task scheduling, buffering systems, and BFS traversal**.
""")

st.subheader("Queue Patterns")
st.markdown("""
1. BFS Traversal Pattern  
2. Level Order Traversal Pattern  
3. Multi Source BFS Pattern  
4. Circular Queue Pattern  
5. Deque Pattern  
6. Monotonic Queue Pattern  
7. Sliding Window Maximum Pattern  
8. Task Scheduling Pattern  
9. K Distance BFS Pattern  
10. Rotting Oranges Pattern  
11. Minimum Steps BFS Pattern  
12. Queue Simulation Pattern  
13. Producer Consumer Pattern  
14. Stream Processing Pattern  
15. Event Processing Pattern  
16. Priority Queue Scheduling Pattern  
17. Multi Queue Load Balancing Pattern  
18. Window Processing Pattern  
19. Layered BFS Pattern  
20. Queue Based Topological Sort Pattern
""")


# HASHING
st.header("Hashing")

st.subheader("Introduction")
st.markdown("""
Hashing maps keys to indices using a **hash function**.
It allows **average O(1) lookup, insertion, and deletion**, making it one of the most powerful techniques in algorithms.
""")

st.subheader("Hashing Patterns")
st.markdown("""
1. Frequency Counting Pattern  
2. Two Sum Pattern  
3. Complement Lookup Pattern  
4. Prefix Sum Hash Pattern  
5. Subarray Sum Pattern  
6. Longest Substring Without Repeat Pattern  
7. Group Anagrams Pattern  
8. Hash Map Caching Pattern  
9. Hash Set Lookup Pattern  
10. Duplicate Detection Pattern  
11. Intersection Pattern  
12. Sliding Window Hash Pattern  
13. Pattern Mapping Pattern  
14. Character Counting Pattern  
15. Dictionary Simulation Pattern  
16. Hash Based Memoization Pattern  
17. Pair Counting Pattern  
18. Pattern Frequency Matching Pattern  
19. Hash Map Graph Representation Pattern  
20. Key Value Aggregation Pattern
""")


# TREES
st.header("Trees")

st.subheader("Introduction")
st.markdown("""
Trees represent hierarchical relationships where each node may have multiple children.
They are widely used in **file systems, databases, compilers, and search engines**.
""")

st.subheader("Trees Patterns")
st.markdown("""
1. DFS Traversal Pattern  
2. BFS Traversal Pattern  
3. Tree Height Pattern  
4. Tree Diameter Pattern  
5. Path Sum Pattern  
6. Root to Leaf Path Pattern  
7. Tree Balance Check Pattern  
8. Lowest Common Ancestor Pattern  
9. Tree Serialization Pattern  
10. Tree Construction Pattern  
11. Tree Mirror Pattern  
12. Subtree Detection Pattern  
13. Boundary Traversal Pattern  
14. Zigzag Traversal Pattern  
15. Vertical Order Pattern  
16. Tree DP Pattern  
17. Maximum Path Sum Pattern  
18. Tree Flatten Pattern  
19. Tree to Linked List Pattern  
20. Tree Pruning Pattern
""")


# GRAPHS
st.header("Graph")

st.subheader("Introduction")
st.markdown("""
Graphs represent relationships between entities using **nodes and edges**.
They are used in **network routing, recommendation systems, transportation, and distributed systems**.
""")

st.subheader("Graph Patterns")
st.markdown("""
1. BFS Traversal Pattern  
2. DFS Traversal Pattern  
3. Cycle Detection Pattern  
4. Connected Components Pattern  
5. Topological Sort Pattern  
6. Shortest Path Pattern  
7. Dijkstra Pattern  
8. Bellman Ford Pattern  
9. Floyd Warshall Pattern  
10. Minimum Spanning Tree Pattern  
11. Union Find Pattern  
12. Bipartite Graph Pattern  
13. Grid Graph Pattern  
14. Multi Source BFS Pattern  
15. Graph Coloring Pattern  
16. Path Counting Pattern  
17. Network Flow Pattern  
18. Strongly Connected Components Pattern  
19. Graph Backtracking Pattern  
20. State Graph Pattern
""")


# DYNAMIC PROGRAMMING
st.header("Dynamic Programming")

st.subheader("Introduction")
st.markdown("""
Dynamic Programming solves problems by **breaking them into overlapping subproblems**
and storing intermediate results to avoid recomputation.
""")

st.subheader("Dynamic Programming Patterns")
st.markdown("""
1. Fibonacci Pattern  
2. Climbing Stairs Pattern  
3. 0/1 Knapsack Pattern  
4. Unbounded Knapsack Pattern  
5. Subset Sum Pattern  
6. Partition Equal Subset Pattern  
7. Longest Increasing Subsequence Pattern  
8. Longest Common Subsequence Pattern  
9. Edit Distance Pattern  
10. Matrix Chain Multiplication Pattern  
11. Coin Change Pattern  
12. Rod Cutting Pattern  
13. DP on Trees Pattern  
14. Bitmask DP Pattern  
15. Grid Path Pattern  
16. Palindrome Partition Pattern  
17. Interval DP Pattern  
18. Digit DP Pattern  
19. DP with State Compression Pattern  
20. DP Optimization Pattern
""")


# GREEDY
st.header("Greedy Algorithms")

st.subheader("Introduction")
st.markdown("""
Greedy algorithms build solutions by **making the locally optimal choice at each step**.
They work when a problem satisfies the **greedy choice property** and **optimal substructure**.
""")

st.subheader("Greedy Algorithms Patterns")
st.markdown("""
1. Activity Selection Pattern  
2. Interval Scheduling Pattern  
3. Fractional Knapsack Pattern  
4. Huffman Coding Pattern  
5. Greedy Graph Pattern  
6. Minimum Coin Pattern  
7. Gas Station Pattern  
8. Jump Game Pattern  
9. Task Scheduling Pattern  
10. Minimum Platforms Pattern  
11. Greedy Tree Construction Pattern  
12. Greedy Matching Pattern  
13. Greedy Sorting Pattern  
14. Greedy Heap Pattern  
15. Greedy Graph Coloring Pattern  
16. Greedy String Construction Pattern  
17. Greedy Resource Allocation Pattern  
18. Greedy Merge Pattern  
19. Greedy Replacement Pattern  
20. Greedy Partition Pattern
""")


# BACKTRACKING
st.header("Backtracking")

st.subheader("Introduction")
st.markdown("""
Backtracking systematically explores all possible solutions and **undoes decisions when constraints are violated**.
It is commonly used in **combinatorial search problems**.
""")

st.subheader("Backtracking Patterns")
st.markdown("""
1. Subset Generation Pattern  
2. Permutation Generation Pattern  
3. Combination Generation Pattern  
4. N Queens Pattern  
5. Sudoku Solver Pattern  
6. Word Search Pattern  
7. Maze Path Pattern  
8. Palindrome Partition Pattern  
9. Combination Sum Pattern  
10. Graph Coloring Pattern  
11. Hamiltonian Path Pattern  
12. Subset Sum Pattern  
13. Knight Tour Pattern  
14. Balanced Parentheses Generation Pattern  
15. String Permutation Pattern  
16. K Partition Pattern  
17. Backtracking with Pruning Pattern  
18. Decision Tree Pattern  
19. State Space Search Pattern  
20. Constraint Satisfaction Pattern
""")