import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq


# Function to generate Huffman codes
def generate_codes(node, code, huffman_codes):
    if node is None:
        return

    # If leaf node, store the code
    if node.char is not None:
        huffman_codes[node.char] = code
        return

    generate_codes(node.left, code + "0", huffman_codes)
    generate_codes(node.right, code + "1", huffman_codes)


# Huffman Coding function
def huffman_coding(characters, frequencies):
    priority_queue = []

    # Create leaf nodes and push into priority queue
    for char, freq in zip(characters, frequencies):
        heapq.heappush(priority_queue, Node(char, freq))

    # Build Huffman Tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    # Generate Huffman codes
    huffman_codes = {}
    root = priority_queue[0]
    generate_codes(root, "", huffman_codes)

    return huffman_codes


# Driver code
characters = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [5, 9, 12, 13, 16, 45]

codes = huffman_coding(characters, frequencies)

print("Character | Huffman Code")
print("-------------------------")
for char in codes:
    print(f"{char:9} | {codes[char]}")
