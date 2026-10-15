
import nltk
from nltk.tag import RegexpTagger, UnigramTagger
from nltk.corpus import treebank

# Download required datasets
nltk.download("treebank", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

# Load tagged corpus and split into training/testing data
sentences = list(treebank.tagged_sents())
split = int(0.8 * len(sentences))
train_data = sentences[:split]
test_data = sentences[split:]

# Rule-based tagger using regular expressions
patterns = [
    (r".*ing$", "VBG"),
    (r".*ed$", "VBD"),
    (r".*es$", "VBZ"),
    (r".*s$", "NNS"),
    (r".*ly$", "RB"),
    (r".*ous$", "JJ"),
    (r".*", "NN")
]

rule_tagger = RegexpTagger(patterns)

# Probabilistic tagger trained on corpus
prob_tagger = UnigramTagger(train_data)

# Evaluate accuracy
rule_accuracy = rule_tagger.evaluate(test_data)
prob_accuracy = prob_tagger.evaluate(test_data)

print("POS TAGGING COMPARISON")
print("-" * 40)
print(f"Rule-Based Accuracy: {rule_accuracy * 100:.2f}%")
print(f"Probabilistic Accuracy: {prob_accuracy * 100:.2f}%")

# Display sample tagging
text = "The quick brown fox jumps over the lazy dog"
tokens = nltk.word_tokenize(text)

print("\nSample Text:", text)
print("\nRule-Based Tags:")
print(rule_tagger.tag(tokens))

print("\nProbabilistic Tags:")
print(prob_tagger.tag(tokens))
