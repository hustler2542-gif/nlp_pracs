
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

# Input text
text = "Natural language processing is a branch of artificial intelligence"

# Tokenize text
words = word_tokenize(text.lower())

# Generate N-Grams
unigrams = list(ngrams(words, 1))
bigrams = list(ngrams(words, 2))
trigrams = list(ngrams(words, 3))

# Display results
print("Original Text:", text)

print("\nUnigrams:")
print(Counter(unigrams))

print("\nBigrams:")
print(Counter(bigrams))

print("\nTrigrams:")
print(Counter(trigrams))
