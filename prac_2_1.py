

# Step 1: Import NLTK
import nltk

# Step 2: Download required tokenizer (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')

# Step 3: Import tokenizers
from nltk.tokenize import sent_tokenize, word_tokenize

# Step 4: Input text
text = """
Natural Language Processing (NLP) is a branch of Artificial Intelligence.
It enables computers to understand human language.
Python provides many libraries for NLP such as NLTK and spaCy.
"""

# Step 5: Sentence Tokenization
sentences = sent_tokenize(text)

print("----- Sentence Tokenization -----")
for i, sentence in enumerate(sentences, start=1):
    print(f"Sentence {i}: {sentence}")

# Step 6: Word Tokenization
words = word_tokenize(text)

print("\n----- Word Tokenization -----")
print(words)

# Step 7: Total Counts
print("\nTotal Number of Sentences:", len(sentences))
print("Total Number of Words:", len(words))