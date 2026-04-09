import heapq, re
from collections import Counter

def _huffman(words_by_freq):
    if not words_by_freq: return {}
    if len(words_by_freq) == 1: return {words_by_freq[0][0]: '0'}
    heap = [(freq, i, word) for i,(word,freq) in enumerate(words_by_freq)]
    heapq.heapify(heap)
    nid = len(heap)
    while len(heap) > 1:
        f1,i1,n1 = heapq.heappop(heap)
        f2,i2,n2 = heapq.heappop(heap)
        heapq.heappush(heap,(f1+f2, nid, [n1,n2]))
        nid += 1
    codes = {}
    def traverse(node, pre):
        if isinstance(node, str): codes[node] = pre or '0'
        else: traverse(node[0], pre+'0'); traverse(node[1], pre+'1')
    traverse(heap[0][2], '')
    return codes

def build_dictionary(text):
    words = re.findall(r'[a-z]+', text.lower())
    freq  = Counter(words)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    codes   = _huffman(sorted_words)
    reverse = {v:k for k,v in codes.items()}
    avg_len = sum(len(c) for c in codes.values()) / max(len(codes),1)
    return codes, reverse, {'total_words': len(codes), 'avg_code_len': avg_len}
