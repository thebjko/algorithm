from heapq import heapify, heappop
heap = []
for word in open(0):
    word = word.strip()
    heap += [(len(word), word)]

heap = list(set(heap[1:]))
heapify(heap)

while heap:
    print(heappop(heap)[1])
