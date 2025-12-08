# Manual Loop:
# This method involves iterating through a sequence and updating a dictionary.
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counts = {}

for item in data:
    if item not in counts:
        counts[item] = 0
    counts[item] += 1

print(counts)


# Using collections.Counter:
# The Counter class from the collections module is specifically designed for counting hashable objects.
from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counts = Counter(data)

print(counts)


# Using collections.defaultdict:
# The defaultdict from collections allows specifying a default factory for missing keys, simplifying the counting logic.
from collections import defaultdict

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counts = defaultdict(int) # int is the default factory, so missing keys default to 0

for item in data:
    counts[item] += 1

print(dict(counts)) # Convert back to a regular dictionary if needed

