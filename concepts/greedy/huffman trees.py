class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def build_frequency_dict(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


def build_huffman_tree(frequency):
    nodes = [Node(char, freq) for char, freq in frequency.items()]

    while len(nodes) > 1:
        # Sort nodes by frequency
        nodes = sorted(nodes, key=lambda node: node.freq)

        # Pick two nodes with the lowest frequencies
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Create a new internal node with these two nodes as children
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node to the list of nodes
        nodes.append(merged)

    return nodes[0]  # Root of the Huffman tree


def generate_huffman_codes(root):
    codes = {}

    def generate_codes_helper(node, current_code):
        if node is None:
            return

        if node.char is not None:
            # It's a leaf node
            codes[node.char] = current_code
            return

        # Traverse the left and right children
        generate_codes_helper(node.left, current_code + "0")
        generate_codes_helper(node.right, current_code + "1")

    generate_codes_helper(root, "")
    return codes


def encode_text(text, huffman_codes):
    encoded_text = ""
    for char in text:
        encoded_text += huffman_codes[char]
    return encoded_text


def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree

    return decoded_text


def huffman_coding(text):
    frequency = build_frequency_dict(text)
    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = generate_huffman_codes(huffman_tree)

    encoded_text = encode_text(text, huffman_codes)
    decoded_text = decode_text(encoded_text, huffman_tree)

    return encoded_text, decoded_text, huffman_codes


# Example usage
text = "this is an example for huffman encoding"
encoded_text, decoded_text, huffman_codes = huffman_coding(text)

print(f"Original text: {text}")
print(f"Encoded text: {encoded_text}")
print(f"Decoded text: {decoded_text}")
print(f"Huffman Codes: {huffman_codes}")
