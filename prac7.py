
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import RegexpParser

# Download required resources
for resource in ["punkt", "punkt_tab", "averaged_perceptron_tagger_eng",
                 "maxent_ne_chunker_tab", "words"]:
    nltk.download(resource, quiet=True)

text = "Sundar Pichai works at Google in California. He studied at Stanford University."

# Tokenization and POS tagging
tokens = word_tokenize(text)
tagged_words = pos_tag(tokens)

print("Original Text:")
print(text)

print("\nPOS Tags:")
print(tagged_words)

# Named Entity Recognition
print("\nNamed Entities:")
named_entities = ne_chunk(tagged_words)

for entity in named_entities:
    if hasattr(entity, "label"):
        name = " ".join(word for word, tag in entity.leaves())
        print(name, "->", entity.label())

# Noun phrase chunking
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

chunk_parser = RegexpParser(grammar)
chunks = chunk_parser.parse(tagged_words)

print("\nNoun Phrases:")
for subtree in chunks.subtrees():
    if subtree.label() == "NP":
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(phrase)
