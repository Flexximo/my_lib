# Heap with priority!
import heapq
import string
import random


xs = [(random.randrange(10), c) for c in string.ascii_uppercase]

heapq.heapify(xs)   # each next item in heap after i elem is 2i+1 and 2i+2, etc its children
heapq.heappop(xs)   # pops first (0, "E") elem and creates heap of the rest items
heapq.heappush(xs, (2, 'X'))    # Obvious what it does
