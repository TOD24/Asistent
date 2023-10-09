from Def import Programs, initialization, vectors
from words import data_set


vectorizer, clf = initialization(data_set)
while True:
    text = input("Введите команду: ")
    r = vectors(text, vectorizer, clf)
    Programs(r)
