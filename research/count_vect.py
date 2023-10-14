from sklearn.feature_extraction.text import CountVectorizer


examples = [
    "apple ball cat",
    "ball cat dog",
]
max_features = 100
ngrams = 3 
vectorizer = CountVectorizer(max_features=max_features,ngram_range = (1,ngrams))
x = vectorizer.fit_transform(examples)
print(vectorizer.get_feature_names_out())
print(x.toarray())



