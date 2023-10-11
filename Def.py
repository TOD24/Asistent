import subprocess
import os
# from initialization import initialize_recognizer
from initialization import initialization
from words import data_set
from initialization import vectors


def Programs(file_puth):  # функция запуска программ по пути
    try:
        subprocess.Popen(file_puth, shell=True)
        print(f"Программа {file_puth} запущенна")
    except Exception as e:
        print(f"ошибка при запуске программы {e}")


def sustem(comand):  # функция работы с питанием компа
    try:
        if "off" in comand:
            os.system("shutdown /s /t 0")
        elif "reboot" in comand:
            os.system("shutdown /r /t 0")
        elif "h" in comand:
            os.system("shutdown /h /t 0")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def voises():  # распознание голоса или тек
    # initialize_recognizer()
    vectorizer, clf = initialization(data_set)
    while True:
        text = input("Введите команду: ")
        # text = recognize()
        comand = text.split()
        r = vectors(text, vectorizer, clf)
        if r == "off" and "отключись" in comand:
            break
        elif r == "off" and "компютер" in comand:
            sustem(r)
        else:
            Programs(r)


def sp(test):
    t = input(test)
    return t
