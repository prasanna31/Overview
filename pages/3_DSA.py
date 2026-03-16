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
    background-color: #ffffff;
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


import streamlit as st

st.header("Array Patterns")


with st.expander("1. Two Pointer Pattern"):

    st.markdown("""
# Two Pointer Pattern

The **Two Pointer Pattern** is a technique where **two indices (pointers)** traverse a data structure 
— usually an array or string — in order to reduce time complexity from **O(n²)** to **O(n)**.

Instead of checking every possible pair using nested loops, two pointers move strategically
through the data to examine only the necessary elements.

This pattern is extremely common in technical interviews and is used in problems involving:

• pairs in sorted arrays  
• palindrome checks  
• removing duplicates  
• partitioning arrays  
• container problems  
• merging sorted data  

------------------------------------------------------------

# Core Idea

The naive approach for pair problems is:
```python
    for i in range(n):
        for j in range(i+1, n):
```
This results in **O(n²)** comparisons.

Two pointer technique avoids this by scanning the array once.

Example pointer initialization:

    left = 0
    right = len(arr) - 1

Pointers move based on a condition until they meet.

------------------------------------------------------------

# Types of Two Pointer Techniques

## 1. Opposite Direction Pointers

Pointers start at **both ends** of the array and move toward each other.

Visualization

    left -> -> -> <- <- <- right

Common Uses

• pair sum in sorted arrays  
• palindrome checks  
• container with most water  
• trapping rain water  

Example

    [1,2,3,4,6]
     ^       ^
    left    right

------------------------------------------------------------

## 2. Same Direction Pointers

Both pointers move forward.

Visualization

    slow -> -> -> ->
    fast -> -> -> ->

One pointer scans the array while the other tracks valid elements.

Common Uses

• remove duplicates  
• move zeros  
• stable filtering  

------------------------------------------------------------

## 3. Fast and Slow Pointer (Runner Technique)

Two pointers move at **different speeds**.

Visualization

    slow -> -> -> ->
    fast -> -> -> -> -> -> ->

Common Uses

• detect cycle in linked list  
• find middle element  
• detect loop in arrays  

------------------------------------------------------------

# When To Use Two Pointers

Use this pattern when:

### 1. The array is sorted

Sorted data allows pointer movement decisions.

Example problems

• Two Sum II  
• Pair with target sum  
• remove duplicates  

------------------------------------------------------------

### 2. Need to examine pairs

Instead of nested loops.

Example

    find pair whose sum = target

------------------------------------------------------------

### 3. Need to compress or filter data

Examples

• remove duplicates  
• move zeros  
• partition array  

------------------------------------------------------------

### 4. Need symmetric comparisons

Example

    palindrome check

------------------------------------------------------------

# Generic Template (Opposite Direction)
```python
    left = 0
    right = len(arr) - 1

    while left < right:

        if condition:
            return result

        elif need_bigger_value:
            left += 1

        else:
            right -= 1
```
Time Complexity

    O(n)

Space Complexity

    O(1)

Each pointer moves at most **n times**.

------------------------------------------------------------

# Generic Template (Same Direction)
```python
    slow = 0

    for fast in range(len(arr)):

        if condition:
            arr[slow] = arr[fast]
            slow += 1
```
Used for

• removing duplicates  
• filtering elements  

------------------------------------------------------------

# Example 1 — Pair With Target Sum

Problem

Find two numbers that add up to a target.

Sorted array

    [1,2,3,4,6]
    target = 6

Solution
```python
    def pair_sum(arr, target):

        left = 0
        right = len(arr) - 1

        while left < right:

            s = arr[left] + arr[right]

            if s == target:
                return left, right

            elif s < target:
                left += 1

            else:
                right -= 1

        return None
```
Time Complexity

    O(n)

Space Complexity

    O(1)

------------------------------------------------------------

# Example 2 — Remove Duplicates (Sorted Array)

Input

    [1,1,2,2,3,4,4]

Solution
```python
    def remove_duplicates(arr):

        slow = 0

        for fast in range(1, len(arr)):

            if arr[fast] != arr[slow]:
                slow += 1
                arr[slow] = arr[fast]

        return slow + 1
```
------------------------------------------------------------

# Example 3 — Palindrome Check
```python
    def is_palindrome(s):

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
```
------------------------------------------------------------

# Visual Intuition

Array

    [1,2,3,4,6]
    target = 6

Step 1

    1 + 6 = 7
    move right

Step 2

    1 + 4 = 5
    move left

Step 3

    2 + 4 = 6
    solution found

Only **3 comparisons** instead of **10 comparisons** using nested loops.

------------------------------------------------------------

# Complexity

Time Complexity

    O(n)

Space Complexity

    O(1)

------------------------------------------------------------

# Common Interview Problems

Two Sum II  
Container With Most Water  
3Sum  
Trapping Rain Water  
Remove Duplicates from Sorted Array  
Valid Palindrome  
Move Zeroes  

------------------------------------------------------------

# Key Insight

Two pointers allow us to replace nested loops.

    O(n²)  ->  O(n)

This makes it one of the **most powerful patterns in algorithm design**.
""")
with st.expander("2. Sliding Window Pattern"):
    st.write("Maintain a window over a subarray and expand or shrink it to solve problems involving contiguous ranges.")

with st.expander("3. Prefix Sum Pattern"):
    st.write("Precompute cumulative sums so that range sum queries can be answered in constant time.")

with st.expander("4. Difference Array Pattern"):
    st.write("Use an auxiliary array to efficiently perform multiple range updates.")

with st.expander("5. Kadane’s Algorithm Pattern"):
    st.write("Find the maximum sum subarray by tracking the maximum sum ending at each position.")

with st.expander("6. Cyclic Sort Pattern"):
    st.write("Used when numbers are in a fixed range; place elements at their correct indices by swapping.")

with st.expander("7. Partition Pattern"):
    st.write("Divide the array into two groups based on a pivot element.")

with st.expander("8. Dutch National Flag Pattern"):
    st.write("Three-way partitioning of elements into low, mid, and high categories.")

with st.expander("9. Binary Search Pattern"):
    st.write("Repeatedly divide a sorted search space in half to find an element efficiently.")

with st.expander("10. Rotated Array Search Pattern"):
    st.write("Binary search variant used when a sorted array has been rotated.")

with st.expander("11. Subarray Sum Pattern"):
    st.write("Find subarrays with specific sums using prefix sums or hash maps.")

with st.expander("12. Product Except Self Pattern"):
    st.write("Compute products of all elements except the current one without division.")

with st.expander("13. Merge Sorted Arrays Pattern"):
    st.write("Combine two sorted arrays into one sorted sequence.")

with st.expander("14. Frequency Counting Pattern"):
    st.write("Use hash maps or arrays to count occurrences of elements.")

with st.expander("15. Greedy Rearrangement Pattern"):
    st.write("Rearrange elements to satisfy constraints using greedy decisions.")

with st.expander("16. Matrix Traversal Pattern"):
    st.write("Systematically visit elements in a 2D grid.")

with st.expander("17. Spiral Traversal Pattern"):
    st.write("Traverse a matrix layer by layer in spiral order.")

with st.expander("18. Diagonal Traversal Pattern"):
    st.write("Traverse elements across matrix diagonals.")

with st.expander("19. Range Query Pattern"):
    st.write("Answer queries on array ranges using preprocessing techniques.")

with st.expander("20. Array Simulation Pattern"):
    st.write("Simulate operations step-by-step to model array transformations.")


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