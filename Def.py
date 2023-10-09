import subprocess
from sklearn.feature_extraction.text import CountVectorizer  # pip install scikit-learn
from sklearn.linear_model import LogisticRegression
from words import TRIGGERS


import sounddevice as sd
import vosk
import json
import queue


def Programs(file_puth):  # функция запуска программ по пути
    try:
        subprocess.Popen(file_puth, shell=True)
        print(f"Программа {file_puth} запущенна")
    except:
        print("ошибка при запуске программы")


def initialization(data):
    # Обучение матрицы на data_set модели
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(data.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(data.values()))
    return vectorizer, clf


def vectors(data, vectorizer, clf):
    # принимает текст и векторы для сравнения
    # проверяем есть ли имя бота в data, если нет, то return
    trg = TRIGGERS.intersection(data.split())
    if not trg:
        return

    # удаляем имя бота из текста
    data.replace(list(trg)[0], '')

    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    return answer


q = queue.Queue()

# Глобальные переменные
model = None  # Модель Vosk будет инициализирована в функции initialize_recognizer
device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])


def initialize_recognizer():
    global model
    # Инициализируем модель Vosk
    model = vosk.Model('model_small')


def recognize():
    def callback(indata, frames, time, status):
        q.put(bytes(indata))
    # Постоянная прослушка микрофона
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        print("Говорите: ")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                print(f"+{data}")
                # Здесь должна быть функция для обработки распознанного текста из data
                return data
            else:
                # print(rec.PartialResult())
                data2 = json.loads(rec.PartialResult())["partial"]
                print(f"-{data2}")
