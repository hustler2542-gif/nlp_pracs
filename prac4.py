
# Experiment No. 4
# Minimum Edit Distance for Spelling Correction

def minimum_edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first column and row
    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,        # Deletion
                dp[i][j - 1] + 1,        # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )

    return dp[m][n]


def correct_spelling(word, dictionary):
    best_word = word
    min_distance = float("inf")

    for candidate in dictionary:
        distance = minimum_edit_distance(word.lower(), candidate.lower())

        if distance < min_distance:
            min_distance = distance
            best_word = candidate

    return best_word, min_distance


# Sample dictionary
dictionary = [
    "natural", "language", "processing", "computer",
    "science", "python", "machine", "learning",
    "algorithm", "spelling", "correction", "model"
]

# Sample text containing spelling mistakes
sample_text = """
Natural languge processng is an important field.
Python is used for machne learning.
Speling corection improves text quality.
"""

print("=" * 60)
print("MINIMUM EDIT DISTANCE - SPELLING CORRECTION")
print("=" * 60)

print("\nOriginal Text:")
print(sample_text)

print("\nSpelling Correction Results:")
print("-" * 60)

# Evaluate selected misspelled words
test_words = ["languge", "processng", "machne", "speling", "corection"]

for word in test_words:
    corrected, distance = correct_spelling(word, dictionary)
    print(
        f"Original: {word:<12} "
        f"Corrected: {corrected:<15} "
        f"Edit Distance: {distance}"
    )

print("\nMinimum Edit Distance Examples:")
print("-" * 60)

examples = [
    ("kitten", "sitting"),
    ("book", "back"),
    ("hello", "hallo")
]

for word1, word2 in examples:
    distance = minimum_edit_distance(word1, word2)
    print(f"{word1} -> {word2}: {distance}")

print("\nEvaluation:")
print("-" * 60)

# Compare predictions against known correct words
actual_words = ["language", "processing", "machine",
                "spelling", "correction"]

correct_count = 0

for wrong, actual in zip(test_words, actual_words):
    predicted, _ = correct_spelling(wrong, dictionary)

    if predicted == actual:
        correct_count += 1

accuracy = (correct_count / len(actual_words)) * 100

print(f"Total test words: {len(actual_words)}")
print(f"Correct predictions: {correct_count}")
print(f"Correction accuracy: {accuracy:.2f}%")
