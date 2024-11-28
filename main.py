import heapq
from collections import Counter

def freq_count(string):
    return Counter(string)

# print(freq_count("hello"))

def huffman_codes(string):
    freq_dict=freq_count(string)
    heap=[[freq,[char,""]] for char,freq in freq_dict.items()]
    heapq.heapify(heap)
    while len(heap)>1:
        first_low=heapq.heappop(heap)
        second_low=heapq.heappop(heap)
        for pair in first_low[1:]:
            pair[1]="0"+pair[1]
        for pair in second_low[1:]:
            pair[1]="1"+pair[1]
        heapq.heappush(heap,[first_low[0]+second_low[0]]+first_low[1:]+second_low[1:])
        print(heap)

    huffman_tree=heap[0][1:]
    huffman_dict={char: code for char,code in huffman_tree}
    encoded_string="".join(huffman_dict[char] for char in string)
    return encoded_string

print(huffman_codes("hello"))