import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

stop_words = stopwords.words('english')

print("Total English Stop Words:", len(stop_words))
print(stop_words)