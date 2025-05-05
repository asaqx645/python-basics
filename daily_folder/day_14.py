from functools import reduce
from collections import defaultdict

# === Step 1: Input Data ===
documents = [
    "hello world",
    "hello again",
    "hello world world",
    "test the map reduce example"
]

# === Step 2: Map Function ===
def map_words(doc):
    return [(word, 1) for word in doc.split()]

# Simulate the Map Phase
mapped = []
for doc in documents:
    mapped.extend(map_words(doc))

print("=== MAPPED OUTPUT ===")
print(mapped)

# === Step 3: Shuffle (Group by Key) ===
shuffled = defaultdict(list)
for word, count in mapped:
    shuffled[word].append(count)

print("\n=== SHUFFLED (GROUPED BY KEY) ===")
for word in shuffled:
    print(f"{word}: {shuffled[word]}")

# === Step 4: Reduce Function ===
def reduce_counts(counts):
    return reduce(lambda a, b: a + b, counts)

# Final Word Counts
reduced = {word: reduce_counts(counts) for word, counts in shuffled.items()}

print("\n=== REDUCED (FINAL COUNTS) ===")
for word, total in reduced.items():
    print(f"{word}: {total}")
