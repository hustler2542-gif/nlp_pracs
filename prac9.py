
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# Sample sentiment dataset
texts = [
    "I love this product",
    "This movie is excellent",
    "The service was amazing",
    "I am very happy",
    "This is a wonderful experience",
    "The food was delicious",
    "I hate this product",
    "This movie is terrible",
    "The service was awful",
    "I am very disappointed",
    "This is a horrible experience",
    "The food was disgusting",
    "The product is great",
    "I really enjoyed it",
    "Everything was fantastic",
    "The product is bad",
    "I regret buying it",
    "Everything was disappointing"
]

labels = [
    "positive", "positive", "positive", "positive",
    "positive", "positive", "negative", "negative",
    "negative", "negative", "negative", "negative",
    "positive", "positive", "positive", "negative",
    "negative", "negative"
]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.30, random_state=42, stratify=labels
)

# Convert text into numerical TF-IDF features
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X_train_vec, y_train)
nb_predictions = nb_model.predict(X_test_vec)

# Train SVM model
svm_model = LinearSVC(random_state=42)
svm_model.fit(X_train_vec, y_train)
svm_predictions = svm_model.predict(X_test_vec)

# Evaluate models
print("NAIVE BAYES RESULTS")
print("Accuracy:", round(accuracy_score(y_test, nb_predictions) * 100, 2), "%")
print(classification_report(y_test, nb_predictions, zero_division=0))

print("\nSVM RESULTS")
print("Accuracy:", round(accuracy_score(y_test, svm_predictions) * 100, 2), "%")
print(classification_report(y_test, svm_predictions, zero_division=0))

# Test custom sentences
test_sentences = [
    "The movie was fantastic",
    "I hate this terrible product"
]

test_vec = vectorizer.transform(test_sentences)

print("\nSENTIMENT PREDICTIONS")
for sentence, nb_pred, svm_pred in zip(
    test_sentences,
    nb_model.predict(test_vec),
    svm_model.predict(test_vec)
):
    print("\nText:", sentence)
    print("Naive Bayes:", nb_pred)
    print("SVM:", svm_pred)
