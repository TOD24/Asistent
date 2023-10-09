from Def import *
from words import data_set


initialize_recognizer()
vectorizer, clf = initialization(data_set)
while True:
    #    text = input("Введите команду: ")
    text = recognize()
    r = vectors(text, vectorizer, clf)
    print(r)
#    Programs(r)
