import heapq


class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        self.code = ''

    def __lt__(self, other):
        return self.freq < other.freq


def CalculateProbability(the_data):
    the_symbols = dict()
    for item in the_data:
        if the_symbols.get(item) is None:
            the_symbols[item] = 1
        else:
            the_symbols[item] += 1
    return the_symbols


def CalculateCodes(node, value=''):
    newValue = value + str(node.code)
    if node.left:
        CalculateCodes(node.left, newValue)
    if node.right:
        CalculateCodes(node.right, newValue)
    if not node.left and not node.right:
        the_codes[node.symbol] = newValue
    return the_codes


def OutputEncoded(the_data, coding):
    encodingOutput = []
    for element in the_data:
        print(coding[element], end='')
        encodingOutput.append(coding[element])
    the_string = ''.join([str(item) for item in encodingOutput])
    return the_string


def build_huffman_tree(probabilities):
    priority_queue = [Node(symbol, freq) for symbol, freq in probabilities.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        left.code = '0'
        right.code = '1'

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def huffman_encoding(data):
    probabilities = CalculateProbability(data)
    root = build_huffman_tree(probabilities)
    huffman_codes = CalculateCodes(root)
    encoded_data = OutputEncoded(data, huffman_codes)
    return encoded_data, huffman_codes, root


def huffman_decoding(encoded_data, root):
    decoded_data = []
    node = root
    for bit in encoded_data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if not node.left and not node.right:
            decoded_data.append(node.symbol)
            node = root
    return ''.join(decoded_data)


# Example usage:
data = "this is an example for huffman encoding"
the_codes = dict()
encoded_data, huffman_codes, root = huffman_encoding(data)
decoded_data = huffman_decoding(encoded_data, root)

print("\nOriginal data:", data)
print("Encoded data:", encoded_data)
print("Huffman Codes:", huffman_codes)
print("Decoded data:", decoded_data)
