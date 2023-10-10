from Def import Programs
from initialization import initialization, vectors
from words import data_set


# initialize_recognizer()
vectorizer, clf = initialization(data_set)
while True:
    text = input("Введите команду: ")
    # text = recognize()
    comand = text.split()
    r = vectors(text, vectorizer, clf)
    if r == "off" and "отключись" in comand:
        break
    print(r)
    # Programs(r)
