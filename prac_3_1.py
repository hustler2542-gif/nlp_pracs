
# Experiment No. 3
# Implement Stemming and Lemmatization Techniques
# Compare and Analyze Results

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK resources
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Input words
words = [
    "playing",
    "played",
    "plays",
    "studies",
    "studying",
    "running",
    "easily",
    "better",
    "cars",
    "children"
]

print("=" * 65)
print("STEMMING AND LEMMATIZATION")
print("=" * 65)

print(f"{'Original Word':<18}{'Stemmed Word':<20}{'Lemma':<20}")
print("-" * 65)

for word in words:
    stem = stemmer.stem(word)

    # Default POS is noun; specify verb for action words
    if word in ["playing", "played", "plays", "studying",
                "running"]:
        lemma = lemmatizer.lemmatize(word, pos="v")
    elif word == "better":
        lemma = lemmatizer.lemmatize(word, pos="a")
    else:
        lemma = lemmatizer.lemmatize(word, pos="n")

    print(f"{word:<18}{stem:<20}{lemma:<20}")

print("\n" + "=" * 65)
print("COMPARISON AND ANALYSIS")
print("=" * 65)

print("""
1. Stemming:
   Removes prefixes or suffixes using simple rules.
   It may produce a root that is not a valid English word.

2. Lemmatization:
   Converts a word into its dictionary base form (lemma).
   It uses vocabulary and linguistic information.

3. Key Difference:
   Stemming is generally faster but less linguistically accurate.
   Lemmatization is more meaningful but requires more resources.

4. Conclusion:
   Stemming is useful for quick text normalization, while
   lemmatization is useful when meaningful base words are needed.
""")
