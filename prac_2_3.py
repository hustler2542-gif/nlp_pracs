# Experiment No. 1
# Aim: Perform Stop-word Removal using NLTK

# Step 1: Import NLTK
import nltk

# Step 2: Download required datasets (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Step 3: Import required modules
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Step 4: Input text
text = """
Natural Language Processing is a branch of Artificial Intelligence.
It enables computers to understand, analyze, and generate human language.
NLTK provides many useful tools for text preprocessing.
"""

# Step 5: Convert text into words (Tokenization)
tokens = word_tokenize(text)

print("Original Tokens:")
print(tokens)

# Step 6: Load English stop words
stop_words = set(stopwords.words('english'))

# Step 7: Remove stop words
filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

# Step 8: Display stop words
print("\nEnglish Stop Words:")
print(stop_words)

# Step 9: Display filtered words
print("\nTokens after Stop-word Removal:")
print(filtered_words)

# Step 10: Join filtered words into a sentence
filtered_text = " ".join(filtered_words)

print("\nFiltered Text:")
print(filtered_text)

# Step 11: Display statistics
print("\nStatistics")
print("Total Words Before Removal :", len(tokens))
print("Total Words After Removal  :", len(filtered_words))
print("Stop Words Removed         :", len(tokens) - len(filtered_words))