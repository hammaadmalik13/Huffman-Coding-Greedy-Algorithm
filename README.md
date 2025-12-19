# Huffman Coding Using Greedy Algorithm

This repository contains a Python implementation of the **Huffman Coding Algorithm**, a popular **greedy algorithm** used for **lossless data compression**.  
It generates optimal prefix codes based on the frequency of characters.

---

## 🧠 Problem Statement

Given a set of characters and their corresponding frequencies, generate binary codes such that:
- No code is a prefix of another (prefix property)
- The total encoded length is minimized

---

## ⚙️ Algorithm Approach

Huffman Coding follows a greedy strategy:

1. Create a leaf node for each character with its frequency.
2. Insert all nodes into a **min-heap (priority queue)**.
3. Repeatedly remove the two nodes with the smallest frequencies.
4. Merge them into a new node with combined frequency.
5. Insert the merged node back into the heap.
6. Repeat until only one node remains (root of Huffman Tree).
7. Traverse the tree to generate binary codes:
   - Left edge → `0`
   - Right edge → `1`

---

## 🧪 Example Input

```python
characters = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [5, 9, 12, 13, 16, 45]
